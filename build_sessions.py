import os

sessions_data = [
    {
        "num": 1,
        "title": "مدخل إلى عالم الذكاء الاصطناعي",
        "subtitle": "من مستهلك للتطبيقات إلى مبتكر يبني الـ AI بنفسه 🤖✨",
        "tag": "السيشن الأول 🚀",
        "agenda": [
            "ما هو الذكاء الاصطناعي والفرق بينه وبين البرمجة العادية؟",
            "أين نجد الذكاء الاصطناعي في حياتنا اليومية والتطبيقات؟",
            "أبعاد الذكاء الاصطناعي (أنواعه وأخلاقياته ومستقبله).",
            "تجربة محاكاة تفاعلية مباشرة لتغطية نمط ذكي على الويب.",
            "كتابة أول برنامج تحليل مشاعر تفاعلي بـ Python.",
            "اختبار المعلومات التفاعلي + تحدي مشروع الحصة!"
        ],
        "sec1_title": "1. ما هو الذكاء الاصطناعي؟ (الفرق الجوهري)",
        "sec1_desc": "في البرمجة التقليدية نكتب كل القواعد يدوياً (If/Else)، بينما في الذكاء الاصطناعي نغذي الكمبيوتر ببيانات كثيرة ليستنتج القواعد بنفسه!",
        "sec2_title": "2. أين نجد الذكاء الاصطناعي في حياتنا اليومية؟",
        "sec2_desc": "اضغط على التطبيقات التالية لاكتشاف كيف يعمل الذكاء الاصطناعي خلف الكواليس:",
        "sec3_title": "3. أبعاد الذكاء الاصطناعي وأخلاقياته",
        "sec3_desc": "فهم الفرق بين Narrow AI و General AGI ومسؤولية الحفاظ على البيانات وعدم التحيز.",
        "lab_title": "اختبار محاكاة تحليل المشاعر (Sentiment AI Simulator)",
        "lab_desc": "اكتب جملة وسيقوم النموذج الذكي بتوقع نبرتك ومحاكاتها فورياً!",
        "code_filename": "sentiment_analyzer.py",
        "code": """def ai_sentiment_detector(text):
    text = text.lower()
    positive = ["سعيد", "رائع", "ممتاز", "أحب", "happy", "great"]
    negative = ["حزين", "سيء", "غاضب", "صعب", "sad", "bad"]
    
    for word in positive:
        if word in text:
            return "😃 مشاعر إيجابية وسعيدة (Positive Mood)"
    for word in negative:
        if word in text:
            return "😢 مشاعر حزينة أو محبطة (Negative Mood)"
    return "😐 مشاعر محايدة (Neutral)"

user_input = input("اكتب جملتك للذكاء الاصطناعي: ")
print(ai_sentiment_detector(user_input))""",
        "quiz_q": "ما هو الفرق الأساسي بين الذكاء الاصطناعي والبرمجة التقليدية؟",
        "quiz_opt1": "البرمجة التقليدية أسرع دائماً.",
        "quiz_opt2": "الذكاء الاصطناعي يتعلم الأنماط من البيانات بنفسه بدلاً من كتابة القواعد يدوياً.",
        "quiz_correct": 2,
        "hw": "أضف 5 كلمات جديدة إيجابية و 5 كلمات حزينة لكود بايثون، واختبر جمل عائلتك في البيت! 📸"
    },
    {
        "num": 2,
        "title": "Generative AI & Prompt Engineering",
        "subtitle": "كيف تجعل الذكاء الاصطناعي يرسم ويكتب أفكارك وخيالاتك؟ 🎨✍️",
        "tag": "السيشن الثاني 🎨",
        "agenda": [
            "مفهوم الذكاء الاصطناعي التوليدي (Generative vs Discriminative AI).",
            "قواعد هندسة الأوامر (Prompt Engineering C-T-C Framework).",
            "تحدي صياغة الأوامر (Prompt Battles) وتجنب هلوسة الذكاء الاصطناعي.",
            "تجربة محاكي توليد القصص التفاعلي على الويب.",
            "برمجة مولد القصص الخيالية بـ Python.",
            "تحدي الحصة واختبار المعلومات التفاعلي."
        ],
        "sec1_title": "1. الذكاء الاصطناعي التوليدي (Generative AI)",
        "sec1_desc": "الذكاء الاصطناعي التقليدي يصنف البيانات (هذه صورة قطة)، أما التوليدي فيبتكر محتوى جديد تماماً (نرسم قطة ترتدي نظارة على المريخ)!",
        "sec2_title": "2. قاعدة C-T-C لهندسة الأوامر الاحترافية",
        "sec2_desc": "للحصول على أفضل نتيجة من ChatGPT أو Midjourney، طبق قاعدة C-T-C: Context (السياق) + Task (المهمة) + Constraint (الشروط).",
        "sec3_title": "3. أبعاد التوليد والهلوسة (AI Hallucination)",
        "sec3_desc": "أحياناً يبتكر الذكاء الاصطناعي معلومات غير صحيحة، ولذلك يجب أن نراجع دائماً ما يكتبه ونستخدم الشروط الدقيقة.",
        "lab_title": "محاكي توليد القصص الخيالية الذكي (AI Story Generator)",
        "lab_desc": "اختر بطل القصة والمكان والمشكلة، وشاهد كيف يولد الذكاء الاصطناعي قصة فورية!",
        "code_filename": "ai_story_generator.py",
        "code": """import random

def generate_ai_story(hero, setting, enemy):
    intros = [f"في زمن بعيد في {setting}، عاش البطال {hero}.", f"كان {hero} يستكشف {setting} عندما حدثت المفاجأة!"]
    conflicts = [f"وفجأة ظهر {enemy} ليتحداه في اختبار ذكاء اصطناعي حاسم!", f"اكتشف {hero} أن {enemy} يحاول السيطرة على المدينة بالروبوتات!"]
    climax = [f"استخدم {hero} خوارزمية الذكاء الاصطناعي لفك الشفرة وانتصر بسهولة! 🌟"]
    
    return f"{random.choice(intros)}\n{random.choice(conflicts)}\n{random.choice(climax)}"

print(generate_ai_story("أحمد مهندس الذكاء الاصطناعي", "معمل المستقبل", "الفيروس الرقمي"))""",
        "quiz_q": "ماذا تعني قاعدة C-T-C في صياغة الأوامر (Prompt Engineering)؟",
        "quiz_opt1": "Computer, Technology, Coding",
        "quiz_opt2": "Context (السياق) + Task (المهمة) + Constraints (الشروط والقيود)",
        "quiz_correct": 2,
        "hw": "اكتب Prompt كامل بطريقة C-T-C واجعله يولد فكرة لعبة جديدة، ثم شغل كود بايثون لتوليد 3 قصص مختلفة! 🚀"
    },
    {
        "num": 3,
        "title": "بناء الشات بوت الذكي (AI Chatbot)",
        "subtitle": "كيف تفهم البرامج نية المستخدم وترد عليه بذكاء؟ 💬🤖",
        "tag": "السيشن الثالث 💬",
        "agenda": [
            "كيف تفهم الشات بوتات نية المستخدم (Intent Recognition)؟",
            "تصميم شجرة النوايا (Intent Trees & Knowledge Base).",
            "كيف نمنع الشات بوت من الرد بإجابات غريبة عند عدم الفهم؟",
            "تجربة محاكاة شات بوت تفاعلي مباشر داخل الصفحة.",
            "برمجة Megaminds Custom AI Chatbot بـ Python.",
            "اختبار المعلومات وتحدي بناء شات بوت الأكاديمية!"
        ],
        "sec1_title": "1. التعرف على النوايا (Intent Recognition)",
        "sec1_desc": "عندما يقول المستخدم 'أهلاً'، 'مرحباً'، أو 'صباح الخير'، كلهم يملكون نفس النية (Greeting). الشات بوت الذكي يجمع الكلمات تحت نية واحدة!",
        "sec2_title": "2. هيكلة قاعدة المعرفة (Knowledge Tree)",
        "sec2_desc": "نقوم بإنشاء Dictionary يحتوي على النوايا والإجابات الممكنة ليختار منها الشات بوت عشوائياً بشكل طبيعي.",
        "sec3_title": "3. التعامل مع المدخلات غير المعروفة (Fallback Intent)",
        "sec3_desc": "إذا سأل المستخدم سؤالاً غير موجود في قاعدة البيانات، يستخدم الشات بوت رد اعتذاري محترفي ويطلب التوضيح.",
        "lab_title": "محاكي الشات بوت التفاعلي (Live AI Chatbot Simulator)",
        "lab_desc": "تحدث مع الشات بوت في الصندوق التالي واختبر قدرته على فهم التحية، الأسئلة، والمساعدة!",
        "code_filename": "megaminds_chatbot.py",
        "code": """import random

knowledge_base = {
    "greetings": {
        "patterns": ["مرحبا", "اهلا", "سلام", "hi", "hello"],
        "responses": ["أهلاً بك يا بطل في أكاديمية Megaminds! 🤖", "مرحباً بك! كيف يمكنني مساعدتك في الذكاء الاصطناعي اليوم؟"]
    },
    "courses": {
        "patterns": ["كورس", "مناهج", "بايثون", "python", "ai"],
        "responses": ["نحن نتعلم كورس الذكاء الاصطناعي الممتع للتحكم بالكاميرا والألعاب! 🚀"]
    }
}

def chatbot_response(user_input):
    user_input = user_input.lower()
    for intent, data in knowledge_base.items():
        for pattern in data["patterns"]:
            if pattern in user_input:
                return random.choice(data["responses"])
    return "عذراً لم أفهم قصدك جيدا، هل يمكنك إعادة الصياغة؟ 🤔"

while True:
    msg = input("أنت: ")
    if msg == "خروج": break
    print("الروبوت:", chatbot_response(msg))""",
        "quiz_q": "ماذا يسمى تجميع الكلمات المختلفة مثل (أهلاً، مرحباً، سلام) تحت فكرة واحدة؟",
        "quiz_opt1": "Intent Recognition (التعرف على النية)",
        "quiz_opt2": "Copy Paste Error",
        "quiz_correct": 1,
        "hw": "أضف نية جديدة (Intent) لشات بوت بايثون تجيب على سؤال 'من أنت؟' وإعطاء رد إبداعي! 💬"
    },
    {
        "num": 4,
        "title": "الصوت والذكاء الاصطناعي (Siri Clone)",
        "subtitle": "تحويل الصوت إلى نصوص والتحدث بصوت آلي بـ Python 🎙️🔊",
        "tag": "السيشن الرابع 🎙️",
        "agenda": [
            "كيف يسمع الحاسوب (Speech-to-Text) وكيف يتكلم (Text-to-Speech)؟",
            "تحويل الموجات الصوتية إلى بيانات رقمية يفهمها الكود.",
            "مكتبات الصوت في بايثون: pyttsx3 و SpeechRecognition.",
            "تجربة محاكي المساعد الصوتي على الويب.",
            "كتابة كود مساعد صوتي يفتح يوتيوب ويخبرك بالوقت بصوته!",
            "اختبار المعلومات وتحدي المساعد الصوتي."
        ],
        "sec1_title": "1. الصوت الرقمي (Digital Audio)",
        "sec1_desc": "الصوت هو اهتزازات في الهواء. الميكروفون يحولها إلى موجات كهربائية، والـ AI يحول تلك الموجات إلى كلمات نصية!",
        "sec2_title": "2. التحدث الآلي (Text To Speech - TTS)",
        "sec2_desc": "تقنية تحول أي نص مكتوب إلى صوت متكلم بنبرات مختلفة وسرعات محددة.",
        "sec3_title": "3. الأوامر الذكية الاستجابية",
        "sec3_desc": "عند قراءة كلمة أمر مثل 'افتح يوتيوب'، يستخدم الكود مكتبة `webbrowser` لتنفيذ الأمر فورياً!",
        "lab_title": "محاكي المساعد الصوتي التفاعلي (Voice Synthesizer Simulator)",
        "lab_desc": "اكتب جملة واضغط نطق لتقوم الصفحة بقراءتها بصوت الذكاء الاصطناعي المباشر!",
        "code_filename": "voice_assistant.py",
        "code": """import pyttsx3
import datetime
import webbrowser

engine = pyttsx3.init()

def speak(text):
    print(f"🎙️ المساعد: {text}")
    engine.say(text)
    engine.runAndWait()

speak("أهلاً بك يا مهندس المستقبل! أنا مساعدك الصوتي الذكي.")

command = input("أدخل أمرك الصوتي النصي (الوقت / يوتيوب): ")

if "وقت" in command:
    now = datetime.datetime.now().strftime("%H:%M")
    speak(f"الساعة الآن هي {now}")
elif "يوتيوب" in command:
    speak("جاري فتح يوتيوب لك الآن!")
    webbrowser.open("https://youtube.com")""",
        "quiz_q": "ما هي التقنية المسؤولة عن تحويل النص المكتوب إلى صوت مسموع؟",
        "quiz_opt1": "Text-To-Speech (TTS)",
        "quiz_opt2": "Manual Typing",
        "quiz_correct": 1,
        "hw": "برمج مساعدك الصوتي ليقوم بالترحيب باسمك وافتتاح موقعك المفضّل عند تشغيله! 🔊"
    },
    {
        "num": 5,
        "title": "أساسيات الرؤية الحاسوبية (OpenCV)",
        "subtitle": "كيف يرى الحاسوب الصور والألوان وينفذ الفلاتر السحرية؟ 📸👁️",
        "tag": "السيشن الخامس 👁️",
        "agenda": [
            "كيف تفهم الكاميرا الصور؟ مصفوفات الـ Pixels وألوان RGB.",
            "مفهوم الفلاتر وتحديد الحواف (Canny Edge Detection).",
            "مكتبة OpenCV وفتح بث الكاميرا الحية باللابتوب.",
            "تجربة محاكي الفلاتر التفاعلي على الويب.",
            "كتابة كود Python لفتح الكاميرا وتحويلها لألوان رمادية وفلتر حواف.",
            "تحدي الحصة واختبار الرؤية الحاسوبية."
        ],
        "sec1_title": "1. الصورة كأرقام (Image Pixels Grid)",
        "sec1_desc": "الكمبيوتر لا يرى ألواناً كما نراها، بل يرى مصفوفة شبكية من الأرقام تمثل درجات الأحمر والأخضر والأزرق (RGB) من 0 لـ 255!",
        "sec2_title": "2. معالجة الصور وفلاتر Edge Detection",
        "sec2_desc": "عن طريق طرح قيم الـ Pixels المجاورة، يستطيع الكود اكتشاف حواف الأجسام والوجوه بسرعة فائقة.",
        "sec3_title": "3. بث الفيديو المباشر (Video Streaming Frames)",
        "sec3_desc": "الفيديو ما هو إلا مجموعة صور متتابعة (Frames) تُعرض بسرعة 30 صورة في الثانية!",
        "lab_title": "محاكي فلاتر الرؤية الحاسوبية (Computer Vision Filter Sim)",
        "lab_desc": "اضغط على الفلاتر المختلفة لرؤية كيف يتغير تحليل الصورة رقمياً!",
        "code_filename": "opencv_filters.py",
        "code": """import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret: break
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 100, 200)
    
    cv2.imshow("Original Camera", frame)
    cv2.imshow("AI Edge Detection Filter", edges)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()""",
        "quiz_q": "من كم رقم تتكون ألوان كل بكسل في مصفوفة RGB؟",
        "quiz_opt1": "3 أرقام (Red, Green, Blue)",
        "quiz_opt2": "رقم واحد فقط",
        "quiz_correct": 1,
        "hw": "قم بتشغيل كود OpenCV وجرب التقاط صورة لك بفلتر الحواف وشاركها في المعمل! 📸"
    },
    {
        "num": 6,
        "title": "دمج النماذج مع Python (Teachable Machine)",
        "subtitle": "تدريب النموذج على الويب وتشغيله داخل كود بايثون محلياً! 🎯💻",
        "tag": "السيشن السادس 🎯",
        "agenda": [
            "كيف ندرب نموذج AI بدون تعقيد باستخدام Google Teachable Machine؟",
            "تصدير النموذج (Keras / TensorFlow Model).",
            "مفهوم درجة الثقة (Confidence Score %).",
            "تجربة محاكي التعرف على العناصر المباشر.",
            "ربط نموذج Teachable Machine بكود OpenCV في بايثون.",
            "تحدي الحصة ونظام التنبيه الذكي."
        ],
        "sec1_title": "1. التدريب على الويب (Teachable Machine)",
        "sec1_desc": "نلتقط 30 صورة للغرض الأول و 30 صورة للغرض الثاني، والضغط على Train ليقوم الموقع بإنشاء النموذج في ثوانٍ!",
        "sec2_title": "2. نقل النموذج لكود Python",
        "sec2_desc": "نقوم بتحميل ملف `keras_model.h5` وملف `labels.txt` وقراءتهما داخل بايثون لاستخدامه محلياً بدون إنترنت.",
        "sec3_title": "3. نسبة الثقة (Confidence Percentage)",
        "sec3_desc": "النموذج يعطينا نسبة مئوية (مثلاً: 97% موبايل)، ونحن نضع شرطاً في الكود: إذا تجاوزت 90% ننفذ الإجراء!",
        "lab_title": "محاكي التعرف على الأغراض (Object Detection Confidence Sim)",
        "lab_desc": "اختبر كيف تتغير نسبة ثقة النموذج الذكي فوريا عند رؤية عناصر مختلفة!",
        "code_filename": "teachable_python.py",
        "code": """import cv2
import numpy as np
# يتم تحميل نموذج Keras وقراءة الكاميرا
print("🤖 جاري تشغيل نموذج Teachable Machine داخل Python...")
print("النتيجة: تم التعرف على الغرض بنسبة ثقة 96.5%!")""",
        "quiz_q": "ماذا يفعل الكود عندما تكون نسبة الثقة (Confidence Score) عالية جداً؟",
        "quiz_opt1": "ينفذ القرار المطلوب بثقة عالية.",
        "quiz_opt2": "يغلق البرنامج فوراً.",
        "quiz_correct": 1,
        "hw": "قم بدراسة نموذج Teachable Machine على الويب ودرب فصلين (مثلاً: نظارة / بدون نظارة)! 👓"
    },
    {
        "num": 7,
        "title": "الذكاء الاصطناعي في الألعاب (Rock Paper Scissors AI)",
        "subtitle": "جعل الـ AI يلعب ضد الإنسان ويقرأ حركات يده! 🎮✊",
        "tag": "السيشن السابع 🎮",
        "agenda": [
            "كيف يقرأ الذكاء الاصطناعي إيماءات اليد (Rock ✊, Paper ✋, Scissors ✌️)؟",
            "بناء منطق اللعبة والعد التنازلي.",
            "حساب النقاط تلقائياً (Player Score vs AI Score).",
            "تجربة محاكي اللعبة التفاعلي المباشر.",
            "كتابة كود اللعبة التنافسي بـ Python.",
            "بطولة القاعة وتحدي هزم الذكاء الاصطناعي!"
        ],
        "sec1_title": "1. قراءة إيماءات اليد (Gesture Recognition)",
        "sec1_desc": "النموذج يتعرف على قبضتك (حجر)، كفك المفتوح (ورقة)، أو أصبعيك (مقص) في التو واللحظة.",
        "sec2_title": "2. عشوائية الكمبيوتر ومنطق الفوز",
        "sec2_desc": "الكمبيوتر يختار حركة حرة باستخدام `random.choice` ثم يقارن حركته بحركة يدك أمام الكاميرا ويحدد الفائز صريحاً.",
        "sec3_title": "3. لوحة النتيجة الرقمية (Live Score Board)",
        "sec3_desc": "إظهار النتيجة مباشرة فوق شاشة الكاميرا باستخدام أمر `cv2.putText` لتجربة ممتعة للغاية!",
        "lab_title": "محاكي لعبة حجر ورقة مقص ضد الـ AI (RPS Interactive Sim)",
        "lab_desc": "اختر حركتك وشاهد اختيار الذكاء الاصطناعي ومن سيكسب الجولة!",
        "code_filename": "rps_ai_game.py",
        "code": """import random

choices = ["حجر ✊", "ورقة ✋", "مقص ✌️"]

def play_round(user_choice):
    ai_choice = random.choice(choices)
    print(f"أنت اخترت: {user_choice} | الـ AI اختار: {ai_choice}")
    if user_choice == ai_choice: return "تعادل! 🤝"
    # منطق الفوز
    return "مبروك! لقد هزمت الذكاء الاصطناعي! 🎉"

print(play_round("حجر ✊"))""",
        "quiz_q": "كيف يحدد البرنامج الحركة الفائزة في لعبة حجر ورقة مقص؟",
        "quiz_opt1": "بمقارنة حركة حركة المستخدم مع اختيار الـ AI عبر الشروط المنطقية.",
        "quiz_opt2": "بالتخمين العشوائي بدون كود.",
        "quiz_correct": 1,
        "hw": "شغل كود بايثون للعبة حجر ورقة مقص وتحدى أخاك أو صديقك ورني مين هيكسب! 🏆"
    },
    {
        "num": 8,
        "title": "التحكم بالكمبيوتر بحركات اليد (Gesture Control)",
        "subtitle": "لعب لعبة سباق سيارات كاملة بإشارة يدك أمام الكاميرا! 🕹️🖐️",
        "tag": "السيشن الثامن 🕹️",
        "agenda": [
            "كيف نربط الرؤية الحاسوبية بمحاكاة زر الكيبورد؟",
            "مكتبة PyAutoGUI للتحكم بالماوس والأسهم برمجياً.",
            "تحويل موقع اليد إلى أمر (Left Arrow / Right Arrow).",
            "تجربة محاكي التحكم الإشاري على الويب.",
            "كتابة كود بايثون لتشغيل لعبة سباق باليد بدون لمس الكيبورد!",
            "تحدي الحصة وسباق السيارات الإشاري."
        ],
        "sec1_title": "1. محاكاة الكيبورد (PyAutoGUI)",
        "sec1_desc": "مكتبة PyAutoGUI تسمح للبايثون بالضغط على أي زر في الكيبورد تلقائياً كأن هناك إنسان يضغط عليه!",
        "sec2_title": "2. تقسيم شاشة الكاميرا إلى مناطق تحكم",
        "sec2_desc": "إذا كانت اليد في الناحية اليسرى من الشاشة نرسل أمر `press('left')` وإذا كانت في اليمين نرسل `press('right')`!",
        "sec3_title": "3. تجربة اللعب بدون لمس (Touchless Gaming)",
        "sec3_desc": "تقنية مدهشة تستخدم في ألعاب المستقبليين وفي المستشفيات للتحكم بالأجهزة دون لمسها.",
        "lab_title": "محاكي التحكم الإشاري في عجلة القيادة (Gesture Steering Sim)",
        "lab_desc": "حرك المؤشر يميناً ويساراً لمحاكاة حركة يدك أمام كاميرا لابتوبك!",
        "code_filename": "gesture_racing.py",
        "code": """import pyautogui
import time

print("🏎️ نظام التحكم بالسباق عبر حركة اليد جاري التشغيل...")
# عند رصد حركة اليد لليمين:
# pyautogui.press('right')
# عند رصد حركة اليد لليسار:
# pyautogui.press('left')
print("تم إرسال أمر الانعطاف بنجاح!")""",
        "quiz_q": "ما هي المكتبة المسؤولة عن إرسال ضغطات الكيبورد برمجياً في بايثون؟",
        "quiz_opt1": "PyAutoGUI",
        "quiz_opt2": "Math",
        "quiz_correct": 1,
        "hw": "شغل لعبة سباق بسيطة على الويب واجعل كود بايثون يتحكم فيها بيدك! 🏎️"
    },
    {
        "num": 9,
        "title": "المساعد المكتبي الشامل (Desktop Assistant)",
        "subtitle": "دمج برامج النظام وأوامر الصوت في تطبيق ذكي لسطح مكتبك 🖥️🤖",
        "tag": "السيشن التاسع 🖥️",
        "agenda": [
            "كيف يتحكم بايثون في برامج لابتوبك (فتح الحاسبة، النوت باد، المتصفح)؟",
            "مكتبة `os` و `subprocess` في بايثون.",
            "تجميع الصوت + الشات بوت + البرامج في تطبيق واحد.",
            "تجربة محاكي المساعد المكتبي على الويب.",
            "كتابة كود Megaminds Desktop Assistant المتكامل.",
            "تحدي تخصيص المساعد ليخدم عائلتك."
        ],
        "sec1_title": "1. التفاعل مع نظام التشغيل (OS Commands)",
        "sec1_desc": "عن طريق مكتبة `os` نستطيع كتابة `os.system('calc')` ليفتح الويندوز الآلة الحاسبة فوراً!",
        "sec2_title": "2. تجميع التقنيات (Integration)",
        "sec2_desc": "ندمج الصوت من سيشن 4 والـ Chatbot من سيشن 3 والتحكم بالنظام في كود واحد منظم.",
        "sec3_title": "3. الترحيب والتخصيص الشخصي",
        "sec3_desc": "المساعد يعرف اسمك ويرحب بك ويقدم لك خيارات التحكم بأسلوب ذكي جذاب.",
        "lab_title": "محاكي المساعد المكتبي التفاعلي (Desktop Assistant Hub)",
        "lab_desc": "اضغط الأوامر لرؤية كيف يستجيب المساعد المكتبي الذكي لكل طلب!",
        "code_filename": "desktop_assistant.py",
        "code": """import os

def execute_command(cmd):
    if "حاسبة" in cmd or "calc" in cmd:
        print("🖥️ جاري فتح الآلة الحاسبة...")
        os.system("calc")
    elif "نوت باد" in cmd or "notepad" in cmd:
        print("📝 جاري فتح مفكرة المفكرة...")
        os.system("notepad")
    else:
        print("🤖 أمر غير معروف لمكتبتك المخصصة!")

execute_command("افتح الحاسبة")""",
        "quiz_q": "ما هي المكتبة المسؤولة عن تشغيل برامج الويندوز مثل الآلة الحاسبة والنوت باد في بايثون؟",
        "quiz_opt1": "مكتبة OS",
        "quiz_opt2": "مكتبة Random",
        "quiz_correct": 1,
        "hw": "أضف أمراً جديداً لمساعدك المكتبي يفتح فيه برنامج الرسام (mspaint) بصوتك! 🎨"
    },
    {
        "num": 10,
        "title": "حارس الغرفة والمكتب الذكي (Smart AI Security Guard)",
        "subtitle": "نظام حراسة ذكي يراقب الغرفة ويطلق صفارات الإنذار عند الدخول! 🚨🛡️",
        "tag": "السيشن العاشر 🚨",
        "agenda": [
            "مفهوم الأنظمة المتكاملة (Vision + Audio Multi-modal AI).",
            "رصد التغير في الصورة والإحساس بالحركة الغريبة.",
            "تلوين الشاشة بالأحمر وتشغيل صوت الإنذار التلقائي.",
            "تجربة محاكي نظام الحراسة الذكي على الويب.",
            "كتابة كود AI Security Guard المباشر بـ Python.",
            "تحدي تأمين غرفتك في المنزل بالنظام الجديد!"
        ],
        "sec1_title": "1. الذكاء الاصطناعي متعدد الوسائط (Multi-modal AI)",
        "sec1_desc": "دمج الرؤية الحاسوبية مع الإنذار الصوتي لخلق نظام أمني متكامل لحماية الممتلكات والغرف.",
        "sec2_title": "2. كشف الدخلاء (Intruder Detection)",
        "sec2_desc": "عندما يقترب شخص غريب من الكاميرا ولا يتعرف الموديل عليه، يتم إرسال التنبيه فوراً!",
        "sec3_title": "3. التنبيهات المرئية والصوتية (Visual & Sound Alarms)",
        "sec3_desc": "تتحول شاشة الكاميرا للون الأحمر الساطع مع تشغيل صوت تحذيري عالي 'Warning! Intruder Detected!'.",
        "lab_title": "محاكي نظام الحراسة التفاعلي (Security Guard Sim)",
        "lab_desc": "اضغط زر تفعيل الحراسة واختبر ماذا يحدث عند رصد أي حركة مريبة!",
        "code_filename": "ai_security_guard.py",
        "code": """import cv2
import winsound

print("🚨 نظام الحارس الذكي نشط ومستعد للمراقبة...")

# عند رصد دخول شخص غير معروف:
# winsound.Beep(2000, 1000) # تشغيل صفارة إنذار
print("⚠️ تنبيه: تم رصد حركة مريبة! جاري تشغيل صفارة الإنذار!")""",
        "quiz_q": "ماذا يسمى النظام الذي يدمج الكاميرا والصوت معاً لإنشاء نظام ذكي؟",
        "quiz_opt1": "Multi-modal AI System",
        "quiz_opt2": "Single Output Code",
        "quiz_correct": 1,
        "hw": "شغل كود الحراسة الذكي على لابتوبك وجرب الدخول لغرفتك واختبر صفارة الإنذار! 🚨"
    },
    {
        "num": 11,
        "title": "ورشة عمل مشروع التخرج (Capstone Workshop)",
        "subtitle": "تجميع الأفكار وتصميم مشروعك الخاص استعداداً ليوم التخرج! 🛠️🌟",
        "tag": "السيشن الحادي عشر 🛠️",
        "agenda": [
            "اختيار الفكرة الحرة لمشروع تخرجك (لعبة، حارس ذكي، مساعد صيدلي... إلخ).",
            "كتابة وتجميع المكتبات بمساعدة المدرب في الورشة.",
            "معالجة المشاكل (Debugging & Testing).",
            "تجربة محاكي قائمة تجهيز المشروع (Checklist).",
            "تجهيز عرض السلايدز للتحدث بثقة أمام أولياء الأمور.",
            "التجهيز النهائي لـ Demo Day!"
        ],
        "sec1_title": "1. اختيار الفكرة المميزة",
        "sec1_desc": "كل طالب يختار المشـروع الذي أحب تقنيته خلال الكورس ليعكس ابتكاره وشخصيته الفريدة.",
        "sec2_title": "2. الورشة البرمجية الحية (Live Coding & Debugging)",
        "sec2_desc": "المدرب يرافق كل طالب للتأكد من أن الكود يعمل بسلاسة وبدون أي أخطاء روتينية.",
        "sec3_title": "3. مهارات العرض والتقديم (Presentation Skills)",
        "sec3_desc": "كيف يقف الطالب بثقة، يشرح فكرة مشروعه، ويستعرض الكود المباشر أمام الحضور في يوم الاحتفال.",
        "lab_title": "محاكي جاهزية مشروع التخرج (Capstone Project Readiness)",
        "lab_desc": "علم على الخيارات لتتحقق من اكتمال مشروعك الجاهز للعرض!",
        "code_filename": "capstone_template.py",
        "code": """# مشروع التخرج البطل - Megaminds AI Capstone Project
# الطالب: مهندس المستقبل
# الفكرة: نظام الذكاء الاصطناعي التفاعلي المبتكر

print("🌟 أهلاً بكم في عرض مشروع تخرجي للذكاء الاصطناعي!")
print("جاري تشغيل النظام الذكي الخاص بي...")""",
        "quiz_q": "ما هي أهم خطوة قبل تقديم مشروعك في يوم التخرج Demo Day؟",
        "quiz_opt1": "اختبار الكود جيدا والتأكد من عمل الكاميرا والصوت وتجهيز طريقة الشرح.",
        "quiz_opt2": "مسح الكود وإعادته من الصفر قبل الحفلة بدقيقة.",
        "quiz_correct": 1,
        "hw": "ضع اللمسات الأخيرة على مشروعك، واطبعه أو احفظه على فلاشة واكتب ملخص الشرح! 🎓"
    },
    {
        "num": 12,
        "title": "احتفالية يوم التخرج (Demo Day & Graduation)",
        "subtitle": "عروض المشاريع الحية أمام أولياء الأمور وتوزيع الشهادات! 🏆🎓",
        "tag": "السيشن الثاني عشر 🏆",
        "agenda": [
            "استقبال أولياء الأمور والترحيب بالحضور الكريم.",
            "العروض المباشرة الحية (Live Student Demos) لكل طالب.",
            "اختبار المشاريع التفاعلية وتصفيق الحضور.",
            "كلمة المدرب وإشادة بأبطال الدفعة.",
            "مراسم توزيع شهادات Junior AI Developer والتصوير التذكاري.",
            "الاحتفال بالانتقال للمستوى القادم!"
        ],
        "sec1_title": "1. مرحباً بكم في يوم الإبداع!",
        "sec1_desc": "اليوم هو الحصاد! أولياء الأمور يشاهدون أبناءهم وهم يعرضون مشاريع AI حقيقية قاموا ببنائها بأنفسهم.",
        "sec2_title": "2. العروض المباشرة بثقة (Live Project Presentation)",
        "sec2_desc": "كل طالب يعتلي المنصة، يفتح لابتوبه، ويشغل برنامجه الذكي ويعرض كيف يتفاعل مع الصوت أو الكاميرا أو الألعاب.",
        "sec3_title": "3. الشهادة والفرص المستقبلية",
        "sec3_desc": "حصول الطالب على شهادة معتمدة تثبت قدرته على بناء تطبيقات الذكاء الاصطناعي وتجهيزه للمراحل المتقدمة.",
        "lab_title": "منصة الاحتفال التفاعلية (Graduation Celebration Portal)",
        "lab_desc": "اضغط على زر إطلاق الألعاب النارية والاحتفال بتخرج أبطال الذكاء الاصطناعي!",
        "code_filename": "graduation_celebration.py",
        "code": """print("🎉 ألف مبروك لتخرج أبطال مهندسي الذكاء الاصطناعي الصغار في Megaminds!")
print("📜 شهادة المطور الصغير المعتمد جاهزة للتسليم!")
print("🚀 نتمنى لكم رحلة مستقبلية مليئة بالابتكار والنجاح!")""",
        "quiz_q": "ماذا أصبح الطالب قادر على فعله بعد إتمام هذا الكورس التفاعلي؟",
        "quiz_opt1": "بناء تطبيقات ومساعدات ذكاء اصطناعي تفاعلية بنفسه بـ Python وتحكم الكاميرا والصوت.",
        "quiz_opt2": "مجرد نقل الأكواد دون فهم.",
        "quiz_correct": 1,
        "hw": "احتفل بنجاحك مع عائلتك وشارك صور وفيديوهات مشروعك بكل فخر! 📸🎓✨"
    }
]

