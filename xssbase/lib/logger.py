import simple_chalk as chalk

def info(text):
 toPrint="[+] " + text
 print(chalk.blue.bold(toPrint))

def payload(text):
 toPrint="" + text
 print(chalk.blue.bold(toPrint))

def success(text):
 toPrint="[V] "+ text 
 print(chalk.green.bold(toPrint))

def ask(text):
 toPrint="[?] "+ text
 print(chalk.yellow.bold(toPrint))

def warning(text):
 toPrint="[!] "+ text
 print(chalk.yellow.bold(toPrint))

def error(text):
 toPrint="[?] "+ text
 print(chalk.red.bold(toPrint))