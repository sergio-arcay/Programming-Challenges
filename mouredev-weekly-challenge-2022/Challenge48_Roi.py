from datetime import datetime, timedelta
from cryptography.fernet import Fernet  # pip install cryptography

REGALOS = [b'gAAAAABjhUITEU-ayu0SYUPf5ueAsHdqRKM2ClYyeiWB7q6iuk_bsIAXI8gnpjMvguIw-N3VtAgl88FF2alaSZ_nqRnicktAIoLJfPJ2-jy4KGvpPLMIdn4=', b'gAAAAABjhUIT8IXA_LFuqw4LKnap_Wb5c-uK_sCllj1DJfLjmxb6Yqqg7y309B17l50F2ARJHiiunKDQ74t8w1qfTxchZzIhAg==', b'gAAAAABjhUITz8FrzJrFcGvqLGZbes5w-CKNM-Wv2PQzAyCiGjWmpDlSuYcimbRk87ABYenR_6g7uJZQPcrIruDIfuLxd0crrg==', b'gAAAAABjhUITLts1XTGryedmUUTqvowbMPJUk91ZzogSbPDrpp-HeSVs6W3fz9mQZe5BxaIWRZJ5lStfghSyp9Gr3nI9kmYz2g==', b'gAAAAABjhUITl_WfKAU0z-nCloQOnHDwYXk5J6Vn16JaIDl5ms-XgnkndxRQgrRJtWPaQmIfjEej7_y63Zj80KG8A98L3vVPr-AH3OsXOQSsnVDKeEdLKGWhnpEwn-jfDMqrCSmjB_UFY0wWzBDe9_kxySpWlG2-oA==', b'gAAAAABjhUITbJmLCpsZNx7kU3NPX5G39Uka5Hpu7UFUSs031gi2_AyYegPD7fticczKmOcPb1fFtfJODLBXBIKb_DLR4q8CvMSmhAzcAeiEqMsF70gqB04=', b'gAAAAABjhUITIZzAylerM0r4KhObpxKf3F1jj0GSbbCaO4yUO1VDq-NSBLGlubjRiCO6XIfbCiVPs3IOun3d476WIWtYy_-jiyQ4j_XxhjQOsNn78KTNHJkgD1KbiSVIcE-JeKCI7oMy', b'gAAAAABjhUITI8MnFwsubrZXwetBXpKPuy2LH9jhAQnPkwwhua9npVrnGkkq0OSS81_n6AbBKTax6FXc-JLSHFaWp6S_GEgNQalgozv-4oCvbpd9HgPxQYI=', b'gAAAAABjhUITyr-c6KirrV3P4YnrnLYLONnDaV6LWV8RHKKbu6co2gubwS3qPYe8ivdaiXJTQCDP9DQ7sTkwiWpVTxXKsigyWUJuFGBnoXDjYC6z6BDuIYM8rxbZ2tE4UVO9QeeXB9mFllAvgwzNbiFTD_o5bYlhPXrjLhzyWVLZC-3KUaRMzm4=', b'gAAAAABjhUITBDnJ8m2WlKcP9uUtbEFebISDMDCCPlAhMWaeMkigblLJj7Z4CxYQL0yGSvdYw9rfzSxm-zkcf4-VghKt-GI5uSqYRg8uRcefbTDgmUiNuag=', b'gAAAAABjhUITNU0YEgIRZYHvg5h5eYQp6gO7Vy57Cw-Q7r0S-Y0ZZ24F4V77FRDJIcoXeQyyEhZaLMdsH-HtgobtXZcLOmMjaQ==', b'gAAAAABjhUITNfdqls1bLDDHHzZ_B-Aw9LUfN6gqwyUTk188MCpGJHP8x0X2f2sOZ0xlwih0XW0gO5hQXaQV6pwMHboxxmYUU38IA6h_4dHNno3Q5hYcEKLHyl2c_Vl1C-cItHAW0vSCC3ujs-h006wFgRtI592SFg==', b'gAAAAABjhUITj3wesWaIkchhOlFW88XJWNx9GDRzCHcjBZ6F9485wADDRaJlRtIiCfyjSnKLJUlOTngAwDTJfosExl6Q8IjJLo0L3sL9Vi5UXIY1hq5pXPc=', b'gAAAAABjhUITbKsqlcGkTOfibhzfJW_etLIt9gToKUFP58ridjTspVutTGgCvyCb-Oh8O2uy4zA_IARVADt5vLc8U7NikBM1vkZzpsP-Oz0Bsah9Qb7931_-G1C45NN8xnxWIzFms70j', b'gAAAAABjhUITrt8vd46akFCFwYwmtO2A2A38HbwX388wN-2heRz4Miep3MKDQFbdfGDYd5l_XUXKjwU2EUQcw24pTZ8iL9A2srkyGCvJCVWBo0stYjhOvOM=', b'gAAAAABjhUIT8Hh2N3MfUYoX8V8IeGZ-Zh4bF1nU60Ngxpemozr-BLSG9qpYmwaP3MtSIi75TWZyspYv7gvIQgU9MrFWsnMIEsPHw3W3RUNLr1XXRBiHgWmIEjaiobIWk7NkF4IwhS-cINykLlpU0M11dOOsKgRSbg==', b'gAAAAABjhUITgG-ciVLnjmJjriMoCHOY9l2kBQyMmU2FgQJ-ZRQchFBS5EeyQAlWHQAr0O0GB8c2MqZkNNoJJm9NPTWgly9sXHtKLgLSJpintoq-2IkEYro=', b'gAAAAABjhUITxKAIali3p80D4kuiW98P2a7lUkefK96v0cIrTgThYCMkVUZXxCPcPzOugdQ7HWFYhx_RnQyUA_NCEmYK9N8gkAe14XHQwtv-uaVjl-XzgxSBl85aHv6slvtYh5ccW5HR', b'gAAAAABjhUITgdytngDalSadGojgrokhVZ9Lw0mwGG0j0ONFSTVA0Yq0pnhZtMjKdg8h0kZjq6MC5dyCUSbA0zSGcxUm2kUmx4ZMLIiazzvRzlQj53IUgmXPL_sfdlI1X-mp8jJfZ4Sb', b'gAAAAABjhUITYcq-9_QC1G4-YE4hQvb_BOG5m20terkhzSfuuX-v42YI2BIgCyjJb5Ab4tKuDGPxMFIxQIwNPgIV7mPNVBLcN1y5xE-B8tw9cRvqSleHg_8=', b'gAAAAABjhUITameDy_KY_vju8PWhpUQ8TWj60USe9K-4i-my1GJA9GHLzyfJl-zgFX0kCznQ_HKMB0MHJRlKAzzf78n6gOdng65BMeej6wyeeU0bn1ld3Na4LPIbYRUSlyrCCH7d4CZo', b'gAAAAABjhUITpejLmx6cKxkDjiOFiwwOp6Kxt7VgUJIlfZoQF_OXxK-4Zhw4b2XeJrrjBqJroBN1RFybPF9UneM1COuJ83cvkQ==', b'gAAAAABjhUIT4iXuqF1X0SJp9WmlAs88G-ldK9voPZi0t_enKXB3RnZhKGbTf0HarYdE4nD076KkHnmEQeQbjtGG-6_AbOahgVVZlvxnsTVOPAEL5SENPLI=', b'gAAAAABjhUIT-JH2qdtsXCp5O8MkpuVYE3On1eORFX99Csf-s8o9KobFcef8d6wGD66r_8WqQkizkkA45RSgo1K2lk-Lh8TGyFHpw9w64-SOrnLjaw6B2bo=']
KEY = b'dWPwLbQYRxQe1-WxV4v8tRy0IXFBKDp640EAzC7yFw0='  # No pierdas esto, ¡lo necesitarás para ver qué es cada regalo!
fernet = Fernet(KEY)

