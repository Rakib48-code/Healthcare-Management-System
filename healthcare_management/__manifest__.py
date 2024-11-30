{
    'name' : 'Healthcare Management System',
    'category' : 'Health Care System',
    'summary' : 'Mange Heatlcare',
    'sequence' : '-100',
    'depends' : ['base','mail'],
    'data' : [
        'security/ir.model.access.csv',
        'data/patient_data.xml',
        'wizard/create_appointment_view.xml',
        'views/heatlcare_menu.xml',
        'views/view_patient_menu.xml',
        'views/view_female_patient.xml',
        'views/view_male_patient.xml',
        'views/view_kids_patient.xml',
        'views/view_appointment.xml',
    ],
    'demo' : [
        'demo/demo.xml',
    ],
    'installable' : True,
    'application' : True,
}