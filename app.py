"""
Coco-Guard: Mobile-First Coconut Disease Diagnostics
Designed with Soft UI Evolution + Neumorphism Blend, #d2c68e background,
Instrument Serif typography applied throughout, enhanced output readability,
and balanced, lively emojis for farmers.
"""

import os
import sys
import json
import threading
from typing import Optional, Dict, Any
from PIL import Image, ImageTk
import customtkinter as ctk
from tkinter import filedialog

# --- DYNAMIC FONT REGISTRATION (INSTRUMENT SERIF) ---
FONT_SERIF = "Instrument Serif"

def register_custom_fonts():
    """Dynamically registers Instrument Serif font on Windows for the process."""
    if sys.platform.startswith("win"):
        try:
            import ctypes
            FR_PRIVATE = 0x10
            base_dir = os.path.dirname(os.path.abspath(__file__))
            candidate_dirs = [base_dir, os.path.dirname(base_dir)]
            for d in candidate_dirs:
                for font_file in ["InstrumentSerif-Regular.ttf", "InstrumentSerif-Italic.ttf"]:
                    font_path = os.path.join(d, font_file)
                    if os.path.exists(font_path):
                        ctypes.windll.gdi32.AddFontResourceExW(font_path, FR_PRIVATE, 0)
        except Exception:
            pass

register_custom_fonts()

# --- SOFT UI EVOLUTION & NEUMORPHISM DESIGN TOKENS ---
COLOR_BG = "#d2c68e"                   # Warm Sand / Khaki Background Canvas

# Molded Neumorphic Surfaces (Subtle Depth & Tactile Relief)
COLOR_NEU_CARD_BG = "#14161A"          # Molded Raised Card Surface
COLOR_NEU_CARD_BORDER = "#2B303A"      # Specular Top-Left Highlight Rim
COLOR_NEU_SHADOW_RIM = "#0D0E11"       # Subtle Ambient Base Rim

# Recessed Debossed Wells (Camera & Content Sections)
COLOR_WELL_INSET = "#0A0B0E"           # Deep Inset Depressed Well
COLOR_WELL_BORDER = "#1E2229"          # Soft Inner Shadow Rim

# Extruded Tactile Buttons (Convex Molded State)
COLOR_BTN_CONVEX = "#1F232B"           # Resting Convex Button Face
COLOR_BTN_HOVER = "#2A2F3A"            # Soft Lift on Hover (200ms feel)
COLOR_BTN_DEBOSSED = "#0B0C0F"         # Pressed / Inset Active State

# Highlights & High-Contrast Borders
COLOR_RIM_SPECULAR = "#383F4D"         # Soft Highlight Border
COLOR_RIM_ACTIVE = "#FFFFFF"           # Crisp Active Selection Border

# Typography Tokens (WCAG 4.5:1+ Compliant)
COLOR_TEXT_WHITE = "#FFFFFF"           # High-Contrast Pure White
COLOR_TEXT_DARK = "#000000"            # Solid Black for Title on Sand BG
COLOR_TEXT_PRIMARY = "#F4F4F6"         # Off-White Headlines
COLOR_TEXT_MUTED = "#A1A1AA"           # Neutral Light Slate Grey for Headings
COLOR_TEXT_SECONDARY = "#71717A"       # Secondary Tag Grey
COLOR_TEXT_SAND_DARK = "#2E2B1E"       # Earthy Dark Charcoal on Sand BG

# Badges & Status
COLOR_BADGE_BG = "#191C22"             # Pill Badge Surface
COLOR_BADGE_TEXT = "#D4D4D8"           # Light Grey Badge Text