COMIENZO = datetime(2022, 12, 1)
FINAL = datetime(2022, 12, 24)


def calendario_adVEDineto(fecha: datetime) -> (str, timedelta):
    """Devuelve un regalo de adviento para una fecha y una delta temporal con el tiempo para el siguiente regalo"""
    if COMIENZO <= fecha < FINAL:
        return fernet.decrypt(REGALOS[(fecha - COMIENZO).days]).decode(), \
               timedelta(hours=(24-fecha.hour - 1), minutes=(60 - fecha.minute - 1), seconds=(60 - fecha.second - 1))
    elif fecha < COMIENZO:
        return "Aún no hay regalo, paciencia :(", COMIENZO - fecha
    elif fecha >= FINAL:  # No, para el año que viene aún no hay regalos ;)
        return "!Felices Fiestas!", timedelta(days=(365+(365-fecha.timetuple().tm_yday)), hours=(24-fecha.hour - 1), minutes=(60 - fecha.minute - 1), seconds=(60 - fecha.second - 1))


if __name__ == '__main__':
    hoy = datetime.now()
    # TRAMPAS:
    # hoy = datetime(2022, 12, 26, 19, 30)

    print("Hoy es: ", hoy, end="\n\n")
    regalo, delta = calendario_adVEDineto(hoy)
    print("\t", regalo, end="\n\n")
    print("Quedan ", delta, " para el próximo regalo")

