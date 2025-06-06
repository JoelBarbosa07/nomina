class PayrollCalculator:
    def calculate(self, employee, events):
        total = 0.0
        for event in events:
            if employee.payment_type == 'hourly':
                base = event.hours * employee.base_rate
                extras = event.extra_hours * employee.base_rate * 1.5
                total += base + extras
            elif employee.payment_type == 'fixed':
                total += employee.base_rate
            elif employee.payment_type == 'variable':
                total += event.total
        return round(total, 2)