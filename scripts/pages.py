"""Page data for scripts/build.py.

Every fact about another app must trace to that provider's own page, listed in
the page's `sources`. Where a provider does not state something, the copy says
so instead of guessing.
"""
from build_helpers import table

UPDATED = "2026-09-19"
UPDATED_LABEL = "September 19, 2026"

SRC = {
    "calai": ("Cal AI website", "https://www.calai.app/"),
    "calai_store": ("Cal AI on the App Store", "https://apps.apple.com/us/app/cal-ai-calorie-tracker/id6480417616"),
    "snap": ("SnapCalorie website", "https://www.snapcalorie.com/"),
    "snap_faq": ("SnapCalorie FAQ", "https://www.snapcalorie.com/faq.html"),
    "snap_store": ("SnapCalorie on the App Store", "https://apps.apple.com/us/app/snapcalorie-ai-calorie-counter/id1574239307"),
    "mf": ("MacroFactor website", "https://macrofactor.com/macrofactor/"),
    "mf_store": ("MacroFactor on the App Store", "https://apps.apple.com/us/app/macrofactor-macro-tracker/id1553503471"),
    "mf_vs": ("MacroFactor on its photo logging and nutrient coverage", "https://macrofactor.com/macrofactor-vs-cal-ai/"),
    "crono_gold": ("Cronometer Gold", "https://cronometer.com/gold/"),
    "crono_photo": ("Cronometer Photo Log", "https://cronometer.com/blog/photo-logging/"),
    "crono_coach": ("Cronometer Crono Coach help article", "https://support.cronometer.com/hc/en-us/articles/49995994334100-Mobile-Crono-Coach"),
    "crono_store": ("Cronometer on the App Store", "https://apps.apple.com/us/app/cronometer-calorie-counter/id1145935738"),
    "mfp_premium": ("MyFitnessPal Premium", "https://www.myfitnesspal.com/premium"),
    "mfp_store": ("MyFitnessPal on the App Store", "https://apps.apple.com/us/app/myfitnesspal-calorie-counter/id341232718"),
    "mfp_coach": ("MyFitnessPal Nutrition Coach help article", "https://support.myfitnesspal.com/hc/en-us/articles/45212266254221-Introducing-Nutrition-Coach-Your-Nutrition-A"),
    "fitia": ("Fitia website", "https://fitia.app/en/"),
    "fitia_premium": ("Fitia Premium", "https://fitia.app/premium/"),
    "fitia_store": ("Fitia on the App Store", "https://apps.apple.com/us/app/fitia-calorie-counter-diet/id1448277011"),
    "welling_faq": ("Welling FAQ", "https://www.welling.ai/faq"),
    "welling_store": ("Welling on the App Store", "https://apps.apple.com/us/app/welling-ai-food-health-coach/id6503678413"),
    "nutricam_store": ("NutriCam on the App Store", "https://apps.apple.com/us/app/nutricam-ai-nutrient-tracker/id6745231558"),
}

NUTRICAM_PRICE = "Free download. Pro is $9.99 a month, or $34.99 to $49.99 a year (U.S. App Store, confirmed August 26, 2026)"
PHOTO_CAVEAT = (
    '<div class="caveat"><p>No app can measure a meal from a photo. A picture cannot show oil, sauces, hidden '
    "ingredients, or portion weight. Every number from every app on this page is an estimate until you correct "
    "the foods and portions. We have not run an accuracy test across these apps, so this page makes no accuracy "
    "ranking.</p></div>"
)


