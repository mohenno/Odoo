# -*- coding: utf-8 -*-
from odoo import http

# class CitasMadl(http.Controller):
#     @http.route('/citas_madl/citas_madl/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/citas_madl/citas_madl/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('citas_madl.listing', {
#             'root': '/citas_madl/citas_madl',
#             'objects': http.request.env['citas_madl.citas_madl'].search([]),
#         })

#     @http.route('/citas_madl/citas_madl/objects/<model("citas_madl.citas_madl"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('citas_madl.object', {
#             'object': obj
#         })