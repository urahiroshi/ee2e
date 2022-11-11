const execE2E = (command, target) => {
  const src = chrome.runtime.getURL('content-script/main.js');
  import(src).then(({ main }) => {
    main({ command, target });
  });
};

export { execE2E };