VS_CAL_AI = {
    "slug": "nutricam-vs-cal-ai",
    "title": "NutriCam vs Cal AI (2026): advisor vs photo calorie counter",
    "description": "Cal AI is a fast photo calorie and macro counter on iPhone and Android. NutriCam is an iPhone advisor that adds vitamins and minerals to the photo and tells you what to eat next. Compared from each app's own pages, September 2026.",
    "eyebrow": "Comparison · 2026",
    "h1": "NutriCam vs Cal AI (2026)",
    "lede": 'Short answer: pick <a href="https://www.calai.app/" rel="noopener noreferrer">Cal AI</a> if you want a fast photo count of calories, protein, carbs, and fat, or if you are on Android. Pick NutriCam if you are on iPhone and want the photo to also show vitamins and minerals, then answer “what should I eat next?” from the day you already logged. Cal AI counts the plate. NutriCam advises on the next one.',
    "disclosure": "We make one of the two apps on this page.",
    "published": UPDATED,
    "updated": UPDATED,
    "updated_label": UPDATED_LABEL,
    "about": [("Cal AI", "https://www.calai.app/")],
    "sections": [
        {
            "h2": "NutriCam vs Cal AI at a glance",
            "wide": True,
            "html": table(
                ["Dimension", "NutriCam", "Cal AI"],
                [
                    ["Core job", "Advisor: what is on the plate, and what to eat next", "Counter: calories and macros from a photo"],
                    ["Platform", "iPhone only", "iPhone and Android"],
                    ["Photo logging", "Default capture. Free tier included, with limits", "Yes. Scan results require a subscription after the trial"],
                    ["Nutrients shown", "Calories, macros, plus vitamins and minerals such as iron, B12, magnesium, iodine", "Calories, protein, carbs, fat. Its own pages make no micronutrient claim"],
                    ["“What should I eat next?”", "The home job, from today’s log, targets, workouts, and Apple Health sleep when connected", "Not a feature its own pages describe"],
                    ["Voice logging", "Yes. Say what you ate", "Not stated on its own pages"],
                    ["Free tier", "Yes, with limits. Same advisor on free and paid", "Free download with a 3-day trial. No permanent free tier described"],
                    ["Price", NUTRICAM_PRICE, "Subscription. The App Store lists “Unlimited” plans from $2.99 to $29.99 without showing the billing period"],
                    ["Medical device", "No", "No"],
                ],
            ),
        },
        {
            "h2": "Which one should you use?",
            "html": "<p>Use Cal AI if the only question is “how many calories and how much protein was that?” and you want the answer on iPhone or Android. It is the best-known app for that job.</p>"
            "<p>Use NutriCam if the question continues past the count. After the photo, NutriCam shows vitamins and minerals on the same card and answers what to eat next, using the meals you logged today, your targets, your workouts, and your sleep when Apple Health is connected.</p>"
            "<p>If you need Android, this comparison is over. NutriCam is iPhone only.</p>",
        },
        {
            "h2": "Does Cal AI track vitamins and minerals?",
            "html": "<p>Cal AI’s website and App Store listing name calories, protein, carbs, and fat. We found no vitamin or mineral claim on either, as of September 19, 2026. If micronutrients matter to you, that is the practical difference between the two apps. NutriCam shows vitamins and minerals such as iron, vitamin B12, magnesium, and iodine against your targets.</p>"
            '<p>For the deepest micronutrient tracking of any app, neither is the answer. That is Cronometer. See <a href="/nutricam-vs-cronometer/">NutriCam vs Cronometer</a>.</p>'
            + PHOTO_CAVEAT,
        },
        {
            "h2": "A Cal AI alternative that tells you what to eat next",
            "html": '<p>A calorie count tells you what happened. It does not tell you what to do at dinner. NutriCam’s advisor takes the same photo log and turns it into a next-meal answer. Example: a short night, a hard lower-body session, protein and carbs behind target. The answer is a plate, a chicken rice bowl with vegetables, not “eat clean.” Details: <a href="/what-should-i-eat-next/">what should I eat next</a>.</p>'
            '<p>Other options are on <a href="/cal-ai-alternatives/">Cal AI alternatives</a>.</p>',
        },
    ],
    "faq": [
        ("NutriCam vs Cal AI: which is better?", "Better for what. Cal AI is a fast photo calorie and macro counter on iPhone and Android. NutriCam is an iPhone advisor that adds vitamins and minerals to the photo and tells you what to eat next. Pick the job."),
        ("Does Cal AI track micronutrients?", "Cal AI's own website and App Store listing name calories, protein, carbs, and fat. We found no vitamin or mineral claim there as of September 19, 2026. NutriCam shows vitamins and minerals such as iron, B12, magnesium, and iodine."),
        ("Is Cal AI free?", "Cal AI is a free download with a 3-day trial. Its App Store listing says scan results require a subscription. NutriCam has a free tier with the same advisor as the paid plan."),
        ("Is NutriCam on Android like Cal AI?", "No. NutriCam by LAYERTWO is iPhone only. Cal AI is on iPhone and Android."),
        ("Can Cal AI tell me what to eat next?", "Cal AI's own pages do not describe a next-meal feature. That is NutriCam's main job: it uses today's logged meals, your targets, workouts, and Apple Health sleep when connected."),
        ("Which is more accurate, NutriCam or Cal AI?", "We have not run a controlled accuracy test, so we do not claim one. Both estimate from a photo. Oils, sauces, and portion size can throw off any photo estimate. Correct the portions before you trust the log."),
        ("Are these medical devices?", "No."),
    ],
    "sources": [SRC["calai"], SRC["calai_store"], SRC["nutricam_store"]],
}


