const tf = require('@tensorflow/tfjs');
const tfn = require('@tensorflow/tfjs-node');

const formatData = ([dx1, dy1, dx2, dy2]) => {
  const relu = (value) => (value > 0 ? value : 0);
  return [dx1, dy1, dx2, dy2, -dx1, -dy1, -dx2, -dy2].map((value) => (
    relu(value) / 2000
  ));
};

const toTensors = (inputNx2x4) => {
  const rowForTs1 = [];
  const rowForTs2 = [];
  inputNx2x4.forEach(input2x4 => {
    rowForTs1.push(formatData(input2x4[0]));
    rowForTs2.push(formatData(input2x4[1]));
  });
  return [tf.tensor(rowForTs1), tf.tensor(rowForTs2)];
};

const testDatas = [
  [[0,126,498,161],[0,23,498,58]],
  [[0,23,498,58],[0,229,498,264]],
  [[0,23,498,58],[0,-80,498,-45]],
  [[0,23,498,58],[0,332,498,369]],
  [[0,332,498,369],[0,23,498,58]],
  [[110, 0, 101, 0], [173, 0, 162, 0]],
];

(async () => {
  const tensors = toTensors(testDatas);
  tensors.forEach(ts => ts.print());
  const modelFile = tfn.io.fileSystem('../training/output/model.json');
  const model = await tf.loadLayersModel(modelFile);
  model.predict(tensors).print();
})();
