from odoo import api, models, fields

class HospitalDoctor(models.Model):
    _name = 'hospital.doctor'
    _inherit = ['mail.thread','mail.activity.mixin']
    _description = 'Hospital Doctor'

    name = fields.Char(string='Name', required=True, tracking=True)
    age = fields.Integer('Age', tracking=True)
    gender = fields.Selection([
        ('male','Male'),
        ('female','Female'),
    ], string='Gender', required=True, tracking=True)
    note = fields.Text(string='Description')
    image = fields.Binary(string='Image')