from odoo import fields, models, api, _

class SchoolMarksheet(models.Model):
    _name = "school.marksheet"
    _description = "Marksheet Table"

    name = fields.Char(string='Marksheet Name', required=True)
    student_id = fields.Many2one('school.student', string='Student', required=True)
    class_id = fields.Many2one('school.class', string='Class', related='student_id.class_id', store=True)
    total_marks = fields.Float(string='Total Marks', compute='_compute_total_marks', store=True)
    percentage = fields.Float(string='Percentage', compute='_compute_percentage', store=True)
    grade = fields.Char(string='Grade', compute='_compute_grade', store=True)
    marksheet_line_ids = fields.One2many('school.marksheet.line', 'marksheet_id', string='Marksheet Lines')

    @api.depends('marksheet_line_ids.obtained_marks')
    def _compute_total_marks(self):
        for record in self:
            record.total_marks = sum(line.obtained_marks for line in record.marksheet_line_ids)

    @api.depends('total_marks', 'marksheet_line_ids')
    def _compute_percentage(self):
        for record in self:
            total_subjects = len(record.marksheet_line_ids)
            record.percentage = (record.total_marks / (total_subjects * 100)) * 100 if total_subjects > 0 else 0

    @api.depends('percentage')
    def _compute_grade(self):
        for record in self:
            if record.percentage >= 90:
                record.grade = 'A+'
            elif record.percentage >= 80:
                record.grade = 'A'
            elif record.percentage >= 70:
                record.grade = 'B+'
            elif record.percentage >= 60:
                record.grade = 'B'
            elif record.percentage >= 50:
                record.grade = 'C+'
            elif record.percentage >= 40:
                record.grade = 'C'
            else:
                record.grade = 'F'

class SchoolMarksheetLine(models.Model):
    _name = 'school.marksheet.line'
    _description = 'Marksheet Line Information'

    marksheet_id = fields.Many2one('school.marksheet', string='Marksheet', required=True, ondelete='cascade')
    subject_id = fields.Many2one('school.subject', string='Subject', required=True)
    obtained_marks = fields.Float(string='Obtained Marks', required=True)