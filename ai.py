import os

artifact_dir = r'C:\Users\rowan\.gemini\antigravity\brain\aa53095d-7d4b-4093-96e9-dfc4f3516d88'

sessions_data = [
    {
        "num": 1,
        "title": "عالم الذكاء الاصطناعي - من مستهلك إلى صانع 🤖✨",
        "slides": [
            {"title": "رحلتك للتحكم في الذكاء الاصطناعي 🤖", "content": "من مجرد مستخدم للتطبيقات إلى مبتكر ومهندس يبني الذكاء الاصطناعي بنفسه.", "code": "Traditional Programming vs Machine Learning"},
            {"title": "كيف تفكر البرامج العادية؟ 💻", "content": "تعتمد على كتابة قواعد صريحة (If / Else). إذا ظهر تغيير لم يتوقعه المبرمج يفشل البرنامج!", "code": "[Inputs] + [Explicit Rules] ➔ [Outputs]"},
            {"title": "وكيف يفكر الذكاء الاصطناعي؟ 🧠", "content": "نغذي الحاسوب ببيانات وأمثلة كثيرة وهو يستنتج النمط والقواعد بنفسه!", "code": "[Big Data + Examples] ➔ [AI Pattern Learning] ➔ [Model]"},
            {"title": "تجربة اليوم 🧪", "content": "بناء موديل يقرأ مشاعرك وتصميم أول مساعد ذكاء اصطناعي تفاعلي بـ Python!", "code": "Google Teachable Machine + Sentiment Assistant"}
        ]
    },
    {
        "num": 2,
        "title": "Generative AI & Prompt Engineering 🎨✍️",
        "slides": [
            {"title": "الذكاء الاصطناعي التوليدي 🎨", "content": "كيف تجعل الكمبيوتر يرسم ويكتب أفكارك وخيالاتك دون أن ترسمها بيدك؟", "code": "Generative AI vs Discriminative AI"},
            {"title": "قواعد هندسة الأوامر (Prompt Engineering) 🎯", "content": "تعلم قاعدة C-T-C (Context, Task, Constraint) للحصول على أفضل النتائج!", "code": "Context + Task + Constraints = Professional Prompt"},
            {"title": "تحدي اليوم 🏆", "content": "تحدي الـ Prompt Battles وبناء مولد قصص خيالية ذكي بـ Python!", "code": "python generate_ai_story(hero, setting, enemy)"}
        ]
    },
    {
        "num": 3,
        "title": "بناء الشات بوت الذكي (AI Chatbot) 💬🤖",
        "slides": [
            {"title": "كيف تعمل الشات بوتات؟ 💬", "content": "فهم النية (Intent Recognition) وقراءة الكلمات المفتاحية في جملة المستخدم.", "code": "User Pattern ➔ Pattern Matching ➔ AI Response"},
            {"title": "تخيل شجرة الردود (Intent Tree) 🌳", "content": "تصميم قاعدة معرفة تحوي التحيات، الاستفسارات، والدعم الآلي.", "code": "knowledge_base = {'greetings': {...}, 'academy': {...}}"},
            {"title": "تطبيق اليوم 💻", "content": "بناء Megaminds Custom AI Chatbot يتفاعل معك بـ Python!", "code": "while True: message = input('أنت: ')"}
        ]
    },
    {
        "num": 4,
        "title": "الصوت والذكاء الاصطناعي (Audio AI - Siri Clone) 🎙️🔊",
        "slides": [
            {"title": "كيف يسمع ويفتح الكمبيوتر؟ 🎙️", "content": "تحويل الموجات الصوتية إلى نصوص وتحويل النصوص إلى صوت متكلم (TTS).", "code": "SpeechToText + TextToSpeech (pyttsx3)"},
            {"title": "بناء المساعد الصوتي 🔊", "content": "برمجة مساعدك الصوتي الخاص ليجيبك بصوته ويفتح مواقعك المفضلة!", "code": "speak('أهلاً بك في Megaminds Voice Assistant')"},
            {"title": "تحدي اليوم 🚀", "content": "إضافة أوامر صوتية تفتح يوتيوب وجوجل وتخبرك بالوقت الحقيقي!", "code": "webbrowser.open('https://youtube.com')"}
        ]
    },
    {
        "num": 5,
        "title": "أساسيات الرؤية الحاسوبية (OpenCV Filters) 📸👁️",
        "slides": [
            {"title": "كيف يرى الحاسوب الصور؟ 👁️", "content": "الصور عبارة عن مصفوفات من الأرقام والـ Pixels وقيم ألوان RGB.", "code": "Pixels (Red, Green, Blue) Array Grid"},
            {"title": "فتح كاميرا اللابتوب 📸", "content": "التقاط البث المباشر وقراءة الصور إطاراً بإطار (Frames).", "code": "cap = cv2.VideoCapture(0)"},
            {"title": "إضافة الفلاتر السحرية 🪄", "content": "تحويل الكاميرا لألوان رمادية وتحديد الحواف بفلتر Canny!", "code": "cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)"}
        ]
    },
    {
        "num": 6,
        "title": "دمج النماذج مع Python (Teachable + OpenCV) 🎯💻",
        "slides": [
            {"title": "من الويب إلى Python 🌐➔🐍", "content": "تصدير نموذج الذكاء الاصطناعي وتشغيله داخل كود Python محلياً.", "code": "Export Keras / TensorFlow Model"},
            {"title": "التعرف المباشر على الأغراض 📱", "content": "جعل الكاميرا تتعرف على أغراضك الشخصية وتكتب اسمها بدقة عالية!", "code": "AI Detected: Mobile Phone (94%)"},
            {"title": "تحدي اليوم 🏆", "content": "تصميم نظام تنبيه ذكي عند رصد غرض معين أمام الكاميرا!", "code": "if confidence > 0.9: trigger_alarm()"}
        ]
    },
    {
        "num": 7,
        "title": "الذكاء الاصطناعي في الألعاب (Rock Paper Scissors AI) 🎮✊",
        "slides": [
            {"title": "كيف يلعب الـ AI ضد الإنسان؟ 🎮", "content": "التعرف على إيماءات اليد (Gestures) واتخاذ القرار المناسب.", "code": "Rock ✊ | Paper ✋ | Scissors ✌️"},
            {"title": "بناء حلبة المنافسة ⚔️", "content": "جعل الكمبيوتر يختار حركته ويقارنها بحركتك ويحسب النقاط تلقائياً!", "code": "determine_winner(player_choice, ai_choice)"},
            {"title": "بطولة القاعة 🏆", "content": "تحدي الطلاب لبعضهم وللـ AI ومعرفة من سيهزم الآلة!", "code": "Player Score vs AI Score"}
        ]
    },
    {
        "num": 8,
        "title": "التحكم بالكمبيوتر بحركات اليد (Gesture Control) 🕹️🖐️",
        "slides": [
            {"title": "التحكم بدون لمس! 🖐️", "content": "ربط الرؤية الحاسوبية بمحاكاة الضغط على أسهم الكيبورد.", "code": "Camera Vision ➔ PyAutoGUI KeyPress"},
            {"title": "مكتبة PyAutoGUI ⌨️", "content": "إرسال أوامر تحريك الماوس والضغط على الأسهم برمجياً.", "code": "pyautogui.press('left') / pyautogui.press('up')"},
            {"title": "لعب لعبة كاملة بإشارة يدك 🏎️", "content": "تشغيل لعبة سباق سيارات والتحكم فيها بيدك أمام الكاميرا!", "code": "simulate_hand_gesture_control('JUMP')"}
        ]
    },
    {
        "num": 9,
        "title": "المساعد الصوتي والمكتبي الشامل (Desktop Assistant) 🖥️🤖",
        "slides": [
            {"title": "المساعد الشخصي الذكي 🖥️", "content": "دمج برامج النظام وأوامر الصوت في تطبيق ذكي واحد لمكتبك.", "code": "Megaminds Personal Desktop Assistant"},
            {"title": "التحكم في النظام ⚙️", "content": "فتح الآلة الحاسبة، النوت باد، وقراءة الوقت بـ Python.", "code": "os.system('calc') / os.system('notepad')"},
            {"title": "تطوير المساعد 🚀", "content": "تخصيص الردود والترحيب بكل فرد في عائلتك!", "code": "execute_user_command(command)"}
        ]
    },
    {
        "num": 10,
        "title": "حارس الغرفة والمكتب الذكي (Smart AI Security Guard) 🚨🛡️",
        "slides": [
            {"title": "الأنظمة التفاعلية المتكاملة 🚨", "content": "دمج الكاميرا والصوت لرصد أي حركة غريبة وإطلاق التنبيهات.", "code": "Multi-modal AI: Vision + Audio Alarm"},
            {"title": "كود نظام الحراسة 🛡️", "content": "مراقبة البث المباشر وتلوين الشاشة بالأحمر عند رصد حركة مريبة!", "code": "SYSTEM: ACTIVE GUARD MODE 🚨"},
            {"title": "التحدي 🏆", "content": "تأمين غرفتك الخاصة في البيت بنظامك الذكي الجديد!", "code": "Trigger Audio Warning on Intruder"}
        ]
    },
    {
        "num": 11,
        "title": "ورشة عمل مشروع التخرج (Capstone Project Workshop) 🛠️🌟",
        "slides": [
            {"title": "اختيار الفكرة الحرة 💡", "content": "اختيار فكرة مشروعك الخاص (لعبة، حارس ذكي، مساعد شخصي).", "code": "Student Unique AI Capstone Project"},
            {"title": "التصميم والبرمجة 💻", "content": "كتابة الأكواد وتجميع المكتبات بمساعدة المدرب في الورشة.", "code": "Code + Integration + Testing"},
            {"title": "التجهيز لـ Demo Day 🎓", "content": "تجهيز السلايدز واختبار المشروع حي قبل يوم التخرج السعيد!", "code": "Prepare Presentation & Live Demo"}
        ]
    },
    {
        "num": 12,
        "title": "احتفالية يوم التخرج (Demo Day & Graduation) 🏆🎓",
        "slides": [
            {"title": "أهلاً بأولياء الأمور 🌟", "content": "مرحباً بكم في يوم عرض إبداعات ومشاريع أبطال المستقبل!", "code": "Megaminds AI Graduation Demo Day"},
            {"title": "العروض الحية (Live Student Demos) 🎤", "content": "كل طالب يقدم مشروعه المباشر ويختبر الأكواد أمام الجميع بثقة!", "code": "Live Code Showcase & Interactive Demo"},
            {"title": "توزيع الشهادات 📜", "content": "تكريم أبطال الدفعة وتوزيع شهادات Junior AI Developer!", "code": "Certificates Ceremony & Celebration 📸"}
        ]
    }
]

