from odoo import api,fields, models, _
from datetime import date

class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _description = 'Hospital Appointment'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'patient_id'

    patient_id = fields.Many2one('hospital.patient', string='Patient Name', required=True, tracking=True)
    appointment_date = fields.Date(string='Appointment Date', tracking=True)
    booking_date = fields.Date(string='Booking Date', default=fields.Date.context_today, tracking=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], string='Gender', related='patient_id.gender', readonly=False)
    ref = fields.Char(string='Reference', related='patient_id.ref', readonly=False)
    state = fields.Selection([
        ('draft','Draft'),
        ('confirm','Confirmed'),
        ('approve','Approved'),
        ('cancel','Cancel')
    ], string='Status', tracking=True, default='draft')
    note = fields.Text(string='Description')
    active = fields.Boolean('Active', default=True)
    sl_no = fields.Char(string='SL NO', required=True, copy=False, readonly=True, default=lambda self: _('New'))
    appointment_serial_no = fields.Integer(string='Appointment Serial')
    date_of_birth = fields.Date(string='Date of Birth', related='patient_id.date_of_birth',readonly=False)
    age = fields.Integer(string='Age',compute='_compute_age', readonly=False)
    doctors_id = fields.Many2one('hospital.doctor', string='Doctor')


    # age compute
    @api.depends('date_of_birth')
    def _compute_age(self):
        today = date.today()
        for r in self:
            if r.date_of_birth:
                r.age = today.year - r.date_of_birth.year
            else:
                r.age = 0



    # @api.onchange('patient_id')
    # def onchange_patient_id(self):
    #     self.ref = self.patient_id.ref


    # @api.onchange('patient_id')
    # def _onchange_gender(self):
    #     self.gender = self.patient_id.gender



    def action_draft(self):
        self.state = 'draft'

    def action_confirm(self):
        self.state = 'confirm'

    def action_approve(self):
        self.state = 'approve'

    def action_cancel(self):
        self.state = 'cancel'

    # generate sequence number
    @api.model
    def create(self, vals):
        if not vals.get('note'):
            vals['note'] = 'New Patient'
        if vals.get('sl_no', _('New')) == _('New'):
            vals['sl_no'] = self.env['ir.sequence'].next_by_code('appointment.appointment') or _('New')
        res = super(HospitalAppointment, self).create(vals)
        return res
