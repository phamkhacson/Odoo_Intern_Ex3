from odoo import api, fields, models


class Approver(models.Model):
    _name = "plan.approve"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    approver = fields.Many2one('res.users', string='Name')
    plan_id = fields.Many2one('plan.sale.order', string='Plan ID')
    approve_status = fields.Selection([
        ('approved', 'Approved'),
        ('not_approved_yet', 'Not approved yet'),
        ('refuse', 'Refuse')
    ], default="not_approved_yet", readonly=True)
    is_user = fields.Boolean(compute="identify")

    def identify(self):
        for rec in self:
            if rec.approver.id == self.env.user.id:
                rec.is_user = True
            else:
                rec.is_user = False

    def approve_plan(self):
        self.approve_status = "approved"
        self.plan_id.sudo().message_post(body="I approved")

    def refuse_plan(self):
        self.approve_status = "refuse"
        self.plan_id.sudo().message_post(body="I refused")
