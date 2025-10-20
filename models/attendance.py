from odoo import fields, models, api, _

class SchoolAttendance(models.Model):
    _name = "school.attendance"
    _description = "Attendance Table"

    student_id = fields.Many2one('school.student', string="Student", required=True)
    class_id = fields.Many2one('school.class', related="student_id.class_id", string="Class", required=True)
    date = fields.Date(string="Date", required=True, default=fields.Date.today)
    status = fields.Selection([
        ('present', 'Present'),
        ('absent', 'Absent')
    ], string="Status", required=True)
