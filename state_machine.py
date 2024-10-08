from transitions import Machine  # pip install transitions

# Klasse `Process` repräsentiert einen Ablauf mit drei Schritten
class Process:
    # Definiert drei Zustände: step1, step2, finish
    states = ['step1', 'step2', 'finish']

    def __init__(self):
        # Initialisiere die Maschine mit dem Startzustand 'step1'
        self.machine = Machine(model=self, states=Process.states, initial='step1')
        # Definiere eine Transition von 'step1' zu 'step2'
        self.machine.add_transition('go_to_step2', 'step1', 'step2')
        # Definiere eine Transition von 'step2' zu 'finish'
        self.machine.add_transition('finish_process', 'step2', 'finish')

# Erstelle eine Instanz der Klasse `Process`
process = Process()

# Zeige den aktuellen Zustand ('step1')
print(process.state)  # Output: step1

# Führe die Transition zu 'step2' durch
process.go_to_step2()
print(process.state)  # Output: step2

# Führe die Transition zu 'finish' durch
process.finish_process()
print(process.state)  # Output: finish
