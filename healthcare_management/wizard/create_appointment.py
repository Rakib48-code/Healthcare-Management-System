from odoo import api, fields, models, _


class CreateAppointmentWizard(models.TransientModel):
    _name = 'create.appointment.wizard'
    _description = 'Create Appointment Wizard'

    date_appointment = fields.Date('Date', required=False)
    patient_id = fields.Many2one('hospital.patient', string='Patient', required=True)
    appointment_serial_no = fields.Integer(string='Appointment Serial')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], string='Gender')
    date_of_birth = fields.Date(string='Date of Birth')

    def action_create(self):
        vals = {
            'patient_id': self.patient_id.id,
            'appointment_date': self.date_appointment,
            'appointment_serial_no': self.appointment_serial_no,
            'gender': self.gender,
            'date_of_birth': self.date_of_birth,
        }
        appointment_rec = self.env['hospital.appointment'].create(vals)
        return {
            'name': _('Appointment'),
            'view_mode': 'form',
            'res_model': 'hospital.appointment',
            'res_id': appointment_rec.id,
            'type': 'ir.actions.act_window',
            'target': 'new',
        }

    # def action_view(self):
    #     action = self.env.ref('healthcare_management.view_patient_menu').read()[0]
    #     action['domain'] = [('patient_id', '=', self.patient_id.id)]
    #     return action
