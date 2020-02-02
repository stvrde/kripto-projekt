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
layout = [  [sg.Text("Blockchain", size=(30, 2),font=("Helvetica", 15))],
			[sg.Text("Vrsta mreže", size=(20, 1)), sg.Text(client.getblockchaininfo()["chain"])],
			[sg.Text("Broj blokova", size=(20, 1)), sg.Text(client.getblockchaininfo()["blocks"])],
			[sg.Text("Težina", size=(20, 1)), sg.Text(client.getblockchaininfo()["difficulty"])],
			[sg.Text("Veličina na disku", size=(20, 2)), sg.Text(client.getblockchaininfo()["size_on_disk"])],
            [sg.Text("Podaci o bloku po zelji", size=(25, 1),font=("Helvetica", 15))],
            [sg.Text('Unesi broj bloka koji zelis: '), sg.InputText(default_text="123123",size=(20,2)), sg.Submit('Submit')],
            [sg.Text("Blok s najvise transakcija u nekom rasponu", size=(35, 1),font=("Helvetica", 15))],
            [sg.Text('Unesi min range: '), sg.InputText(default_text="123120",size=(20,1))],
            [sg.Text('Unesi max range: '), sg.InputText(default_text="123125",size=(20,2)), sg.Submit('Find')],
            [sg.Button('Blockchaininfo'), sg.Button('Cancel')] ]
#print(client.getblockchaininfo())
#print(client.getblockstats(1000))
# Create the Window
window = sg.Window('Window Title', layout)
#print(client.getblockstats(169069))
def blockinfo(n):
    n=int(n)
    return client.getblockstats(n)
def txs(i,j):
    print(i,j)
    i=int(i)
    j=int(j)
    lista=[]
    for n in range(i,j):
        lista.append(int(client.getblockstats(n)["txs"]))
    return (max(lista),(lista.index(max(lista))+i)) #return most tx in range + block height
#print(txs(123120,123124))
#print(blockinfo(16969))
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read() 

    if event in (None, 'Cancel'):   # if user closes window or clicks cancel
        break
    if event in ('Walletinfo'):
    	sg.Popup(event, client.getblockchaininfo())
    if event in ('Blockchaininfo'):
    	sg.Popup(event, client.getblockchaininfo())
    if event in ('Submit'):
    	sg.Popup(event, blockinfo(values[0]))
    if event in ('Find'):
    	sg.Popup('Najvise transakcija u ovom range-u: ', txs(values[1],values[2])[0], 'ima blok: ',txs(values[1],values[2])[1])

window.close()