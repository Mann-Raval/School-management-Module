from odoo import fields, models, api, _

class SchoolExam(models.Model):
    _name = "school.exam"
    _description = "Exam Table"

    name = fields.Char(string="Exam Name", required=True)
    exam_date = fields.Date(string="Exam Date", required=True)
    class_id = fields.Many2many('school.class', string="Class", required=True)
    subject_id = fields.Many2one('school.subject', string="Subject", required=True)
    total_marks = fields.Integer(string="Total Marks", required=True)
