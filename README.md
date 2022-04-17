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
