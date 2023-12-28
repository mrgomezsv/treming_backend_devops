# -*- coding: utf-8 -*-
# from odoo import http


# class TremingBackendDevops(http.Controller):
#     @http.route('/treming_backend_devops/treming_backend_devops', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/treming_backend_devops/treming_backend_devops/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('treming_backend_devops.listing', {
#             'root': '/treming_backend_devops/treming_backend_devops',
#             'objects': http.request.env['treming_backend_devops.treming_backend_devops'].search([]),
#         })

#     @http.route('/treming_backend_devops/treming_backend_devops/objects/<model("treming_backend_devops.treming_backend_devops"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('treming_backend_devops.object', {
#             'object': obj
#         })
