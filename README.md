# Graph-Generator
2軸グラフ、対数グラフ、近似曲線を手早く作成するプログラム

![default](https://user-images.githubusercontent.com/44617952/48715137-aa673300-ec57-11e8-9dc2-a57e71c80f59.PNG)

「Import file」からグラフにしたいcsvファイルを取り込むと、上のような画面になります。

点や線のスタイル、対数軸設定、Y軸のどちらに描画するかなどを決めることができます。

![1](https://user-images.githubusercontent.com/44617952/48715196-cbc81f00-ec57-11e8-8256-0a61a882a89e.PNG)


「Output」でグラフが出力されます。

グラフの凡例は、ドラッグ&ドロップで移動させることが可能です。

![2](https://user-images.githubusercontent.com/44617952/48715210-d5518700-ec57-11e8-8fa9-24b75eb1823c.PNG)

## exeファイルのダウンロード

ファイルサイズが大きいためここにアップロードできませんでした。そのため、GoogleDriveにアップロードしています。

https://drive.google.com/drive/folders/11a72Dv8PkcwaphS6R3fnzCi6qv7Ku_QM?usp=sharing

## 各設定項目の詳細

- X-axis name：X軸のラベル名称
- Y1-axis name：Y1軸のラベル名称
- Y2-axis name：Y2軸のラベル名称
- Label：描画するデータの凡例名称、空欄で凡例なし
- Marker：データ点に用いるマーカー
- Line：線の選択
- Approx：n次多項式による近似曲線
- Degree：n次多項式のn
- Approx Label：近似曲線の凡例名称、空欄で凡例なし

## 注意点

- 近似曲線を描画するときは、元のデータ点を結ぶ直線は描画されません
- ラベルに日本語を用いる場合は、「Noto Sans CJK JP」というフォントを入れる必要があります

## 更新内容

- 2018/11/23 

csvにヘッダがある場合に動作しない不具合を解消しました。

横軸が対数の場合（周波数など）に、近似曲線に補正をかける機能を実装しました。多項式の係数決定に用いるxの値をlog10としています。

## 今後実装予定

- X軸がlog、Y軸がlinearのときに近似曲線を正しく描画
- 他の近似曲線の導入
- 可能であれば、デフォルトで日本語対応
