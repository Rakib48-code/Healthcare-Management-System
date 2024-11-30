from odoo import api, fields, models

class CreateAppointmentWizard(models.TransientModel):
    _name = 'create.appointment.wizard'
    _description = 'Create Appointment Wizard'

    name = fields.Char('Name', required=True)
    patient_id = fields.Many2one('hospital.patient', string='Patient', required=True)


    def action_create(self):
        print('Button is clicked')