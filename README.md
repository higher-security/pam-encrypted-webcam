BETA VERSION (NOT WORKING)

# Instruction

1. Install required packages

    apt-get -y install libpam-python

2. Copy scripts

    cp pam_custom.py pam_encrypted_webcam.sh /lib/security 

3. Add the following line `/etc/pam.d/common-auth

    auth  [success=2 default=ignore] pam_python.so pam_custom.py /lib/security/pam_custom.sh
