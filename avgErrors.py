import json

filename = "props_melbourne.json"

with open(filename, 'r') as propsFile:
    data=propsFile.read()

# parse file
obj = json.loads(data)

ctd = 0
readoutError = 0
for qubit in obj['qubits']:
    readoutError += qubit[4]['value']
    ctd += 1
readoutError = readoutError/ctd
print(f"Avg. readout error: {readoutError}")

ctd = 0
cxError = 0
for gate in obj['gates']:
    if gate['gate'] == 'cx':
        cxError += gate['parameters'][0]['value']
        ctd += 1
cxError = cxError/ctd
print(f"Avg. cxError error: {cxError}")
