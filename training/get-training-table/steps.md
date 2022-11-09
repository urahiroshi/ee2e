https://jp.mercari.com/signup/identification?params=hoge&step=2

```js
const c1 = getCoordinates(/姓（全角）/)
const c2 = getCoordinates(/名（全角）/)
const c3 = getCoordinates(/姓カナ（全角）/)
const c4 = getCoordinates(/名カナ（全角）/)
const c5 = getCoordinates(/生年月日/)
toTrainingTable([c1,c2,c3,c4,c5])
```

https://jp.mercari.com/sell/create

```js
const clist = [
  [/カテゴリー/, 'select'],
  [/商品の状態/, 'select'],
  /商品名/,
  [/商品の説明/, 'textarea'],
  [/配送料の負担/, 'select'],
  [/配送の方法/, 'select'],
  [/発送元の地域/, 'select'],
  [/発送までの日数/, 'select'],
  /販売価格/
].map((selectors) => getCoordinates(selectors));
toTrainingTable(clist);
```