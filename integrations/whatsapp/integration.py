from twilio.rest import Client

class WhatsAppBot:
    def __init__(self, account_sid, auth_token):
        self.client = Client(account_sid, auth_token)
    
    def parse_message(self, message_body):
        parts = message_body.split()
        try:
            return {
                'employee': parts[0],
                'date': parts[1],
                'event_type': ' '.join(parts[2:-2]),
                'base_pay': float(parts[-2].replace('$','').replace(',','')),
                'extra_hours': int(parts[-1].replace('h','')) if 'h' in parts[-1] else 0
            }
        except (ValueError, IndexError) as e:
            raise ValueError(f"Formato de mensaje inválido: {str(e)}")

    def send_confirmation(self, to_number, message):
        return self.client.messages.create(
            body=message,
            from_whatsapp='whatsapp:+14155238886',
            to=f'whatsapp:{to_number}'
        )