# --- REFINED COMPACT REFERENCE DATABASE WITH LIVELY EMOJIS ---
FALLBACK_DISEASE_DB: Dict[str, Dict[str, Any]] = {
    "BUD": {
        "en": {
            "condition_title": "Bud Rot (Phytophthora palmivora)",
            "possibility_score": "High Probability",
            "symptoms_analysis": (
                "• 🥀 Central spear leaf yellows, rots, and droops.\n"
                "• ⚠️ Heart tissue decays with foul necrotic odor.\n"
                "• 🍂 Young fronds detach easily when pulled gently."
            ),
            "cure_and_medication": (
                "1. ✂️ Cut & burn infected crown tissue immediately.\n"
                "2. 🛡️ Apply 10% Bordeaux Paste on exposed cut surface.\n"
                "3. 💧 Spray surrounding palms with 1% Bordeaux mixture."
            ),
            "fun_fact": "Coconut palms have a single central growing bud; if destroyed, the tree cannot survive.",
            "suggested_next_step": "Isolate palm and apply Bordeaux paste."
        },
        "ta": {
            "condition_title": "மொட்டு அழுகல் (Phytophthora palmivora)",
            "possibility_score": "அதிக சாத்தியக்கூறு",
            "symptoms_analysis": (
                "• 🥀 நடுக்குருத்து இலை மஞ்சள் நிறமாகி அழுகி தொங்கும்.\n"
                "• ⚠️ மகுடப்பகுதி அழுகி கடுமையான துர்நாற்றம் வீசும்.\n"
                "• 🍂 இளங்குருத்து இலைகள் எளிதில் உடைந்து விழும்."
            ),
            "cure_and_medication": (
                "1. ✂️ பாதிக்கப்பட்ட மகுடப்பகுதியை வெட்டி உடனடியாக எரிக்கவும்.\n"
                "2. 🛡️ வெட்டப்பட்ட இடத்தில் 10% போர்டோ பேஸ்ட் பூசவும்.\n"
                "3. 💧 சுற்றியுள்ள மரங்களுக்கு 1% போர்டோ கலவை தெளிக்கவும்."
            ),
            "fun_fact": "தென்னை மரத்திற்கு ஒரே ஒரு வளர்ச்சி மொட்டு மட்டுமே உண்டு; அது அழிந்தால் மரம் இறந்துவிடும்.",
            "suggested_next_step": "பாதிக்கப்பட்ட பகுதியை வெட்டி போர்டோ பேஸ்ட் பூசவும்."
        }
    },
    "LEAF": {
        "en": {
            "condition_title": "Leaf Rot (Colletotrichum gloeosporioides)",
            "possibility_score": "High Probability",
            "symptoms_analysis": (
                "• 🍂 Blackened, water-soaked distal lesions on leaflets.\n"
                "• 💨 Leaf ends rot, turn brittle, and shred in high winds."
            ),
            "cure_and_medication": (
                "1. ✂️ Prune & destroy rotten distal leaflets.\n"
                "2. 🛡️ Spray crown with Hexaconazole (0.1%) or Mancozeb.\n"
                "3. 💧 Clear plantation basin to prevent standing water."
            ),
            "fun_fact": "Leaf Rot fungi exploit rainy monsoon periods and water-stressed palms.",
            "suggested_next_step": "Prune infected leaflets and spray Hexaconazole."
        },
        "ta": {
            "condition_title": "இலை அழுகல் (Colletotrichum gloeosporioides)",
            "possibility_score": "அதிக சாத்தியக்கூறு",
            "symptoms_analysis": (
                "• 🍂 இலை நுனிகளில் கருமை கலந்த நீர் கசிவு போன்ற புள்ளிகள்.\n"
                "• 💨 இலைகள் அழுகி காற்றில் கிழிந்து உடையும்."
            ),
            "cure_and_medication": (
                "1. ✂️ அழுகிய இலை நுனிகளை வெட்டி பாதுகாப்பாக எரிக்கவும்.\n"
                "2. 🛡️ மரத்தின் மகுடத்திற்கு ஹெக்சகோனசோல் (0.1%) தெளிக்கவும்.\n"
                "3. 💧 வேர்ப்பகுதியில் நீர் தேங்காமல் வடிகால் வசதி செய்யவும்."
            ),
            "fun_fact": "இலை அழுகல் நோய் பெரும்பாலும் காற்று மற்றும் மழைத்துளிகள் மூலம் எளிதில் பரவுகிறது.",
            "suggested_next_step": "அழுகிய இலைகளை வெட்டி ஹெக்சகோனசோல் தெளிக்கவும்."
        }
    },
    "STEM": {
        "en": {
            "condition_title": "Stem Bleeding (Ceratocystis paradoxa)",
            "possibility_score": "High Probability",
            "symptoms_analysis": (
                "• 🩸 Dark reddish-brown exudation oozing from trunk fissures.\n"
                "• 🪵 Fluid dries pitch-black with internal fibrous decay."
            ),
            "cure_and_medication": (
                "1. 🪓 Chisel infected bark tissue down to sound wood.\n"
                "2. 🛡️ Paint wound with hot Coal Tar or 10% Bordeaux Paste.\n"
                "3. 🌱 Soil application of Trichoderma + neem cake at base."
            ),
            "fun_fact": "The bleeding sap contains oxidized tannins that harden into a dark crust on the trunk.",
            "suggested_next_step": "Chisel diseased bark and seal with Coal Tar."
        },
        "ta": {
            "condition_title": "தண்டு இரத்தக்கசிவு (Ceratocystis paradoxa)",
            "possibility_score": "அதிக சாத்தியக்கூறு",
            "symptoms_analysis": (
                "• 🩸 தண்டுப் பிளவுகளிலிருந்து அடர் சிவப்பு-பழுப்பு நிற திரவம் கசியும்.\n"
                "• 🪵 திரவம் உலர்ந்து கறுப்பாக மாறும்; மரத்தின் உள்பகுதி நார்கள் சிதையும்."
            ),
            "cure_and_medication": (
                "1. 🪓 பாதிக்கப்பட்ட தண்டுப் பட்டையை நல்ல மரம் வரை செதுக்கவும்.\n"
                "2. 🛡️ செதுக்கிய இடத்தில் சூடான நிலக்கரி தார் (Coal Tar) பூசவும்.\n"
                "3. 🌱 வேர்ப்பகுதியில் வேப்பம்பிண்ணாக்கு + ட்ரைக்கோடெர்மா இடவும்."
            ),
            "fun_fact": "தண்டு இரத்தக்கசிவு நோய் மரத்தின் உள்பகுதி நார்களை பலவீனப்படுத்துகிறது.",
            "suggested_next_step": "பட்டையைச் செதுக்கி சூடான நிலக்கரி தார் பூசவும்."
        }
    },
    "GRAY": {
        "en": {
            "condition_title": "Gray Leaf Spot (Pestalotiopsis palmarum)",
            "possibility_score": "High Probability",
            "symptoms_analysis": (
                "• ⚪ Oval grayish-white spots with dark brown halos on older fronds.\n"
                "• 🔥 Lesions coalesce, causing premature leaf scorching."
            ),
            "cure_and_medication": (
                "1. 💧 Spray foliage with Copper Oxychloride (3g/L).\n"
                "2. 🌾 Supplement soil potassium with Muriate of Potash (MOP).\n"
                "3. 🚫 Avoid saline irrigation water."
            ),
            "fun_fact": "Gray Leaf Spot is heavily exacerbated when coconut palms lack potassium in sandy soil.",
            "suggested_next_step": "Spray Copper Oxychloride and apply Potash."
        },
        "ta": {
            "condition_title": "சாம்பல் இலைப் புள்ளி (Pestalotiopsis palmarum)",
            "possibility_score": "அதிக சாத்தியக்கூறு",
            "symptoms_analysis": (
                "• ⚪ முதிர்ந்த இலைகளில் பழுப்பு நிற விளிம்புடன் சாம்பல் புள்ளிகள் தோன்றும்.\n"
                "• 🔥 புள்ளிகள் ஒன்றுசேர்ந்து இலைகள் விரைவாக காய்ந்து உதிரும்."
            ),
            "cure_and_medication": (
                "1. 💧 காப்பர் ஆக்சிகுளோரைடு (1L-க்கு 3g) தண்ணீரில் கலந்து தெளிக்கவும்.\n"
                "2. 🌾 மரத்திற்கு பொட்டாஷ் (MOP) உரமிட்டு எதிர்ப்புத் திறனை கூட்டவும்.\n"
                "3. 🚫 உவர் நீரால் பாசனம் செய்வதைத் தவிர்க்கவும்."
            ),
            "fun_fact": "மண்ணில் பொட்டாசியம் சத்து குறையும்போது இந்நோய் தீவிரமடைகிறது.",
            "suggested_next_step": "காப்பர் ஆக்சிகுளோரைடு தெளித்து பொட்டாஷ் இடவும்."
        }
    },
    "HEALTHY": {
        "en": {
            "condition_title": "Healthy Coconut Palm (Cocos nucifera)",
            "possibility_score": "Confirmed Healthy (95%)",
            "symptoms_analysis": (
                "• 🌴 Deep green, vibrant fronds with intact leaf margins.\n"
                "• ✨ Clean crown symmetry; zero pathogenic necrosis or boring."
            ),
            "cure_and_medication": (
                "1. ✅ No therapeutic intervention required.\n"
                "2. 💧 Maintain routine irrigation (~45-50L/palm/week).\n"
                "3. 🌱 Apply biannual balanced NPK + micronutrients (Borax)."
            ),
            "fun_fact": "A healthy coconut palm produces 12–14 new fronds and up to 80 nuts annually.",
            "suggested_next_step": "Maintain routine nutrition and irrigation."
        },
        "ta": {
            "condition_title": "ஆரோக்கியமான தென்னை மரம் (Cocos nucifera)",
            "possibility_score": "உறுதிப்படுத்தப்பட்ட நலம் (95%)",
            "symptoms_analysis": (
                "• 🌴 அடர்ந்த பசுமையான இலைகள்; சேதமில்லாத இலை விளிம்புகள்.\n"
                "• ✨ சீரான இலை மகுடம்; நோய் அல்லது பூச்சி தாக்குதல் இல்லை."
            ),
            "cure_and_medication": (
                "1. ✅ ரசாயன மருந்துகள் எதுவும் தேவையில்லை.\n"
                "2. 💧 வழக்கமான நீர்ப்பாசனம் (வாரத்திற்கு 45-50L) தொடரவும்.\n"
                "3. 🌱 ஆண்டுக்கு இருமுறை சமச்சீர் NPK மற்றும் போராக்ஸ் உரமிடவும்."
            ),
            "fun_fact": "ஆரோக்கியமான தென்னை மரம் ஆண்டுக்கு 12-14 புதிய இலைகளை உருவாக்கி மகுடத்தை பசுமையாக வைக்கும்.",
            "suggested_next_step": "வழக்கமான நீர் மற்றும் உர மேலாண்மையை தொடரவும்."
        }
    },
    "UNKNOWN": {
        "en": {
            "condition_title": "Atypical Foliar Presentation",
            "possibility_score": "Under Evaluation",
            "symptoms_analysis": (
                "• ❓ Atypical discoloration not matching primary 4 palm pathogens.\n"
                "• 🔬 Requires visual differentiation from pest or nutrient stress."
            ),
            "cure_and_medication": (
                "1. 🛑 Quarantine palm to prevent potential pathogen spread.\n"
                "2. 📸 Capture close-up photos of fronds, crown, and stem.\n"
                "3. 👨‍🌾 Consult your local Agricultural Extension Officer or KVK."
            ),
            "fun_fact": "Over 100 physiological and insect disorders affect coconut palms worldwide.",
            "suggested_next_step": "Consult agricultural expert for tissue assay."
        },
        "ta": {
            "condition_title": "அறியப்படாத நிலை / விரிவான பரிசோதனை தேவை",
            "possibility_score": "ஆய்வில் உள்ளது",
            "symptoms_analysis": (
                "• ❓ முக்கிய 4 தென்னை நோய்களுடன் பொருந்தாத அசாதாரண இலை நிறமாற்றம்.\n"
                "• 🔬 பூச்சி அல்லது சத்துக் குறைபாடா என விரிவான கள ஆய்வு தேவை."
            ),
            "cure_and_medication": (
                "1. 🛑 நோய் பரவலைத் தடுக்க பாதிக்கப்பட்ட மரத்தை தனிமைப்படுத்தவும்.\n"
                "2. 📸 இலை மற்றும் தண்டுப் பகுதிகளை புகைப்படமெடுக்கவும்.\n"
                "3. 👨‍🌾 வேளாண்மை விரிவாக்க அலுவலர் அல்லது KVK-யிடம் ஆலோசிக்கவும்."
            ),
            "fun_fact": "தென்னை மரங்களில் 100-க்கும் மேற்பட்ட உடலியல் குறைபாடுகள் ஆவணப்படுத்தப்பட்டுள்ளன.",
            "suggested_next_step": "வேளாண் விஞ்ஞானியிடம் இலை மாதிரியைக் காண்பிக்கவும்."
        }
    }
}

