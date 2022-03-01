from odoo import api, fields, models
from odoo.exceptions import MissingError, ValidationError


class BusinessPlan(models.Model):
    _name = "plan.sale.order"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    plan_status = fields.Selection([
        ('new', 'New'),
        ('sent', 'Sent'),
        ('approved', 'Approved'),
        ('refuse', 'Refuse')
    ], default="new", readonly='1')
    name = fields.Char(string="Name", required="True")
    order_ids = fields.Many2one('sale.order', string="Order Ids", readonly='1')
    plan_info = fields.Text(string="Business plan info", required="True")
    approver = fields.One2many('plan.approve', 'plan_id', string="Approver")

    def new_business_plan(self):
        if not self.order_ids:
            raise MissingError("Invalid Order")
        else:
            self.plan_status = "sent"
            list_user = []
            for rec in self.approver:
                list_user.append(rec.id)
            self.sudo().message_post(body="Sent to approvers", partner_ids=list_user)

    def save_business_plan(self):
        if not self.order_ids:
            raise MissingError("Invalid Order")
        else:
            check = 0
            for rec in self.approver:
                if rec.approve_status == "not_approved_yet":
                    raise ValidationError("Not Approve Yet")
                    break
                elif rec.approve_status == "approved":
                    check += 1
            if check == len(self.approver):
                self.plan_status = "approved"
            else:
                self.plan_status = "refuse"
