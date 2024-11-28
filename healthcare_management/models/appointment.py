from odoo import api,fields, models, _

class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _description = 'Hospital Appointment'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    patient_id = fields.Many2one('hospital.patient', string='Patient', required=True, tracking=True)
    appointment_time = fields.Datetime(string='Appointment Time', default=fields.Datetime.now, tracking=True)
    booking_date = fields.Date(string='Booking Date', default=fields.Date.context_today, tracking=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], string='Gender', tracking=True)
    ref = fields.Char(string='Reference', tracking=True)
    state = fields.Selection([
        ('draft','Draft'),
        ('confirm','Confirmed'),
        ('approve','Approved'),
        ('cancel','Cancel')
    ], string='Status', tracking=True)
    note = fields.Text(string='Description')
    sl_no = fields.Char(string='SL NO', required=True, copy=False, readonly=True, default=lambda self: _('New'))


    @api.onchange('patient_id')
    def onchange_patient_id(self):
        self.ref = self.patient_id.ref


    @api.onchange('patient_id')
    def _onchange_gender(self):
        self.gender = self.patient_id.gender



    def action_draft(self):
        self.state = 'draft'

    def action_confirm(self):
        self.state = 'confirm'

    def action_approve(self):
        self.state = 'approve'

    def action_cancel(self):
        self.state = 'cancel'

    @api.model
    def create(self, vals):
        if not vals.get('note'):
            vals['note'] = 'New Patient'
        if vals.get('sl_no', _('New')) == _('New'):
            vals['sl_no'] = self.env['ir.sequence'].next_by_code('appointment.appointment') or _('New')
        res = super(HospitalAppointment, self).create(vals)
        return res