CAL_AI_ALTERNATIVES = {
    "slug": "cal-ai-alternatives",
    "title": "6 Cal AI alternatives for iPhone (2026), picked by job",
    "description": "Cal AI counts calories and macros from a photo. If you want micronutrients, a free tier, a verified database, adaptive targets, or a next-meal answer, these are the alternatives: NutriCam, SnapCalorie, Cronometer, MacroFactor, MyFitnessPal, Welling.",
    "eyebrow": "Alternatives · 2026",
    "h1": "6 Cal AI alternatives for iPhone (2026)",
    "lede": "Short answer: the best Cal AI alternative depends on what you are missing. For a next-meal answer with vitamins and minerals on iPhone, NutriCam. For free photo logs, SnapCalorie (3 a day). For a verified micronutrient database, Cronometer. For calorie targets that adapt every week, MacroFactor. For the biggest food database and a diary coach, MyFitnessPal. For a chat-style coach, Welling.",
    "disclosure": "NutriCam is ours. The other five are not, and we say where they are the better pick.",
    "published": UPDATED,
    "updated": UPDATED,
    "updated_label": UPDATED_LABEL,
    "about": [("Cal AI", "https://www.calai.app/")],
    "item_list": [
        ("NutriCam", "https://nutricam.app/"),
        ("SnapCalorie", "https://www.snapcalorie.com/"),
        ("Cronometer", "https://cronometer.com/"),
        ("MacroFactor", "https://macrofactor.com/macrofactor/"),
        ("MyFitnessPal", "https://www.myfitnesspal.com/"),
        ("Welling", "https://www.welling.ai/"),
    ],
    "sections": [
        {
            "h2": "Cal AI alternatives at a glance",
            "wide": True,
            "html": table(
                ["App", "Best for", "Photo logging", "Tells you what to eat next", "Platforms", "Price"],
                [
                    ["NutriCam", "Next-meal answer with vitamins and minerals", "Default capture. Free tier included, with limits", "Yes. Uses today’s log, targets, workouts, and sleep", "iPhone", NUTRICAM_PRICE],
                    ["SnapCalorie", "Free photo logs and 100+ micronutrients", "Free up to 3 AI logs a day, then Premium", "Not an in-app feature its pages describe", "iPhone, Android", "Premium $19.99 a month or $149 a year"],
                    ["Cronometer", "Verified database, up to 95 nutrients", "Photo Log, Gold only", "Crono Coach and Food Suggestions, Gold only", "iPhone, Android, web", "Free tier. Gold $10.99 a month or $59.99 a year"],
                    ["MacroFactor", "Calorie and macro targets that adapt weekly", "Yes, in the paid plan", "No. Coaching adjusts targets, not meals", "iPhone, Android", "$11.99 a month or $71.99 a year. No free tier"],
                    ["MyFitnessPal", "Largest diary ecosystem", "Meal Scan, Premium and Premium+", "Coach, Premium tiers, iOS in six English-speaking countries", "iPhone, Android, web", "Free tier. Premium $79.99 a year, Premium+ $99.99 a year"],
                    ["Welling", "Chat-style AI coach", "Yes, with a subscription", "Yes. Coach suggests ideas for remaining calories and macros", "iPhone, Android", "Subscription. Monthly from $19.99 on the App Store"],
                ],
            ),
        },
        {
            "h2": "How we picked",
            "html": "<p>We started from what Cal AI’s own pages describe: photo logging of calories, protein, carbs, and fat, on iPhone and Android, with a subscription after a 3-day trial. Each alternative below does one thing Cal AI’s pages do not describe. Every fact comes from that app’s own website, help center, or App Store listing. We did not test accuracy, so nothing here is an accuracy ranking.</p>"
            + PHOTO_CAVEAT,
        },
        {
            "h2": "The six alternatives",
            "html": "<h3>1. NutriCam: best for “what should I eat next?”</h3>"
            '<p>NutriCam is our app. It is iPhone only. You photograph a meal or say what you ate, confirm the estimate, and see calories, macros, and vitamins and minerals such as iron, B12, magnesium, and iodine. Then you ask what to eat next. The advisor uses today’s log, your targets, your workouts, and Apple Health sleep when connected. The free tier has the same advisor as the paid one. Skip it if you need Android or a verified food database. <a href="/nutricam-vs-cal-ai/">NutriCam vs Cal AI</a>.</p>'
            "<h3>2. SnapCalorie: best free photo logging</h3>"
            "<p>SnapCalorie’s FAQ says the app is free for up to 3 AI logs a day, with unlimited logs on Premium ($19.99 a month or $149 a year). Its App Store listing claims 100+ micronutrients including vitamins, minerals, and amino acids. It supports voice logging. Its pages do not describe next-meal suggestions based on your day.</p>"
            "<h3>3. Cronometer: best verified micronutrient database</h3>"
            '<p>Cronometer tracks up to 95 nutrients and compounds, and the free tier includes that depth plus a barcode scanner. Photo Log, voice logging, and Crono Coach are Gold features ($10.99 a month or $59.99 a year). With Photo Log the AI suggests foods and the numbers come from the database. Choose it if you will maintain a precise diary. <a href="/nutricam-vs-cronometer/">NutriCam vs Cronometer</a>.</p>'
            "<h3>4. MacroFactor: best adaptive targets</h3>"
            "<p>MacroFactor’s coaching algorithm makes weekly changes to your calorie and macro plan. It has AI photo logging, speech-to-text logging, and tracks 54 items from macros to micronutrients. There is no free tier, only a 7-day trial, then $11.99 a month or $71.99 a year. It does not suggest meals.</p>"
            "<h3>5. MyFitnessPal: best if you want the big diary</h3>"
            "<p>MyFitnessPal has a free diary with a large food database. Meal Scan, voice logging, and barcode scanning sit on the paid tiers. Its Coach can tell you what to eat with your remaining calories, on Premium tiers, on iOS, in English, in six countries. Premium is $79.99 a year and Premium+ is $99.99 a year.</p>"
            "<h3>6. Welling: best chat-style coach</h3>"
            "<p>Welling is an AI coach you talk to. It logs from photos and text and gives ideas for your remaining calories and macros. Its FAQ says a full vitamin and mineral panel is not supported yet; it tracks fiber, sodium, and sugar. All features need a subscription after the trial.</p>",
        },
    ],
    "faq": [
        ("What is the best Cal AI alternative?", "It depends on what you are missing. NutriCam for a next-meal answer with vitamins and minerals on iPhone. SnapCalorie for free photo logs. Cronometer for a verified micronutrient database. MacroFactor for adaptive targets. MyFitnessPal for the biggest diary. Welling for a chat-style coach."),
        ("Is there a free alternative to Cal AI?", "Yes. SnapCalorie's FAQ says it is free for up to 3 AI photo logs a day. NutriCam has a free tier with photo logging, with limits, and the same advisor as the paid plan. Cronometer has a deep free tier, but its Photo Log is a Gold feature."),
        ("Which Cal AI alternative tracks vitamins and minerals?", "Cronometer tracks up to 95 nutrients. SnapCalorie claims 100+ micronutrients. MacroFactor tracks 54 items including micronutrients. NutriCam shows vitamins and minerals such as iron, B12, magnesium, and iodine on the photo card."),
        ("Which Cal AI alternative tells me what to eat next?", "NutriCam is built around that question and uses today's log, targets, workouts, and sleep. MyFitnessPal's Coach and Welling's coach can suggest food for your remaining calories and macros. Cronometer has Crono Coach on Gold."),
        ("Which Cal AI alternatives work on Android?", "SnapCalorie, Cronometer, MacroFactor, MyFitnessPal, and Welling are on Android. NutriCam is iPhone only."),
        ("Which alternative is the most accurate?", "We did not run an accuracy test, so we do not rank accuracy. Every photo-based number is an estimate. Apps that map the photo to a verified database, such as Cronometer, rely on you to confirm foods and portions."),
    ],
    "sources": [SRC["calai"], SRC["calai_store"], SRC["snap_faq"], SRC["snap_store"], SRC["crono_gold"], SRC["crono_photo"], SRC["crono_coach"], SRC["mf"], SRC["mf_store"], SRC["mf_vs"], SRC["mfp_premium"], SRC["mfp_coach"], SRC["mfp_store"], SRC["welling_faq"], SRC["welling_store"], SRC["nutricam_store"]],
}


