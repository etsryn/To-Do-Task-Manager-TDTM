import fitz
import PyPDF2
import os
def __init__64bit_pie(__init__64bit__f):
    __init__64bit__dpf = fitz.Document(__init__64bit__f)
    return __init__64bit__dpf.isEncrypted
def __init__64bit_ep(__init__64bit__dpf, __init__64bit__pd, __init__64bit__opf, __init__64bit__f):
    if not __init__64bit_pie(__init__64bit__f):
        perm = int(
            fitz.PDF_PERM_ACCESSIBILITY
            | fitz.PDF_PERM_PRINT
            | fitz.PDF_PERM_COPY
            | fitz.PDF_PERM_ANNOTATE
        )
        encrypt_meth = fitz.PDF_ENCRYPT_AES_256
        __init__64bit__dpf.save(__init__64bit__opf, encryption=encrypt_meth, user_pw=__init__64bit__pd, permissions=perm)
def __init__64bit_dp(__init__64bit__f):
    if __init__64bit_pie(__init__64bit__f):
        __init__64bit__pd = "__init__64_TB"
        pdf = fitz.open(__init__64bit__f)
        if pdf.authenticate(__init__64bit__pd):
            pdf.save('__init__64bit__dcpf')
def __init__64bit_rp():
    with open('__init__64bit__dcpf', 'rb') as __init__64bit__pf_:
        pdf_reader = PyPDF2.PdfReader(__init__64bit__pf_)
        __init__b4bit_fp = pdf_reader.pages[0]
        __init__b4bit_fpt = __init__b4bit_fp.extract_text()
        __init__64bit__ln = __init__b4bit_fpt.split('\n')
        __init__64bit__l = []
        for i in range(0,4):
            __init__64bit__l.append(__init__64bit__ln[i])
        with open("temp.txt", "w") as __init__:
            for i in range(0,4):
                __init__.write(__init__64bit__l[i])
                __init__.write("\n")
def __init__64bit__dp():
    __init__64bit_pfp = '__init__64bit__dcpf'
    if os.path.exists(__init__64bit_pfp):
        os.remove(__init__64bit_pfp)
def __init__64bit__ini():
    __init__64bit__f = 'inaccessible.pdf'
    pdf = fitz.open(__init__64bit__f)
    __init__64bit__pd = '__init__64bit__pd'
    __init__64bit_ep(pdf, __init__64bit__pd, 'protected.pdf', __init__64bit__f)
    __init__64bit_dp(__init__64bit__f)
if __name__ == '__main__':
    __init__64bit__ini()
    __init__64bit_rp()
    __init__64bit__dp()