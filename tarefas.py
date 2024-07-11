class Tarefa:
    def __init__(self, descricao, prioridade):
        self.descricao = descricao
        self.prioridade = prioridade
        
class GerenciadorDeTarefas:
    def __init__(self):
        self.tarefas = []
        
    def adicionar(self, tarefa):
        self.tarefas.append(tarefa)
        
    def listar(self):
        for i, tarefa in enumerate(self.tarefas, start = 1):
            print(f"{i}. Descrição: {tarefa.descricao}, Prioridade: {tarefa.prioridade}")
            
if __name__ == "__main__":
    gerenciador = GerenciadorDeTarefas()
    
    while True:
        print("-------------------------------")
        print("1- Adicionar Tarefa")
        print("2- Listar Tarefa")
        print("3- Sair")
        print("-------------------------------")
        
        escolha = input("Escolha uma opção de acordo com o menu: ")
        
        if escolha == "1":
            descricao = input("Digite a descrição da tarefa: ")
            prioridade = input("Digite a prioridade da tarefa: ")
            tarefa = Tarefa(descricao, prioridade)
            gerenciador.adicionar(tarefa)
            
        elif escolha == "2":
            print("Lista de tarefas!!")
            gerenciador.listar()
            
        elif escolha == "3":
            print("Saindo do menu escolhas...")
            break
        
        else:
            print("Escolha inválida!! Tente de acordo com o menu indicado..")