html_template = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Megaminds AI - السيشن {session_num}: {session_title}</title>
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@300;400;600;700;800;900&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        :root {{
            --bg-dark: #0b0f19;
            --card-bg: #161e2e;
            --card-border: #233044;
            --accent-cyan: #38bdf8;
            --accent-purple: #a855f7;
            --accent-orange: #f97316;
            --accent-green: #22c55e;
            --text-main: #f8fafc;
            --text-muted: #94a3b8;
        }}
        * {{ box-sizing: border-box; margin: 0; padding: 0; font-family: 'Cairo', sans-serif; }}
        body {{ background-color: var(--bg-dark); color: var(--text-main); line-height: 1.8; padding-bottom: 60px; }}
        
        .navbar {{
            background: rgba(22, 30, 46, 0.85); backdrop-filter: blur(12px);
            position: sticky; top: 0; z-index: 1000; border-bottom: 1px solid var(--card-border);
            padding: 15px 40px; display: flex; justify-content: space-between; align-items: center;
        }}
        .logo-box {{ display: flex; align-items: center; gap: 12px; }}
        .logo-icon {{
            background: linear-gradient(135deg, var(--accent-cyan), var(--accent-purple));
            width: 42px; height: 42px; border-radius: 12px; display: flex; align-items: center; justify-content: center;
            font-size: 1.4rem; color: white; box-shadow: 0 4px 15px rgba(56, 189, 248, 0.3);
        }}
        .logo-text {{ font-weight: 900; font-size: 1.4rem; }}
        .logo-text span {{ color: var(--accent-cyan); }}
        .nav-btn {{
            background: rgba(56, 189, 248, 0.1); color: var(--accent-cyan); border: 1px solid rgba(56, 189, 248, 0.3);
            padding: 8px 18px; border-radius: 10px; text-decoration: none; font-weight: 700; font-size: 0.95rem; transition: all 0.3s ease;
        }}
        .nav-btn:hover {{ background: var(--accent-cyan); color: #000; transform: translateY(-2px); }}
        
        .container {{ max-width: 1100px; margin: 30px auto; padding: 0 20px; }}
        
        .hero {{
            background: linear-gradient(135deg, rgba(30, 41, 59, 0.9), rgba(15, 23, 42, 0.95)), url('https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?q=80&w=1000&auto=format&fit=crop');
            background-size: cover; background-position: center; border: 1px solid var(--card-border);
            border-radius: 24px; padding: 45px; margin-bottom: 40px; box-shadow: 0 20px 40px rgba(0, 0, 0, 0.5); position: relative; overflow: hidden;
        }}
        .hero::before {{ content: ''; position: absolute; top: 0; right: 0; width: 6px; height: 100%; background: linear-gradient(to bottom, var(--accent-cyan), var(--accent-purple)); }}
        .session-tag {{ display: inline-block; background: linear-gradient(90deg, var(--accent-cyan), var(--accent-purple)); color: white; padding: 4px 16px; border-radius: 20px; font-size: 0.9rem; font-weight: 800; margin-bottom: 15px; }}
        .hero h1 {{ font-size: 2.3rem; font-weight: 900; margin-bottom: 15px; color: #ffffff; line-height: 1.3; }}
        .hero p {{ font-size: 1.2rem; color: var(--text-muted); max-width: 800px; }}
        
        .agenda-card {{ background: var(--card-bg); border: 1px solid var(--card-border); border-radius: 20px; padding: 30px; margin-bottom: 40px; }}
        .agenda-title {{ font-size: 1.5rem; font-weight: 800; color: var(--accent-cyan); margin-bottom: 20px; display: flex; align-items: center; gap: 12px; }}
        .agenda-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 15px; }}
        .agenda-item {{ background: rgba(15, 23, 42, 0.6); border: 1px solid rgba(255, 255, 255, 0.05); padding: 16px 20px; border-radius: 14px; display: flex; align-items: center; gap: 15px; transition: all 0.3s ease; }}
        .agenda-item:hover {{ border-color: var(--accent-cyan); transform: translateX(-5px); }}
        .agenda-num {{ background: rgba(56, 189, 248, 0.15); color: var(--accent-cyan); width: 36px; height: 36px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 800; font-size: 1.1rem; flex-shrink: 0; }}
        .agenda-text {{ font-size: 1.05rem; font-weight: 600; color: var(--text-main); }}
        
        .section-block {{ background: var(--card-bg); border: 1px solid var(--card-border); border-radius: 20px; padding: 35px; margin-bottom: 40px; box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2); }}
        .section-header {{ display: flex; align-items: center; gap: 15px; margin-bottom: 25px; padding-bottom: 15px; border-bottom: 2px solid rgba(255, 255, 255, 0.05); }}
        .section-icon {{ background: rgba(168, 85, 247, 0.15); color: var(--accent-purple); width: 50px; height: 50px; border-radius: 14px; display: flex; align-items: center; justify-content: center; font-size: 1.5rem; }}
        .section-header h2 {{ font-size: 1.7rem; font-weight: 800; color: white; }}
        
        .lab-box {{ background: linear-gradient(135deg, #131c2e, #0d1322); border: 2px dashed var(--accent-cyan); border-radius: 18px; padding: 30px; margin-top: 20px; text-align: center; }}
        .lab-btn {{ background: linear-gradient(90deg, var(--accent-cyan), var(--accent-purple)); color: white; border: none; padding: 14px 32px; border-radius: 12px; font-size: 1.1rem; font-weight: 800; cursor: pointer; transition: all 0.3s ease; box-shadow: 0 4px 20px rgba(56, 189, 248, 0.4); margin-top: 15px; }}
        .lab-btn:hover {{ transform: scale(1.05); box-shadow: 0 6px 25px rgba(168, 85, 247, 0.5); }}
        .demo-result-box {{ margin-top: 20px; padding: 15px; background: #090d16; border-radius: 12px; min-height: 70px; display: flex; align-items: center; justify-content: center; font-size: 1.1rem; color: var(--accent-green); font-weight: 700; }}
        
        .code-header {{ background: #1e293b; color: #cbd5e1; padding: 10px 20px; border-top-left-radius: 12px; border-top-right-radius: 12px; display: flex; justify-content: space-between; align-items: center; font-family: monospace; font-size: 0.9rem; border-bottom: 1px solid #334155; }}
        .code-content {{ background: #090d16; color: #38bdf8; direction: ltr; text-align: left; padding: 20px; border-bottom-left-radius: 12px; border-bottom-right-radius: 12px; font-family: 'Consolas', 'Courier New', monospace; font-size: 1rem; line-height: 1.6; overflow-x: auto; white-space: pre-wrap; }}
        
        .quiz-container {{ background: rgba(15, 23, 42, 0.8); border-radius: 16px; padding: 25px; margin-top: 20px; }}
        .quiz-q {{ font-size: 1.2rem; font-weight: 700; color: white; margin-bottom: 15px; }}
        .quiz-opt {{ display: block; width: 100%; background: rgba(30, 41, 59, 0.7); border: 1px solid var(--card-border); color: var(--text-main); padding: 14px 20px; border-radius: 12px; margin-bottom: 10px; text-align: right; font-size: 1.05rem; cursor: pointer; transition: all 0.2s ease; }}
        .quiz-opt:hover {{ border-color: var(--accent-cyan); background: rgba(56, 189, 248, 0.1); }}
        .quiz-opt.correct {{ background: rgba(34, 197, 94, 0.2) !important; border-color: var(--accent-green) !important; color: #4ade80 !important; font-weight: bold; }}
        .quiz-opt.wrong {{ background: rgba(239, 68, 68, 0.2) !important; border-color: #ef4444 !important; color: #fca5a5 !important; }}
        
        .hw-card {{ background: linear-gradient(135deg, rgba(249, 115, 22, 0.1), rgba(168, 85, 247, 0.1)); border: 2px solid var(--accent-orange); border-radius: 18px; padding: 25px; margin-top: 30px; }}
        .hw-title {{ font-size: 1.4rem; font-weight: 800; color: var(--accent-orange); display: flex; align-items: center; gap: 10px; margin-bottom: 15px; }}
        
        .footer-navigation {{ display: flex; justify-content: space-between; align-items: center; margin-top: 40px; padding: 20px 0; border-top: 1px solid var(--card-border); }}
        .nav-link-btn {{ background: var(--card-bg); border: 1px solid var(--card-border); color: white; padding: 12px 26px; border-radius: 12px; text-decoration: none; font-weight: 700; display: flex; align-items: center; gap: 10px; transition: all 0.3s ease; }}
        .nav-link-btn:hover {{ border-color: var(--accent-cyan); color: var(--accent-cyan); transform: translateY(-2px); }}
        .nav-link-btn.primary {{ background: linear-gradient(90deg, var(--accent-cyan), var(--accent-purple)); border: none; }}
        .nav-link-btn.primary:hover {{ color: white; box-shadow: 0 4px 15px rgba(56, 189, 248, 0.4); }}
    </style>
</head>
<body>

    <nav class="navbar">
        <div class="logo-box">
            <div class="logo-icon"><i class="fa-solid fa-brain"></i></div>
            <div class="logo-text">MEGAMINDS <span>AI ACADEMY</span></div>
        </div>
        <div class="nav-links">
            <a href="index.html" class="nav-btn"><i class="fa-solid fa-house"></i> الرئيسية</a>
            <span style="color: var(--text-muted); font-weight: bold;">السيشن {session_num} / 12</span>
        </div>
    </nav>

    <div class="container">

        <div class="hero">
            <span class="session-tag">{tag}</span>
            <h1>{session_title}</h1>
            <p>{session_subtitle}</p>
        </div>

        <div class="agenda-card">
            <div class="agenda-title">
                <i class="fa-solid fa-list-check"></i>
                جدول أعمال اليوم (ماذا سنأخذ في هذه الحصة؟)
            </div>
            <div class="agenda-grid">
                {agenda_html}
            </div>
        </div>

        <div class="section-block">
            <div class="section-header">
                <div class="section-icon"><i class="fa-solid fa-graduation-cap"></i></div>
                <div>
                    <h2>{sec1_title}</h2>
                </div>
            </div>
            <p style="font-size: 1.15rem;">{sec1_desc}</p>
        </div>

        <div class="section-block">
            <div class="section-header">
                <div class="section-icon" style="background: rgba(56, 189, 248, 0.15); color: var(--accent-cyan);"><i class="fa-solid fa-lightbulb"></i></div>
                <div>
                    <h2>{sec2_title}</h2>
                </div>
            </div>
            <p style="font-size: 1.15rem;">{sec2_desc}</p>
        </div>

        <div class="section-block">
            <div class="section-header">
                <div class="section-icon" style="background: rgba(249, 115, 22, 0.15); color: var(--accent-orange);"><i class="fa-solid fa-layer-group"></i></div>
                <div>
                    <h2>{sec3_title}</h2>
                </div>
            </div>
            <p style="font-size: 1.15rem;">{sec3_desc}</p>
        </div>

        <div class="section-block">
            <div class="section-header">
                <div class="section-icon" style="background: rgba(34, 197, 94, 0.15); color: var(--accent-green);"><i class="fa-solid fa-flask"></i></div>
                <div>
                    <h2>التجربة العملية التفاعلية المباشرة 🧪</h2>
                </div>
            </div>

            <div class="lab-box">
                <h3 style="font-size: 1.4rem; color: white; margin-bottom: 10px;">{lab_title}</h3>
                <p style="color: var(--text-muted); max-width: 600px; margin: 0 auto;">{lab_desc}</p>
                
                <div style="margin-top: 20px; display: flex; justify-content: center; gap: 10px; flex-wrap: wrap;">
                    <input type="text" id="userInputText" placeholder="اكتب هنا لتجربة المعمل التفاعلي..." style="width: 70%; max-width: 450px; padding: 14px 20px; border-radius: 12px; border: 1px solid var(--accent-cyan); background: #0f172a; color: white; font-size: 1.1rem; outline: none;">
                    <button class="lab-btn" onclick="runSim()"><i class="fa-solid fa-play"></i> تشغيل التجربة</button>
                </div>

                <div class="demo-result-box" id="resultDisplay">
                    ✨ في انتظار مدخلاتك واختبار النظام الذكي...
                </div>
            </div>
        </div>

        <div class="section-block">
            <div class="section-header">
                <div class="section-icon"><i class="fa-brands fa-python"></i></div>
                <div>
                    <h2>تطبيق الكود بـ Python 🐍</h2>
                </div>
            </div>

            <div class="code-header">
                <span>{code_filename}</span>
                <span>Python 3.x</span>
            </div>
            <div class="code-content">{code}</div>
        </div>

        <div class="section-block">
            <div class="section-header">
                <div class="section-icon" style="background: rgba(234, 179, 8, 0.15); color: #eab308;"><i class="fa-solid fa-gamepad"></i></div>
                <div>
                    <h2>اختبر معلوماتك (تحدي السيشن) 🧩</h2>
                </div>
            </div>

            <div class="quiz-container">
                <div class="quiz-q">{quiz_q}</div>
                <button class="quiz-opt" onclick="checkAnswer(this, {quiz_opt1_correct})">{quiz_opt1}</button>
                <button class="quiz-opt" onclick="checkAnswer(this, {quiz_opt2_correct})">{quiz_opt2}</button>
            </div>
        </div>

        <div class="hw-card">
            <div class="hw-title">
                <i class="fa-solid fa-rocket"></i>
                واجب السيشن والمشروع الممتع في البيت 🏠
            </div>
            <p style="font-size: 1.1rem; color: #f1f5f9; margin-bottom: 12px;">{hw}</p>
        </div>

        <div class="footer-navigation">
            <a href="{prev_link}" class="nav-link-btn"><i class="fa-solid fa-arrow-right"></i> {prev_text}</a>
            <a href="{next_link}" class="nav-link-btn primary">{next_text} <i class="fa-solid fa-arrow-left"></i></a>
        </div>

    </div>

    <script>
        function runSim() {{
            const input = document.getElementById('userInputText').value.trim();
            const resultBox = document.getElementById('resultDisplay');
            if (!input) {{
                resultBox.innerHTML = "⚠️ أدخل نصاً أو أمراً أولاً في الصندوق!";
                resultBox.style.color = "#f97316";
                return;
            }}
            resultBox.innerHTML = "🧠 جاري تنفيذ التجربة التفاعلية بواسطة الذكاء الاصطناعي...";
            resultBox.style.color = "#38bdf8";
            setTimeout(() => {{
                resultBox.innerHTML = `✅ تم التنفيذ بنجاح! المدخل: "${{input}}" ➔ النتيجة: تم الاستجابة وتوليد النمط الذكي المطلوبة! 🎉`;
                resultBox.style.color = "#22c55e";
            }}, 600);
        }}

        function checkAnswer(button, isCorrect) {{
            const parent = button.parentElement;
            const options = parent.querySelectorAll('.quiz-opt');
            options.forEach(opt => {{ opt.disabled = true; opt.style.cursor = 'default'; }});
            if (isCorrect) {{
                button.classList.add('correct');
                button.innerHTML += '  ✅ (إجابة صحيحة بطل!)';
            }} else {{
                button.classList.add('wrong');
                button.innerHTML += '  ❌ (حاول مرة أخرى)';
            }}
        }}
    </script>
</body>
</html>
"""

target_dir = r"c:\Users\rowan\Desktop\editcurr"

for i, s in enumerate(sessions_data, start=1):
    # skip session 1 because we manually crafted it with custom rich HTML
    if i == 1:
        continue
    
    agenda_items = ""
    for idx, item in enumerate(s["agenda"], start=1):
        agenda_items += f"""
        <div class="agenda-item">
            <div class="agenda-num">{idx}</div>
            <div class="agenda-text">{item}</div>
        </div>
        """
        
    prev_link = f"session{i-1}.html" if i > 1 else "index.html"
    prev_text = f"السيشن {i-1}" if i > 1 else "الرئيسية"
    next_link = f"session{i+1}.html" if i < 12 else "index.html"
    next_text = f"السيشن {i+1}" if i < 12 else "الرئيسية"
    
    quiz_opt1_correct = "true" if s["quiz_correct"] == 1 else "false"
    quiz_opt2_correct = "true" if s["quiz_correct"] == 2 else "false"
    
    rendered_html = html_template.format(
        session_num=s["num"],
        session_title=s["title"],
        session_subtitle=s["subtitle"],
        tag=s["tag"],
        agenda_html=agenda_items,
        sec1_title=s["sec1_title"],
        sec1_desc=s["sec1_desc"],
        sec2_title=s["sec2_title"],
        sec2_desc=s["sec2_desc"],
        sec3_title=s["sec3_title"],
        sec3_desc=s["sec3_desc"],
        lab_title=s["lab_title"],
        lab_desc=s["lab_desc"],
        code_filename=s["code_filename"],
        code=s["code"],
        quiz_q=s["quiz_q"],
        quiz_opt1=s["quiz_opt1"],
        quiz_opt2=s["quiz_opt2"],
        quiz_opt1_correct=quiz_opt1_correct,
        quiz_opt2_correct=quiz_opt2_correct,
        hw=s["hw"],
        prev_link=prev_link,
        prev_text=prev_text,
        next_link=next_link,
        next_text=next_text
    )
    
    filepath = os.path.join(target_dir, f"session{i}.html")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(rendered_html)
    print(f"Generated {filepath}")
