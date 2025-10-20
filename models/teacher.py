from odoo import fields, models, api, _
from odoo.exceptions import ValidationError

class SchoolTeacher(models.Model):
    _name = "school.teacher"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Teacher Table"

    name = fields.Char(string = "Name", required = True, tracking=True)
    date_of_birth = fields.Date(string = "Date of Birth")
    address = fields.Text(string = "Address")
    department = fields.Selection([
        ('primary','Primary'),
        ('secondary','Secondary'),
        ('higher_secondary','Higher Secondary'),
        ], string = "Department")
    gender = fields.Selection([
        ('male','Male'),
        ('female','Female'),
    ], string = "Gender", default = "male")
    hire_date = fields.Date(string = "Hire Date")
    subject_taught = fields.Integer(string = "Subject Taught")
    contact_no = fields.Char(string='Contact No', size=10)
    image = fields.Binary(string = "Image") 
    email_id = fields.Char(string = "Email ID", required = True)
    name_seq = fields.Char(string='Teacher ID', required=True, copy=False, readonly=True,
                           index=True, default=lambda self: _('New'))
    active = fields.Boolean('Active', default=True)
    
    @api.model
    def create(self, vals):
        if vals.get('name_seq', _('New')) == _('New'):
            vals['name_seq'] = self.env['ir.sequence'].next_by_code('school.teacher.sequence') or _('New')
        result = super(SchoolTeacher, self).create(vals)
        return result
    
    @api.constrains('contact_no')
    def _check_contact_no(self):
        for record in self:
            if not record.contact_no.isdigit():
                raise ValidationError('Contact number must contain only digits.')
            if len(record.contact_no) != 10:
                raise ValidationError('Contact number must be exactly 10 digits long.')