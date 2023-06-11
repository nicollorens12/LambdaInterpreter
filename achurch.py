from antlr4 import *
from lcLexer import lcLexer
from lcParser import lcParser
from lcVisitorArbol import lcVisitorArbol
from lcEval import functionsArbre
from arbre import *
from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import pydot

TOKEN: Final = '5804637848:AAEo6uDhUFyrCLDCV4TD3C8991EeRVquhsc'
BOT_USERNAME: Final = "@NicoLambda_bot"

eArbol = lcVisitorArbol()


def idInUse(id:int,ids:list)-> bool:
    for ida in ids:
        if ida == id:
            return True
    return False


def recorrer_arbol(arbol: Arbre, parent_node: pydot.Node, id: int, ids: list, graf:pydot.Dot):
    match arbol:
        case Buit():
            return
        case Node(x,Buit(),Buit()):
            while idInUse(id,ids):
                id = id + 1
            node = pydot.Node(id,label = x)
            graf.add_node(node)
            ids.append(id)
            
            if parent_node.get_name() != "Root":
                graf.add_edge(pydot.Edge(parent_node.get_name(),node.get_name(), color ="black"))
            
            return
        
        case Node("\\",e,d):
            while idInUse(id,ids):
                id = id + 1
            node = pydot.Node(id, label = "λ" + e.val)
            graf.add_node(node)
            ids.append(id)
            
            if parent_node.get_name() != "Root":
                graf.add_edge(pydot.Edge(parent_node.get_name(),node.get_name(), color ="black"))

            recorrer_arbol(d,node,id,ids,graf)
            return
        
        case Node("λ",e,d):
            while idInUse(id,ids):
                id = id + 1
            node = pydot.Node(id,label = "λ" + e.val)
            graf.add_node(node)
            ids.append(id)
            
            if parent_node.get_name() != "Root":
                graf.add_edge(pydot.Edge(parent_node.get_name(),node.get_name(), color ="black"))

            recorrer_arbol(d,node,id,ids,graf)
            return
        
        case Node(x,e,d):
            while idInUse(id,ids):
                id = id + 1    
            node = pydot.Node(id, label = "@")
            graf.add_node(node)
            ids.append(id)
            
            if parent_node.get_name() != "Root":
                graf.add_edge(pydot.Edge(parent_node.get_name(),node.get_name(), color ="black"))
 
            recorrer_arbol(e,node,id,ids,graf)
            recorrer_arbol(d,node,id,ids,graf)
            return


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
            respostes.append(macro + "≡" +abre2String(eArbol.mapMacros[macro]))
        for resposta in respostes:
            await update.message.reply_text(resposta)


# FUNCIO PER NO PERMETRE OPERAR AMB MACROS NO EXISTENTS 

    
# RESPOSTES BOT

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
    respostes = []
    farbre.respuesta_evaluada = []
    for arbol in arboles:
 
        terme, arb = arbol
        respostes = []
        respostes.append((abre2String(arb),arb))
        respostes = respostes + farbre.evaluar(arb)
        
    for resposta in respostes:
        ans,arbol_graf = resposta
        print()
        await update.message.reply_text(ans)
        if not equal(arbol_graf,Buit()):
            ids = []
            graf = pydot.Dot(graph_type='digraph')
            ids.append(0)
            recorrer_arbol(arbol_graf,pydot.Node("Root"),0,ids,graf)
            graf.write_png("output.png")
            
            await context.bot.send_document(chat_id=update.effective_chat.id, document=open('output.png', 'rb'))
            
   
    eArbol.arboles = []  
    
# GESTIONAMENT ERRORS BOT

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Update {update} caused error {context.error}")
    

if __name__ == '__main__':  
    print("Bot Arrancant...")
    app = Application.builder().token(TOKEN).build()
     
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
    
    
    
    