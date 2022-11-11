import { FQ } from './fq.js';

const getAllInputElements = () => {
  return ['input', 'textarea'].map(selector => (
    Array.prototype.map.call(document.querySelectorAll(selector), e => e)
  )).flat();
}

const main = ({ command, target }) => {
  const fqElement = FQ(target);
  if (fqElement) {
    alert(JSON.stringify(fqElement.element.getBoundingClientRect()));
  } else {
    alert(`not found ${target}`);
  }
}

export { main };
