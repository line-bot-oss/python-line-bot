"""
   Copyright 2021 line-bot-oss

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

from flask import Flask, abort, request
from linebot import WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import (
    FollowEvent,
    ImageMessage,
    MessageEvent,
    TextMessage,
    UnfollowEvent,
)

from app import settings
from app.receivers import (
    follow,
    receive_image_message,
    receive_text_message,
    unfollow,
)
from app.wrapper import LINE

app = Flask(__name__)

line = LINE(settings.LINE_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(settings.LINE_CHANNEL_SECRET)


@app.route("/", methods=["GET"])
def index() -> str:
    return "python-line-bot-oss hello"


@app.route("/callback", methods=["POST"])
def callback() -> str:
    signature = request.headers["X-Line-Signature"]

    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return "OK"


@handler.add(MessageEvent, message=TextMessage)
def text_message(event: MessageEvent) -> None:
    receive_text_message(line, event)


@handler.add(MessageEvent, message=ImageMessage)
def image_message(event: MessageEvent) -> None:
    receive_image_message(line, event)


@handler.add(FollowEvent)
def follow_event(event: FollowEvent) -> None:
    follow(line, event)


@handler.add(UnfollowEvent)
def unfollow_event(event: UnfollowEvent) -> None:
    unfollow(line, event)
