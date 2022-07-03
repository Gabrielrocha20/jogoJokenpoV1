import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
import jogo
from random import choice


class JogoJokenpo(QMainWindow, jogo.Ui_Jokenpo):
    def __init__(self, parent=None):
        super().__init__(parent)

        super().setupUi(self)
        self.maquina = None
        self.btnPedra.clicked.connect(self.pedra)
        self.btnPapel.clicked.connect(self.papel)
        self.btnTesoura.clicked.connect(self.tesoura)

        self.btnDepositar.clicked.connect(self.fichas)

        self._carteira = 0
        self._vitoria = 0

    @property
    def carteira(self):
        return self._carteira

    @carteira.setter
    def carteira(self, value):
        self._carteira = value

    @property
    def vitoria(self):
        return self._vitoria

    @vitoria.setter
    def vitoria(self, value):
        self._vitoria = value

    def fichas(self):
        deposito = self.inputDepositar.text()
        self.carteira += int(deposito)
        self.labelFichas.setText(f'Fichas \n {str(self.carteira)}')

    def pedra(self, valor):
        valor = self.inputValor.text()
        if int(valor) > self._carteira:
            self.labelJogo.setText('FICHAS INSUFICIENTES')
        else:
            self.carteira -= int(valor)
            self.labelFichas.setText(f'Fichas \n {str(self.carteira)}')
            if self._vitoria >= 3:
                self.maquina = choice(['PAPEL', 'PEDRA'])
            else:
                self.maquina = choice(['PAPEL', 'PEDRA', 'TESOURA'])

            if self.maquina == 'PEDRA':
                self.labelJogo.setText('EMPATE')
                self.labelJogo.setStyleSheet("color:red")
                self.carteira += int(valor) / 2
                self.labelFichas.setText(f'Fichas \n {str(self.carteira)}')
                self.vitoria -= 0.5
            if self.maquina == 'PAPEL':
                self.labelJogo.setText('DERROTA')
                self.labelJogo.setStyleSheet("color:red")
                self.labelFichas.setText(f'Fichas \n {str(self.carteira)}')
                self.vitoria -= 1
            if self.maquina == 'TESOURA':
                self.labelJogo.setText('VITORIA')
                self.labelJogo.setStyleSheet("color:green")
                self.carteira += int(valor) * 2
                self.labelFichas.setText(f'Fichas \n {str(self.carteira)}')
                self.vitoria += 1

    def papel(self, valor):
        valor = self.inputValor.text()
        if int(valor) > self._carteira:
            self.labelJogo.setText('FICHAS INSUFICIENTES')
        else:
            self.carteira -= int(valor)
            self.labelFichas.setText(f'Fichas \n {str(self.carteira)}')
            if self._vitoria >= 3:
                self.maquina = choice(['PAPEL', 'PEDRA'])
            else:
                self.maquina = choice(['PAPEL', 'PEDRA', 'TESOURA'])
            if self.maquina == 'PAPEL':
                self.labelJogo.setText('EMPATE')
                self.labelJogo.setStyleSheet("color:red")
                self.carteira += int(valor) / 2
                self.labelFichas.setText(f'Fichas \n {str(self.carteira)}')
                self.vitoria -= 0.5
            if self.maquina == 'TESOURA':
                self.labelJogo.setText('DERROTA')
                self.labelJogo.setStyleSheet("color:red")
                self.labelFichas.setText(f'Fichas \n {str(self.carteira)}')
                self.vitoria -= 1
            if self.maquina == 'PEDRA':
                self.labelJogo.setText('VITORIA')
                self.labelJogo.setStyleSheet("color:green")
                self.carteira += int(valor) * 2
                self.labelFichas.setText(f'Fichas \n {str(self.carteira)}')
                self.vitoria += 1

    def tesoura(self, valor):
        valor = self.inputValor.text()
        if int(valor) > self._carteira:
            self.labelJogo.setText('FICHAS INSUFICIENTES')
        else:
            self.carteira -= int(valor)
            self.labelFichas.setText(f'Fichas \n {str(self.carteira)}')
            if self._vitoria >= 3:
                self.maquina = choice(['PAPEL', 'TESOURA'])
            else:
                self.maquina = choice(['PAPEL', 'PEDRA', 'TESOURA'])
            if self.maquina == 'TESOURA':
                self.labelJogo.setText('EMPATE')
                self.labelJogo.setStyleSheet("color:red")
                self.carteira += int(valor) / 2
                self.labelFichas.setText(f'Fichas \n {str(self.carteira)}')
                self.vitoria -= 0.5
            if self.maquina == 'PEDRA':
                self.labelJogo.setText('DERROTA')
                self.labelJogo.setStyleSheet("color:red")
                self.labelFichas.setText(f'Fichas \n {str(self.carteira)}')
                self.vitoria -= 1
            if self.maquina == 'PAPEL':
                self.labelJogo.setText('VITORIA')
                self.labelJogo.setStyleSheet("color:green")
                self.carteira += int(valor) * 2
                self.labelFichas.setText(f'Fichas \n {str(self.carteira)}')
                self.vitoria += 1


if __name__ == '__main__':
    app = QApplication(sys.argv)
    jg = JogoJokenpo()
    jg.show()
    app.exec_()
