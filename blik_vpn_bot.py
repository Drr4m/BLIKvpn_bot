import logging
from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    BotCommand
)
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes
)

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)
  
# Функция для отправки сообщения подключения VPN (используется как для команды /connect, так и для callback)
async def send_connect_message(chat_id, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Андроид (android OS)", callback_data="android")],
        [InlineKeyboardButton("Айфон (iOS)", callback_data="iphone")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await context.bot.send_message(
        chat_id=chat_id,
        text="🎉 Поздравляем, вы активировали аккаунт BLIK, 150₽ у вас на балансе! Обращаем внимание! Данной суммы хватит на 2 недели использования нашего сервиса. \n\nТеперь давайте настроим ваш VPN. Выберите тип вашего устройства:\n",
        reply_markup=reply_markup
    )

# Функция для отправки сообщения оплаты подписки (используется как для команды /pay, так и для callback)
async def send_pay_message(chat_id, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Оплатить подписку 💸", url="https://yandex.ru/maps/?text=стасова+149А")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await context.bot.send_message(
        chat_id=chat_id,
        text="Благодарим вас за использование BLIK VPN!✨\n\nЧтобы продолжать пользоваться быстрым и надежным сервисом без перебоев, пожалуйста, продлите подписку. \n\nМы постоянно работаем над улучшением сервиса для вашего удобства. Если у вас возникнут вопросы, обращайтесь к нашему персональному менеджеру @blikvpnhelp.",
        reply_markup=reply_markup
    )

async def send_android_message(chat_id, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Hiddify", url="https://play.google.com/store/apps/details?hl=ru&id=app.hiddify.com&utm_source=chatgpt.com")]

    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await context.bot.send_message(
        chat_id=chat_id,
        text="1. Установите приложение Hiddify из Google Play Store.\n2.Для получения ссылки на подключение нашего сервера напишите вашему личному менеджеру @blikvpnhelp. Обратите внимание на то, что при возникновения любого вопроса, вы всегда можете обратиться к вашему личному менеджеру. Мы трудимся для вас 24/7!!\n3.В приложении Hiddify выберите регион Другой, затем в правом верхнем углу нажмите на «+» и выберите «вставить из буфера обмена » \n4. Включите VPN. Дайте разрешение приложению на создание туннеля.\n\nТеперь вы можете использовать BLIK! 🎉",
        reply_markup=reply_markup
    )

async def send_iphone_message(chat_id, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Streisand", url="https://apps.apple.com/ru/app/streisand/id6450534064")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await context.bot.send_message(
        chat_id=chat_id,
        text="1. Установите приложение Streisand из App Store.\n2.Для получения ссылки на подключение нашего сервера напишите вашему личному менеджеру @blikvpnhelp. Обратите внимание на то, что при возникновения любого вопроса, вы всегда можете обратиться к вашему личному менеджеру. Мы трудимся для вас 24/7!!\n3.В приложении Streisand в правом верхнем углу нажмите на «+», затем выберите «вставить из буфера» \n4. Включите VPN. Дайте разрешение приложению на создание туннеля.\n\nТеперь вы можете использовать BLIK! 🎉",
        reply_markup=reply_markup
    )

async def send_help_message(chat_id, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Написать менеджеру 👨‍💻", url="https://t.me/blikvpnhelp")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await context.bot.send_message(
        chat_id=chat_id,
        text="Благодарим вас за использование BLIK VPN!✨\n\nЕсли у вас возникли вопросы или вам нужна помощь, наша служба поддержки всегда готова помочь.\nОбращайтесь к нашему персональному менеджеру @blikvpnhelp, и мы оперативно решим ваш вопрос.",
        reply_markup=reply_markup
    )
    


async def send_confidence_message(chat_id, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Я прочитал(а) ✅", callback_data="delete")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await context.bot.send_message(
        chat_id=chat_id,
        text="Политика конфиденциальности Telegram бота @BLIKVPN\n\nАдминистрация Telegram бота @blikbpnbot обязуется сохранять вашу конфиденциальность в Интернете. Мы уделяем большое значение охране предоставленных вами данных. Наша политика конфиденциальности основана на требованиях политик конфиденциальности Telegram и магазинов Apple и Google.\nМы не собираем и не обрабатываем персональные данные пользователей. Наш Telegram бот в целях осуществления работы сервиса использует только неперсонализированный Telegram ID.\n\nСбор и использование персональных данных\nМы не запрашиваем и не собираем никаких персональных данных. Все данные пользователей в нашем сервисе привязаны только к неперсонализированному Telegram ID.\nКогда вы запускаете Telegram бот @blikvpnbot, Telegram автоматически передает нам только ваш Telegram ID, который не дает нам доступа к вашей личной информации.\n\nХранение данных, изменение и удаление\nПользователь, предоставивший свой Telegram-ID нашему Telegram боту @blikvpnbot имеет право на удаление своих данных, привязанных к Telegram ID, кроме информации о блокировке пользователя.\n\nРаскрытие информации третьим лицам\nМы не продаем, не используем и не раскрываем третьим лицам какие-либо данные своих пользователей для каких-либо целей.\n\nПредоставление информации детям\nЕсли вы являетесь родителем или опекуном, и вы знаете, что ваши дети предоставили нам свои данные без вашего согласия, свяжитесь с нами.\n\nИзменения в политике конфиденциальности\nTelegram бот @blikvpnbot может обновлять нашу политику конфиденциальности время от времени. Мы сообщаем о любых изменениях, разместив новую политику конфиденциальности на этой странице. Если вы оставили данные у нас, то мы оповестим вас об изменении в политике конфиденциальности при помощи бота @hitvpnbot.\n\nОбратная связь, заключительные положения\nСвязаться с администрацией Telegram бота @blikvpnbot по вопросам, связанным с политикой конфиденциальности можно с помощью контактной информации указанной в разделе Помощь нашего бота. Если вы не согласны с данной политикой конфиденциальности, вы не можете пользоваться услугами Telegram бота @blikvpnbot.\n",
        reply_markup=reply_markup
    )

# Обработчик команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Создаем клавиатуру с двумя кнопками, которые инициируют callback-запросы
    keyboard = [
        [InlineKeyboardButton("Подключиться 🚀", callback_data="connect")],
        [InlineKeyboardButton("Помощь❔", callback_data="help")],
        [InlineKeyboardButton("Конфиденциальность 🔒", callback_data="confidence")]
    
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    user = update.effective_user
    name = user.username if user.username else user.first_name
    text = (
        "Привет, "+name+"! 👋 Добро пожаловать в BLIK VPN!\n"
        "\n"
        "🔥 Быстрый, безопасный и стабильный VPN-сервис для свободного интернета без ограничений!\n"
        "\n"
        "✅ Высокая скорость – наслаждайся потоковым видео, играми и загрузками без лагов.\n"
        "🔒 Надёжная защита – шифруем твой трафик и скрываем IP-адрес.\n"
        "🚀 Обход блокировок – доступ ко всем сайтам и сервисам, где бы ты ни был.\n"
        "🌍 Серверы по всему миру.\n"
        "⏳ Без ограничений – никаких лимитов на трафик и скорость.\n"
        "🛠 Простота использования – подключение за секунды без сложных настроек.\n"
        "💬 Поддержка 24/7 – всегда на связи, чтобы помочь тебе.\n"
        "\n"
        "Готов начать? Нажимай «Подключиться» и пользуйся интернетом без границ! 🚀\n"
    )
    await update.message.reply_text(text, reply_markup=reply_markup)


# Обработчик команды /connect
async def connect(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await send_connect_message(update.effective_chat.id, context)

# Обработчик команды /android
async def android(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await send_android_message(update.effective_chat.id, context)

# Обработчик команды /iphone
async def iphone(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await send_iphone_message(update.effective_chat.id, context)

# Обработчик команды /pay
async def pay(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await send_pay_message(update.effective_chat.id, context)

# Обработчик команды /help
async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await send_help_message(update.effective_chat.id, context)

# Обработчик команды /confidence
async def confidence(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await send_confidence_message(update.effective_chat.id, context)


# Callback-обработчик для inline кнопок
async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()  # Обязательно нужно ответить на callback-запрос
    data = query.data

    if data == "connect":
        await send_connect_message(query.message.chat.id, context)
    elif data == "pay":
        await send_pay_message(query.message.chat.id, context)
    elif data == "android":
        await send_android_message(query.message.chat.id, context)
    elif data == "iphone":
        await send_iphone_message(query.message.chat.id, context)
    elif data == "help":
        await send_help_message(query.message.chat.id, context)
    elif data == "confidence":
        await send_confidence_message(query.message.chat.id, context)
    elif data == "delete":
        await query.delete_message()
    else:
        pass


# Функция для установки команд бота (для бокового меню в Telegram)
async def set_commands(app: Application) -> None:
    commands = [
        BotCommand("start", "🚀 Подключение VPN 🚀"),
        BotCommand("pay", "💸 Оплата подписки 💸"),
        BotCommand("help", "💬 Поддержка 💬"),
        BotCommand("confidence", "🔒 Политика конфеденциальности 🔒"),
    ]
    await app.bot.set_my_commands(commands)


def main() -> None:
    # Замените на ваш токен (рекомендуется обновить токен, если он был опубликован)
    token = "8023702786:AAF3bhiqfw-yqmpQt_K8Q7f0NU1x3ccjegs"
    
    # Создаем приложение бота с post_init для установки команд
    application = Application.builder().token(token).post_init(set_commands).build()
    
    # Регистрируем обработчики команд
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("connect", connect))
    application.add_handler(CommandHandler("pay", pay))
    application.add_handler(CommandHandler("android", android))
    application.add_handler(CommandHandler("iphone", iphone))
    application.add_handler(CommandHandler("help", help))
    application.add_handler(CommandHandler("confidence", confidence))
    # Регистрируем обработчик callback-запросов для inline кнопок
    application.add_handler(CallbackQueryHandler(button_callback))
    
    # Запускаем бота (polling)
    application.run_polling()


if __name__ == '__main__':
    main()
