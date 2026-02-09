def hitung_nilai(tugas, uts, uas):

    nilai_akhir = (tugas * 0.3) + (uts * 0.3) + (uas * 0.4)
    
    if nilai_akhir >= 85:
        grade = 'A'
    elif nilai_akhir >= 70:
        grade = 'B'
    elif nilai_akhir >= 55:
        grade = 'C'
    elif nilai_akhir >= 40:
        grade = 'D'
    else:
        grade = 'E'
    
    print(f"Nilai : {nilai_akhir}")
    print(f"Grade : {grade}")

hitung_nilai(80, 75, 90)
