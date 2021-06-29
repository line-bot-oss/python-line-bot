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

import os
from os.path import join

from linebot.models import MessageEvent, TextSendMessage

from app.wrapper import LINE

RESOUCE_DIR = "images"


def receive_image_message(bot: LINE, event: MessageEvent) -> None:
    """when receive image message event

    Args:
        bot (LINE): LINEBot Client
        event (MessageEvent): MessageEvent
    """
    bot.save_content_from_message_id(
        event.message.id,
        join(os.getcwd(), RESOUCE_DIR, f"{event.message.id}.jpg"),
    )
    bot.reply_message(event.reply_token, TextSendMessage("保存しました。"))
