

import os

def custom_auth(user, password, command):
  return os.system(command + ' ' + user + ' ' + password) == 0

def pam_sm_authenticate(pamh, flags, argv):


  try:
    user = pamh.get_user(None)
    if user == None:
      return pamh.PAM_AUTH_ERR

    password = pamh.authtok
    if password == None:
      ## got no password in authtok - trying through conversation...
      passmsg = pamh.Message(pamh.PAM_PROMPT_ECHO_OFF, "Custom auth: ")
      rsp = pamh.conversation(passmsg)
      password = rsp.resp
      # so we should at this point have the password either through the
      # prompt or from previous module

    if custom_auth(user, password, argv[1]):
      return pamh.PAM_SUCCESS
    else:
      return pamh.PAM_AUTH_ERR

  except pamh.exception, e:
    return e.pam_result

def pam_sm_setcred(pamh, flags, argv):
  return pamh.PAM_SUCCESS

def pam_sm_acct_mgmt(pamh, flags, argv):
  return pamh.PAM_SUCCESS

def pam_sm_open_session(pamh, flags, argv):
  return pamh.PAM_SUCCESS

def pam_sm_close_session(pamh, flags, argv):
  return pamh.PAM_SUCCESS

def pam_sm_chauthtok(pamh, flags, argv):
  return pamh.PAM_SUCCESS
