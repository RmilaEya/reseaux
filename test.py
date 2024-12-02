from netmiko import ConnectHandler

# Informations de connexion au routeur
cisco_router = {
   'device_type': 'cisco_ios',
   'host': 'sandbox-iosxe-latest-1.cisco.com',
   'username': 'admin',
   'password': 'C1sco12345',
   'secret': 'bonjour',  # Mot de passe pour entrer en mode privilégié
   'port': 22,
}

# Connexion au routeur
conn = ConnectHandler(**cisco_router)

# Passer en mode privilegie (enable) avec le mot de passe 'secret'
conn.enable()

# Executer la commande 'show ip int brief'
result = conn.send_command('show ip int brief')
with open("text.txt", "w") as file:
        file.write(result)


result1 = conn.send_command('show clock')

# Afficher le resultat
print(result1)


config_commands = [
    "interface loopback 0",
    "ip address 10.8.8.8 255.255.255.240",  # Masque /28
    "exit",  # Sortir de l'interface
]

# Envoi des commandes de configuration
config = conn.send_config_set(config_commands)


# Fermer la connexion
conn.disconnect()
