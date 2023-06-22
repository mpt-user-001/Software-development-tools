import Main, BD
import pyotp
import qrcode


def reg(log):
    totp_auth = pyotp.totp.TOTP(key()).provisioning_uri(name='Player ' + log, issuer_name='Wallet')
    qrcode.make(totp_auth).save("qr_auth.png")
    

def auto(login, sum_):
    totp = pyotp.TOTP(key())
    while True:
        if totp.verify(input("Enter the Code : ")):
            for i in BD.Row("Player", login, "S"):
                BD.Row("Player", (i[1], i[2], i[3], i[4] + sum_, i[0]), "U")
            Main.menu(login)


def key():
    return "E5EF43e4CKDK"