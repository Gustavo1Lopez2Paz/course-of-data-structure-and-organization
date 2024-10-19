import Node_sandbox as Ns

Juan = Ns.Node("Es jefe de jefes")
Yady = Ns.Node("Le gustan las flores")
Giovany = Ns.Node("Le gustan las princesas")

Juan.next_node = Giovany
Giovany.next_node = Yady

Giovany_data = Giovany.value
Yady_data = Yady.value

print(Giovany_data)
print(Yady_data)