CRONOMETER_ALTERNATIVES = {
    "slug": "cronometer-alternatives",
    "title": "5 Cronometer alternatives with AI photo logging (2026)",
    "description": "Cronometer keeps Photo Log on Gold and expects a careful diary. If you want photo-first logging with micronutrients, these are the alternatives: NutriCam, SnapCalorie, MacroFactor, Fitia, MyFitnessPal. Compared from each app's own pages.",
    "eyebrow": "Alternatives · 2026",
    "h1": "5 Cronometer alternatives with AI photo logging (2026)",
    "lede": "Short answer: nothing beats Cronometer for verified micronutrient depth, so leave only if the diary is the problem. For photo-first logging with vitamins and minerals and a next-meal answer on iPhone, NutriCam. For free photo logs with 100+ micronutrients, SnapCalorie. For photo logging with adaptive targets, MacroFactor. For meal plans, Fitia. For the largest food database, MyFitnessPal.",
    "disclosure": "NutriCam is ours. We say plainly where Cronometer stays the better tool.",
    "published": UPDATED,
    "updated": UPDATED,
    "updated_label": UPDATED_LABEL,
    "about": [("Cronometer", "https://cronometer.com/")],
    "item_list": [
        ("NutriCam", "https://nutricam.app/"),
        ("SnapCalorie", "https://www.snapcalorie.com/"),
        ("MacroFactor", "https://macrofactor.com/macrofactor/"),
        ("Fitia", "https://fitia.app/en/"),
        ("MyFitnessPal", "https://www.myfitnesspal.com/"),
    ],
    "sections": [
        {
            "h2": "Cronometer alternatives at a glance",
            "wide": True,
            "html": table(
                ["App", "Best for", "Photo logging", "Micronutrients", "Platforms", "Price"],
                [
                    ["Cronometer (baseline)", "Verified database and precise diary", "Photo Log, Gold only", "Up to 95 nutrients and compounds, on the free tier too", "iPhone, Android, web", "Free tier. Gold $10.99 a month or $59.99 a year"],
                    ["NutriCam", "Photo-first capture and a next-meal answer", "Default capture. Free tier included, with limits", "Vitamins and minerals such as iron, B12, magnesium, iodine, estimated from the photo", "iPhone", NUTRICAM_PRICE],
                    ["SnapCalorie", "Free photo logs", "Free up to 3 AI logs a day, then Premium", "Claims 100+ micronutrients", "iPhone, Android", "Premium $19.99 a month or $149 a year"],
                    ["MacroFactor", "Adaptive weekly targets", "Yes, in the paid plan", "54 trackable items including micronutrients", "iPhone, Android", "$11.99 a month or $71.99 a year. No free tier"],
                    ["Fitia", "Meal plans", "Premium", "Calories, macros, and 20+ nutrients", "iPhone, Android, web", "Free tier. Premium $19.99 for 1 month on the App Store"],
                    ["MyFitnessPal", "Largest diary ecosystem", "Meal Scan, Premium and Premium+", "No nutrient count stated on its pages", "iPhone, Android, web", "Free tier. Premium $79.99 a year"],
                ],
            ),
        },
        {
            "h2": "When to stay with Cronometer",
            "html": "<p>Stay if you weigh food, build custom recipes, and read nutrient-by-nutrient reports. Cronometer’s free tier already tracks up to 95 nutrients with a barcode scanner, and its Photo Log maps the photo onto verified database entries that you then edit. No photo-first app on this page matches that depth, including ours.</p>"
            "<p>Leave, or add a second app, if the diary is the reason you stopped logging. Search, weigh, edit, repeat is accurate. It is also the step most people quit.</p>",
        },
        {
            "h2": "The five alternatives",
            "html": "<h3>1. NutriCam: best photo-first alternative on iPhone</h3>"
            '<p>NutriCam is our app. The photo is the default capture, not a paid add-on. The card shows calories, macros, and vitamins and minerals, all as estimates you confirm. Then the advisor answers what to eat next from today’s log, targets, workouts, and Apple Health sleep. You give up database depth, Android, and web. Full comparison: <a href="/nutricam-vs-cronometer/">NutriCam vs Cronometer</a>.</p>'
            "<h3>2. SnapCalorie: best free photo logging with micronutrients</h3>"
            "<p>Free for up to 3 AI logs a day per its FAQ. Its App Store listing claims 100+ micronutrients including vitamins, minerals, and amino acids. Premium is $19.99 a month or $149 a year.</p>"
            "<h3>3. MacroFactor: best for adaptive targets</h3>"
            "<p>AI photo logging and speech-to-text logging feed a database-backed log with 54 trackable items. The coaching adjusts calorie and macro targets weekly. No free tier. $11.99 a month or $71.99 a year.</p>"
            "<h3>4. Fitia: best for meal plans</h3>"
            "<p>Fitia builds personalized meal plans and has an AI Coach. Photo and voice logging are Premium features. Its listing names calories, macros, and 20+ nutrients, which is far shallower than Cronometer.</p>"
            "<h3>5. MyFitnessPal: best for the biggest food database</h3>"
            "<p>The free tier is a manual diary. Meal Scan, voice logging, and barcode scanning are paid. Its pages do not state a nutrient count, and the product is calorie and macro first.</p>"
            + PHOTO_CAVEAT,
        },
    ],
    "faq": [
        ("What is the best Cronometer alternative?", "If you want verified micronutrient depth, there is no better tool than Cronometer. If the manual diary is the problem, NutriCam is the photo-first alternative on iPhone with vitamins and minerals and a next-meal answer. SnapCalorie is the alternative with free photo logs."),
        ("Is there a Cronometer alternative with free AI photo logging?", "Yes. NutriCam's free tier includes photo logging, with limits. SnapCalorie is free for up to 3 AI logs a day. Cronometer's own Photo Log requires Gold."),
        ("Does Cronometer have AI photo logging?", "Yes. Photo Log is a Cronometer Gold feature. The AI suggests foods and servings, you edit them, and the nutrient values come from Cronometer's database."),
        ("Which Cronometer alternative tracks the most micronutrients?", "By their own claims: SnapCalorie says 100+ micronutrients, MacroFactor tracks 54 items, Fitia names 20+ nutrients. Cronometer tracks up to 95 nutrients and compounds against verified entries, which is a stronger claim than an estimate from a photo."),
        ("How much does Cronometer Gold cost?", "Cronometer's Gold page lists $10.99 a month billed monthly, or $59.99 billed annually, as of September 19, 2026."),
        ("Can a photo measure vitamins and minerals?", "No. Every app estimates or maps foods from what the camera can see. Confirm foods and portions. Do not treat a camera estimate as a blood test."),
    ],
    "sources": [SRC["crono_gold"], SRC["crono_photo"], SRC["crono_store"], SRC["snap_faq"], SRC["snap_store"], SRC["mf"], SRC["mf_store"], SRC["mf_vs"], SRC["fitia"], SRC["fitia_premium"], SRC["fitia_store"], SRC["mfp_premium"], SRC["mfp_store"], SRC["nutricam_store"]],
}


