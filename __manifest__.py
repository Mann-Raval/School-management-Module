{
    'name':'School Management',
    'version':'13.0.1.0.0',
    'category':'Education',
    'author':'Mann Raval',
    'license': 'AGPL-3',
    'summary':'School Management System',
    'description': """Module for managing a school:
        - Manage students
        - Manage teachers
        - Manage classes, subjects, attendance, marksheets, and exams""",
    'depends':['base','mail','web'],
    'data': [
        'security/ir.model.access.csv',
        'views/student.xml',
        'views/teacher.xml',
        'views/classes.xml',
        'views/subjects.xml',
        'views/attendance.xml',
        'views/marksheet.xml',
        'views/exams.xml',
        'views/marksheet_report_template.xml',
        'views/marksheet_report_action.xml',
        'data/sequence.xml',
    ],
    'demo':[],
    'qweb':[],
    'installable':True,
    'application':True,
    'auto_install':False
}