from odoo import models,api

class OrderXlsx(models.AbstractModel): 
    _name="report.restaurant.report_order"
    _inherit = 'report.report_xlsx.abstract' 


    # _name = 'report.module_name.report_name'
    # _inherit = 'report.report_xlsx.abstract'


    def generate_xlsx_report(self, workbook, data, orders):
        print("--------------Order Bill XLSX Report----------------")
        
        sheet = workbook.add_worksheet('Bill Report')
        
        formats_title=workbook.add_format({'bold':True,
                                            'font_size':12,
                                            'align':'center',
                                            'font':'Times new roman',
                                            })
        
        formats_body=workbook.add_format({'font_size':10,
                                            'align':'center',
                                            'font':'Times new roman',
                                            })
        
        # Set column widths for better readability
        sheet.set_column('A:H', 25)
        
         # Write titles for Sale Order
        sheet.write(0, 0, 'Order ID', formats_title)
        sheet.write(0, 1, 'Customer', formats_title)
        sheet.write(0, 2, 'Order Date', formats_title)
        sheet.write(0, 3, 'Total Amount', formats_title)

        # Write titles for Order Lines (One2many field)
        sheet.write(0, 4, 'Product', formats_title)
        sheet.write(0, 5, 'Quantity', formats_title)
        sheet.write(0, 6, 'Unit Price', formats_title)
        sheet.write(0, 7, 'Subtotal', formats_title)
        
        row = 1
        col = 0
        
        date_format = workbook.add_format({'num_format': 'yyyy-mm-dd'})  # Date format for date fields
        
         # Loop through Sale Orders
        for order in orders:
            sheet.write(row, col, order.name, formats_body)  # Sale Order ID
            sheet.write(row, col + 1, order.partner_id.name, formats_body)  # Customer Name
            sheet.write(row, col + 2, order.date_order, date_format)  # Order Date
            sheet.write(row, col + 3, order.amount_total, formats_body)  # Total Amount
            
            row=row+1
            line_row = row 
            for line in order.order_line:
                # Add order line details
                sheet.write(line_row, col + 4, line.product_id.name, formats_body)  # Product Name
                sheet.write(line_row, col + 5, line.product_uom_qty, formats_body)  # Quantity
                sheet.write(line_row, col + 6, line.price_unit, formats_body)  # Unit Price
                sheet.write(line_row, col + 7, line.price_subtotal, formats_body)  # Subtotal
                line_row += 1  # Move to the next row for each line

            row = line_row  # Move to the next row after finishing the current sale order








