from odoo import api, fields, models, _
from datetime import date

class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Hospital Patient'
    _inherit = ['mail.thread','mail.activity.mixin']

    name = fields.Char(string='Patient Name', required=True, tracking=True)
    date_of_birth = fields.Date(string='Date of Birth',tracking=True)
    gender = fields.Selection([
        ('male','Male'),
        ('female','Female')
    ], string='Gender', tracking=True)
    ref = fields.Char(string='Reference', default='PAT', tracking=True) #default value set
    age = fields.Integer(string='Age', compute='_compute_age', readonly=False)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirmed'),
        ('approve', 'Approved'),
        ('cancel', 'Cancelled')
    ], string='Status', tracking=True, default='draft')
    patient_image = fields.Binary(string='Image')
    note = fields.Text(string='Description')
    active = fields.Boolean('Active', default=True)
    sl_no = fields.Char(string='SL NO', required=True, copy=False, readonly=True, default=lambda self: _('New'))
    appointment_ids = fields.One2many('hospital.appointment', 'patient_id', string='Appointments')
    doctor_id = fields.Many2one('hospital.doctor', string='Doctor')


    @api.depends('date_of_birth')
    def _compute_age(self):
        today = date.today()
        for rec in self:
            if rec.date_of_birth:
                rec.age = today.year - rec.date_of_birth.year
            else:
                rec.age = 0

    # statusbar click action
    @api.model
    def action_draft(self):
        for rec in self:
            rec.state = 'draft'
        # self.state = 'draft'


    def action_confirm(self):
        self.state = 'confirm'

    def action_approve(self):
        self.state = 'approve'

    def action_cancel(self):
        self.state = 'cancel'


    # generate number create
    @api.model
    def create(self, vals):
        if not vals.get('note'):
            vals['note'] = 'New Patient'
        if vals.get('sl_no', _('New')) == _('New'):
            vals['sl_no'] = self.env['ir.sequence'].next_by_code('patient.patient') or _('New')
        res = super(HospitalPatient, self).create(vals)
        return res

    #name get function
    # def name_get(self):
    #     result = []
    #     for rec in self:
    #         name = rec.ref + ' ' + rec.name
    #         result.append((rec.id, name))
    #     return result



