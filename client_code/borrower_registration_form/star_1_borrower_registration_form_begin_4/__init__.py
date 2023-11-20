from ._anvil_designer import star_1_borrower_registration_form_begin_4Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class star_1_borrower_registration_form_begin_4(star_1_borrower_registration_form_begin_4Template):
  def __init__(self,user_id, **properties):
    # Set Form properties and Data Bindings.
    self.userId = user_id
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def home_borrower_registration_form_copy_1_click(self, **event_args):
    open_form('bank_users.user_form')

  def button_next_click(self, **event_args):
    marital_status = self.marital_status_borrower_registration_dropdown.selected_value
    user_id = self.userId
    if not marital_status:
      Notification("please provide all Details").show()
    else:
      anvil.server.call('add_borrower_step4',marital_status,user_id)
      if marital_status == 'UN-Married':
        open_form('borrower_registration_form.star_1_borrower_registration_form_begin_7',userId = user_id)
      elif marital_status == 'Married':
        open_form('borrower_registration_form.star_1_borrower_registration_form_begin_4.star_1_borrower_registration_form_begin_4a',userId=user_id)
      else:
        open_form('borrower_registration_form.star_1_borrower_registration_form_begin_7',userId = user_id)

  
  def button_1_click(self, **event_args):
    open_form('borrower_registration_form.star_1_borrower_registration_form_begin_3.star_1_borrower_registration_form_begin_3c',userId=user_id)


    
    
    
    
