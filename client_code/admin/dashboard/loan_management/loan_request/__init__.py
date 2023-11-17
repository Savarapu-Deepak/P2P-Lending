from ._anvil_designer import loan_requestTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class loan_request(loan_requestTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    
    self.customer_id = []
    self.email_id = []
    self.full_name = []
    self.interest_rate = []
    self.loan_id = []
    self.loan_status = []
    self.max_amount = []
    self.min_amount = []
    self.application_status = []
    self.timestamp = []
    self.tenure = []
    self.total_repayment_amount = []

    data = tables.app_tables.loan_details.search()
    for row in data:
      self.customer_id.append(row['customer_id'])
      self.email_id.append(row['email_id'])
      self.full_name.append(row['full_name'])
      self.interest_rate.append(row['interest_rate'])
      self.loan_id.append(row['loan_id'])
      self.loan_status.append(row['loan_status'])
      self.max_amount.append(row['max_amount'])
      self.min_amount.append(row['min_amount'])
      self.application_status.append(row['application_status'])
      self.timestamp.append(row['timestamp'])
      self.tenure.append(row['tenure'])
      self.total_repayment_amount.append(row['total_repayment_amount'])
      
      self.label_13.text = self.customer_id[-1]
      self.label_14.text = self.email_id[-1]
      self.label_15.text = self.full_name[-1]
      self.label_16.text = self.interest_rate[-1]
      self.label_17.text = self.loan_id[-1]
      self.label_18.text = self.loan_status[-1]
      self.label_19.text = self.max_amount[-1]
      self.label_20.text = self.min_amount[-1]
      self.label_21.text = self.application_status[-1]
      self.label_22.text = self.timestamp[-1]
      self.label_23.text = self.tenure[-1]
      self.label_24.text = self.total_repayment_amount[-1]

    self.coustmer_id = self.label_13.text
    self.email_id = self.label_14.text

    for i in self.loan_status:
      if i :
        anvil.server.call('lender',self.coustmer_id,self.email_id)

  def button_1_copy_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('admin.dashboard.loan_management')

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('admin.dashboard.loan_management')