DISEASE_TARGETS: Dict[str, Dict[str, str]] = {
    "BUD": {
        "id": "BUD",
        "emoji": "🌿",
        "label": "BUD ROT",
        "target_name": "Bud Rot",
        "pathogen": "Phytophthora palmivora"
    },
    "LEAF": {
        "id": "LEAF",
        "emoji": "🍂",
        "label": "LEAF ROT",
        "target_name": "Leaf Rot",
        "pathogen": "Colletotrichum gloeosporioides"
    },
    "STEM": {
        "id": "STEM",
        "emoji": "🩸",
        "label": "STEM BLEED",
        "target_name": "Stem Bleeding",
        "pathogen": "Ceratocystis paradoxa"
    },
    "GRAY": {
        "id": "GRAY",
        "emoji": "⚪",
        "label": "GRAY SPOT",
        "target_name": "Gray Leaf Spot",
        "pathogen": "Pestalotiopsis palmarum"
    },
    "HEALTHY": {
        "id": "HEALTHY",
        "emoji": "🌴",
        "label": "HEALTHY",
        "target_name": "Healthy Coconut Palm",
        "pathogen": "None"
    },
    "UNKNOWN": {
        "id": "UNKNOWN",
        "emoji": "❓",
        "label": "UNKNOWN",
        "target_name": "Unknown / Full Pathology Examination",
        "pathogen": "Broad scan"
    },
}

class CocoGuardApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # --- WINDOW / ANDROID VIEWPORT CONFIGURATION ---
        self.title("Coco-Guard")
        self.geometry("440x880")
        self.minsize(380, 720)
        self.configure(fg_color=COLOR_BG)

        # State
        self.active_disease_id: Optional[str] = None
        self.selected_image_path: Optional[str] = None
        self.selected_photo_image: Optional[ImageTk.PhotoImage] = None
        self.is_analyzing = False
        self.current_lang = "en"  # "en" or "ta"

        # Complete bilingual result payload
        self.current_bilingual_result: Optional[Dict[str, Any]] = None

        self._build_ui()

    def _build_ui(self):
        # Main scrollable canvas on warm sand background
        self.main_scroll = ctk.CTkScrollableFrame(
            self,
            fg_color=COLOR_BG,
            scrollbar_fg_color=COLOR_BG,
            scrollbar_button_color="#B5A973",
            scrollbar_button_hover_color="#9C915E",
            corner_radius=0
        )
        self.main_scroll.pack(fill="both", expand=True)

        # --- 1. EDITORIAL HEADER WITH INSTRUMENT SERIF & SUBSCRIPT ---
        top_frame = ctk.CTkFrame(self.main_scroll, fg_color="transparent")
        top_frame.pack(fill="x", padx=20, pady=(16, 10))

        brand_col = ctk.CTkFrame(top_frame, fg_color="transparent")
        brand_col.pack(side="left", anchor="w")

        self.title_label = ctk.CTkLabel(
            brand_col,
            text="🌴 Coco-Guard",
            font=ctk.CTkFont(family=FONT_SERIF, size=34, weight="bold"),
            text_color=COLOR_TEXT_DARK,
            anchor="w"
        )
        self.title_label.pack(anchor="w")

        # Tiny yet visible subscript: "🌾 for the farmers, by the farmers."
        self.subscript_label = ctk.CTkLabel(
            brand_col,
            text="🌾 for the farmers, by the farmers.",
            font=ctk.CTkFont(family=FONT_SERIF, size=13, slant="italic"),
            text_color=COLOR_TEXT_SAND_DARK,
            anchor="w"
        )
        self.subscript_label.pack(anchor="w", pady=(1, 0))

        # --- 2. CAMERA / SHUTTER CONTAINER (SOFT UI MOLDED ENVELOPE) ---
        shutter_container = ctk.CTkFrame(
            self.main_scroll,
            fg_color=COLOR_NEU_CARD_BG,
            border_width=1,
            border_color=COLOR_NEU_CARD_BORDER,
            corner_radius=18
        )
        shutter_container.pack(fill="x", padx=16, pady=(0, 14))

        # Viewport Preview Box: Debossed, recessed well
        self.preview_box = ctk.CTkLabel(
            shutter_container,
            text="",
            fg_color=COLOR_WELL_INSET,
            corner_radius=12,
            height=180
        )
        self.preview_box.pack(fill="x", padx=12, pady=(12, 10))

        # Neumorphic Convex Capsule Shutter Button with Instrument Serif
        self.shutter_btn = ctk.CTkButton(
            shutter_container,
            text="📸  CAPTURE / SELECT PALM PHOTO",
            font=ctk.CTkFont(family=FONT_SERIF, size=14, weight="bold"),
            fg_color=COLOR_BTN_CONVEX,
            hover_color=COLOR_BTN_HOVER,
            text_color=COLOR_TEXT_WHITE,
            border_width=1,
            border_color=COLOR_RIM_SPECULAR,
            corner_radius=25,
            height=46,
            command=self.on_shutter_clicked
        )
        self.shutter_btn.pack(fill="x", padx=12, pady=(0, 14))

        # --- 3. DISEASE ANALYSIS PRESETS (NEUMORPHIC TACTILE TILES) ---
        presets_label_frame = ctk.CTkFrame(self.main_scroll, fg_color="transparent")
        presets_label_frame.pack(fill="x", padx=18, pady=(4, 6))

        self.options_title = ctk.CTkLabel(
            presets_label_frame,
            text="🔬 DISEASE ANALYSIS PRESETS",
            font=ctk.CTkFont(family=FONT_SERIF, size=13, weight="bold"),
            text_color=COLOR_TEXT_DARK,
            anchor="w"
        )
        self.options_title.pack(side="left")

        # 6 Presets Frame (Sculpted Molded Base)
        self.buttons_frame = ctk.CTkFrame(
            self.main_scroll,
            fg_color=COLOR_NEU_CARD_BG,
            border_width=1,
            border_color=COLOR_NEU_CARD_BORDER,
            corner_radius=16
        )
        self.buttons_frame.pack(fill="x", padx=16, pady=(0, 14))

        # 3 columns x 2 rows tactile grid
        self.buttons_frame.grid_columnconfigure((0, 1, 2), weight=1)

        self.disease_buttons: Dict[str, ctk.CTkButton] = {}
        disease_keys = ["BUD", "LEAF", "STEM", "GRAY", "HEALTHY", "UNKNOWN"]

        for idx, key in enumerate(disease_keys):
            target = DISEASE_TARGETS[key]
            row = idx // 3
            col = idx % 3
            btn = ctk.CTkButton(
                self.buttons_frame,
                text=f"{target['emoji']}  {target['label']}",
                font=ctk.CTkFont(family=FONT_SERIF, size=13, weight="bold"),
                fg_color=COLOR_BTN_CONVEX,
                hover_color=COLOR_BTN_HOVER,
                text_color=COLOR_TEXT_WHITE,
                border_width=1,
                border_color=COLOR_RIM_SPECULAR,
                corner_radius=12,
                height=44,
                command=lambda k=key: self.on_disease_button_clicked(k)
            )
            btn.grid(row=row, column=col, padx=6, pady=6, sticky="nsew")
            self.disease_buttons[key] = btn

        # --- 4. DIAGNOSIS OUTPUT CARD (MOLDED SOFT CARD WITH RECESSED WELLS) ---
        self.output_card = ctk.CTkFrame(
            self.main_scroll,
            fg_color=COLOR_NEU_CARD_BG,
            border_width=1,
            border_color=COLOR_NEU_CARD_BORDER,
            corner_radius=18
        )

        # Header inside output card: Status pill & Neumorphic language button
        badge_row = ctk.CTkFrame(self.output_card, fg_color="transparent")
        badge_row.pack(fill="x", padx=16, pady=(14, 6))

        self.status_badge = ctk.CTkLabel(
            badge_row,
            text="🩺 BOTANICAL DOCTOR ASSESSMENT",
            font=ctk.CTkFont(family=FONT_SERIF, size=12, weight="bold"),
            fg_color=COLOR_BADGE_BG,
            text_color=COLOR_BADGE_TEXT,
            corner_radius=14,
            padx=12,
            pady=4
        )
        self.status_badge.pack(side="left")

        # Soft Neumorphic Language Capsule Button with Instrument Serif
        self.lang_btn = ctk.CTkButton(
            badge_row,
            text="🌐 தமிழில் பார்க்க",
            font=ctk.CTkFont(family=FONT_SERIF, size=13, weight="bold"),
            fg_color=COLOR_BTN_CONVEX,
            hover_color=COLOR_BTN_HOVER,
            text_color=COLOR_TEXT_WHITE,
            border_width=1,
            border_color=COLOR_RIM_SPECULAR,
            corner_radius=16,
            width=140,
            height=30,
            command=self.toggle_output_language
        )
        self.lang_btn.pack(side="right")

        # Headline with Instrument Serif
        self.condition_heading = ctk.CTkLabel(
            self.output_card,
            text="",
            font=ctk.CTkFont(family=FONT_SERIF, size=23, weight="bold"),
            text_color=COLOR_TEXT_PRIMARY,
            anchor="w",
            wraplength=380,
            justify="left"
        )
        self.condition_heading.pack(fill="x", padx=16, pady=(8, 2))

        # Possibility Tag with Instrument Serif
        self.possibility_label = ctk.CTkLabel(
            self.output_card,
            text="",
            font=ctk.CTkFont(family=FONT_SERIF, size=13),
            text_color=COLOR_TEXT_MUTED,
            anchor="w",
            wraplength=380,
            justify="left"
        )
        self.possibility_label.pack(fill="x", padx=16, pady=(0, 10))

        # Symptoms Recessed Well (Debossed Soft Inset)
        self.symptoms_container = ctk.CTkFrame(
            self.output_card,
            fg_color=COLOR_WELL_INSET,
            border_width=1,
            border_color=COLOR_WELL_BORDER,
            corner_radius=12
        )
        self.symptoms_container.pack(fill="x", padx=14, pady=6)

        self.symptoms_header = ctk.CTkLabel(
            self.symptoms_container,
            text="🔍 DIAGNOSIS & OBSERVED SYMPTOMS",
            font=ctk.CTkFont(family=FONT_SERIF, size=13, weight="bold"),
            text_color=COLOR_TEXT_MUTED,
            anchor="w"
        )
        self.symptoms_header.pack(fill="x", padx=12, pady=(10, 4))

        # Highly Readable Output Text in Instrument Serif
        self.symptoms_body = ctk.CTkLabel(
            self.symptoms_container,
            text="",
            font=ctk.CTkFont(family=FONT_SERIF, size=14),
            text_color=COLOR_TEXT_WHITE,
            wraplength=360,
            justify="left",
            anchor="w"
        )
        self.symptoms_body.pack(fill="x", padx=12, pady=(0, 12))

        # Cure & Medication Recessed Well (Debossed Soft Inset)
        self.treatment_container = ctk.CTkFrame(
            self.output_card,
            fg_color=COLOR_WELL_INSET,
            border_width=1,
            border_color=COLOR_WELL_BORDER,
            corner_radius=12
        )
        self.treatment_container.pack(fill="x", padx=14, pady=(6, 14))

        self.treatment_header = ctk.CTkLabel(
            self.treatment_container,
            text="💊 CURE & RECOMMENDED MEDICATION",
            font=ctk.CTkFont(family=FONT_SERIF, size=13, weight="bold"),
            text_color=COLOR_TEXT_MUTED,
            anchor="w"
        )
        self.treatment_header.pack(fill="x", padx=12, pady=(10, 4))

        # Highly Readable Output Text in Instrument Serif
        self.treatment_body = ctk.CTkLabel(
            self.treatment_container,
            text="",
            font=ctk.CTkFont(family=FONT_SERIF, size=14),
            text_color=COLOR_TEXT_WHITE,
            wraplength=360,
            justify="left",
            anchor="w"
        )
        self.treatment_body.pack(fill="x", padx=12, pady=(0, 12))

        # Fun Fact Recessed Well with Soft Pill Badge
        self.fun_fact_container = ctk.CTkFrame(
            self.output_card,
            fg_color=COLOR_WELL_INSET,
            border_width=1,
            border_color=COLOR_WELL_BORDER,
            corner_radius=12
        )
        self.fun_fact_container.pack(fill="x", padx=14, pady=(6, 16))

        fun_fact_header_row = ctk.CTkFrame(self.fun_fact_container, fg_color="transparent")
        fun_fact_header_row.pack(fill="x", padx=12, pady=(10, 4))

        self.fun_fact_header = ctk.CTkLabel(
            fun_fact_header_row,
            text="💡 BOTANICAL FUN FACT",
            font=ctk.CTkFont(family=FONT_SERIF, size=13, weight="bold"),
            text_color=COLOR_TEXT_MUTED,
            anchor="w"
        )
        self.fun_fact_header.pack(side="left")

        self.fun_fact_badge = ctk.CTkLabel(
            fun_fact_header_row,
            text="⚡ GEMINI 3.5 FLASH-LITE",
            font=ctk.CTkFont(family=FONT_SERIF, size=11, weight="bold"),
            fg_color=COLOR_BADGE_BG,
            text_color=COLOR_BADGE_TEXT,
            corner_radius=10,
            padx=8,
            pady=2
        )
        self.fun_fact_badge.pack(side="right")

        # Highly Readable Output Text in Instrument Serif
        self.fun_fact_body = ctk.CTkLabel(
            self.fun_fact_container,
            text="",
            font=ctk.CTkFont(family=FONT_SERIF, size=14),
            text_color=COLOR_TEXT_WHITE,
            wraplength=360,
            justify="left",
            anchor="w"
        )
        self.fun_fact_body.pack(fill="x", padx=12, pady=(0, 12))

    # --- ACTIONS & BOTANICAL DOCTOR LOGIC ---

    def on_shutter_clicked(self):
        """Single shutter action: captures/selects image, previews inside the recessed well."""
        file_path = filedialog.askopenfilename(
            title="Select Coconut Palm Image for Botanical Doctor Analysis",
            filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.webp;*.bmp"), ("All Files", "*.*")]
        )
        if not file_path:
            return

        self.selected_image_path = file_path
        self._display_preview(file_path)

        # Clear prior analysis cache
        self.current_bilingual_result = None
        self.current_lang = "en"

        if self.active_disease_id:
            self._trigger_botanical_analysis(self.active_disease_id)
        else:
            self._show_output_card()
            self.status_badge.configure(text="📸 PHOTO LOADED", text_color=COLOR_TEXT_WHITE)
            self.condition_heading.configure(text="Photo Ready for Botanical Analysis")
            self.possibility_label.configure(text="Select a disease button above to verify if it is present.")
            self.symptoms_body.configure(text="👉 Click BUD, LEAF, STEM, GRAY, HEALTHY, or UNKNOWN to dispatch the Botanical Doctor.")
            self.treatment_body.configure(text="💊 Medication and cure will appear once a disease hypothesis is evaluated.")
            self.fun_fact_body.configure(
                text="The coconut palm is known as 'Kalpavriksha' in Sanskrit, meaning 'the tree that provides all the necessities of life'."
            )
            self.lang_btn.configure(state="disabled")

    def _display_preview(self, file_path: str):
        try:
            img = Image.open(file_path)
            img.thumbnail((380, 170), Image.Resampling.LANCZOS)
            photo = ImageTk.PhotoImage(img)
            self.selected_photo_image = photo
            self.preview_box.configure(image=photo, text="")
        except Exception:
            self.preview_box.configure(text=f"Loaded: {os.path.basename(file_path)}", text_color=COLOR_TEXT_WHITE)

    def on_disease_button_clicked(self, disease_id: str):
        """User clicks a disease button: triggers convex-to-debossed tactile feedback and runs analysis."""
        self.active_disease_id = disease_id
        self._highlight_button(disease_id)

        if not self.selected_image_path:
            self._show_output_card()
            self.status_badge.configure(text="⚠️ PALM PHOTO NEEDED", text_color=COLOR_TEXT_MUTED)
            self.condition_heading.configure(text=f"Testing for {DISEASE_TARGETS[disease_id]['target_name']}")
            self.possibility_label.configure(text="No photo selected yet.")
            self.symptoms_body.configure(text="📸 Please tap 'CAPTURE / SELECT PALM PHOTO' above to load a picture to analyze.")
            self.treatment_body.configure(text="🔬 The Botanical Doctor requires an image to verify this pathology.")
            self.fun_fact_body.configure(
                text="Coconut palms do not have a taproot; instead, they have a fibrous root system with 4,000 to 7,000 roots."
            )
            self.lang_btn.configure(state="disabled")
            return

        self._trigger_botanical_analysis(disease_id)

    def _highlight_button(self, disease_id: str):
        """Applies tactile debossed state to active button and convex state to unselected ones."""
        for key, btn in self.disease_buttons.items():
            if key == disease_id:
                btn.configure(
                    border_color=COLOR_RIM_ACTIVE,
                    border_width=2,
                    fg_color=COLOR_BTN_DEBOSSED
                )
            else:
                btn.configure(
                    border_color=COLOR_RIM_SPECULAR,
                    border_width=1,
                    fg_color=COLOR_BTN_CONVEX
                )

    def _show_output_card(self):
        if not self.output_card.winfo_ismapped():
            self.output_card.pack(fill="x", padx=16, pady=(0, 24))

    def _trigger_botanical_analysis(self, disease_id: str):
        """Dispatches the tailored Botanical Doctor prompt requesting concise, shrunk-down English & Tamil outputs."""
        self._show_output_card()
        target = DISEASE_TARGETS[disease_id]

        self.status_badge.configure(text="🩺 BOTANICAL DOCTOR EXAMINING...", text_color=COLOR_TEXT_WHITE)
        self.condition_heading.configure(text=f"Inspecting for {target['target_name']}...")
        self.possibility_label.configure(text="Evaluating cellular necrosis, lesions, and foliar symptoms...")
        self.symptoms_body.configure(text="🔬 Botanical Doctor is inspecting image tissue against pathology markers...")
        self.treatment_body.configure(text="💊 Formulating concise medication protocol in English & Tamil...")
        self.fun_fact_body.configure(text="⚡ Querying Gemini 3.5 Flash-Lite for live pathology & botanical facts...")
        self.shutter_btn.configure(state="disabled")
        self.lang_btn.configure(state="disabled")
        self.is_analyzing = True

        thread = threading.Thread(
            target=self._botanical_doctor_worker,
            args=(self.selected_image_path, disease_id),
            daemon=True
        )
        thread.start()

    def _botanical_doctor_worker(self, file_path: str, disease_id: str):
        api_key = self._get_gemini_api_key()

        if not api_key:
            fallback = FALLBACK_DISEASE_DB.get(disease_id, FALLBACK_DISEASE_DB["UNKNOWN"])
            result = {
                "is_target_matched": (disease_id == "HEALTHY"),
                "en": dict(fallback["en"]),
                "ta": dict(fallback["ta"])
            }
            result["en"]["possibility_score"] = "Reference Benchmark (API Key Standby)"
            result["ta"]["possibility_score"] = "முன்னிருப்பு தரவு (API Key காத்திருக்கிறது)"
            self.after(0, lambda: self._on_botanical_analysis_complete(disease_id, result))
            return

        try:
            from google import genai

            client = genai.Client(api_key=api_key)
            pil_image = Image.open(file_path).convert("RGB")
            pil_image.thumbnail((1024, 1024), Image.Resampling.LANCZOS)

            target = DISEASE_TARGETS[disease_id]

            conciseness_instruction = (
                "CRITICAL CONCISENESS & SHRINK RULES:\n"
                "- Keep outputs ultra-compact, precise, and shrunk down for rapid reading on mobile.\n"
                "- Include appropriate helpful emojis (e.g. • 🍂, 1. ✂️, 2. 🛡️) to make it engaging and lively.\n"
                "- symptoms_analysis: Exactly 2 to 3 bullet points (•) describing key visual markers. No introductory filler.\n"
                "- cure_and_medication: Exactly 2 to 3 numbered steps (1., 2.) with precise chemical names and dosages.\n"
                "- fun_fact: Exactly 1 punchy, memorable sentence.\n"
                "- Provide identical concise structure for BOTH English ('en') and Tamil ('ta')."
            )

            if disease_id == "UNKNOWN":
                prompt = (
                    "You are an authoritative Botanical Doctor and Agricultural Plant Pathologist specializing in coconut palms (Cocos nucifera).\n"
                    "The user has requested an open-ended botanical pathology diagnosis under the UNKNOWN protocol.\n\n"
                    f"{conciseness_instruction}\n\n"
                    "Respond STRICTLY in valid JSON format with this exact structure:\n"
                    "{\n"
                    '  "is_target_matched": true,\n'
                    '  "en": {\n'
                    '    "condition_title": "Concise Diagnosis Headline in English",\n'
                    '    "possibility_score": "e.g. High Probability (85%)",\n'
                    '    "symptoms_analysis": "• 🍂 Short bullet 1\\n• 🔍 Short bullet 2",\n'
                    '    "cure_and_medication": "1. ✂️ Short step 1\\n2. 🛡️ Short step 2",\n'
                    '    "fun_fact": "1 punchy sentence in English.",\n'
                    '    "suggested_next_step": "Short advice"\n'
                    '  },\n'
                    '  "ta": {\n'
                    '    "condition_title": "சுருக்கமான தலைப்பு தமிழில்",\n'
                    '    "possibility_score": "சாத்தியக்கூறு தமிழில்",\n'
                    '    "symptoms_analysis": "• 🍂 சுருக்கமான குறிப்பு 1\\n• 🔍 சுருக்கமான குறிப்பு 2",\n'
                    '    "cure_and_medication": "1. ✂️ சுருக்கமான சிகிச்சை 1\\n2. 🛡️ சுருக்கமான சிகிச்சை 2",\n'
                    '    "fun_fact": "1 சுவாரஸ்யமான வரி தமிழில்.",\n'
                    '    "suggested_next_step": "வழிகாட்டல் தமிழில்"\n'
                    '  }\n'
                    "}"
                )
            else:
                prompt = (
                    f"You are an authoritative Botanical Doctor and Agricultural Plant Pathologist specializing in coconut palms (Cocos nucifera).\n"
                    f"The user has provided an image and specifically asks you to analyze if it has:\n"
                    f"TARGET DISEASE: {target['target_name']} ({target['pathogen']})\n\n"
                    f"{conciseness_instruction}\n\n"
                    f"INSTRUCTIONS:\n"
                    f"1. ANALYZE if the given picture has {target['target_name']} or not.\n"
                    f"2. IF YES: State possibility (e.g. 'Confirmed (90%)'), 2-3 short bulleted visual symptoms with emojis, and 2-3 numbered medication steps.\n"
                    f"3. IF NO: State 'Negative: Looks like [Alternative Disease / Healthy / Unknown]', explain in 2 bullets why it diverges, and advise next button.\n"
                    f"4. Provide full outputs in BOTH English and natural Tamil for farmers.\n\n"
                    "Respond STRICTLY in valid JSON format with this exact structure:\n"
                    "{\n"
                    '  "is_target_matched": true or false,\n'
                    '  "en": {\n'
                    '    "condition_title": "Concise Headline in English",\n'
                    '    "possibility_score": "Short possibility score in English",\n'
                    '    "symptoms_analysis": "• 🍂 Short bullet 1\\n• 🔍 Short bullet 2",\n'
                    '    "cure_and_medication": "1. ✂️ Actionable step 1\\n2. 🛡️ Actionable step 2",\n'
                    '    "fun_fact": "1 punchy sentence in English.",\n'
                    '    "suggested_next_step": "Short button recommendation in English"\n'
                    '  },\n'
                    '  "ta": {\n'
                    '    "condition_title": "சுருக்கமான தலைப்பு தமிழில்",\n'
                    '    "possibility_score": "சாத்தியக்கூறு தமிழில்",\n'
                    '    "symptoms_analysis": "• 🍂 சுருக்கமான குறிப்பு 1\\n• 🔍 சுருக்கமான குறிப்பு 2",\n'
                    '    "cure_and_medication": "1. ✂️ சுருக்கமான சிகிச்சை 1\\n2. 🛡️ சுருக்கமான சிகிச்சை 2",\n'
                    '    "fun_fact": "1 சுவாரஸ்யமான வரி தமிழில்.",\n'
                    '    "suggested_next_step": "அடுத்த கட்ட வழிகாட்டல் தமிழில்"\n'
                    '  }\n'
                    "}"
                )

            response = client.models.generate_content(
                model="gemini-3.5-flash-lite",
                contents=[
                    pil_image,
                    prompt
                ]
            )

            raw_text = response.text or ""
            parsed = self._extract_bilingual_json(raw_text, disease_id)
            self.after(0, lambda: self._on_botanical_analysis_complete(disease_id, parsed))
        except Exception as err:
            fallback = FALLBACK_DISEASE_DB.get(disease_id, FALLBACK_DISEASE_DB["UNKNOWN"])
            err_dict = {
                "is_target_matched": False,
                "en": {
                    "condition_title": f"{target['target_name']} Assessment (Offline Mode)",
                    "possibility_score": "Local Benchmark",
                    "symptoms_analysis": fallback['en']['symptoms_analysis'],
                    "cure_and_medication": fallback['en']['cure_and_medication'],
                    "fun_fact": fallback['en']['fun_fact'],
                    "suggested_next_step": f"Notice: {str(err)[:50]}..."
                },
                "ta": {
                    "condition_title": f"{target['target_name']} மதிப்பீடு (உள்ளூர் தரவு)",
                    "possibility_score": "உள்ளூர் நிலை",
                    "symptoms_analysis": fallback['ta']['symptoms_analysis'],
                    "cure_and_medication": fallback['ta']['cure_and_medication'],
                    "fun_fact": fallback['ta']['fun_fact'],
                    "suggested_next_step": "இணைப்பு சீரானதும் மீண்டும் முயற்சி செய்யவும்."
                }
            }
            self.after(0, lambda: self._on_botanical_analysis_complete(disease_id, err_dict))

    def _extract_bilingual_json(self, text: str, disease_id: str) -> Dict[str, Any]:
        """Safely extracts bilingual JSON payload with guaranteed English and Tamil blocks."""
        clean = text.replace("```json", "").replace("```", "").strip()
        start = clean.find("{")
        end = clean.rfind("}")
        if start != -1 and end != -1 and end > start:
            clean = clean[start:end+1]

        fallback = FALLBACK_DISEASE_DB.get(disease_id, FALLBACK_DISEASE_DB["UNKNOWN"])

        try:
            data = json.loads(clean)
            is_matched = data.get("is_target_matched", True)

            if "en" not in data or not isinstance(data["en"], dict):
                en_block = {
                    "condition_title": data.get("condition_title", fallback["en"]["condition_title"]),
                    "possibility_score": data.get("possibility_score", "High Probability"),
                    "symptoms_analysis": data.get("symptoms_analysis", fallback["en"]["symptoms_analysis"]),
                    "cure_and_medication": data.get("cure_and_medication", fallback["en"]["cure_and_medication"]),
                    "fun_fact": data.get("fun_fact", fallback["en"]["fun_fact"]),
                    "suggested_next_step": data.get("suggested_next_step", "")
                }
            else:
                en_block = data["en"]

            if "ta" not in data or not isinstance(data["ta"], dict):
                ta_block = dict(fallback["ta"])
            else:
                ta_block = data["ta"]

            return {
                "is_target_matched": is_matched,
                "en": en_block,
                "ta": ta_block
            }
        except Exception:
            return {
                "is_target_matched": True,
                "en": dict(fallback["en"]),
                "ta": dict(fallback["ta"])
            }

    def _on_botanical_analysis_complete(self, disease_id: str, result: Dict[str, Any]):
        self.shutter_btn.configure(state="normal")
        self.is_analyzing = False
        self.current_bilingual_result = result
        self.current_lang = "en"

        self._render_output_view(lang="en")
        self.lang_btn.configure(state="normal", text="🌐 தமிழில் பார்க்க")

    def toggle_output_language(self):
        """Instantly toggles all output bodies and titles between English and Tamil with zero network delay."""
        if not self.current_bilingual_result:
            return

        if self.current_lang == "en":
            self.current_lang = "ta"
            self._render_output_view(lang="ta")
            self.lang_btn.configure(text="🌐 Read in English")
        else:
            self.current_lang = "en"
            self._render_output_view(lang="en")
            self.lang_btn.configure(text="🌐 தமிழில் பார்க்க")

    def _render_output_view(self, lang: str = "en"):
        if not self.current_bilingual_result:
            return

        data = self.current_bilingual_result
        is_matched = data.get("is_target_matched", True)
        content = data.get(lang, data.get("en", {}))

        if lang == "ta":
            self.status_badge.configure(
                text="🩺 தாவரவியல் மருத்துவர் ஆய்வு" if is_matched else "⚠️ வேறு நோய் சாத்தியம்",
                text_color=COLOR_TEXT_WHITE
            )
            self.symptoms_header.configure(text="🔍 ஆய்வு & அறிகுறிகள்")
            self.treatment_header.configure(text="💊 பரிந்துரை & சிகிச்சை")
            self.fun_fact_header.configure(text="💡 தாவரவியல் சுவாரஸ்ய தகவல்")
            self.fun_fact_badge.configure(text="⚡ ஜெமினி 3.5 ஃப்ளாஷ்-லைட்")
        else:
            self.status_badge.configure(
                text="🩺 BOTANICAL DOCTOR ASSESSMENT" if is_matched else "⚠️ ALTERNATIVE CONDITION DETECTED",
                text_color=COLOR_TEXT_WHITE
            )
            self.symptoms_header.configure(text="🔍 DIAGNOSIS & OBSERVED SYMPTOMS")
            self.treatment_header.configure(text="💊 CURE & RECOMMENDED MEDICATION")
            self.fun_fact_header.configure(text="💡 BOTANICAL FUN FACT")
            self.fun_fact_badge.configure(text="⚡ GEMINI 3.5 FLASH-LITE")

        # Set title with Instrument Serif
        self.condition_heading.configure(text=content.get("condition_title", ""))

        # Set possibility score
        possibility = content.get("possibility_score", "")
        next_step = content.get("suggested_next_step", "")
        if next_step and not is_matched:
            if lang == "ta":
                self.possibility_label.configure(
                    text=f"📊 சாத்தியக்கூறு: {possibility}  •  🧭 வழிகாட்டல்: {next_step}",
                    text_color=COLOR_TEXT_MUTED
                )
            else:
                self.possibility_label.configure(
                    text=f"📊 Possibility: {possibility}  •  🧭 Guidance: {next_step}",
                    text_color=COLOR_TEXT_MUTED
                )
        else:
            prefix = "📊 சாத்தியக்கூறு / நிலை:" if lang == "ta" else "📊 Possibility / Status:"
            self.possibility_label.configure(
                text=f"{prefix} {possibility}",
                text_color=COLOR_TEXT_MUTED
            )

        # Set body paragraphs (ENTIRE OUTPUT TRANSLATED & HIGHLY READABLE)
        self.symptoms_body.configure(text=content.get("symptoms_analysis", ""))
        self.treatment_body.configure(text=content.get("cure_and_medication", ""))
        self.fun_fact_body.configure(text=content.get("fun_fact", ""))

    def _get_gemini_api_key(self) -> str:
        key = os.environ.get("GEMINI_API_KEY", "").strip()
        base_dir = os.path.dirname(os.path.abspath(__file__))
        candidate_dirs = [base_dir, os.path.dirname(base_dir)]

        if not key:
            for d in candidate_dirs:
                prop_path = os.path.join(d, "local.properties")
                if os.path.exists(prop_path):
                    try:
                        with open(prop_path, "r", encoding="utf-8") as f:
                            for line in f:
                                if line.startswith("GEMINI_API_KEY="):
                                    key = line.split("=", 1)[1].strip()
                                    if key:
                                        break
                    except Exception:
                        pass
                if key:
                    break

        if not key:
            for d in candidate_dirs:
                env_path = os.path.join(d, ".env")
                if os.path.exists(env_path):
                    try:
                        with open(env_path, "r", encoding="utf-8") as f:
                            for line in f:
                                if line.startswith("GEMINI_API_KEY="):
                                    key = line.split("=", 1)[1].strip()
                                    if key:
                                        break
                    except Exception:
                        pass
                if key:
                    break

        # No hardcoded fallback key — must be set via .env or environment variable
        return key


if __name__ == "__main__":
    app = CocoGuardApp()
    app.mainloop()
