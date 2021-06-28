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

from linebot.api import LineBotApi
from linebot.models import MessageEvent, TextSendMessage


def receive_text_message(bot: LineBotApi, event: MessageEvent) -> None:
    """when receive text message

    Args:
        event (MessageEvent): MessageEvent
    """
    bot.reply_message(
        event.reply_token, TextSendMessage(text=event.message.text)
    )