html_template = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Megaminds AI - Session {session_num}</title>
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;900&display=swap" rel="stylesheet">
    <style>
        :root {{
            --primary-cyan: #4EB8D6;
            --primary-dark: #1E293B;
            --accent-orange: #F27346;
            --bg-ice: #E3F0F5;
            --card-white: #FFFFFF;
        }}
        * {{ box-sizing: border-box; margin: 0; padding: 0; font-family: 'Cairo', sans-serif; }}
        body {{ background-color: #0f172a; color: var(--primary-dark); display: flex; justify-content: center; align-items: center; min-height: 100vh; overflow: hidden; }}
        .slide-container {{ width: 90vw; max-width: 1200px; height: 85vh; max-height: 700px; background: var(--bg-ice); border-radius: 24px; box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5); position: relative; overflow: hidden; display: flex; flex-direction: column; }}
        .header-bar {{ background: var(--card-white); padding: 15px 30px; display: flex; justify-content: space-between; align-items: center; border-bottom: 4px solid var(--primary-cyan); }}
        .logo {{ font-weight: 900; font-size: 1.4rem; color: var(--primary-dark); }}
        .logo span {{ color: var(--accent-orange); }}
        .slide-badge {{ background: var(--primary-cyan); color: white; padding: 4px 16px; border-radius: 20px; font-size: 0.9rem; font-weight: 700; }}
        .slide-content {{ flex: 1; padding: 40px; display: none; flex-direction: column; justify-content: center; animation: fadeIn 0.4s ease-in-out; }}
        .slide-content.active {{ display: flex; }}
        @keyframes fadeIn {{ from {{ opacity: 0; transform: translateY(10px); }} to {{ opacity: 1; transform: translateY(0); }} }}
        h1 {{ font-size: 2.2rem; color: var(--primary-dark); margin-bottom: 15px; font-weight: 900; }}
        h2 {{ font-size: 1.8rem; color: var(--primary-dark); margin-bottom: 20px; }}
        p {{ font-size: 1.25rem; line-height: 1.7; color: #334155; margin-bottom: 20px; }}
        .card {{ background: var(--card-white); padding: 25px; border-radius: 16px; border-top: 5px solid var(--accent-orange); box-shadow: 0 10px 15px -3px rgba(0,0,0,0.05); margin-top: 15px; }}
        .code-box {{ background: #1e293b; color: #38bdf8; direction: ltr; text-align: left; padding: 20px; border-radius: 12px; font-family: monospace; font-size: 1.1rem; margin-top: 15px; }}
        .footer-nav {{ background: var(--card-white); padding: 15px 30px; display: flex; justify-content: space-between; align-items: center; border-top: 1px solid #cbd5e1; }}
        .nav-btn {{ background: var(--primary-cyan); color: white; border: none; padding: 10px 24px; border-radius: 12px; font-weight: 700; font-size: 1rem; cursor: pointer; transition: all 0.2s ease; }}
        .nav-btn:hover {{ background: #3ba3c0; transform: translateY(-2px); }}
        .nav-btn.secondary {{ background: var(--accent-orange); }}
        .nav-btn.secondary:hover {{ background: #e05e32; }}
        .nav-btn:disabled {{ background: #cbd5e1; cursor: not-allowed; transform: none; }}
        .slide-counter {{ font-weight: 700; color: #64748b; }}
        .home-link {{ text-decoration: none; color: var(--primary-cyan); font-weight: 700; margin-right: 15px; }}
    </style>
</head>
<body>

    <div class="slide-container">
        <div class="header-bar">
            <div class="logo">MEGAMINDS <span>ACADEMY</span></div>
            <div>
                <a href="index.html" class="home-link">🏠 القائمة الرئيسية</a>
                <span class="slide-badge">Session {session_num}</span>
            </div>
        </div>

        {slides_html}

        <div class="footer-nav">
            <button class="nav-btn" id="prevBtn" onclick="changeSlide(-1)" disabled>السابقة ➔</button>
            <div class="slide-counter" id="slideCounter">الشريحة 1 من {total_slides}</div>
            <button class="nav-btn secondary" id="nextBtn" onclick="changeSlide(1)">التالية ⬅</button>
        </div>
    </div>

    <script>
        let currentSlide = 1;
        const totalSlides = {total_slides};

        function changeSlide(direction) {{
            document.getElementById(`slide-${{currentSlide}}`).classList.remove('active');
            currentSlide += direction;
            
            if (currentSlide < 1) currentSlide = 1;
            if (currentSlide > totalSlides) currentSlide = totalSlides;

            document.getElementById(`slide-${{currentSlide}}`).classList.add('active');
            
            document.getElementById('prevBtn').disabled = (currentSlide === 1);
            document.getElementById('nextBtn').disabled = (currentSlide === totalSlides);
            
            document.getElementById('slideCounter').innerText = `الشريحة ${{currentSlide}} من ${{totalSlides}}`;
        }}

        document.addEventListener('keydown', (e) => {{
            if (e.key === 'ArrowRight' || e.key === 'PageUp') changeSlide(-1);
            if (e.key === 'ArrowLeft' || e.key === 'PageDown' || e.key === 'Space') changeSlide(1);
        }});
    </script>
</body>
</html>
"""

for sess in sessions_data:
    s_num = sess["num"]
    s_title = sess["title"]
    slides = sess["slides"]
    
    slides_code = ""
    for idx, slide in enumerate(slides, start=1):
        active_cls = "active" if idx == 1 else ""
        slides_code += f"""
        <div class="slide-content {active_cls}" id="slide-{idx}">
            <h1>{slide['title']}</h1>
            <p>{slide['content']}</p>
            <div class="card">
                <h3>💡 النقطة الأساسية</h3>
                <div class="code-box">{slide['code']}</div>
            </div>
        </div>
        """
        
    final_html = html_template.format(
        session_num=s_num,
        slides_html=slides_code,
        total_slides=len(slides)
    )
    
    filename = os.path.join(artifact_dir, f"session{s_num}.html")
    with open(filename, "w", encoding="utf-8") as f:
        f.write(final_html)
    print(f"Generated {filename}")

# Generate index.html launch hub
hub_html = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Megaminds AI Curriculum Hub</title>
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;900&display=swap" rel="stylesheet">
    <style>
        body { font-family: 'Cairo', sans-serif; background: #0f172a; color: white; padding: 40px; }
        .container { max-width: 1100px; margin: 0 auto; }
        h1 { color: #4EB8D6; text-align: center; margin-bottom: 10px; font-size: 2.5rem; }
        p.subtitle { text-align: center; color: #94a3b8; margin-bottom: 40px; font-size: 1.2rem; }
        .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 20px; }
        .card { background: #1e293b; border-radius: 16px; padding: 25px; border-top: 5px solid #4EB8D6; transition: all 0.3s ease; text-decoration: none; color: white; display: flex; flex-direction: column; justify-content: space-between; }
        .card:hover { transform: translateY(-5px); border-top-color: #F27346; box-shadow: 0 15px 30px rgba(0,0,0,0.4); }
        .card h3 { font-size: 1.3rem; margin-bottom: 10px; color: #38bdf8; }
        .card p { font-size: 0.95rem; color: #cbd5e1; line-height: 1.5; }
        .btn { background: #F27346; color: white; padding: 8px 16px; border-radius: 8px; font-weight: 700; text-align: center; margin-top: 15px; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Megaminds AI Curriculum Presentation Hub 🚀</h1>
        <p class="subtitle">انقر على أي سيشن لفتح العرض التفاعلي الشرائحي المباشر (Sessions 1 - 12)</p>
        <div class="grid">
"""

for sess in sessions_data:
    s_num = sess["num"]
    s_title = sess["title"]
    hub_html += f"""
            <a href="session{s_num}.html" class="card">
                <div>
                    <h3>Session {s_num}</h3>
                    <p>{s_title}</p>
                </div>
                <div class="btn">افتح العرض ➔</div>
            </a>
    """

hub_html += """
        </div>
    </div>
</body>
</html>
"""

hub_filename = os.path.join(artifact_dir, "index.html")
with open(hub_filename, "w", encoding="utf-8") as f:
    f.write(hub_html)
print(f"Generated Hub {hub_filename}")