BEST_AI = {
    "slug": "best-ai-calorie-tracker-apps",
    "title": "8 best AI calorie tracker apps for iPhone (2026), by job",
    "description": "The best AI calorie tracker depends on the job: Cal AI for a fast photo count, Cronometer for verified micronutrients, MacroFactor for adaptive targets, SnapCalorie for free photo logs, NutriCam for what to eat next. Eight apps compared from their own pages.",
    "eyebrow": "Guide · 2026",
    "h1": "8 best AI calorie tracker apps for iPhone (2026)",
    "lede": "Short answer: there is no single best AI calorie tracker, because the apps do different jobs. Cal AI is the fast photo counter for calories and macros. Cronometer is the verified micronutrient database. MacroFactor adapts your targets every week. SnapCalorie gives 3 free photo logs a day. MyFitnessPal is the biggest diary. Fitia builds meal plans. Welling is a chat coach. NutriCam, our app, photographs the meal, shows vitamins and minerals, and tells you what to eat next.",
    "disclosure": "We make NutriCam, so this list is ordered by job, not by score, and the criteria come first.",
    "published": UPDATED,
    "updated": UPDATED,
    "updated_label": UPDATED_LABEL,
    "about": [],
    "item_list": [
        ("Cal AI", "https://www.calai.app/"),
        ("Cronometer", "https://cronometer.com/"),
        ("MacroFactor", "https://macrofactor.com/macrofactor/"),
        ("SnapCalorie", "https://www.snapcalorie.com/"),
        ("NutriCam", "https://nutricam.app/"),
        ("MyFitnessPal", "https://www.myfitnesspal.com/"),
        ("Fitia", "https://fitia.app/en/"),
        ("Welling", "https://www.welling.ai/"),
    ],
    "sections": [
        {
            "h2": "How this list was made",
            "html": "<p>Five questions, answered only from each app’s own website, help center, or App Store listing on September 19, 2026:</p>"
            "<ol><li>Is photo logging free, or on a paid tier?</li><li>Does the app show vitamins and minerals, or only calories and macros?</li><li>Does the app tell you what to eat next from today’s log?</li><li>Which platforms?</li><li>What does it cost, where the provider states a price and a period?</li></ol>"
            "<p>What this list is not: an accuracy test. We did not weigh meals and compare apps, so no app here is called “most accurate.” Where an app’s pages do not state something, the table says so.</p>",
        },
        {
            "h2": "AI calorie tracker apps compared",
            "wide": True,
            "html": table(
                ["App", "Best for", "Photo logging", "Vitamins and minerals", "Tells you what to eat next", "Platforms", "Price"],
                [
                    ["Cal AI", "Fast photo count of calories and macros", "Yes. Subscription after a 3-day trial", "No claim on its own pages", "Not described on its pages", "iPhone, Android", "App Store lists plans from $2.99 to $29.99, periods not shown"],
                    ["Cronometer", "Verified micronutrient database", "Photo Log, Gold only", "Up to 95 nutrients, free tier included", "Crono Coach, Gold only", "iPhone, Android, web", "Free tier. Gold $10.99 a month or $59.99 a year"],
                    ["MacroFactor", "Targets that adapt weekly", "Yes, in the paid plan", "54 trackable items", "No. Adjusts targets, not meals", "iPhone, Android", "$11.99 a month or $71.99 a year. No free tier"],
                    ["SnapCalorie", "Free photo logs", "Free up to 3 a day, then Premium", "Claims 100+ micronutrients", "Not an in-app feature its pages describe", "iPhone, Android", "Premium $19.99 a month or $149 a year"],
                    ["NutriCam", "What to eat next, with micronutrients", "Default capture. Free tier included, with limits", "Yes, such as iron, B12, magnesium, iodine", "Yes. Uses today’s log, targets, workouts, sleep", "iPhone", NUTRICAM_PRICE],
                    ["MyFitnessPal", "Largest diary ecosystem", "Meal Scan, paid tiers", "No count stated", "Coach, paid tiers, iOS, six countries", "iPhone, Android, web", "Free tier. Premium $79.99 a year"],
                    ["Fitia", "Meal plans", "Premium", "20+ nutrients", "AI Coach and meal plans", "iPhone, Android, web", "Free tier. Premium $19.99 for 1 month"],
                    ["Welling", "Chat-style coach", "Yes, with a subscription", "Fiber, sodium, sugar only", "Yes, for remaining calories and macros", "iPhone, Android", "Monthly from $19.99 on the App Store"],
                ],
            ),
        },
        {
            "h2": "The eight apps",
            "html": "<h3>Cal AI: best for a fast photo calorie count</h3><p>Cal AI’s pages describe one job: photograph food, get calories, protein, carbs, and fat. It is on iPhone and Android. The App Store listing says scan results need a subscription after a 3-day trial. <a href=\"/nutricam-vs-cal-ai/\">NutriCam vs Cal AI</a>.</p>"
            "<h3>Cronometer: best for verified micronutrients</h3><p>Up to 95 nutrients and compounds, a barcode scanner, and custom recipes on the free tier. Photo Log, voice logging, and Crono Coach are on Gold. The AI suggests foods; the numbers come from the database. <a href=\"/nutricam-vs-cronometer/\">NutriCam vs Cronometer</a>.</p>"
            "<h3>MacroFactor: best for adaptive targets</h3><p>MacroFactor’s coaching algorithm makes weekly changes to your calorie and macro plan. It has AI photo logging and speech-to-text logging. There is no free tier.</p>"
            "<h3>SnapCalorie: best free photo logging</h3><p>Three free AI logs a day, per its FAQ. Its listing claims 100+ micronutrients and supports voice logging.</p>"
            "<h3>NutriCam: best for “what should I eat next?”</h3><p>Ours, and iPhone only. Photograph a meal or say what you ate, confirm the estimate, and see calories, macros, and vitamins and minerals. Then ask what to eat next. The advisor uses today’s log, your targets, workouts, and Apple Health sleep when connected. It is the wrong pick if you need Android, a barcode-first diary, or a verified database. <a href=\"/what-should-i-eat-next/\">How the next-meal answer works</a>.</p>"
            "<h3>MyFitnessPal: best for the biggest diary</h3><p>A free manual diary with a very large food database. Meal Scan, voice logging, and barcode scanning are on paid tiers. Coach answers what to eat with your remaining calories, on Premium tiers, on iOS, in six English-speaking countries.</p>"
            "<h3>Fitia: best for meal plans</h3><p>Personalized meal plans plus an AI Coach. Photo and voice logging are Premium. The free version has basic tracking and barcode scanning with ads.</p>"
            "<h3>Welling: best chat-style coach</h3><p>You log by chatting, with photos or text, and the coach suggests ideas for your remaining calories and macros. Its FAQ says a full vitamin and mineral panel is not supported yet. A subscription is required after the trial.</p>"
            + PHOTO_CAVEAT,
        },
    ],
    "faq": [
        ("What is the best AI calorie tracker app for iPhone in 2026?", "It depends on the job. Cal AI for a fast photo count of calories and macros. Cronometer for verified micronutrients. MacroFactor for adaptive targets. SnapCalorie for free photo logs. NutriCam for a photo log with vitamins and minerals that tells you what to eat next."),
        ("Which AI calorie tracker has free photo logging?", "SnapCalorie is free for up to 3 AI logs a day. NutriCam's free tier includes photo logging, with limits. Cal AI, Cronometer, MacroFactor, MyFitnessPal, Fitia, and Welling put photo logging on a paid plan."),
        ("Is there an app that tracks vitamins and minerals from a photo?", "Yes, as estimates. NutriCam shows vitamins and minerals such as iron, B12, magnesium, and iodine on the photo card. SnapCalorie claims 100+ micronutrients. Cronometer's Photo Log (Gold) maps the photo to database entries with up to 95 nutrients. No photo can measure micronutrients exactly."),
        ("Is there an AI nutrition app that tells me what to eat next?", "Yes. NutriCam is built around that question and uses today's log, targets, workouts, and sleep. MyFitnessPal Coach, Welling, Cronometer's Crono Coach, and Fitia's AI Coach also give food guidance on their paid plans."),
        ("How accurate are AI photo calorie counters?", "They estimate. A photo cannot show oil, sauces, hidden ingredients, or portion weight. We did not run an accuracy test, so this page does not rank accuracy. Confirm foods and portions in any app before trusting the day's total."),
        ("Are AI calorie tracker apps worth paying for?", "Pay when the paid feature is the one you will use daily. If that is photo logging, note that SnapCalorie and NutriCam include it free, while most others put it behind a subscription."),
        ("Who wrote this list?", "LAYERTWO, LLC, the company that makes NutriCam. That is why the list is ordered by job instead of by score, and why every fact about another app links to that app's own pages."),
    ],
    "sources": [SRC["calai"], SRC["calai_store"], SRC["crono_gold"], SRC["crono_photo"], SRC["crono_coach"], SRC["mf"], SRC["mf_store"], SRC["mf_vs"], SRC["snap_faq"], SRC["snap_store"], SRC["mfp_premium"], SRC["mfp_coach"], SRC["mfp_store"], SRC["fitia"], SRC["fitia_premium"], SRC["fitia_store"], SRC["welling_faq"], SRC["welling_store"], SRC["nutricam_store"]],
}

