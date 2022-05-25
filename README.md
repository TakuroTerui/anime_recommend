### アニメリスト
- いいね前
![スクリーンショット 2022-05-25 11 34 52](https://user-images.githubusercontent.com/77182341/170167489-6304d7e0-204c-4908-9417-db4bb2d573d5.png)

- いいね後
![スクリーンショット 2022-05-25 11 36 22](https://user-images.githubusercontent.com/77182341/170167674-7d939718-cf87-450b-a1ba-1d6797cbf1bc.png)

### レコメンドリスト
![スクリーンショット 2022-05-25 11 36 04](https://user-images.githubusercontent.com/77182341/170167609-c1bfae70-f4dd-481e-9651-0130a5975e6f.png)


参考
https://dse-souken.com/2021/03/25/ai-20/

|テーブル論理名|テーブル物理名|
|-|-|
|アニメ|animes|
<br/>

|#|PK|UK|カラム論理名|カラム物理名|データ型|桁|NULL|DEFAULT|備考|
|-|-|-|-|-|-|-|-|-|-|
|1|○|N/A|アニメid|id|INT unsigned|N/A|NO|auto_increment||
|2|N/A|N/A|アニメ名|name|VARCHAR|100|NO|N/A||
|3|N/A|N/A|タイプ|type|VARCHAR|30|NO|N/A||
|4|N/A|N/A|評価|rating|FLOAT|5, 2|NO|N/A||
|5|N/A|N/A|評価者数|members|INT unsigned|N/A|NO|N/A||
<br/><br/>

|テーブル論理名|テーブル物理名|
|-|-|
|ジャンル|genres|
<br/>

|#|PK|UK|カラム論理名|カラム物理名|データ型|桁|NULL|DEFAULT|備考|
|-|-|-|-|-|-|-|-|-|-|
|1|○|N/A|ジャンルid|id|INT unsigned|N/A|NO|auto_increment||
|2|N/A|N/A|ジャンル名|name|VARCHAR|30|NO|N/A||
<br/><br/>

|テーブル論理名|テーブル物理名|
|-|-|
|アニメとジャンルの中間テーブル|anime_genres|
<br/>

|#|PK|UK|カラム論理名|カラム物理名|データ型|桁|NULL|DEFAULT|備考|
|-|-|-|-|-|-|-|-|-|-|
|1|N/A|N/A|アニメid|anime_id|INT unsigned|N/A|NO|N/A||
|2|N/A|N/A|ジャンルid|genre_id|INT unsigned|N/A|NO|N/A||
<br/><br/>

|テーブル論理名|テーブル物理名|
|-|-|
|評価|ratings|
<br/>

|#|PK|UK|カラム論理名|カラム物理名|データ型|桁|NULL|DEFAULT|備考|
|-|-|-|-|-|-|-|-|-|-|
|1|○|N/A|評価id|id|INT unsigned|N/A|NO|auto_increment||
|2|N/A|N/A|ユーザーid|user_id|INT unsigned|N/A|NO|N/A|仮のuser_id|
|3|N/A|N/A|評価|rating|FLOAT|5, 2|NO|N/A||
<br/><br/>

|テーブル論理名|テーブル物理名|
|-|-|
|いいね|favorites|
<br/>

|#|PK|UK|カラム論理名|カラム物理名|データ型|桁|NULL|DEFAULT|備考|
|-|-|-|-|-|-|-|-|-|-|
|1|N/A|N/A|ユーザーid|user_id|INT unsigned|N/A|NO|N/A||
|2|N/A|N/A|アニメid|anime_id|INT unsigned|N/A|NO|N/A|本当のuser_id|
