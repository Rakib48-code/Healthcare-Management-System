from odoo import api, fields, models

class CreateAppointmentWizard(models.TransientModel):
    _name = 'create.appointment.wizard'
    _description = 'Create Appointment Wizard'

    date_appointment = fields.Datetime('Date', required=True)
    patient_id = fields.Many2one('hospital.patient', string='Patient', required=True)


    def action_create(self):
        vals = {
            'patient_id' : self.patient_id.id,
            'appointment_time' : self.date_appointment,
        }
        self.env['hospital.appointment'].create(vals)