# -- coding: utf-8 --
import math
from odoo import fields, models, exceptions, api
from datetime import datetime, timedelta
from odoo.exceptions import ValidationError
from num2words import num2words
from odoo import fields, models, exceptions, api
from datetime import datetime, timedelta
from odoo.exceptions import ValidationError
from num2words import num2words

class fact2(models.Model):
    _inherit = 'account.invoice'

    @api.multi
    def concatenar_facturas(self):
        lista = list()

        inv = None
        for i in self:
            lista.append(i.id)
            if len(i.related_invoices) > 0:
                for related in i.related_invoices:
                    lista.append(related.id)
            inv = self.env['account.invoice'].browse(lista)
        return inv

    def agregar_punto_de_miles(self,numero,moneda):
        # numero_con_punto='.'.join([str(int(numero))[::-1][i:i+3] for i in range(0,len(str(int(numero))),3)])[::-1]
        # return numero_con_punto
        if moneda != self.env.user.company_id.currency_id.id:
            entero=int(numero)
            decimal='{0:.2f}'.format(numero-entero)
            entero_string = '.'.join([str(int(entero))[::-1][i:i + 3] for i in range(0, len(str(int(entero))), 3)])[::-1]
            # if decimal == '0.00':
                # numero_con_punto = entero_string
            # else:
            decimal_string=str(decimal).split('.')
            numero_con_punto=entero_string+','+decimal_string[1]
            mon=self.env['res.currency'].browse(moneda)
            numero_con_punto = mon.name + numero_con_punto
        else:
            if numero > 0:
                numero_con_punto='.'.join([str(int(numero))[::-1][i:i+3] for i in range(0,len(str(int(numero))),3)])[::-1]
            else:
                numero*=-1
                numero_con_punto = '.'.join([str(int(numero))[::-1][i:i + 3] for i in range(0, len(str(int(numero))), 3)])[::-1]
                numero_con_punto='-'+numero_con_punto
        num_return=numero_con_punto
        return num_return

    def sacacoma(self, n):
        return int(n)

    def sacacorchete(self, n):
        a = n.split("]")
        print(n)
        print(a)
        print(a[-1])
        b = len(a)
        # if(b>0):
        #     return a[1]
        # else:
        #     return a[0]
        return a[-1]


    # funciones para gigi

    def numerodetalleventa(self):
        a = len(self.invoice_line_ids)
        print(a)
        return

    def vercadenaexenta(self, p):
        print('hola')
        print(p)
        a = int(p)
        # a = p.find("Exento")
        # print(a)

        aux='nook'
        if(a == 0):
            aux = 'ok'

        print(aux)
        return aux


    def vercadenacinco(self, p):
        a = int(p)
        aux = 'nook'
        if(a == 5):
            aux = 'ok'

        print(aux)
        return aux

    def vercadenadiez(self, p):
        a = int(p)
        aux = 'nook'
        if(a == 10):
            aux = 'ok'
        return aux

    # def agregar_punto_de_miles(self,numero):
    #     numero_con_punto='.'.join([str(int(numero))[::-1][i:i+3] for i in range(0,len(str(int(numero))),3)])[::-1]
    #     return numero_con_punto

    def calcular_letras(self,numero,moneda):
        # letras=self.monto_en_letras = num2words(numero, lang='es').upper()
        if moneda!=self.env.user.company_id.currency_id.id:
            nuevo_numero = str(numero).split('.')
            entero =  num2words(int(nuevo_numero[0]), lang='es').upper()
            if len(nuevo_numero[1]) == 1:
                if nuevo_numero[1] == '0':
                    decimal = num2words(int(nuevo_numero[1]), lang='es').upper()
                else:
                    decimal = num2words(int(nuevo_numero[1]+'0'), lang='es').upper()
            else:
                decimal = num2words(int(nuevo_numero[1]), lang='es').upper()
            letras = 'DOLARES AMERICANOS '+ entero + ' CON ' + decimal + ' CENTAVOS'
        else:
            letras = num2words(numero, lang='es').upper()
            letras= 'GUARANIES '+ letras
        letras_return=letras+'--- '
        return letras_return
        # return letras

    def redondeo(self,n):
        print('hola')
        a = round(n)
        return a

    @api.multi
    def invoice_print(self):
        """
        Funcion heredada del original account.invoice para que  referencie al QWEB de la Factura
        """

        return self.env.ref('report_factura_gigigogo10').report_action(self)


    def elcalculo(self):
        return '10.000'

    def vercredito(self, p):
        # print('hola')
        # print(p)
        a = p.find("redito")
        # print(a)

        aux='nook'
        if(a > -1):
            aux = 'ok'
        return aux

    def vercontado(self, p):
        # print('hola')
        # print(p)
        a = p.find("ontado")
        # print(a)

        aux='nook'
        if(a > -1):
            aux = 'ok'
        #
        # print(aux)
        return aux

    def cortaracincuenta(self, p):
        a = str(p)
        print (a)
        c = 'hola puto'
        d = 'alamierda'
        print (a[0:50])
        return a[0:50]