from __future__ import print_function, division

import unittest
from Cartas import Carta, Mazo, Mano, ManoPersona


class Test(unittest.TestCase):

    def testManoEliminarParejas(self):
        print("-----------------------------------Eliminar parejas---------------------------------------------")
        mazo = Mazo()
        mazo.barajar()
        mano = ManoPersona("Jugador1")
        mazo.mover_cartas(mano, 5)
        mano.imprimir()
        mano.eliminar_parejas()
        mano.imprimir()

    def testMazoEliminar(self):
        print("-------------------------------Eliminar-----------------------------------------------------")
        mazo = Mazo()
        mazo.imprimir()
        carta23 = Carta(2, 3)
        print("se va a eliminar la carta: {0}".format(carta23))
        mazo.eliminar_carta(carta23)
        mazo.imprimir()
        self.assertFalse(mazo.esta_carta(carta23))

    def testMazoBarajar(self):
        print("--------------------------------Barajar---------------------------------------------")
        mazo = Mazo()
        mazo.imprimir()
        mazo.barajar()
        mazo.imprimir()
    
    def testMazoMoverCartas(self):
        print("-----------------------------------Mover-------------------------------------------------")
        mazo = Mazo()
        mano = Mano()
        mazo.mover_cartas(mano, 5)
        mazo.imprimir()
        mano.imprimir()
        self.assertEqual(mano.cartas.__len__(), 5)

    
        

if __name__ == "__main__":
    unittest.main()
