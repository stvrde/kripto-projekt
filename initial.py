import PySimpleGUI as sg

from bitcoinrpc.authproxy import AuthServiceProxy #, JSONRPCException

def connect_to_client(user, password, host, port):
    url = 'http://' + user + ':' + password + '@' + host + ':' + port
    return AuthServiceProxy(url)
host = 'blockchain.oss.unist.hr'
user = 'student'
password = 'WYVyF5DTERJASAiIiYGg4UkRH'
port = '8332'
client = connect_to_client(user, password, host, port)

#print(client.getdifficulty())
#print(client.verifychain())


sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text("Wallet", size=(30, 2),font=("Helvetica", 15)), sg.Text("Blockchain", size=(30, 2),font=("Helvetica", 15))],
			[sg.Text("Ime novčanika", size=(36, 1)), sg.Text(client.getwalletinfo()["walletname"]), sg.Text("Vrsta mreže", size=(20, 1)), sg.Text(client.getblockchaininfo()["chain"])],
			[sg.Text("Verzija novčanika", size=(30, 1)), sg.Text(client.getwalletinfo()["walletversion"]), sg.Text("Broj blokova", size=(20, 1)), sg.Text(client.getblockchaininfo()["blocks"])],
			[sg.Text("Stanje novčanika", size=(27, 1)), sg.Text(client.getwalletinfo()["balance"]), sg.Text("Težina", size=(20, 1)), sg.Text(client.getblockchaininfo()["difficulty"])],
			[sg.Text("Broj transakcija", size=(35, 1)), sg.Text(client.getwalletinfo()["txcount"]), sg.Text("Veličina na disku", size=(20, 1)), sg.Text(client.getblockchaininfo()["size_on_disk"])],
            [sg.Button('Blockchaininfo'),sg.Button('Walletinfo'), sg.Button('Cancel')] ]
#print(client.getblockchaininfo())
#print(client.getblockstats(1000))
# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()

    if event in (None, 'Cancel'):   # if user closes window or clicks cancel
        break
    if event in ('Walletinfo'):
    	sg.Popup(event, client.getwalletinfo())
    if event in ('Blockchaininfo'):
    	sg.Popup(event, client.getblockchaininfo())

window.close()
