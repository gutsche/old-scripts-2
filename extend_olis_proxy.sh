source /opt/vdt/setup.sh
voms-proxy-init -voms cms -cert ~/.globus/oliver/usercert.pem -key ~/.globus/oliver/userkey.pem -out ~/.globus/oliver/proxy -valid 1000:00
export X509_USER_PROXY=~/.globus/oliver/proxy