PAGES = [VS_CAL_AI, CAL_AI_ALTERNATIVES, CRONOMETER_ALTERNATIVES, BEST_AI]

SRC["etm_howto"] = ("Eat This Much how-to", "https://www.eatthismuch.com/how-to/")
SRC["etm_pricing"] = ("Eat This Much pricing", "https://eatthismuch.com/pricing")
SRC["etm_annual"] = (
    "Eat This Much on annual billing",
    "https://help.eatthismuch.com/help/how-do-i-change-from-a-monthly-to-an-annual-subscription-or-vice-versa",
)

DINNER_FROM_WORKOUT = {
    "slug": "dinner-from-workout-and-what-you-ate",
    "title": "Is there an app that suggests dinner based on my workout and what I already ate?",
    "description": "Yes. Apps suggest dinner from today's meals and a workout. MyFitnessPal Coach, Welling, and NutriCam do. You still have to log the food.",
    "eyebrow": "Answer · 2026",
    "h1": "Is there an app that suggests dinner based on my workout and what I already ate?",
    "lede": 'Yes. <a href="https://support.myfitnesspal.com/hc/en-us/articles/45212266254221-Introducing-Nutrition-Coach-Your-Nutrition-A" rel="noopener noreferrer">MyFitnessPal\'s Nutrition Coach</a>, <a href="https://www.welling.ai/faq" rel="noopener noreferrer">Welling</a>, and NutriCam can suggest dinner from today\'s log and a workout. MyFitnessPal uses remaining calories from the diary. Welling answers remaining-calorie ideas in chat. NutriCam, on iPhone, uses logged meals, workouts, and sleep when connected. You still have to log the food. A phone does not see the plate.',
    "disclosure": "We make NutriCam. The other apps on this page are not ours, and we say where they are the better pick.",
    "published": "2026-10-02",
    "updated": "2026-10-02",
    "updated_label": "October 2, 2026",
    "about": [
        ("MyFitnessPal Nutrition Coach", "https://support.myfitnesspal.com/hc/en-us/articles/45212266254221-Introducing-Nutrition-Coach-Your-Nutrition-A"),
        ("Welling", "https://www.welling.ai/faq"),
        ("Eat This Much", "https://www.eatthismuch.com/how-to/"),
    ],
    "sections": [
        {
            "h2": "Which apps suggest dinner from today's log and a workout",
            "wide": True,
            "html": table(
                ["App", "Dinner it can name", "Uses today's meals", "Uses today's workout", "Platforms", "Price"],
                [
                    [
                        "MyFitnessPal Nutrition Coach",
                        "Food ideas for remaining calories and macros",
                        "Yes. Today's diary plus recent history",
                        "Step data. Help page includes “what should I eat before or after a workout?” Logged workout type is not in the listed inputs",
                        "Coach: iPhone, English, six countries. App: iPhone and Android",
                        "Coach is Premium and Premium+ only",
                    ],
                    [
                        "Eat This Much",
                        "A generated dinner. If lunch went off-plan, log it and regenerate the remaining meals so they fill the leftover targets",
                        "Yes, once you log what you actually ate",
                        "Premium weekly layout can use a workout-day nutrition profile with more calories and protein",
                        "Web, iPhone, Android",
                        "Free day planner. Premium $5 a month billed annually, $59.99 a year (site and help center, October 2, 2026)",
                    ],
                    [
                        "Welling",
                        "Chat ideas for remaining calories and macros",
                        "Yes. Photo, text, or voice log",
                        "Yes. Chat or Apple Health. Burned calories add to the daily target unless you turn that off",
                        "iPhone and Android",
                        "Subscription. App Store lists monthly plans from $9.49 to $22.99 (October 2, 2026)",
                    ],
                    [
                        "Cronometer Crono Coach",
                        "Meal suggestions from the diary, goals, preferences, and logging habits",
                        "Yes, if the day is logged",
                        "Not stated as a Coach input on the help article",
                        "iPhone, Android, web",
                        "Crono Coach is a Gold feature",
                    ],
                    [
                        "Fitia",
                        "Personalized meal plans and an AI Coach",
                        "Yes. Photo, voice, or typed log",
                        "Apple Health workouts update calorie balance. Pages describe plans more than a tonight card from this morning's session",
                        "iPhone, Android, web",
                        "Premium $19.99 a month or $59.99 a year on the App Store (October 2, 2026)",
                    ],
                    [
                        "NutriCam",
                        "A next-meal answer, including remaining-macro recipes on the App Store listing",
                        "Yes. Photo or spoken log, confirmed before it is the day's record",
                        "Yes. Workouts logged in the app, plus Apple Health sleep when connected",
                        "iPhone only",
                        NUTRICAM_PRICE,
                    ],
                ],
            ),
        },
        {
            "h2": "What “based on my workout” actually uses",
            "html": "<p>Most apps treat the workout as extra calories. MyFitnessPal adds exercise to remaining calories when that setting is on. Welling does the same by default, and its FAQ says you can turn it off. Eat This Much can give workout days a higher calorie and protein profile on Premium. That is a budget change. It is not a plate.</p>"
            "<p>A smaller set uses the session as context for the next meal. NutriCam's site says the advisor uses logged workouts with today's meals and targets. Welling will estimate burn from a described session, or take a number you type, and can then suggest food for what is left. MyFitnessPal's Coach help page lists step data among its inputs, and names “what should I eat before or after a workout?” as a question you can ask. It does not list a logged workout type next to the diary.</p>"
            "<p>If you need Android, MyFitnessPal, Eat This Much, Welling, Cronometer, and Fitia are the list. NutriCam is iPhone only.</p>",
        },
        {
            "h2": "You still have to log what you already ate",
            "html": "<p>No phone sees lunch on its own. Photograph it, say it, scan it, or type it. Then dinner has something to work from.</p>"
            "<p>Eat This Much's how-to is blunt about the off-plan case: delete the dishes you skipped, add what you did eat, then regenerate the remaining meals so they fill the leftover targets. MyFitnessPal Coach reads the diary you already kept. Welling and NutriCam start from a confirmed log. Cronometer's Crono Coach starts from the same diary that makes Cronometer useful in the first place.</p>"
            '<p>That is the whole job. Remaining protein after a logged day is a dinner cue. A blank diary is a recipe app. How NutriCam turns the log into a next-meal card: <a href="/what-should-i-eat-next/">what should I eat next</a>.</p>',
        },
        {
            "h2": "Why remaining calories after a workout are a guess",
            "html": "<p>Wearable calorie burn is an estimate. Welling's FAQ says most trackers overestimate, and it tells people chasing fat loss not to eat those calories back after low-to-moderate sessions. You can turn off adding activity to the daily target.</p>"
            "<p>Use remaining protein and carbohydrate from the food log as the dinner cue. Treat the watch bonus as a maybe. Oils, sauces, and portion size throw photo logs off in the other direction, so confirm the foods before you ask what to eat tonight.</p>"
            + PHOTO_CAVEAT,
        },
        {
            "h2": "Photo calorie counters are a different job",
            "html": '<p><a href="https://www.calai.app/" rel="noopener noreferrer">Cal AI</a> photographs food and returns calories, protein, carbs, and fat. Its site also says it can track exercises with connected fitness products. We found no dinner suggestion from today\'s meals on its website or App Store listing as of October 2, 2026. That is a counter. This question is an advisor.</p>'
            '<p>Full split: <a href="/nutricam-vs-cal-ai/">NutriCam vs Cal AI</a>. Other photo apps, by job: <a href="/best-ai-calorie-tracker-apps/">best AI calorie tracker apps</a>. For a verified micronutrient diary rather than a tonight card, <a href="/nutricam-vs-cronometer/">NutriCam vs Cronometer</a>.</p>',
        },
    ],
    "faq": [
        (
            "Does MyFitnessPal already suggest dinner from remaining calories?",
            "Yes. Nutrition Coach is a Premium and Premium+ iOS feature in the United States, United Kingdom, Ireland, Canada, Australia, and New Zealand. It uses today's diary, calorie and macro targets, saved meals, recipes, the food database, and step data. Its help page includes “What should I eat with my remaining calories?” Coach cannot log food for you.",
        ),
        (
            "Can any app know what I ate if I never logged it?",
            "No. A phone does not see the plate unless you photograph it, describe it, scan it, or type it. Eat This Much, MyFitnessPal, Welling, Cronometer, Fitia, and NutriCam all start from a log. Log lunch before you ask about dinner.",
        ),
        (
            "Should I eat back the calories my watch says I burned?",
            "Treat them as a guess. Welling's FAQ says most wearables overestimate burn, and you can stop adding activity to the daily target. Remaining protein and carbs from the food log are a more useful dinner cue than the watch's extra calories.",
        ),
        (
            "Does Cal AI suggest dinner from my workout?",
            "Cal AI's website and App Store listing describe a photo count of calories, protein, carbs, and fat, plus exercise tracking with connected apps. We found no next-meal or dinner-from-today's-log claim there as of October 2, 2026. That job sits on Coach-style apps and on NutriCam.",
        ),
        (
            "What does NutriCam use when I ask what to eat tonight?",
            "Today's confirmed meals, remaining calorie and macro targets, micronutrient gaps such as iron, B12, magnesium, and iodine, workouts logged in the app, and Apple Health sleep when connected. The App Store listing also names recipes based on remaining macros. Confirm portions first. Details: what should I eat next.",
        ),
        (
            "Is a dinner suggestion from an app medical advice?",
            "No. Wellness guidance from a log. Not a medical device. None of the apps on this page diagnose, treat, or cure a deficiency or any condition.",
        ),
    ],
    "sources": [
        SRC["mfp_coach"],
        SRC["welling_faq"],
        SRC["welling_store"],
        SRC["etm_howto"],
        SRC["etm_pricing"],
        SRC["etm_annual"],
        SRC["crono_coach"],
        SRC["fitia_store"],
        SRC["calai"],
        SRC["calai_store"],
        SRC["nutricam_store"],
    ],
}

PAGES.append(DINNER_FROM_WORKOUT)
