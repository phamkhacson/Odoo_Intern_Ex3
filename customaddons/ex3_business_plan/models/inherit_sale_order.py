from odoo import api, fields, models
from odoo.exceptions import AccessError, MissingError


class CreateBusinessPlan(models.Model):
    _inherit = "sale.order"
    business_plan = fields.Many2one('plan.sale.order', string="Business Plan")

    def create_business_plan(self):
        view_form_id = self.env.ref('ex3_business_plan.create_business_plan_form').id
        sale_order = self.id
        return {
            'name': 'Create business plan',
            'view_mode': 'form',
            'res_model': 'plan.sale.order',
            'view_id': view_form_id,
            'type': 'ir.actions.act_window',
            'target': 'current',
            'context': {
                'default_order_ids': sale_order
            }
        }

    def check_plan(self):
        if not self.business_plan:
            raise MissingError("Have not business plan")
        else:
            if self.business_plan.order_ids.name == self.env['plan.sale.order'].search([('order_ids', '=', self.id)],
                                                                                       limit=1).order_ids.name:
                if self.business_plan.plan_status == "approved":
                    pass
                elif self.business_plan.plan_status == "sent":
                    raise AccessError("Plan is solving")
                else:
                    raise AccessError("Plan is refused")
            else:
                raise AccessError("Plan is not apply for order")
