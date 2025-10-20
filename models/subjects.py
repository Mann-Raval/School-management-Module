from odoo import fields, models, api, _

class SchoolSubject(models.Model):
    _name = "school.subject"
    _description = "Subject Table"

    name = fields.Char(string="Subject Name", required=True)
    subject_code = fields.Char(string="Subject Code", required=True)
    teacher_id = fields.Many2many('school.teacher', 'name', string="Subject Teachers")
    class_ids = fields.Many2many('school.class', string="Classes")