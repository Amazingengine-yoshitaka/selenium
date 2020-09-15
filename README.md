# selenium
## 概要
Selenium の環境構築が面倒だったため Docker 上で開発環境を再現できるように設定ファイルと sample script をまとめました。
`docker-compose up -d`するだけで Selenium と Python および Headless Chrome の環境が出来上がります。ブラウザを用いた処理を自動化したい場合や、テスト自動化のベースとしてご利用ください。 Headless なので GUI 環境のないサーバー上でも動作します。

https://qiita.com/sikkim/items/447b72e6ec45849058cd

## 事前準備
Dockerをインストールして、dockerコマンドと docker-compose コマンドが使用できるようにしてください。

## 使い方
### install と起動方法

```bash
$ git clone https://github.com/Amazingengine-yoshitaka/selenium
$ cd selenium
$ docker-compose up -d
```

正常に起動できていれば下記のようになります。

```bash
$ docker-compose ps
Name           Command                   State   Ports
-----------------------------------------------------------------------
chrome0        /opt/bin/entry_point.sh   Up      0.0.0.0:5900->5900/tcp
chrome1        /opt/bin/entry_point.sh   Up      0.0.0.0:5900->5900/tcp
chrome2        /opt/bin/entry_point.sh   Up      0.0.0.0:5900->5900/tcp
python         tail -f /dev/null         Up
selenium-hub0  /opt/bin/entry_point.sh   Up      0.0.0.0:4444->4444/tcp
selenium-hub1  /opt/bin/entry_point.sh   Up      0.0.0.0:4444->4444/tcp
selenium-hub2  /opt/bin/entry_point.sh   Up      0.0.0.0:4444->4444/tcp
```

### 終了方法

```bash
$ docker-compose down
```

### sample script の実行

```bash
$ docker exec python python script/sample.py
```

実行するとGoogleにアクセスして screenshot を取得します。
script/images directory に画像 file が保存されます。

### VNC接続による debug
`VNC`で接続するとブラウザの動きを確認しながら debug することができます。Docker環境のIPアドレスにVNC(デフォルトは5900番ポート)でアクセスした上で sample script を実行してみてください。デフォルトのパスワードは "secret" です。

vnc://localhost
