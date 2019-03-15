# -*- coding: utf-8 -*-
from odoo import http

# class FacturaRapidsoft(http.Controller):
#     @http.route('/factura_rapidsoft/factura_rapidsoft/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/factura_rapidsoft/factura_rapidsoft/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('factura_rapidsoft.listing', {
#             'root': '/factura_rapidsoft/factura_rapidsoft',
#             'objects': http.request.env['factura_rapidsoft.factura_rapidsoft'].search([]),
#         })

#     @http.route('/factura_rapidsoft/factura_rapidsoft/objects/<model("factura_rapidsoft.factura_rapidsoft"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('factura_rapidsoft.object', {
#             'object': obj
#         })