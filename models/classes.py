from odoo import fields, models

class SchoolClass(models.Model):
    _name = 'school.class'
    _description = 'Class Table'

    name = fields.Char(string='Class Name', required=True)
    class_code = fields.Char(string='Class Code', required=True)
    teacher_id = fields.Many2one('school.teacher', string='Class Teacher')
    student_ids = fields.One2many('school.student', 'class_id', string='Students')
    subject_ids = fields.Many2many('school.subject', string='Subjects')
    active = fields.Boolean(string='Active', default=True)