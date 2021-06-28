# python-line-bot
LINEBot for Python with flask

## 現在の機能
- オウム返し

## はじめに
LINEBOTを作るためのLINE公式アカウント作成・設定

https://qiita.com/nanato12/items/25e2db9461bb6ac2b8c5

初期構築
```sh
$ pipenv shell
(python-line-bot) $ pipenv install
```

## 使い方
`.env` の作成

```sh
(python-line-bot) $ touch .env
```

`.env` に LINEBotの情報を書き込む

```conf
LINE_CHANNEL_SECRET=XXXXXXXXXXXXXX
LINE_CHANNEL_ACCESS_TOKEN=XXXXXXXXXXXXXXXXXXXXXXX
```

実行

```sh
(python-line-bot) $ make run
python main.py --debug --port=3000
 * Serving Flask app 'app' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://127.0.0.1:3000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 229-842-426
```
