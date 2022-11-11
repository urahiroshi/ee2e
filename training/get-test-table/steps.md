https://jp.mercari.com/signup/identification?params=hoge&step=2

```js
const c1 = getCoordinates(/姓（全角）/)
const c2 = getCoordinates(/名（全角）/)
const c3 = getCoordinates(/姓カナ（全角）/)
const c4 = getCoordinates(/名カナ（全角）/)
const c5 = getCoordinates(/生年月日/)
toTable([c1,c2,c3,c4,c5])
```
