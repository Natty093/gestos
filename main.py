import cv2
import mediapipe as mp
import math
import os

# --- CONFIGURACIÓN ---
RUTA_FELIZ = os.path.join("assets", "sonrie.jpg")
RUTA_LENGUA = os.path.join("assets", "Muejejeje.jpg")

UMBRAL_SONRISA = 67
UMBRAL_LENGUA = 26

# --- CARGA DE RECURSOS ---
print(f"Cargando recursos desde: {os.getcwd()}/assets")

img_feliz = cv2.imread(RUTA_FELIZ)
img_lengua = cv2.imread(RUTA_LENGUA)

if img_feliz is None or img_lengua is None:
    print("ERROR: No se encontraron las imágenes en 'assets'.")
    exit()

# --- INICIO DE MEDIAPIPE ---
mp_face_mesh = mp.solutions.face_mesh
mp_drawing = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

# Variable para saber si la ventana del meme está abierta o no
ventana_meme_abierta = False

with mp_face_mesh.FaceMesh(
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as face_mesh:

    while cap.isOpened():
        success, image = cap.read()
        if not success:
            continue

        # Espejo
        image = cv2.flip(image, 1)
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = face_mesh.process(image_rgb)
        
        estado = "normal" 

        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                h, w, _ = image.shape
                
                # Puntos clave
                p_izq = face_landmarks.landmark[61]
                p_der = face_landmarks.landmark[290]
                p_arr = face_landmarks.landmark[13]
                p_aba = face_landmarks.landmark[14]

                cx_izq, cy_izq = int(p_izq.x * w), int(p_izq.y * h)
                cx_der, cy_der = int(p_der.x * w), int(p_der.y * h)
                cx_arr, cy_arr = int(p_arr.x * w), int(p_arr.y * h)
                cx_aba, cy_aba = int(p_aba.x * w), int(p_aba.y * h)

                ancho_boca = math.hypot(cx_der - cx_izq, cy_der - cy_izq)
                alto_boca = math.hypot(cx_aba - cx_arr, cy_aba - cy_arr)
                print(f"Ancho: {int(ancho_boca)} | Alto: {int(alto_boca)}")
                # Detección
                if ancho_boca > UMBRAL_SONRISA:
                    estado = "sonrisa"
                elif alto_boca > UMBRAL_LENGUA:
                    estado = "lengua"
                
                mp_drawing.draw_landmarks(
                    image=image,
                    landmark_list=face_landmarks,
                    connections=mp_face_mesh.FACEMESH_TESSELATION,
                    landmark_drawing_spec=None,
                    connection_drawing_spec=mp_drawing.DrawingSpec(color=(200,200,200), thickness=1, circle_radius=1)
                )

        # --- LÓGICA DEL POP-UP ---

        cv2.imshow(' Camara ', image)

        if estado == "sonrisa":
            cv2.imshow('Reaccion', img_feliz)
            ventana_meme_abierta = True
            
        elif estado == "lengua":
            cv2.imshow('Reaccion', img_lengua)
            ventana_meme_abierta = True
            
        else:
            if ventana_meme_abierta:
                try:
                    cv2.destroyWindow('Reaccion')
                except:
                    pass 
                ventana_meme_abierta = False

        # Salir con ESC
        if cv2.waitKey(5) & 0xFF == 27:
            break

cap.release()
cv2.destroyAllWindows()