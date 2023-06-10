from antlr4 import *
from lcLexer import lcLexer
from lcParser import lcParser
from lcVisitorArbol import lcVisitorArbol
from lcEval import functionsArbre
from arbre import *
from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN: Final = '5804637848:AAEo6uDhUFyrCLDCV4TD3C8991EeRVquhsc'
BOT_USERNAME: Final = "@NicoLambda_bot"

eArbol = lcVisitorArbol()

# COMANDAMENTS

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    eArbol.mapMacros = {}
    eArbol.arboles = []
    await update.message.reply_text("AChurchBot! \n Benvingut " + str(update.message.from_user.first_name) + "!")
    
async def author_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("AChurchBot!\n @ Nicolas Llorens Somalo, 2023")
    
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("/start \n/author \n/help \n/macros \n? Expressió λ-Càlcul")
    
async def macros_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    respostes = []
    if len(eArbol.mapMacros) == 0:
        await update.message.reply_text("Encara no hi ha cap macro definida en el sistema")
    else:
        for macro in eArbol.mapMacros:
            respostes.append(macro + "≡" +toStringArbre(eArbol.mapMacros[macro]))
        for resposta in respostes:
            await update.message.reply_text(resposta)


# FUNCIO PER NO PERMETRE OPERAR AMB MACROS NO EXISTENTS 
    
# RESPOSTES

async def enviar_resposta(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    missatge: str = update.message.text
    input_stream = InputStream(missatge)
    lexer = lcLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = lcParser(token_stream)
    tree = parser.root()
    farbre = functionsArbre()
    eArbol.visit(tree)
    
    arboles = eArbol.arboles
    resposta = []
    farbre.respuesta_evaluada = []
    for arbol in arboles:
        terme, arb = arbol
        astring = toStringArbre(arb)
        resposta.append(astring)
        resposta = resposta + farbre.evaluar(arb)
        print(len(resposta))
    for mensaje in resposta:
        await update.message.reply_text(mensaje)
    print("Afegir macro size: " + str(len(eArbol.mapMacros)))
    eArbol.arboles = []
    
    
# GESTIONAMENT ERRORS

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Update {update} caused error {context.error}")
    
    
    

if __name__ == '__main__':  
    print("Starting bot...")
    app = Application.builder().token(TOKEN).build()
    
    #if(eArbol is None):
    #    eArbol = lcVisitorArbol()
        
    # Comandes
    app.add_handler(CommandHandler('start',start_command))
    app.add_handler(CommandHandler('author',author_command))
    app.add_handler(CommandHandler('help',help_command))
    app.add_handler(CommandHandler('macros',macros_command))
    
    # Missatges
    app.add_handler(MessageHandler(filters.TEXT, enviar_resposta))
    
    # Errors
    app.add_error_handler(error)
    
    # Polling del bot
    print("Polling...")
    app.run_polling(poll_interval=1)
    
    
    
    