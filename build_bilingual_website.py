import os

sessions_data = [
    {
        "num": 1,
        "title_ar": "مدخل إلى عالم الذكاء الاصطناعي",
        "title_en": "Introduction to Artificial Intelligence",
        "subtitle_ar": "من مستهلك للتطبيقات إلى مبتكر يبني الـ AI بنفسه 🤖✨",
        "subtitle_en": "From app consumer to innovator building AI yourself 🤖✨",
        "tag_ar": "السيشن الأول 🚀",
        "tag_en": "Session 1 🚀",
        "agenda_ar": [
            "ما هو الذكاء الاصطناعي والفرق بينه وبين البرمجة العادية؟",
            "أين نجد الذكاء الاصطناعي في حياتنا اليومية والتطبيقات؟",
            "أبعاد الذكاء الاصطناعي (أنواعه وأخلاقياته ومستقبله).",
            "تجربة محاكاة تفاعلية مباشرة لتغطية نمط ذكي على الويب.",
            "كتابة أول برنامج تحليل مشاعر تفاعلي بـ Python.",
            "اختبار المعلومات التفاعلي + تحدي مشروع الحصة!"
        ],
        "agenda_en": [
            "What is AI & how does it differ from traditional programming?",
            "Where do we find AI in our daily lives and apps?",
            "AI dimensions (types, ethics, and future outlook).",
            "Live interactive hands-on AI sentiment simulation.",
            "Writing your first interactive Python sentiment classifier.",
            "Interactive quiz + session assignment challenge!"
        ],
        "sec1_title_ar": "1. ما هو الذكاء الاصطناعي؟ (الفرق الجوهري)",
        "sec1_title_en": "1. What is Artificial Intelligence? (Core Difference)",
        "sec1_desc_ar": "في البرمجة التقليدية نكتب كل القواعد يدوياً (If/Else)، بينما في الذكاء الاصطناعي نغذي الكمبيوتر ببيانات كثيرة ليستنتج القواعد بنفسه!",
        "sec1_desc_en": "In traditional programming we write all rules manually (If/Else), whereas in AI we feed the computer lots of data to infer rules by itself!",
        "sec2_title_ar": "2. أين نجد الذكاء الاصطناعي في حياتنا اليومية؟",
        "sec2_title_en": "2. Where do we find AI in our daily lives?",
        "sec2_desc_ar": "اضغط على التطبيقات التالية لاكتشاف كيف يعمل الذكاء الاصطناعي خلف الكواليس:",
        "sec2_desc_en": "Click on the cards below to discover how AI works behind the scenes:",
        "sec3_title_ar": "3. أبعاد الذكاء الاصطناعي وأخلاقياته",
        "sec3_title_en": "3. AI Dimensions & Ethics",
        "sec3_desc_ar": "فهم الفرق بين Narrow AI و General AGI ومسؤولية الحفاظ على البيانات وعدم التحيز.",
        "sec3_desc_en": "Understanding Narrow AI vs General AGI, data privacy, and avoiding algorithmic bias.",
        "lab_title_ar": "اختبار محاكاة تحليل المشاعر (Sentiment AI Simulator)",
        "lab_title_en": "Sentiment AI Simulator",
        "lab_desc_ar": "اكتب جملة وسيقوم النموذج الذكي بتوقع نبرتك ومحاكاتها فورياً!",
        "lab_desc_en": "Type any sentence and the AI model will detect your sentiment instantly!",
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
        "quiz_q_ar": "ما هو الفرق الأساسي بين الذكاء الاصطناعي والبرمجة التقليدية؟",
        "quiz_q_en": "What is the main difference between AI and traditional programming?",
        "quiz_opt1_ar": "البرمجة التقليدية أسرع دائماً.",
        "quiz_opt1_en": "Traditional programming is always faster.",
        "quiz_opt2_ar": "الذكاء الاصطناعي يتعلم الأنماط من البيانات بنفسه بدلاً من كتابة القواعد يدوياً.",
        "quiz_opt2_en": "AI learns patterns from data by itself instead of manual hardcoded rules.",
        "quiz_correct": 2,
        "hw_ar": "أضف 5 كلمات جديدة إيجابية و 5 كلمات حزينة لكود بايثون، واختبر جمل عائلتك في البيت! 📸",
        "hw_en": "Add 5 new positive and 5 negative words to your Python code and test family sentences at home! 📸"
    },
    {
        "num": 2,
        "title_ar": "Generative AI & Prompt Engineering",
        "title_en": "Generative AI & Prompt Engineering",
        "subtitle_ar": "كيف تجعل الذكاء الاصطناعي يرسم ويكتب أفكارك وخيالاتك؟ 🎨✍️",
        "subtitle_en": "How to make AI draw and write your creative ideas & imaginations? 🎨✍️",
        "tag_ar": "السيشن الثاني 🎨",
        "tag_en": "Session 2 🎨",
        "agenda_ar": [
            "مفهوم الذكاء الاصطناعي التوليدي (Generative vs Discriminative AI).",
            "قواعد هندسة الأوامر (Prompt Engineering C-T-C Framework).",
            "تحدي صياغة الأوامر (Prompt Battles) وتجنب هلوسة الذكاء الاصطناعي.",
            "تجربة محاكي توليد القصص التفاعلي على الويب.",
            "برمجة مولد القصص الخيالية بـ Python.",
            "تحدي الحصة واختبار المعلومات التفاعلي."
        ],
        "agenda_en": [
            "Generative vs Discriminative AI concepts.",
            "Prompt Engineering C-T-C Framework (Context, Task, Constraints).",
            "Prompt Battles challenge & avoiding AI hallucinations.",
            "Interactive Story Generator web simulator.",
            "Programming a Fantasy Story Generator in Python.",
            "Interactive quiz & prompt engineering challenge."
        ],
        "sec1_title_ar": "1. الذكاء الاصطناعي التوليدي (Generative AI)",
        "sec1_title_en": "1. Generative AI",
        "sec1_desc_ar": "الذكاء الاصطناعي التقليدي يصنف البيانات (هذه صورة قطة)، أما التوليدي فيبتكر محتوى جديد تماماً (نرسم قطة ترتدي نظارة على المريخ)!",
        "sec1_desc_en": "Traditional AI classifies data (e.g. 'this is a cat photo'), while Generative AI invents completely new content (e.g. 'a cat wearing glasses on Mars')!",
        "sec2_title_ar": "2. قاعدة C-T-C لهندسة الأوامر الاحترافية",
        "sec2_title_en": "2. The C-T-C Prompt Engineering Rule",
        "sec2_desc_ar": "للحصول على أفضل نتيجة من ChatGPT أو Midjourney، طبق قاعدة C-T-C: Context (السياق) + Task (المهمة) + Constraint (الشروط).",
        "sec2_desc_en": "For best results from ChatGPT or Midjourney, use C-T-C: Context + Task + Constraints.",
        "sec3_title_ar": "3. أبعاد التوليد والهلوسة (AI Hallucination)",
        "sec3_title_en": "3. AI Hallucinations & Limitations",
        "sec3_desc_ar": "أحياناً يبتكر الذكاء الاصطناعي معلومات غير صحيحة، ولذلك يجب أن نراجع دائماً ما يكتبه ونستخدم الشروط الدقيقة.",
        "sec3_desc_en": "AI sometimes invents false facts (hallucinations), so we must double-check output using strict constraints.",
        "lab_title_ar": "محاكي توليد القصص الخيالية الذكي (AI Story Generator)",
        "lab_title_en": "AI Story Generator Simulator",
        "lab_desc_ar": "اختر بطل القصة والمكان والمشكلة، وشاهد كيف يولد الذكاء الاصطناعي قصة فورية!",
        "lab_desc_en": "Pick a hero, setting, and conflict to see AI craft a story live!",
        "code_filename": "ai_story_generator.py",
        "code": """import random

def generate_ai_story(hero, setting, enemy):
    intros = [f"في زمن بعيد في {setting}، عاش البطل {hero}.", f"كان {hero} يستكشف {setting} عندما حدثت المفاجأة!"]
    conflicts = [f"وفجأة ظهر {enemy} ليتحداه في اختبار ذكاء اصطناعي حاسم!", f"اكتشف {hero} أن {enemy} يحاول السيطرة على المدينة!"]
    climax = [f"استخدم {hero} خوارزمية الذكاء الاصطناعي وانتصر بسهولة! 🌟"]
    
    return f"{random.choice(intros)}\n{random.choice(conflicts)}\n{random.choice(climax)}"

print(generate_ai_story("أحمد مهندس الذكاء الاصطناعي", "معمل المستقبل", "الفيروس الرقمي"))""",
        "quiz_q_ar": "ماذا تعني قاعدة C-T-C في صياغة الأوامر (Prompt Engineering)؟",
        "quiz_q_en": "What does the C-T-C rule stand for in Prompt Engineering?",
        "quiz_opt1_ar": "Computer, Technology, Coding",
        "quiz_opt1_en": "Computer, Technology, Coding",
        "quiz_opt2_ar": "Context (السياق) + Task (المهمة) + Constraints (الشروط والقيود)",
        "quiz_opt2_en": "Context + Task + Constraints",
        "quiz_correct": 2,
        "hw_ar": "اكتب Prompt كامل بطريقة C-T-C واجعله يولد فكرة لعبة جديدة، ثم شغل كود بايثون لتوليد 3 قصص مختلفة! 🚀",
        "hw_en": "Write a full C-T-C prompt to generate a new game idea, then run Python code to generate 3 unique stories! 🚀"
    },
    {
        "num": 3,
        "title_ar": "بناء الشات بوت الذكي (AI Chatbot)",
        "title_en": "Building an AI Chatbot",
        "subtitle_ar": "كيف تفهم البرامج نية المستخدم وترد عليه بذكاء؟ 💬🤖",
        "subtitle_en": "How programs understand user intents and respond intelligently? 💬🤖",
        "tag_ar": "السيشن الثالث 💬",
        "tag_en": "Session 3 💬",
        "agenda_ar": [
            "كيف تفهم الشات بوتات نية المستخدم (Intent Recognition)؟",
            "تصميم شجرة النوايا (Intent Trees & Knowledge Base).",
            "كيف نمنع الشات بوت من الرد بإجابات غريبة عند عدم الفهم؟",
            "تجربة محاكاة شات بوت تفاعلي مباشر داخل الصفحة.",
            "برمجة Megaminds Custom AI Chatbot بـ Python.",
            "اختبار المعلومات وتحدي بناء شات بوت الأكاديمية!"
        ],
        "agenda_en": [
            "How chatbots recognize user intents (Intent Recognition).",
            "Designing Intent Trees & Knowledge Base.",
            "Handling unknown inputs with fallback responses.",
            "Live interactive chatbot simulator.",
            "Programming a custom Megaminds AI Chatbot in Python.",
            "Interactive quiz & chatbot building challenge!"
        ],
        "sec1_title_ar": "1. التعرف على النوايا (Intent Recognition)",
        "sec1_title_en": "1. Intent Recognition",
        "sec1_desc_ar": "عندما يقول المستخدم 'أهلاً'، 'مرحباً'، أو 'صباح الخير'، كلهم يملكون نفس النية (Greeting). الشات بوت الذكي يجمع الكلمات تحت نية واحدة!",
        "sec1_desc_en": "When a user says 'Hi', 'Hello', or 'Good morning', they all map to the same intent (Greeting). Smart chatbots group patterns into intents!",
        "sec2_title_ar": "2. هيكلة قاعدة المعرفة (Knowledge Tree)",
        "sec2_title_en": "2. Knowledge Tree Structure",
        "sec2_desc_ar": "نقوم بإنشاء Dictionary يحتوي على النوايا والإجابات الممكنة ليختار منها الشات بوت عشوائياً بشكل طبيعي.",
        "sec2_desc_en": "We create a dictionary of intents and responses so the chatbot replies naturally.",
        "sec3_title_ar": "3. التعامل مع المدخلات غير المعروفة (Fallback Intent)",
        "sec3_title_en": "3. Fallback Intent",
        "sec3_desc_ar": "إذا سأل المستخدم سؤالاً غير موجود في قاعدة البيانات، يستخدم الشات بوت رد اعتذاري محترف ويطلب التوضيح.",
        "sec3_desc_en": "If a user asks something outside the knowledge base, the bot provides a polite fallback response.",
        "lab_title_ar": "محاكي الشات بوت التفاعلي (Live AI Chatbot Simulator)",
        "lab_title_en": "Live AI Chatbot Simulator",
        "lab_desc_ar": "تحدث مع الشات بوت في الصندوق التالي واختبر قدرته على فهم التحية، الأسئلة، والمساعدة!",
        "lab_desc_en": "Chat with the bot below to test greetings, course questions, and help!",
        "code_filename": "megaminds_chatbot.py",
        "code": """import random

knowledge_base = {
    "greetings": {
        "patterns": ["مرحبا", "اهلا", "سلام", "hi", "hello"],
        "responses": ["أهلاً بك يا بطل في أكاديمية Megaminds! 🤖", "مرحباً بك! كيف يمكنني مساعدتك اليوم؟"]
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
        "quiz_q_ar": "ماذا يسمى تجميع الكلمات المختلفة مثل (أهلاً، مرحباً، سلام) تحت فكرة واحدة؟",
        "quiz_q_en": "What is it called when different phrases like 'Hi', 'Hello', 'Hey' are grouped under one concept?",
        "quiz_opt1_ar": "Intent Recognition (التعرف على النية)",
        "quiz_opt1_en": "Intent Recognition",
        "quiz_opt2_ar": "Copy Paste Error",
        "quiz_opt2_en": "Copy Paste Error",
        "quiz_correct": 1,
        "hw_ar": "أضف نية جديدة (Intent) لشات بوت بايثون تجيب على سؤال 'من أنت؟' وإعطاء رد إبداعي! 💬",
        "hw_en": "Add a new intent to your Python chatbot answering 'Who are you?' with a creative response! 💬"
    },
    {
        "num": 4,
        "title_ar": "الصوت والذكاء الاصطناعي (Siri Clone)",
        "title_en": "Voice & Audio AI (Siri Clone)",
        "subtitle_ar": "تحويل الصوت إلى نصوص والتحدث بصوت آلي بـ Python 🎙️🔊",
        "subtitle_en": "Converting speech to text and synthesized voice in Python 🎙️🔊",
        "tag_ar": "السيشن الرابع 🎙️",
        "tag_en": "Session 4 🎙️",
        "agenda_ar": [
            "كيف يسمع الحاسوب (Speech-to-Text) وكيف يتكلم (Text-to-Speech)؟",
            "تحويل الموجات الصوتية إلى بيانات رقمية يفهمها الكود.",
            "مكتبات الصوت في بايثون: pyttsx3 و SpeechRecognition.",
            "تجربة محاكي المساعد الصوتي على الويب.",
            "كتابة كود مساعد صوتي يفتح يوتيوب ويخبرك بالوقت بصوته!",
            "اختبار المعلومات وتحدي المساعد الصوتي."
        ],
        "agenda_en": [
            "How computers hear (Speech-to-Text) and speak (Text-to-Speech).",
            "Converting audio waves into digital data.",
            "Python audio libraries: pyttsx3 & SpeechRecognition.",
            "Interactive Voice Synthesizer Simulator.",
            "Programming a voice assistant opening websites and speaking the time!",
            "Interactive quiz & voice assistant challenge."
        ],
        "sec1_title_ar": "1. الصوت الرقمي (Digital Audio)",
        "sec1_title_en": "1. Digital Audio",
        "sec1_desc_ar": "الصوت هو اهتزازات في الهواء. الميكروفون يحولها إلى موجات كهربائية، والـ AI يحول تلك الموجات إلى كلمات نصية!",
        "sec1_desc_en": "Sound is vibration in the air. Microphones convert vibrations to electrical signals, and AI converts signals into text!",
        "sec2_title_ar": "2. التحدث الآلي (Text To Speech - TTS)",
        "sec2_title_en": "2. Text-To-Speech (TTS)",
        "sec2_desc_ar": "تقنية تحول أي نص مكتوب إلى صوت متكلم بنبرات مختلفة وسرعات محددة.",
        "sec2_desc_en": "Technology converting any written text into spoken voice with customizable pitch and speech rate.",
        "sec3_title_ar": "3. الأوامر الذكية الاستجابية",
        "sec3_title_en": "3. Smart Voice Commands",
        "sec3_desc_ar": "عند قراءة كلمة أمر مثل 'افتح يوتيوب'، يستخدم الكود مكتبة `webbrowser` لتنفيذ الأمر فورياً!",
        "sec3_desc_en": "When detecting command phrases like 'open YouTube', Python executes the command instantly via `webbrowser`!",
        "lab_title_ar": "محاكي المساعد الصوتي التفاعلي (Voice Synthesizer Simulator)",
        "lab_title_en": "Voice Synthesizer Simulator",
        "lab_desc_ar": "اكتب جملة واضغط نطق لتقوم الصفحة بقراءتها بصوت الذكاء الاصطناعي المباشر!",
        "lab_desc_en": "Type any sentence and click Speak to hear browser speech synthesis live!",
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
        "quiz_q_ar": "ما هي التقنية المسؤولة عن تحويل النص المكتوب إلى صوت مسموع؟",
        "quiz_q_en": "Which technology converts written text into audible speech?",
        "quiz_opt1_ar": "Text-To-Speech (TTS)",
        "quiz_opt1_en": "Text-To-Speech (TTS)",
        "quiz_opt2_ar": "Manual Typing",
        "quiz_opt2_en": "Manual Typing",
        "quiz_correct": 1,
        "hw_ar": "برمج مساعدك الصوتي ليقوم بالترحيب باسمك وافتتاح موقعك المفضّل عند تشغيله! 🔊",
        "hw_en": "Program your voice assistant to greet you by name and open your favorite website! 🔊"
    },
    {
        "num": 5,
        "title_ar": "أساسيات الرؤية الحاسوبية (OpenCV)",
        "title_en": "Computer Vision Basics (OpenCV)",
        "subtitle_ar": "كيف يرى الحاسوب الصور والألوان وينفذ الفلاتر السحرية؟ 📸👁️",
        "subtitle_en": "How computers see images, colors, and apply magic filters? 📸👁️",
        "tag_ar": "السيشن الخامس 👁️",
        "tag_en": "Session 5 👁️",
        "agenda_ar": [
            "كيف تفهم الكاميرا الصور؟ مصفوفات الـ Pixels وألوان RGB.",
            "مفهوم الفلاتر وتحديد الحواف (Canny Edge Detection).",
            "مكتبة OpenCV وفتح بث الكاميرا الحية باللابتوب.",
            "تجربة محاكي الفلاتر التفاعلي على الويب.",
            "كتابة كود Python لفتح الكاميرا وتحويلها لألوان رمادية وفلتر حواف.",
            "تحدي الحصة واختبار الرؤية الحاسوبية."
        ],
        "agenda_en": [
            "How cameras understand images: Pixel grids & RGB color values.",
            "Filter concepts & Canny Edge Detection.",
            "OpenCV library & accessing laptop live camera feed.",
            "Interactive Computer Vision Filter Simulator.",
            "Writing Python code to convert camera feed to Grayscale & Edge Detection.",
            "Interactive quiz & computer vision challenge."
        ],
        "sec1_title_ar": "1. الصورة كأرقام (Image Pixels Grid)",
        "sec1_title_en": "1. Images as Pixel Numbers",
        "sec1_desc_ar": "الكمبيوتر لا يرى ألواناً كما نراها، بل يرى مصفوفة شبكية من الأرقام تمثل درجات الأحمر والأخضر والأزرق (RGB) من 0 لـ 255!",
        "sec1_desc_en": "Computers see images as a grid matrix of numbers representing Red, Green, and Blue (RGB) values from 0 to 255!",
        "sec2_title_ar": "2. معالجة الصور وفلاتر Edge Detection",
        "sec2_title_en": "2. Image Processing & Edge Detection Filters",
        "sec2_desc_ar": "عن طريق طرح قيم الـ Pixels المجاورة، يستطيع الكود اكتشاف حواف الأجسام والوجوه بسرعة فائقة.",
        "sec2_desc_en": "By analyzing pixel gradient differences, algorithms detect object and facial edges instantly.",
        "sec3_title_ar": "3. بث الفيديو المباشر (Video Streaming Frames)",
        "sec3_title_en": "3. Live Video Frames",
        "sec3_desc_ar": "الفيديو ما هو إلا مجموعة صور متتابعة (Frames) تُعرض بسرعة 30 صورة في الثانية!",
        "sec3_desc_en": "Video is simply a rapid sequence of image frames rendered at 30 frames per second!",
        "lab_title_ar": "محاكي فلاتر الرؤية الحاسوبية (Computer Vision Filter Sim)",
        "lab_title_en": "Computer Vision Filter Simulator",
        "lab_desc_ar": "اضغط على الفلاتر المختلفة لرؤية كيف يتغير تحليل الصورة رقمياً!",
        "lab_desc_en": "Click on different filter buttons to see how image processing changes digital views!",
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
        "quiz_q_ar": "من كم رقم تتكون ألوان كل بكسل في مصفوفة RGB؟",
        "quiz_q_en": "How many values make up each pixel color in an RGB channels matrix?",
        "quiz_opt1_ar": "3 أرقام (Red, Green, Blue)",
        "quiz_opt1_en": "3 numbers (Red, Green, Blue)",
        "quiz_opt2_ar": "رقم واحد فقط",
        "quiz_opt2_en": "Only 1 single number",
        "quiz_correct": 1,
        "hw_ar": "قم بتشغيل كود OpenCV وجرب التقاط صورة لك بفلتر الحواف وشاركها في المعمل! 📸",
        "hw_en": "Run OpenCV python code, capture your photo with edge detection, and share it in class! 📸"
    },
    {
        "num": 6,
        "title_ar": "دمج النماذج مع Python (Teachable Machine)",
        "title_en": "Model Integration with Python (Teachable Machine)",
        "subtitle_ar": "تدريب النموذج على الويب وتشغيله داخل كود بايثون محلياً! 🎯💻",
        "subtitle_en": "Training models on the web and running them inside Python locally! 🎯💻",
        "tag_ar": "السيشن السادس 🎯",
        "tag_en": "Session 6 🎯",
        "agenda_ar": [
            "كيف ندرب نموذج AI بدون تعقيد باستخدام Google Teachable Machine؟",
            "تصدير النموذج (Keras / TensorFlow Model).",
            "مفهوم درجة الثقة (Confidence Score %).",
            "تجربة محاكي التعرف على العناصر المباشر.",
            "ربط نموذج Teachable Machine بكود OpenCV في بايثون.",
            "تحدي الحصة ونظام التنبيه الذكي."
        ],
        "agenda_en": [
            "Training AI models effortlessly with Google Teachable Machine.",
            "Exporting model files (Keras / TensorFlow format).",
            "Understanding Confidence Score percentages.",
            "Live object detection confidence simulator.",
            "Connecting Teachable Machine model to OpenCV in Python.",
            "Session challenge: Smart object detection alarm!"
        ],
        "sec1_title_ar": "1. التدريب على الويب (Teachable Machine)",
        "sec1_title_en": "1. Web Model Training",
        "sec1_desc_ar": "نلتقط 30 صورة للغرض الأول و 30 صورة للغرض الثاني، والضغط على Train ليقوم الموقع بإنشاء النموذج في ثوانٍ!",
        "sec1_desc_en": "We snap 30 images of Object A and 30 of Object B, click Train, and get an AI model in seconds!",
        "sec2_title_ar": "2. نقل النموذج لكود Python",
        "sec2_title_en": "2. Exporting Model to Python",
        "sec2_desc_ar": "نقوم بتحميل ملف `keras_model.h5` وملف `labels.txt` وقراءتهما داخل بايثون لاستخدامه محلياً بدون إنترنت.",
        "sec2_desc_en": "We download `keras_model.h5` and `labels.txt` and load them into Python to run offline.",
        "sec3_title_ar": "3. نسبة الثقة (Confidence Percentage)",
        "sec3_title_en": "3. Confidence Score Threshold",
        "sec3_desc_ar": "النموذج يعطينا نسبة مئوية (مثلاً: 97% موبايل)، ونحن نضع شرطاً في الكود: إذا تجاوزت 90% ننفذ الإجراء!",
        "sec3_desc_en": "The model outputs a probability percentage (e.g. 97% Phone). We execute actions if confidence > 90%!",
        "lab_title_ar": "محاكي التعرف على الأغراض (Object Detection Confidence Sim)",
        "lab_title_en": "Object Detection Confidence Simulator",
        "lab_desc_ar": "اختبر كيف تتغير نسبة ثقة النموذج الذكي فورياً عند رؤية عناصر مختلفة!",
        "lab_desc_en": "Test how AI model confidence changes live when detecting various items!",
        "code_filename": "teachable_python.py",
        "code": """import cv2
import numpy as np
# يتم تحميل نموذج Keras وقراءة الكاميرا
print("🤖 جاري تشغيل نموذج Teachable Machine داخل Python...")
print("النتيجة: تم التعرف على الغرض بنسبة ثقة 96.5%!")""",
        "quiz_q_ar": "ماذا يفعل الكود عندما تكون نسبة الثقة (Confidence Score) عالية جداً؟",
        "quiz_q_en": "What does the code do when the model Confidence Score exceeds threshold?",
        "quiz_opt1_ar": "ينفذ القرار المطلوب بثقة عالية.",
        "quiz_opt1_en": "Executes target action with high certainty.",
        "quiz_opt2_ar": "يغلق البرنامج فوراً.",
        "quiz_opt2_en": "Closes the application immediately.",
        "quiz_correct": 1,
        "hw_ar": "قم بدراسة نموذج Teachable Machine على الويب ودرب فصلين (مثلاً: نظارة / بدون نظارة)! 👓",
        "hw_en": "Train a 2-class model on Teachable Machine (e.g., Glasses ON vs OFF) and test it! 👓"
    },
    {
        "num": 7,
        "title_ar": "الذكاء الاصطناعي في الألعاب (Rock Paper Scissors AI)",
        "title_en": "AI in Games (Rock Paper Scissors AI)",
        "subtitle_ar": "جعل الـ AI يلعب ضد الإنسان ويقرأ حركات يده! 🎮✊",
        "subtitle_en": "Making AI play against humans by reading hand gestures live! 🎮✊",
        "tag_ar": "السيشن السابع 🎮",
        "tag_en": "Session 7 🎮",
        "agenda_ar": [
            "كيف يقرأ الذكاء الاصطناعي إيماءات اليد (Rock ✊, Paper ✋, Scissors ✌️)؟",
            "بناء منطق اللعبة والعد التنازلي.",
            "حساب النقاط تلقائياً (Player Score vs AI Score).",
            "تجربة محاكي اللعبة التفاعلي المباشر.",
            "كتابة كود اللعبة التنافسي بـ Python.",
            "بطولة القاعة وتحدي هزم الذكاء الاصطناعي!"
        ],
        "agenda_en": [
            "How AI reads hand gestures (Rock ✊, Paper ✋, Scissors ✌️).",
            "Building game logic & round countdowns.",
            "Automatic score tracking (Player vs AI Score).",
            "Interactive Rock Paper Scissors AI Simulator.",
            "Writing competitive game code in Python.",
            "Class championship: Beat the AI Challenge!"
        ],
        "sec1_title_ar": "1. قراءة إيماءات اليد (Gesture Recognition)",
        "sec1_title_en": "1. Hand Gesture Recognition",
        "sec1_desc_ar": "النموذج يتعرف على قبضتك (حجر)، كفك المفتوح (ورقة)، أو أصبعيك (مقص) في التو واللحظة.",
        "sec1_desc_en": "The model detects your fist (Rock), open palm (Paper), or V-sign (Scissors) in real time.",
        "sec2_title_ar": "2. عشوائية الكمبيوتر ومنطق الفوز",
        "sec2_title_en": "2. AI Decision Logic & Winner Check",
        "sec2_desc_ar": "الكمبيوتر يختار حركة حرة باستخدام `random.choice` ثم يقارن حركته بحركة يدك أمام الكاميرا ويحدد الفائز صريحاً.",
        "sec2_desc_en": "AI picks a random move via `random.choice`, compares it to your camera gesture, and determines winner.",
        "sec3_title_ar": "3. لوحة النتيجة الرقمية (Live Score Board)",
        "sec3_title_en": "3. On-Screen Live Scoreboard",
        "sec3_desc_ar": "إظهار النتيجة مباشرة فوق شاشة الكاميرا باستخدام أمر `cv2.putText` لتجربة ممتعة للغاية!",
        "sec3_desc_en": "Displaying live scores directly on top of camera stream using `cv2.putText` for ultimate gaming fun!",
        "lab_title_ar": "محاكي لعبة حجر ورقة مقص ضد الـ AI (RPS Interactive Sim)",
        "lab_title_en": "Rock Paper Scissors AI Simulator",
        "lab_desc_ar": "اختر حركتك وشاهد اختيار الذكاء الاصطناعي ومن سيكسب الجولة!",
        "lab_desc_en": "Choose your gesture and see AI's counter move and who wins the round!",
        "code_filename": "rps_ai_game.py",
        "code": """import random

choices = ["حجر ✊", "ورقة ✋", "مقص ✌️"]

def play_round(user_choice):
    ai_choice = random.choice(choices)
    print(f"أنت اخترت: {user_choice} | الـ AI اختار: {ai_choice}")
    if user_choice == ai_choice: return "تعادل! 🤝"
    return "مبروك! لقد هزمت الذكاء الاصطناعي! 🎉"

print(play_round("حجر ✊"))""",
        "quiz_q_ar": "كيف يحدد البرنامج الحركة الفائزة في لعبة حجر ورقة مقص؟",
        "quiz_q_en": "How does the Python game evaluate the round winner?",
        "quiz_opt1_ar": "بمقارنة حركة المستخدم مع اختيار الـ AI عبر الشروط المنطقية.",
        "quiz_opt1_en": "By comparing user gesture to AI move using conditional logic.",
        "quiz_opt2_ar": "بالتخمين العشوائي بدون كود.",
        "quiz_opt2_en": "By random guess without code logic.",
        "quiz_correct": 1,
        "hw_ar": "شغل كود بايثون للعبة حجر ورقة مقص وتحدى أخاك أو صديقك ورني مين هيكسب! 🏆",
        "hw_en": "Run your RPS Python game and challenge your friends to beat your AI! 🏆"
    },
    {
        "num": 8,
        "title_ar": "التحكم بالكمبيوتر بحركات اليد (Gesture Control)",
        "title_en": "Gesture-Controlled PC (PyAutoGUI Racing)",
        "subtitle_ar": "لعب لعبة سباق سيارات كاملة بإشارة يدك أمام الكاميرا! 🕹️🖐️",
        "subtitle_en": "Playing a complete racing game by waving your hands in front of camera! 🕹️🖐️",
        "tag_ar": "السيشن الثامن 🕹️",
        "tag_en": "Session 8 🕹️",
        "agenda_ar": [
            "كيف نربط الرؤية الحاسوبية بمحاكاة زر الكيبورد؟",
            "مكتبة PyAutoGUI للتحكم بالماوس والأسهم برمجياً.",
            "تحويل موقع اليد إلى أمر (Left Arrow / Right Arrow).",
            "تجربة محاكي التحكم الإشاري على الويب.",
            "كتابة كود بايثون لتشغيل لعبة سباق باليد بدون لمس الكيبورد!",
            "تحدي الحصة وسباق السيارات الإشاري."
        ],
        "agenda_en": [
            "Connecting computer vision outputs to keyboard keystrokes.",
            "PyAutoGUI library for controlling mouse & arrow keys.",
            "Mapping hand X-coordinates to Left/Right key presses.",
            "Interactive Gesture Steering Simulator.",
            "Writing Python code to control car racing without touching keyboard!",
            "Session challenge: Touchless Racing Tournament!"
        ],
        "sec1_title_ar": "1. محاكاة الكيبورد (PyAutoGUI)",
        "sec1_title_en": "1. Keyboard Automation (PyAutoGUI)",
        "sec1_desc_ar": "مكتبة PyAutoGUI تسمح للبايثون بالضغط على أي زر في الكيبورد تلقائياً كأن هناك إنسان يضغط عليه!",
        "sec1_desc_en": "PyAutoGUI allows Python to trigger virtual key presses automatically as if a human pressed them!",
        "sec2_title_ar": "2. تقسيم شاشة الكاميرا إلى مناطق تحكم",
        "sec2_title_en": "2. Camera Zone Partitioning",
        "sec2_desc_ar": "إذا كانت اليد في الناحية اليسرى من الشاشة نرسل أمر `press('left')` وإذا كانت في اليمين نرسل `press('right')`!",
        "sec2_desc_en": "If hand is on left side of camera, we send `press('left')`; if on right side, `press('right')`!",
        "sec3_title_ar": "3. تجربة اللعب بدون لمس (Touchless Gaming)",
        "sec3_title_en": "3. Touchless Interactive Gaming",
        "sec3_desc_ar": "تقنية مدهشة تستخدم في ألعاب المستقبليين وفي المستشفيات للتحكم بالأجهزة دون لمسها.",
        "sec3_desc_en": "Futuristic touchless interaction tech used in modern gaming and surgical room controls.",
        "lab_title_ar": "محاكي التحكم الإشاري في عجلة القيادة (Gesture Steering Sim)",
        "lab_title_en": "Gesture Steering Simulator",
        "lab_desc_ar": "حرك المؤشر يميناً ويساراً لمحاكاة حركة يدك أمام كاميرا لابتوبك!",
        "lab_desc_en": "Move your cursor left and right to simulate hand steering live!",
        "code_filename": "gesture_racing.py",
        "code": """import pyautogui
import time

print("🏎️ نظام التحكم بالسباق عبر حركة اليد جاري التشغيل...")
# عند رصد حركة اليد لليمين:
# pyautogui.press('right')
# عند رصد حركة اليد لليسار:
# pyautogui.press('left')
print("تم إرسال أمر الانعطاف بنجاح!")""",
        "quiz_q_ar": "ما هي المكتبة المسؤولة عن إرسال ضغطات الكيبورد برمجياً في بايثون؟",
        "quiz_q_en": "Which Python library automates keyboard key presses?",
        "quiz_opt1_ar": "PyAutoGUI",
        "quiz_opt1_en": "PyAutoGUI",
        "quiz_opt2_ar": "Math",
        "quiz_opt2_en": "Math",
        "quiz_correct": 1,
        "hw_ar": "شغل لعبة سباق بسيطة على الويب واجعل كود بايثون يتحكم فيها بيدك! 🏎️",
        "hw_en": "Launch a web racing game and control the car with Python hand gestures! 🏎️"
    },
    {
        "num": 9,
        "title_ar": "المساعد المكتبي الشامل (Desktop Assistant)",
        "title_en": "Comprehensive Desktop Assistant",
        "subtitle_ar": "دمج برامج النظام وأوامر الصوت في تطبيق ذكي لسطح مكتبك 🖥️🤖",
        "subtitle_en": "Combining system programs & voice commands into one desktop app 🖥️🤖",
        "tag_ar": "السيشن التاسع 🖥️",
        "tag_en": "Session 9 🖥️",
        "agenda_ar": [
            "كيف يتحكم بايثون في برامج لابتوبك (فتح الحاسبة، النوت باد، المتصفح)؟",
            "مكتبة `os` و `subprocess` في بايثون.",
            "تجميع الصوت + الشات بوت + البرامج في تطبيق واحد.",
            "تجربة محاكي المساعد المكتبي على الويب.",
            "كتابة كود Megaminds Desktop Assistant المتكامل.",
            "تحدي تخصيص المساعد ليخدم عائلتك."
        ],
        "agenda_en": [
            "How Python controls PC apps (Calculator, Notepad, Browser).",
            "Python `os` and `subprocess` modules.",
            "Integrating Voice + Chatbot + OS Controls into 1 app.",
            "Interactive Desktop Assistant Hub Simulator.",
            "Writing Megaminds Desktop Assistant Python code.",
            "Customizing assistant for family tasks!"
        ],
        "sec1_title_ar": "1. التفاعل مع نظام التشغيل (OS Commands)",
        "sec1_title_en": "1. Operating System Integration",
        "sec1_desc_ar": "عن طريق مكتبة `os` نستطيع كتابة `os.system('calc')` ليفتح الويندوز الآلة الحاسبة فوراً!",
        "sec1_desc_en": "Using the `os` module, calling `os.system('calc')` opens Windows Calculator instantly!",
        "sec2_title_ar": "2. تجميع التقنيات (Integration)",
        "sec2_title_en": "2. Multi-Module Integration",
        "sec2_desc_ar": "ندمج الصوت من سيشن 4 والـ Chatbot من سيشن 3 والتحكم بالنظام في كود واحد منظم.",
        "sec2_desc_en": "We combine Session 4 Voice + Session 3 Chatbot + OS Automation into a clean codebase.",
        "sec3_title_ar": "3. الترحيب والتخصيص الشخصي",
        "sec3_title_en": "3. Personalized Assistance",
        "sec3_desc_ar": "المساعد يعرف اسمك ويرحب بك ويقدم لك خيارات التحكم بأسلوب ذكي جذاب.",
        "sec3_desc_en": "The assistant recognizes your name, greets you, and manages desktop shortcuts intelligently.",
        "lab_title_ar": "محاكي المساعد المكتبي التفاعلي (Desktop Assistant Hub)",
        "lab_title_en": "Desktop Assistant Hub Simulator",
        "lab_desc_ar": "اضغط الأوامر لرؤية كيف يستجيب المساعد المكتبي الذكي لكل طلب!",
        "lab_desc_en": "Click desktop commands to test smart assistant responses live!",
        "code_filename": "desktop_assistant.py",
        "code": """import os

def execute_command(cmd):
    if "حاسبة" in cmd or "calc" in cmd:
        print("🖥️ جاري فتح الآلة الحاسبة...")
        os.system("calc")
    elif "نوت باد" in cmd or "notepad" in cmd:
        print("📝 جاري فتح المفكرة...")
        os.system("notepad")
    else:
        print("🤖 أمر غير معروف لمكتبتك المخصصة!")

execute_command("افتح الحاسبة")""",
        "quiz_q_ar": "ما هي المكتبة المسؤولة عن تشغيل برامج الويندوز مثل الآلة الحاسبة والنوت باد في بايثون؟",
        "quiz_q_en": "Which module launches Windows applications like Calculator in Python?",
        "quiz_opt1_ar": "مكتبة OS",
        "quiz_opt1_en": "OS module",
        "quiz_opt2_ar": "مكتبة Random",
        "quiz_opt2_en": "Random module",
        "quiz_correct": 1,
        "hw_ar": "أضف أمراً جديداً لمساعدك المكتبي يفتح فيه برنامج الرسام (mspaint) بصوتك! 🎨",
        "hw_en": "Add a new command to your desktop assistant that launches Paint (mspaint) via voice! 🎨"
    },
    {
        "num": 10,
        "title_ar": "حارس الغرفة والمكتب الذكي (Smart AI Security Guard)",
        "title_en": "Smart AI Security Guard",
        "subtitle_ar": "نظام حراسة ذكي يراقب الغرفة ويطلق صفارات الإنذار عند الدخول! 🚨🛡️",
        "subtitle_en": "Smart security system monitoring room and triggering alarms on intruders! 🚨🛡️",
        "tag_ar": "السيشن العاشر 🚨",
        "tag_en": "Session 10 🚨",
        "agenda_ar": [
            "مفهوم الأنظمة المتكاملة (Vision + Audio Multi-modal AI).",
            "رصد التغير في الصورة والإحساس بالحركة الغريبة.",
            "تلوين الشاشة بالأحمر وتشغيل صوت الإنذار التلقائي.",
            "تجربة محاكي نظام الحراسة الذكي على الويب.",
            "كتابة كود AI Security Guard المباشر بـ Python.",
            "تحدي تأمين غرفتك في المنزل بالنظام الجديد!"
        ],
        "agenda_en": [
            "Multi-modal AI concept (Vision + Audio Integration).",
            "Frame motion change detection & intruder sensing.",
            "Visual red screen flashing & automatic siren audio trigger.",
            "Interactive AI Security Guard Simulator.",
            "Writing Python AI Security Guard code.",
            "Session challenge: Securing your room at home!"
        ],
        "sec1_title_ar": "1. الذكاء الاصطناعي متعدد الوسائط (Multi-modal AI)",
        "sec1_title_en": "1. Multi-modal AI Systems",
        "sec1_desc_ar": "دمج الرؤية الحاسوبية مع الإنذار الصوتي لخلق نظام أمني متكامل لحماية الممتلكات والغرف.",
        "sec1_desc_en": "Combining computer vision with audio sirens to build a multi-modal security system.",
        "sec2_title_ar": "2. كشف الدخلاء (Intruder Detection)",
        "sec2_title_en": "2. Intruder Sensing",
        "sec2_desc_ar": "عندما يقترب شخص غريب من الكاميرا ولا يتعرف الموديل عليه، يتم إرسال التنبيه فوراً!",
        "sec2_desc_en": "When an unknown person enters camera view, system immediately raises alerts!",
        "sec3_title_ar": "3. التنبيهات المرئية والصوتية (Visual & Sound Alarms)",
        "sec3_title_en": "3. Multi-Sensory Alarms",
        "sec3_desc_ar": "تتحول شاشة الكاميرا للون الأحمر الساطع مع تشغيل صوت تحذيري عالي 'Warning! Intruder Detected!'.",
        "sec3_desc_en": "Camera screen flashes bright red while sounding a loud warning siren!",
        "lab_title_ar": "محاكي نظام الحراسة التفاعلي (Security Guard Sim)",
        "lab_title_en": "AI Security Guard Simulator",
        "lab_desc_ar": "اضغط زر تفعيل الحراسة واختبر ماذا يحدث عند رصد أي حركة مريبة!",
        "lab_desc_en": "Activate guard mode to test intruder motion alerts live!",
        "code_filename": "ai_security_guard.py",
        "code": """import cv2
import winsound

print("🚨 نظام الحارس الذكي نشط ومستعد للمراقبة...")
print("⚠️ تنبيه: تم رصد حركة مريبة! جاري تشغيل صفارة الإنذار!")""",
        "quiz_q_ar": "ماذا يسمى النظام الذي يدمج الكاميرا والصوت معاً لإنشاء نظام ذكي؟",
        "quiz_q_en": "What is an AI system combining vision and sound called?",
        "quiz_opt1_ar": "Multi-modal AI System",
        "quiz_opt1_en": "Multi-modal AI System",
        "quiz_opt2_ar": "Single Output Code",
        "quiz_opt2_en": "Single Output Code",
        "quiz_correct": 1,
        "hw_ar": "شغل كود الحراسة الذكي على لابتوبك وجرب الدخول لغرفتك واختبر صفارة الإنذار! 🚨",
        "hw_en": "Run your AI guard python code and test your room security siren at home! 🚨"
    },
    {
        "num": 11,
        "title_ar": "ورشة عمل مشروع التخرج (Capstone Workshop)",
        "title_en": "Capstone Project Workshop",
        "subtitle_ar": "تجميع الأفكار وتصميم مشروعك الخاص استعداداً ليوم التخرج! 🛠️🌟",
        "subtitle_en": "Integrating code & preparing your unique project for Demo Day! 🛠️🌟",
        "tag_ar": "السيشن الحادي عشر 🛠️",
        "tag_en": "Session 11 🛠️",
        "agenda_ar": [
            "اختيار الفكرة الحرة لمشروع تخرجك (لعبة، حارس ذكي، مساعد صيدلي... إلخ).",
            "كتابة وتجميع المكتبات بمساعدة المدرب في الورشة.",
            "معالجة المشاكل (Debugging & Testing).",
            "تجربة محاكي قائمة تجهيز المشروع (Checklist).",
            "تجهيز عرض السلايدز للتحدث بثقة أمام أولياء الأمور.",
            "التجهيز النهائي لـ Demo Day!"
        ],
        "agenda_en": [
            "Selecting custom Capstone project ideas.",
            "Code integration & library assembly with instructor support.",
            "Debugging, error handling, and testing.",
            "Interactive Capstone Readiness Checklist Simulator.",
            "Preparing presentation slides for parents showcase.",
            "Final rehearsal for Demo Day!"
        ],
        "sec1_title_ar": "1. اختيار الفكرة المميزة",
        "sec1_title_en": "1. Choosing Your Project Idea",
        "sec1_desc_ar": "كل طالب يختار المشروع الذي أحب تقنيته خلال الكورس ليعكس ابتكاره وشخصيته الفريدة.",
        "sec1_desc_en": "Each student picks a project combining technologies they enjoyed during the course.",
        "sec2_title_ar": "2. الورشة البرمجية الحية (Live Coding & Debugging)",
        "sec2_title_en": "2. Live Coding & Debugging Workshop",
        "sec2_desc_ar": "المدرب يرافق كل طالب للتأكد من أن الكود يعمل بسلاسة وبدون أي أخطاء روتينية.",
        "sec2_desc_en": "Instructors guide each student to ensure clean error-free execution.",
        "sec3_title_ar": "3. مهارات العرض والتقديم (Presentation Skills)",
        "sec3_title_en": "3. Presentation & Public Speaking",
        "sec3_desc_ar": "كيف يقف الطالب بثقة، يشرح فكرة مشروعه، ويستعرض الكود المباشر أمام الحضور في يوم الاحتفال.",
        "sec3_desc_en": "How to stand with confidence, explain AI code logic, and demo projects live to audience.",
        "lab_title_ar": "محاكي جاهزية مشروع التخرج (Capstone Project Readiness)",
        "lab_title_en": "Capstone Readiness Checklist Simulator",
        "lab_desc_ar": "علم على الخيارات لتتحقق من اكتمال مشروعك الجاهز للعرض!",
        "lab_desc_en": "Check off items to verify your project is 100% presentation-ready!",
        "code_filename": "capstone_template.py",
        "code": """# مشروع التخرج البطل - Megaminds AI Capstone Project
print("🌟 أهلاً بكم في عرض مشروع تخرجي للذكاء الاصطناعي!")
print("جاري تشغيل النظام الذكي الخاص بي...")""",
        "quiz_q_ar": "ما هي أهم خطوة قبل تقديم مشروعك في يوم التخرج Demo Day؟",
        "quiz_q_en": "What is the most crucial step before presenting your project on Demo Day?",
        "quiz_opt1_ar": "اختبار الكود جيداً والتأكد من عمل الكاميرا والصوت وتجهيز طريقة الشرح.",
        "quiz_opt1_en": "Testing code thoroughly, checking hardware, and practicing presentation.",
        "quiz_opt2_ar": "مسح الكود وإعادته من الصفر قبل الحفلة بدقيقة.",
        "quiz_opt2_en": "Deleting code and rewriting from scratch 1 minute before event.",
        "quiz_correct": 1,
        "hw_ar": "ضع اللمسات الأخيرة على مشروعك، واطبعه أو احفظه على فلاشة واكتب ملخص الشرح! 🎓",
        "hw_en": "Finalize your project code, save to USB drive, and write presentation notes! 🎓"
    },
    {
        "num": 12,
        "title_ar": "احتفالية يوم التخرج (Demo Day & Graduation)",
        "title_en": "Demo Day & Graduation Ceremony",
        "subtitle_ar": "عروض المشاريع الحية أمام أولياء الأمور وتوزيع الشهادات! 🏆🎓",
        "subtitle_en": "Live student project showcases for parents & certificate ceremony! 🏆🎓",
        "tag_ar": "السيشن الثاني عشر 🏆",
        "tag_en": "Session 12 🏆",
        "agenda_ar": [
            "استقبال أولياء الأمور والترحيب بالحضور الكريم.",
            "العروض المباشرة الحية (Live Student Demos) لكل طالب.",
            "اختبار المشاريع التفاعلية وتصفيق الحضور.",
            "كلمة المدرب وإشادة بأبطال الدفعة.",
            "مراسم توزيع شهادات Junior AI Developer والتصوير التذكاري.",
            "الاحتفال بالانتقال للمستوى القادم!"
        ],
        "agenda_en": [
            "Welcoming parents and guest attendees.",
            "Live student project demonstrations.",
            "Interactive project testing & audience applause.",
            "Instructor keynote & student cohort honors.",
            "Junior AI Developer certificate ceremony & photos.",
            "Celebrating graduation & advancement to next level!"
        ],
        "sec1_title_ar": "1. مرحباً بكم في يوم الإبداع!",
        "sec1_title_en": "1. Welcome to Innovation Day!",
        "sec1_desc_ar": "اليوم هو الحصاد! أولياء الأمور يشاهدون أبناءهم وهم يعرضون مشاريع AI حقيقية قاموا ببنائها بأنفسهم.",
        "sec1_desc_en": "Today is the harvest! Parents watch their children demonstrate real AI applications built from scratch.",
        "sec2_title_ar": "2. العروض المباشرة بثقة (Live Project Presentation)",
        "sec2_title_en": "2. Confident Live Demonstrations",
        "sec2_desc_ar": "كل طالب يعتلي المنصة، يفتح لابتوبه، ويشغل برنامجه الذكي ويعرض كيف يتفاعل مع الصوت أو الكاميرا أو الألعاب.",
        "sec2_desc_en": "Each student steps up to stage, runs their Python AI program, and demonstrates live interaction.",
        "sec3_title_ar": "3. الشهادة والفرص المستقبلية",
        "sec3_title_en": "3. Certification & Future Horizons",
        "sec3_desc_ar": "حصول الطالب على شهادة معتمدة تثبت قدرته على بناء تطبيقات الذكاء الاصطناعي وتجهيزه للمراحل المتقدمة.",
        "sec3_desc_en": "Students receive certified Junior AI Developer credentials preparing them for advanced tracks.",
        "lab_title_ar": "منصة الاحتفال التفاعلية (Graduation Celebration Portal)",
        "lab_title_en": "Graduation Celebration Portal",
        "lab_desc_ar": "اضغط على زر إطلاق الألعاب النارية والاحتفال بتخرج أبطال الذكاء الاصطناعي!",
        "lab_desc_en": "Click the fireworks button to celebrate our Junior AI Developer graduates!",
        "code_filename": "graduation_celebration.py",
        "code": """print("🎉 ألف مبروك لتخرج أبطال مهندسي الذكاء الاصطناعي الصغار في Megaminds!")
print("📜 شهادة المطور الصغير المعتمد جاهزة للتسليم!")
print("🚀 نتمنى لكم رحلة مستقبلية مليئة بالابتكار والنجاح!")""",
        "quiz_q_ar": "ماذا أصبح الطالب قادر على فعله بعد إتمام هذا الكورس التفاعلي؟",
        "quiz_q_en": "What can students build after completing this interactive AI course?",
        "quiz_opt1_ar": "بناء تطبيقات ومساعدات ذكاء اصطناعي تفاعلية بنفسه بـ Python وتحكم الكاميرا والصوت.",
        "quiz_opt1_en": "Build interactive Python AI apps, voice assistants, & vision controls independently.",
        "quiz_opt2_ar": "مجرد نقل الأكواد دون فهم.",
        "quiz_opt2_en": "Just copy-pasting code without understanding.",
        "quiz_correct": 1,
        "hw_ar": "احتفل بنجاحك مع عائلتك وشارك صور وفيديوهات مشروعك بكل فخر! 📸🎓✨",
        "hw_en": "Celebrate your graduation with family and proudly share your project video! 📸🎓✨"
    }
]

html_template = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Megaminds AI - Session {session_num}</title>
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
        
        /* Language visibility controls */
        html[lang="ar"] .lang-en {{ display: none !important; }}
        html[lang="ar"] .lang-ar {{ display: inline !important; }}
        html[lang="ar"] div.lang-ar, html[lang="ar"] p.lang-ar, html[lang="ar"] h1.lang-ar, html[lang="ar"] h2.lang-ar, html[lang="ar"] h3.lang-ar, html[lang="ar"] h4.lang-ar {{ display: block !important; }}

        html[lang="en"] .lang-ar {{ display: none !important; }}
        html[lang="en"] .lang-en {{ display: inline !important; }}
        html[lang="en"] div.lang-en, html[lang="en"] p.lang-en, html[lang="en"] h1.lang-en, html[lang="en"] h2.lang-en, html[lang="en"] h3.lang-en, html[lang="en"] h4.lang-en {{ display: block !important; }}
        
        html[lang="en"] .quiz-opt {{ text-align: left !important; }}
        html[lang="ar"] .quiz-opt {{ text-align: right !important; }}

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
        .nav-links {{ display: flex; align-items: center; gap: 15px; }}
        .nav-btn {{
            background: rgba(56, 189, 248, 0.1); color: var(--accent-cyan); border: 1px solid rgba(56, 189, 248, 0.3);
            padding: 8px 18px; border-radius: 10px; text-decoration: none; font-weight: 700; font-size: 0.95rem; transition: all 0.3s ease;
        }}
        .nav-btn:hover {{ background: var(--accent-cyan); color: #000; transform: translateY(-2px); }}
        
        .lang-btn {{
            background: linear-gradient(90deg, var(--accent-purple), var(--accent-cyan));
            color: white; border: none; padding: 8px 18px; border-radius: 10px; font-weight: 800; font-size: 0.95rem; cursor: pointer; transition: all 0.3s ease; box-shadow: 0 4px 12px rgba(168, 85, 247, 0.3);
        }}
        .lang-btn:hover {{ transform: scale(1.05); box-shadow: 0 6px 18px rgba(56, 189, 248, 0.4); }}
        
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
        .quiz-opt {{ display: block; width: 100%; background: rgba(30, 41, 59, 0.7); border: 1px solid var(--card-border); color: var(--text-main); padding: 14px 20px; border-radius: 12px; margin-bottom: 10px; font-size: 1.05rem; cursor: pointer; transition: all 0.2s ease; }}
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
            <button class="lang-btn" onclick="toggleLanguage()"><i class="fa-solid fa-globe"></i> <span id="langBtnLabel">English</span></button>
            <a href="index.html" class="nav-btn">
                <span class="lang-ar"><i class="fa-solid fa-house"></i> الرئيسية</span>
                <span class="lang-en"><i class="fa-solid fa-house"></i> Home</span>
            </a>
            <span style="color: var(--text-muted); font-weight: bold;">
                <span class="lang-ar">السيشن {session_num} / 12</span>
                <span class="lang-en">Session {session_num} / 12</span>
            </span>
        </div>
    </nav>

    <div class="container">

        <div class="hero">
            <span class="session-tag">
                <span class="lang-ar">{tag_ar}</span>
                <span class="lang-en">{tag_en}</span>
            </span>
            <h1>
                <span class="lang-ar">{title_ar}</span>
                <span class="lang-en">{title_en}</span>
            </h1>
            <p>
                <span class="lang-ar">{subtitle_ar}</span>
                <span class="lang-en">{subtitle_en}</span>
            </p>
        </div>

        <div class="agenda-card">
            <div class="agenda-title">
                <i class="fa-solid fa-list-check"></i>
                <span class="lang-ar">جدول أعمال اليوم (ماذا سنأخذ في هذه الحصة؟)</span>
                <span class="lang-en">Today's Agenda (What will we cover today?)</span>
            </div>
            <div class="agenda-grid">
                {agenda_html}
            </div>
        </div>

        <div class="section-block">
            <div class="section-header">
                <div class="section-icon"><i class="fa-solid fa-graduation-cap"></i></div>
                <div>
                    <h2>
                        <span class="lang-ar">{sec1_title_ar}</span>
                        <span class="lang-en">{sec1_title_en}</span>
                    </h2>
                </div>
            </div>
            <p style="font-size: 1.15rem;">
                <span class="lang-ar">{sec1_desc_ar}</span>
                <span class="lang-en">{sec1_desc_en}</span>
            </p>
        </div>

        <div class="section-block">
            <div class="section-header">
                <div class="section-icon" style="background: rgba(56, 189, 248, 0.15); color: var(--accent-cyan);"><i class="fa-solid fa-lightbulb"></i></div>
                <div>
                    <h2>
                        <span class="lang-ar">{sec2_title_ar}</span>
                        <span class="lang-en">{sec2_title_en}</span>
                    </h2>
                </div>
            </div>
            <p style="font-size: 1.15rem;">
                <span class="lang-ar">{sec2_desc_ar}</span>
                <span class="lang-en">{sec2_desc_en}</span>
            </p>
        </div>

        <div class="section-block">
            <div class="section-header">
                <div class="section-icon" style="background: rgba(249, 115, 22, 0.15); color: var(--accent-orange);"><i class="fa-solid fa-layer-group"></i></div>
                <div>
                    <h2>
                        <span class="lang-ar">{sec3_title_ar}</span>
                        <span class="lang-en">{sec3_title_en}</span>
                    </h2>
                </div>
            </div>
            <p style="font-size: 1.15rem;">
                <span class="lang-ar">{sec3_desc_ar}</span>
                <span class="lang-en">{sec3_desc_en}</span>
            </p>
        </div>

        <div class="section-block">
            <div class="section-header">
                <div class="section-icon" style="background: rgba(34, 197, 94, 0.15); color: var(--accent-green);"><i class="fa-solid fa-flask"></i></div>
                <div>
                    <h2>
                        <span class="lang-ar">التجربة العملية التفاعلية المباشرة 🧪</span>
                        <span class="lang-en">Live Interactive Hands-on Lab 🧪</span>
                    </h2>
                </div>
            </div>

            <div class="lab-box">
                <h3 style="font-size: 1.4rem; color: white; margin-bottom: 10px;">
                    <span class="lang-ar">{lab_title_ar}</span>
                    <span class="lang-en">{lab_title_en}</span>
                </h3>
                <p style="color: var(--text-muted); max-width: 600px; margin: 0 auto;">
                    <span class="lang-ar">{lab_desc_ar}</span>
                    <span class="lang-en">{lab_desc_en}</span>
                </p>
                
                <div style="margin-top: 20px; display: flex; justify-content: center; gap: 10px; flex-wrap: wrap;">
                    <input type="text" id="userInputText" placeholder="اكتب هنا لتجربة المعمل التفاعلي / Type here for live lab..." style="width: 70%; max-width: 450px; padding: 14px 20px; border-radius: 12px; border: 1px solid var(--accent-cyan); background: #0f172a; color: white; font-size: 1.1rem; outline: none;">
                    <button class="lab-btn" onclick="runSim()"><i class="fa-solid fa-play"></i> 
                        <span class="lang-ar">تشغيل التجربة</span>
                        <span class="lang-en">Run Lab</span>
                    </button>
                </div>

                <div class="demo-result-box" id="resultDisplay">
                    <span class="lang-ar">✨ في انتظار مدخلاتك واختبار النظام الذكي...</span>
                    <span class="lang-en">✨ Awaiting your input to test AI live...</span>
                </div>
            </div>
        </div>

        <div class="section-block">
            <div class="section-header">
                <div class="section-icon"><i class="fa-brands fa-python"></i></div>
                <div>
                    <h2>
                        <span class="lang-ar">تطبيق الكود بـ Python 🐍</span>
                        <span class="lang-en">Python Code Implementation 🐍</span>
                    </h2>
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
                    <h2>
                        <span class="lang-ar">اختبر معلوماتك (تحدي السيشن) 🧩</span>
                        <span class="lang-en">Test Your Knowledge (Session Quiz) 🧩</span>
                    </h2>
                </div>
            </div>

            <div class="quiz-container">
                <div class="quiz-q">
                    <span class="lang-ar">{quiz_q_ar}</span>
                    <span class="lang-en">{quiz_q_en}</span>
                </div>
                <button class="quiz-opt" onclick="checkAnswer(this, {quiz_opt1_correct})">
                    <span class="lang-ar">{quiz_opt1_ar}</span>
                    <span class="lang-en">{quiz_opt1_en}</span>
                </button>
                <button class="quiz-opt" onclick="checkAnswer(this, {quiz_opt2_correct})">
                    <span class="lang-ar">{quiz_opt2_ar}</span>
                    <span class="lang-en">{quiz_opt2_en}</span>
                </button>
            </div>
        </div>

        <div class="hw-card">
            <div class="hw-title">
                <i class="fa-solid fa-rocket"></i>
                <span class="lang-ar">واجب السيشن والمشروع الممتع في البيت 🏠</span>
                <span class="lang-en">Session Homework & Home Project 🏠</span>
            </div>
            <p style="font-size: 1.1rem; color: #f1f5f9; margin-bottom: 12px;">
                <span class="lang-ar">{hw_ar}</span>
                <span class="lang-en">{hw_en}</span>
            </p>
        </div>

        <div class="footer-navigation">
            <a href="{prev_link}" class="nav-link-btn">
                <i class="fa-solid fa-arrow-right"></i>
                <span class="lang-ar">{prev_text_ar}</span>
                <span class="lang-en">{prev_text_en}</span>
            </a>
            <a href="{next_link}" class="nav-link-btn primary">
                <span class="lang-ar">{next_text_ar}</span>
                <span class="lang-en">{next_text_en}</span>
                <i class="fa-solid fa-arrow-left"></i>
            </a>
        </div>

    </div>

    <script>
        function toggleLanguage() {{
            const currentLang = document.documentElement.lang || 'ar';
            const newLang = (currentLang === 'ar') ? 'en' : 'ar';
            setLanguage(newLang);
        }}

        function setLanguage(lang) {{
            document.documentElement.lang = lang;
            document.documentElement.dir = (lang === 'ar') ? 'rtl' : 'ltr';
            localStorage.setItem('megaminds_lang', lang);
            
            const btnLabel = document.getElementById('langBtnLabel');
            if (btnLabel) {{
                btnLabel.innerText = (lang === 'ar') ? 'English' : 'العربية';
            }}
        }}

        document.addEventListener('DOMContentLoaded', () => {{
            const savedLang = localStorage.getItem('megaminds_lang') || 'ar';
            setLanguage(savedLang);
        }});

        function runSim() {{
            const input = document.getElementById('userInputText').value.trim();
            const resultBox = document.getElementById('resultDisplay');
            const isAr = (document.documentElement.lang === 'ar');
            
            if (!input) {{
                resultBox.innerHTML = isAr ? "⚠️ أدخل نصاً أو أمراً أولاً في الصندوق!" : "⚠️ Please enter text or a command first!";
                resultBox.style.color = "#f97316";
                return;
            }}
            resultBox.innerHTML = isAr ? "🧠 جاري تنفيذ التجربة التفاعلية بواسطة الذكاء الاصطناعي..." : "🧠 Running live AI interactive simulation...";
            resultBox.style.color = "#38bdf8";
            setTimeout(() => {{
                resultBox.innerHTML = isAr 
                    ? `✅ تم التنفيذ بنجاح! المدخل: "${{input}}" ➔ النتيجة: تم الاستجابة وتوليد النمط الذكي المطلوبة! 🎉`
                    : `✅ Success! Input: "${{input}}" ➔ Result: AI pattern response generated! 🎉`;
                resultBox.style.color = "#22c55e";
            }}, 600);
        }}

        function checkAnswer(button, isCorrect) {{
            const parent = button.parentElement;
            const options = parent.querySelectorAll('.quiz-opt');
            const isAr = (document.documentElement.lang === 'ar');

            options.forEach(opt => {{ opt.disabled = true; opt.style.cursor = 'default'; }});
            if (isCorrect) {{
                button.classList.add('correct');
                button.innerHTML += isAr ? '  ✅ (إجابة صحيحة بطل!)' : '  ✅ (Correct Answer!)';
            }} else {{
                button.classList.add('wrong');
                button.innerHTML += isAr ? '  ❌ (حاول مرة أخرى)' : '  ❌ (Try Again)';
            }}
        }}
    </script>
</body>
</html>
"""

target_dir = r"c:\Users\rowan\Desktop\editcurr"

for i, s in enumerate(sessions_data, start=1):
    agenda_items = ""
    for idx in range(len(s["agenda_ar"])):
        item_ar = s["agenda_ar"][idx]
        item_en = s["agenda_en"][idx]
        agenda_items += f"""
        <div class="agenda-item">
            <div class="agenda-num">{idx+1}</div>
            <div class="agenda-text">
                <span class="lang-ar">{item_ar}</span>
                <span class="lang-en">{item_en}</span>
            </div>
        </div>
        """
        
    prev_link = f"session{i-1}.html" if i > 1 else "index.html"
    prev_text_ar = f"السيشن {i-1}" if i > 1 else "الرئيسية"
    prev_text_en = f"Session {i-1}" if i > 1 else "Home"

    next_link = f"session{i+1}.html" if i < 12 else "index.html"
    next_text_ar = f"السيشن {i+1}" if i < 12 else "الرئيسية"
    next_text_en = f"Session {i+1}" if i < 12 else "Home"

    quiz_opt1_correct = "true" if s["quiz_correct"] == 1 else "false"
    quiz_opt2_correct = "true" if s["quiz_correct"] == 2 else "false"
    
    rendered_html = html_template.format(
        session_num=s["num"],
        title_ar=s["title_ar"],
        title_en=s["title_en"],
        subtitle_ar=s["subtitle_ar"],
        subtitle_en=s["subtitle_en"],
        tag_ar=s["tag_ar"],
        tag_en=s["tag_en"],
        agenda_html=agenda_items,
        sec1_title_ar=s["sec1_title_ar"],
        sec1_title_en=s["sec1_title_en"],
        sec1_desc_ar=s["sec1_desc_ar"],
        sec1_desc_en=s["sec1_desc_en"],
        sec2_title_ar=s["sec2_title_ar"],
        sec2_title_en=s["sec2_title_en"],
        sec2_desc_ar=s["sec2_desc_ar"],
        sec2_desc_en=s["sec2_desc_en"],
        sec3_title_ar=s["sec3_title_ar"],
        sec3_title_en=s["sec3_title_en"],
        sec3_desc_ar=s["sec3_desc_ar"],
        sec3_desc_en=s["sec3_desc_en"],
        lab_title_ar=s["lab_title_ar"],
        lab_title_en=s["lab_title_en"],
        lab_desc_ar=s["lab_desc_ar"],
        lab_desc_en=s["lab_desc_en"],
        code_filename=s["code_filename"],
        code=s["code"],
        quiz_q_ar=s["quiz_q_ar"],
        quiz_q_en=s["quiz_q_en"],
        quiz_opt1_ar=s["quiz_opt1_ar"],
        quiz_opt1_en=s["quiz_opt1_en"],
        quiz_opt2_ar=s["quiz_opt2_ar"],
        quiz_opt2_en=s["quiz_opt2_en"],
        quiz_opt1_correct=quiz_opt1_correct,
        quiz_opt2_correct=quiz_opt2_correct,
        hw_ar=s["hw_ar"],
        hw_en=s["hw_en"],
        prev_link=prev_link,
        prev_text_ar=prev_text_ar,
        prev_text_en=prev_text_en,
        next_link=next_link,
        next_text_ar=next_text_ar,
        next_text_en=next_text_en
    )
    
    filepath = os.path.join(target_dir, f"session{i}.html")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(rendered_html)
    print(f"Generated Bilingual {filepath}")
