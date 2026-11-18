from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import re

TOKEN = "9047622864:AAFqJfndoJt6wFTmZxZIxVnMQCR88jxbfHw"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Hallo, {update.effective_user.first_name}!")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Commands: /start, /help, /about\nКалькулятор: 5 + 3")

async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("I was made by Batyr Gelser, AITU College.")

async def calc(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = re.sub(" ", "", update.message.text)

    op = None
    for smb in "+-*/^%":
        if smb in text:
            op = smb
            break

    if op is None:
        await update.message.reply_text("Wrong enter. Example: 5 + 3")
        return

    try:
        a, b = map(float, text.split(op))

        if op == "+":
            result = a + b
        elif op == "-":
            result = a - b
        elif op == "*":
            result = a * b
        elif op == "/":
            result = a / b
        elif op == "^":
            result = a ** b
        else:
            result = a / 100 * b

        await update.message.reply_text(f"{a:g} {op} {b:g} = {result:g}")

    except ZeroDivisionError:
        await update.message.reply_text("I can't divide by zero")
    except ValueError:
        await update.message.reply_text("Wrong enter. Example: 5 + 3")

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("about", about))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, calc))

app.run_polling()