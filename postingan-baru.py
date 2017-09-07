import datetime, re

sekarang = datetime.datetime.now()
lokasi = "/sdcard/Git/sitis/"

judul = raw_input("Masukkan judul: ")

judullink = judul[:]
judullink = judullink.lower()
judullink = re.sub(r" ", r"-", judullink)
judullink = re.sub(r"\?", r"", judullink)
judullink = re.sub(r"!", r"", judullink)
judullink = re.sub(r"\.", r"", judullink)

tahun = sekarang.year
bulan = sekarang.month
tanggal = sekarang.day
jam = sekarang.hour
menit = sekarang.minute
detik = sekarang.second

if bulan < 10:
    bulan = "0"+str(bulan)
if tanggal < 10:
    tanggal = "0"+str(tanggal)
if jam < 10:
    jam = "0"+str(jam)
if menit < 10:
    menit = "0"+str(menit)
if detik < 10:
    detik = "0"+str(detik)

judulfile = "{tahun}-{bulan}-{tanggal}-{judul}.md"
isi = """---
layout: post
title: "{judul}"
date: {tahun}-{bulan}-{tanggal} {jam}:{menit}:{detik}
---

"""

fileblog = judulfile.format(tahun=tahun, bulan=bulan, tanggal=tanggal, judul=judullink)
isiblog = isi.format(judul=judul, tahun=tahun, bulan=bulan, tanggal=tanggal, jam=jam, menit=menit, detik=detik)

buatfile = open(lokasi+"_posts/"+fileblog, "w")
buatfile.write(isiblog)
