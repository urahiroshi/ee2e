import { execE2E } from './script.js';

async function getCurrentTab() {
  let queryOptions = { active: true, lastFocusedWindow: true };
  let [tab] = await chrome.tabs.query(queryOptions);
  return tab;
}

const executeButton = document.getElementById('executeButton');
executeButton.addEventListener('click', () => {
  const command = document.getElementById('command').value;
  const target = document.getElementById('target').value;
  getCurrentTab().then((tab) => {
    chrome.scripting.executeScript({
      target: {tabId: tab.id},
      func: execE2E,
      args: [command, target],
    },
    (injectionResults) => { console.log(injectionResults); }
  )});
});
