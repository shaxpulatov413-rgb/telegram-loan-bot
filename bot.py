import os
from telegram.ext import ApplicationBuilder

TOKEN = os.getenv("TOKEN")

app = ApplicationBuilder().token(TOKEN).build()

app.run_polling()
