import json

class EmailConfig:
    def __init__(self, config_file='email_config.json'):
        self.config_file = config_file
        self.load_config()

    def load_config(self):
        with open(self.config_file) as f:
            self.config = json.load(f)

    def get_smtp_config(self):
        return self.config['SMTP']

    def get_pop3_config(self):
        return self.config['POP3']

# Example usage:
if __name__ == "__main__":
    email_config = EmailConfig()
    
    smtp_config = email_config.get_smtp_config()
    print("SMTP Config:", smtp_config)

    pop3_config = email_config.get_pop3_config()
    print("POP3 Config:", pop3_config)
