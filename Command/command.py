class Command():
    """
    Essa interface serve para executar um commando passado. 
    Funciona como se o usuário interagisse com uma caixa preta que executa uma determinada ação quando um botão é clicado.
    O histórico de execuções também é salvo."""

    def execute():
        """Executa uma função e armazena num histórico."""
        pass

    def undo():
        """Desfaz uma ação executada"""
        pass
