from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler, MessageHandler, filters
import asyncio
import nest_asyncio
import re
from Key import key

nest_asyncio.apply()

TOKEN = key

async def Start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if "items" not in context.user_data:

        context.user_data["items"] = []

    await update.message.reply_text(
        "привет, я бот тг" + "\nсо мной ты можешь вести список дел по учебе", reply_markup = GetKeyboard()
        )

def GetKeyboard():
    keyboard = [
        [InlineKeyboardButton("добавить в список", callback_data="add")],
        [InlineKeyboardButton("удалить из списка", callback_data="delete")],
        [InlineKeyboardButton("очистить список", callback_data="clear")]
    ]

    return InlineKeyboardMarkup(keyboard)

async def ShowList(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    name = user.full_name
    
    if "items" not in context.user_data:

        context.user_data["items"] = []

    items = context.user_data.get("items", [])

    if not items:
       text = (f"{name}, твой список пуст")

    else:
        text = f"список для ~{name}~\n\n" + "\n".join(items)

    if update.message:
        await update.effective_message.reply_text(text, reply_markup = GetKeyboard())
    else:
        await update.callback_query.message.reply_text(text, reply_markup = GetKeyboard())

async def ButtonHandler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    items = context.user_data["items"]

    context.user_data["action"] = query.data
    if query.data == "add":

        context.user_data["state"] = "waiting_for_input"
        await query.edit_message_text(text=f"что добавить?")

    elif query.data == "delete":
         
        context.user_data["state"] = "waiting_for_input"
        await query.edit_message_text(text=f"что удалить?")
    else:

        items.clear()
        await ShowList(update, context)
        context.user_data["action"] = None

async def TextHandler(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if context.user_data["state"] == "waiting_for_input":
        text = update.message.text
        action = context.user_data.get("action")

        items = context.user_data["items"]
        lines = [line.strip() for line in re.split(r'[\n,;]+', text) if line.strip()]

        if action == "add":
            items.extend(lines)
            await ShowList(update, context)
        elif action == "delete":
            for line in lines:
                if line in items:
                    items.remove(line)
                    await ShowList(update, context)
                else:
                    await ShowList(update, context)

            

        context.user_data["action"] = None
        context.user_data["state"] = None

async def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", Start))
    app.add_handler(CommandHandler("show", ShowList))
    app.add_handler(CallbackQueryHandler(ButtonHandler))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, TextHandler))

    print("Бот запущен")

    await app.run_polling(close_loop=False)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
