// Fill in the volatile columns of the software inventory tables.
//
// The tables are rendered from the inventory YAML files when the documentation is
// built, but the "Latest commit" and language columns are left as empty placeholders
// (see `pwa_pages.project_inventory.to_markdown_table`). This script fills them in from
// the JSON file that is written by `export-inventory-data`.
//
// The JSON file is fetched twice: the copy that is shipped with the documentation is
// applied first, because it is on the same server and always available, and the copy on
// the default branch is applied afterwards if it is newer. That way the tables are up to
// date even if the documentation has not been rebuilt since the data were refreshed.

(() => {
  "use strict";

  const REMOTE_URL =
    "https://raw.githubusercontent.com/ComPWA/PWA-pages/main/docs/software/inventory.json";
  const LOCAL_TIMEOUT = 5000;
  const REMOTE_TIMEOUT = 5000;

  const script = document.currentScript;
  const localURL = new URL("inventory.json", script.src).href;

  function normalizeLanguage(language) {
    // Mirrors the replacements in `pwa_pages.project_inventory`.
    const normalized = language.toLowerCase();
    return normalized === "c" ? "c++" : normalized;
  }

  function formatMonth(isoDate) {
    const [year, month] = isoDate.split("-");
    return `${month}/${year}`;
  }

  function getEntries(span, repositories) {
    const urls = (span.dataset.repos || "").split(" ").filter(Boolean);
    return urls.map((url) => repositories[url]).filter(Boolean);
  }

  function fillLatestCommit(span, entries) {
    const dates = entries.map((entry) => entry.latest_commit).filter(Boolean);
    if (dates.length === 0) return;
    dates.sort(); // ISO 8601 dates sort chronologically
    span.textContent = formatMonth(dates[dates.length - 1]);
  }

  function fillLanguage(span, entries) {
    const minPercentage = parseFloat(span.dataset.minPercentage || "0");
    const wanted = normalizeLanguage(span.dataset.language || "");
    const found = entries.some((entry) =>
      Object.entries(entry.languages || {}).some(
        ([language, percentage]) =>
          normalizeLanguage(language) === wanted && percentage > minPercentage,
      ),
    );
    span.textContent = found ? "✓" : "";
  }

  function applyData(data) {
    const repositories = (data && data.repositories) || {};
    document.querySelectorAll("span.live-value").forEach((span) => {
      const entries = getEntries(span, repositories);
      if (entries.length === 0) return; // keep whatever the inventory file says
      if (span.dataset.field === "latest-commit") {
        fillLatestCommit(span, entries);
      } else if (span.dataset.field === "language") {
        fillLanguage(span, entries);
      }
    });
  }

  function showTimestamp(data) {
    const element = document.querySelector(".inventory-timestamp");
    if (!element || !data.generated) return;
    const date = new Date(data.generated);
    if (isNaN(date.getTime())) return;
    const formatted = date.toLocaleDateString(undefined, {
      year: "numeric",
      month: "long",
      day: "numeric",
    });
    element.textContent = `Repository data fetched on ${formatted}.`;
  }

  async function fetchJSON(url, timeout) {
    const controller = new AbortController();
    const timer = setTimeout(() => controller.abort(), timeout);
    try {
      const response = await fetch(url, { signal: controller.signal });
      if (!response.ok) {
        throw new Error(`${response.status} ${response.statusText}`);
      }
      return await response.json();
    } finally {
      clearTimeout(timer);
    }
  }

  async function update() {
    let local = null;
    try {
      local = await fetchJSON(localURL, LOCAL_TIMEOUT);
      applyData(local);
      showTimestamp(local);
    } catch (error) {
      console.warn(`Could not load ${localURL}: ${error.message}`);
    }
    try {
      const remote = await fetchJSON(REMOTE_URL, REMOTE_TIMEOUT);
      if (!local || !local.generated || remote.generated > local.generated) {
        applyData(remote);
        showTimestamp(remote);
      }
    } catch (error) {
      console.warn(`Could not load ${REMOTE_URL}: ${error.message}`);
    }
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", update);
  } else {
    update();
  }
})();
