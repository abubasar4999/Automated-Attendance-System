
import enroll,spreadsheet,recognition
import  emailing
recognition.load_facial_encodings_and_names_from_memory()

spreadsheet.mark_all_absent()

recognition.run_recognition()




#enroll.enroll_via_camera('Bhavesh')

#spreadsheet.enroll_person_to_sheet('Vaishnavi','vaishnavi23@gmail.com')

#emailing.email_pin('xxxx@gmail.com',1234)

#