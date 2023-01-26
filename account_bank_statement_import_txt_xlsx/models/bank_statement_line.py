from odoo import api, fields, models

class AccountBankStatementLine(models.Model):
    _inherit = 'account.bank.statement.line'

    transaction_number = fields.Char()