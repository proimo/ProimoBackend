from phonenumber_field.modelfields import PhoneNumberField

from common.models import BaseModel


class Lead(BaseModel):
    phone_number = PhoneNumberField('Număr de contact', default=None, blank=True)
