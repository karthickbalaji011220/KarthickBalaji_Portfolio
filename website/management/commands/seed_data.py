from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from website.models import Profile, Skill, Education, Experience, Certification, Achievement, Project


class Command(BaseCommand):
    help = 'Seed initial portfolio data'

    def handle(self, *args, **kwargs):
        # Superuser
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@portfolio.com', 'admin123')
            self.stdout.write(self.style.SUCCESS('Superuser created: admin / admin123'))

        if Profile.objects.exists():
            self.stdout.write('Profile already exists, skipping seed.')
            return

        profile = Profile.objects.create(
            name="Karthick Balaji T",
            role="Full Stack Developer | Backend Developer | AI Fullstack Developer",
            short_intro="Full Stack Developer with 8+ months of experience building 10+ production-ready web applications using Python, Django, React.js, and Java Spring Boot.",
            bio="Full Stack Developer with 8+ months of internship experience building 10+ production-ready web applications. Certified in AI Fullstack (A Grade, 87.13%) from Vetri Technology Solutions. Proficient in REST API design, JWT/OAuth2 authentication, MySQL, MongoDB, and deployment via GitHub and Render.",
            career_objective="Seeking Full Stack or Backend Developer roles in Chennai, Coimbatore, or Bangalore, where I can leverage my expertise in Python, Django, REST APIs, and AI integration to build scalable, production-ready applications.",
            email="karthickbalaji028@gmail.com",
            phone="+91-7339087528",
            location="Chennai, TN — Open to Relocation",
            linkedin="https://linkedin.com/in/karthickbalaji001",
            github="https://github.com/karthickbalaji011220",
        )
        self.stdout.write(self.style.SUCCESS(f'Profile created: {profile.name}'))

        skills = [
            ("Python", 92, "🐍"), ("Django", 90, "🌐"), ("Django REST Framework", 88, "⚡"),
            ("React.js", 82, "⚛️"), ("JavaScript", 80, "🟡"), ("Java", 75, "☕"),
            ("Spring Boot", 75, "🍃"), ("HTML5 & CSS3", 88, "🎨"), ("MySQL", 83, "🗄️"),
            ("MongoDB", 78, "🍃"), ("PostgreSQL", 80, "🐘"), ("Git & GitHub", 90, "🐙"),
            ("Docker", 70, "🐳"), ("OpenAI GPT-4", 82, "🤖"), ("REST API Design", 88, "🔌"),
            ("JWT & OAuth2", 83, "🔐"),
        ]
        for i, (name, pct, icon) in enumerate(skills):
            Skill.objects.create(skill_name=name, percentage=pct, icon=icon, order=i)
        self.stdout.write(self.style.SUCCESS(f'Created {len(skills)} skills'))

        Experience.objects.create(company="Vetri IT Systems Private Limited", role="AI Fullstack Developer Intern", duration="Oct 2025 – Apr 2026", description="Built 10+ production-ready full-stack applications using Python, Django, and React.js. Integrated OpenAI GPT-4, Gemini, Claude, and DeepSeek APIs. Reduced manual data processing by ~40% via scalable REST APIs.", order=0)
        Experience.objects.create(company="Projectcadz Tech", role="Mobile Security Intern", duration="Jul 2025 – Aug 2025", description="Implemented AES encryption and data protection for mobile applications. Identified 10+ vulnerabilities via threat analysis and security audits.", order=1)

        Education.objects.create(degree="M.E. Computer Science Engineering", institution="Hindusthan College of Engineering and Technology, Coimbatore", year="2024", description="CGPA: 7.97", order=0)
        Education.objects.create(degree="B.E. Computer Science Engineering", institution="Hindusthan College of Engineering and Technology, Coimbatore", year="2022", description="CGPA: 7.71", order=1)

        certs = [
            ("AI Fullstack Certificate (A Grade, 87.13%)", "Vetri Technology Solutions", "Sep 2025 – May 2026"),
            ("Meta Front-End Developer Professional Certificate", "Coursera / Meta", "Aug – Oct 2025"),
            ("Python Developer Bootcamp", "Udemy", "Mar – Aug 2022"),
            ("Research Papers — ICA5NT 2024, RISC 2024, ICIT-24", "International Conferences on AI & Networks", "2024"),
        ]
        for i, (t, iss, yr) in enumerate(certs):
            Certification.objects.create(title=t, issuer=iss, year=yr, order=i)

        achievements = [
            ("10+ Production-Ready Applications", "Built and deployed 10+ full-stack web applications during internship with real client usage."),
            ("AI Grade A (87.13%)", "Achieved A Grade in AI Fullstack certification from ISO 9001:2015 certified institution."),
            ("40% Reduction in Manual Processing", "Engineered scalable REST APIs that reduced manual data processing by approximately 40%."),
            ("3 International Research Papers", "Presented research at ICA5NT 2024, RISC 2024, and ICIT-24 conferences."),
        ]
        for i, (t, d) in enumerate(achievements):
            Achievement.objects.create(title=t, description=d, order=i)

        self.stdout.write(self.style.SUCCESS('Data seeding complete!'))
