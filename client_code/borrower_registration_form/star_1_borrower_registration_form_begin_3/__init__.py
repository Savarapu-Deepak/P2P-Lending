from ._anvil_designer import star_1_borrower_registration_form_begin_3Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import re
class star_1_borrower_registration_form_begin_3(star_1_borrower_registration_form_begin_3Template):
  def __init__(self,user_id, **properties):
    # Set Form properties and Data Bindings.
    self.userId = user_id
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
  def home_borrower_registration_button_click(self, **event_args):
    open_form('bank_users.user_form')
    
  def button_1_click(self, **event_args):
    open_form('borrower_registration_form.star_1_borrower_registration_form_begin_2',user_id = self.userId)
  
  def button_2_click(self, **event_args):
    aadhar= self.borrower_registration_aadhar_text.text
    aadhar_card = self.borrower_registration_img_aadhar_file_loader.file
    pan = self.borrower_registration_pan_text.text
    pan_card=self.borrower_registration_img_pan_file_loader.file
    user_id = self.userId
    if not re.match(r'^\d{12}$', aadhar):
      Notification("Please enter a valid 12-digit Aadhaar number")
    # Check if PAN is a valid format
    elif not re.match(r'^[A-Z]{5}[0-9]{4}[A-Z]$', pan):
      Notification("Please enter a valid PAN card number")
    elif not aadhar_card or not pan or not pan_card:
      Notification("Please fill in all required fields")
      anvil.server.call('add_borrower_step3',aadhar,aadhar_card,pan,pan_card,user_id)
      open_form('borrower_registration_form.star_1_borrower_registration_form_begin_3.star_1_borrower_registration_form_begin_3a',user_id=user_id)
  
    