from flask import Flask, request, url_for

app = Flask(__name__)

# create a homepage route
@app.route('/home')
def home():
    home_url = url_for("home")
    about_url = url_for("about")
    resources_url = url_for("resources")
    join_nav_url = url_for("join")
    blog1_url = url_for("show_blog", slug="tech-careers")
    blog2_url = url_for("show_blog", slug="networking-tips")
    blog3_url = url_for("show_blog", slug="salary-talk")
    join_url = url_for("join")
    subscribe_url = url_for("subscribe")
    return """
    <html>
        <head>
            <title>Girl Tech Blog</title>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
        </head>
        
        <body>
            <ul class="nav nav-tabs">
                <li class="nav-item">
                <a class="nav-link active" aria-current="page" href="{}">Home</a>
                </li>
            
                <li class="nav-item">
                <a class="nav-link" href="{}">About</a>
                </li>
                
                <li class="nav-item">
                <a class="nav-link" href="{}">Resources</a>
                </li>
                
                <li class="nav-item">
                <a class="nav-link" href="{}">Join</a>
                </li>
            </ul>
            
            <h1>Welcome to Girl Tech Blog!</h1>
            
            <p>Where innovation meets empowerment. 🚀</p>
            
            <p>Girl Tech is your go-to space for all things tech—designed with curious, creative, and driven women in mind. Whether you're a coder, gamer, engineer, or just tech-curious, this is your digital home. Dive into tutorials, explore the latest trends, and get inspired by women shaping the future of technology. Because tech isn’t just for guys; it’s for you too.</p>
            
            <hr>
            
            <h2> Explore our blogposts</h2>
            
            <style>
            .card-img-top {{height: 300px; object-fit: cover;}}
            </style>

            <div class="row">
                <div class="col-md-4 mb-4">
                    <div class="card h-100 d-flex flex-column">
                        <img src="static/images/girltechcareers.jpeg" class="card-img-top" alt="Tech careers">
                    <div class="card-body d-flex flex-column">
                        <h5 class="card-title">Tech Careers You Have Never Heard Of But Could Totally Rock</h5>
                    <p class="card-text">Discover exciting, lesser-known tech careers where creativity and curiosity thrive — and women are leading the way.</p>
                    <a href="{}" class="btn btn-primary mt-auto">Read more</a>
                    </div>
                </div>
            </div>

            <div class="col-md-4 mb-4">
                <div class="card h-100 d-flex flex-column">
                    <img src="static/images/networking.jpeg" class="card-img-top" alt="Networking">
                    <div class="card-body d-flex flex-column">
                        <h5 class="card-title">Conquer The Crowd: Networking Like a Pro</h5>
                        <p class="card-text">A beginner-friendly guide to confidently navigating your first tech networking event, from prep to follow-up.</p>
                        <a href="{}" class="btn btn-primary mt-auto">Read more</a>
                    </div>
                </div>
            </div>

            <div class="col-md-4 mb-4">
                <div class="card h-100 d-flex flex-column">
                    <img src="static/images/salary.jpg" class="card-img-top" alt="Salary">
                    <div class="card-body d-flex flex-column">
                        <h5 class="card-title">Navigating the Numbers: Salary Talk for New Girls in Tech</h5>
                        <p class="card-text">Learn how to handle salary conversations with confidence and strategy as a newcomer in tech.</p>
                        <a href="{}" class="btn btn-primary mt-auto">Read more</a>
                        </div>
                    </div>
                </div>
            </div>
            
            <br>
          
            <h2> Become a member of Girl Tech</h2>
            <p>As a Girl Tech member, you'll get exclusive access to tutorials, career tips, community events, and inspiring stories from women in tech—all designed to help you grow, connect, and thrive in the industry. Whether you're just starting out or leveling up, there's a place for you here.</p>
            <a href="{}">Join now!</a>
            
            <hr>
           
            <h2>Subscribe to our newsletter</h2>
            <p>Subscribe to the Girl Tech newsletter for a dose of inspiration, tech tips, and updates straight to your inbox.</p>
            
            <form method="POST" action="{}">
                <div class="form-group">
                    <label for="exampleInputName">Name</label>
                    <input type="text" class="form-control" id="exampleInputName" name="name" placeholder="Enter your name" required>
                </div>
                <br>
                <div class="form-group">
                    <label for="exampleInputEmail1">Email address</label>
                    <input type="email" class="form-control" id="exampleInputEmail1" name="email" placeholder="Enter email" required>
                </div>
                <br>            
                <button type="submit" class="btn btn-primary">Subscribe</button>
            </form>
            
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
        </body>
    </html>
    """.format(home_url, about_url, resources_url, join_nav_url, blog1_url, blog2_url, blog3_url, join_url, subscribe_url)


@app.route('/subscribe', methods=["POST"])
def subscribe():
    name = request.form.get("name")
    home_url = url_for("home")
    return """
    <html>
        <head><title>Subscription</title></head>
        <body>
            <p>Thanks for subscribing to our newsletter, {}.</p>
            <p><a href="{}">Back to Home</a></p>
        </body>
        </html>  
    """.format(name, home_url)

# dictionary with blogpost info
blog_posts = {
    "tech-careers": {
        "title": "Tech Careers You’ve Never Heard Of (But Totally Could Rock!)",
        "author": "Girl Tech",
        "body": """
        <p>When most people hear "tech job," they imagine someone glued to a screen, typing endless lines of code. But the truth? Tech is way more diverse — and creative — than you might think. Whether you're analytical, artistic, strategic, or somewhere in between, there's a role for you. And spoiler alert: women are already killing it in these spaces.</p>
    
          <p>Here are five tech careers you <strong>might not have heard of</strong> — but that you could totally thrive in:</p>
    
          <h2>💡 UX Designer (User Experience Designer)</h2>
          <p>If you’re the kind of person who notices when an app feels clunky or a website just <em>works</em>, UX design might be your thing. UX designers make digital experiences smooth, intuitive, and user-friendly. It’s where psychology, creativity, and empathy meet design. And the best part? You don’t need to code — just an eye for what feels right.</p>
    
          <h2>🔐 Cybersecurity Analyst</h2>
          <p>Love solving puzzles or spotting when something feels off? Cybersecurity is about protecting data and systems from hackers and cyber threats. With digital safety becoming more important than ever, cybersecurity analysts are in high demand — and women are underrepresented. That means: massive opportunity.</p>
    
          <h2>🧠 Data Ethics Specialist</h2>
          <p>As tech gets smarter (think AI and big data), we need people who can ask, "Is this the right thing to do?" Data ethics specialists work at the intersection of tech, law, and morality. If you care about fairness, privacy, and accountability, this is a growing space where your voice matters.</p>
    
          <h2>🤖 AI Prompt Engineer</h2>
          <p>This one's new — and super cool. Prompt engineers write clever instructions for AI tools like ChatGPT to get the best results. It's part communication, part creativity, part logic. No coding required, just clear thinking and a playful approach to language and problem-solving.</p>
    
          <h2>📈 Product Manager</h2>
          <p>Think of this as the CEO of a product. Product managers work with designers, developers, and marketers to turn an idea into something real. If you're organised, love bringing people together, and enjoy solving problems from a big-picture view, this is your jam.</p>
    
          <p>So whether you’re tech-curious, mid-career, or just exploring — don’t let the word “tech” scare you. There’s room for storytellers, organisers, artists, thinkers, and dreamers.</p>
    
          <p><strong>The future of tech is diverse — and we want you in it.</strong></p>
        """
    },

    "networking-tips": {
        "title": "Conquer the Crowd: Networking Like a Pro (New Girl in Tech Edition!)",
        "author": "Girl Tech",
        "body": """
        <p>You’re new to tech. You’ve got your first networking event coming up. And if we’re being real? The idea of entering a room full of confident, experienced professionals is… intimidating. But don’t panic — this is your chance to shine, learn, and start building your tribe in tech!</p>
    
            <h2>🔍 Before You Go: Prep Like a Pro</h2>
            <p>Think of this as your mission briefing. Start by researching the event. Check out the speakers, scan the attendee list (if available), and look up the companies or topics being covered. This prep will help you feel grounded and give you conversation starters.</p>
    
            <p>Now, the magic move: create your elevator pitch. Just 20–30 seconds of who you are, what you’re into, and what you’re hoping to gain. Keep it natural, and practice until it flows confidently — not like a robot.</p>
    
            <p>Pro tip: pack business cards (yes, even basic ones), a notebook, and a pen. Dress smart-casual or whatever makes you feel like your most powerful self. Confidence is half the battle.</p>
    
            <h2>🌟 At the Event: Dive In</h2>
            <p>Take a breath. You belong here. Everyone started somewhere. Begin with low-pressure conversations — someone standing solo, or a small, relaxed group. Smile, introduce yourself, and ask open-ended questions like: “What brought you here today?” or “What’s been your favourite part of the event so far?”</p>
    
            <p>Listen like you mean it. Don’t just wait to speak — really engage. People appreciate feeling heard, and it makes you way more memorable.</p>
    
            <p>It’s totally okay to ask for advice! Try: “I’m new to the industry and curious about [topic] — do you have any tips for someone just starting out?” Most people love to share wisdom — and it sparks meaningful conversation.</p>
    
            <h2>📩 After the Event: Keep the Spark Alive</h2>
            <p>Networking doesn’t stop at the venue doors. Follow up within a couple of days. Send a thoughtful LinkedIn request or a quick email referencing your chat. It shows you were paying attention — and keeps the door open.</p>
    
            <p>Want to learn more from someone you clicked with? Ask for a virtual coffee. A 15-minute chat can lead to mentorship, internships, or even your next big break.</p>
    
            <h2>💬 Final Word: You’ve Got This</h2>
            <p>Tech is full of amazing, welcoming people. Show up as yourself — enthusiastic, curious, and ready to grow. Your perspective matters, and your fresh energy is an asset. </p>
    
            <p>Networking isn’t about collecting contacts. It’s about building real, human connections. So go ahead: step into that room, start that conversation, and <strong>own your space</strong> in tech.</p>
    
            <p><strong>Girl Tech’s got your back 💻💪</strong></p>
        """
    },

    "salary-talk": {
        "title": "Navigating the Numbers: Salary Talk for New Girls in Tech",
        "author": "Girl Tech",
        "body": """
        <p>Ah, the salary question — the moment that can make even the most confident tech newbie sweat. “What are your salary expectations?” or worse, “What are you currently making?” Cue the internal panic. But guess what? You’ve got this.</p>
    
            <h2>📊 Know Your Worth</h2>
            <p>Before you walk into any interview, come armed with knowledge. Use tools like Glassdoor, Payscale, and LinkedIn Salary to get a sense of the going rate for your role, experience level, and location. Your number isn’t random — it’s a reflection of your value. Research is power.</p>
    
            <h2>🚫 Skip the Salary History Trap</h2>
            <p>In many places, it’s illegal to ask about your past pay — and even where it’s legal, you don’t have to answer. Try this: <strong>“I’m focused on the value I bring to this role and prefer to discuss salary based on the market rate.”</strong> Professional, clear, and puts the focus where it belongs: forward.</p>
    
            <h2>💬 Talk Ranges, Not Exact Numbers</h2>
            <p>Instead of locking yourself into a single figure, offer a well-researched range. For example: <strong>“Based on my research, I’m looking for something in the range of 60 to 70k, depending on the full package.”</strong> Flexibility shows confidence and leaves room for negotiation.</p>
    
            <h2>🌟 Lead with Value</h2>
            <p>Don’t just talk about what you want — talk about what you bring. Highlight your skills, enthusiasm, and what you’ll contribute. <em>“With my background in UX and project coordination, I’m confident I can make an immediate impact on your product team.”</em></p>
    
            <h2>🧾 Look at the Full Picture</h2>
            <p>Salary is just one slice of the pie. Think about health benefits, remote work, learning stipends, mental health days, and career growth opportunities. These all add serious value to your total package.</p>
    
            <h2>🗣️ Practice Makes Powerful</h2>
            <p>Negotiation is a skill, and like any skill — you get better with practice. Do a mock run with a friend, mentor, or even in the mirror. The more you say it out loud, the more confident you’ll feel.</p>
    
            <h2>⏳ Take Your Time</h2>
            <p>If you’re offered something that feels off, it’s okay to ask for time. Say, <em>“Thank you — I’d love to take a day or two to consider the offer.”</em> Professional. Assertive. Respectful.</p>
    
            <p>💪 As a new girl in tech, your ideas, skills, and voice matter. Don’t be afraid to advocate for yourself. The right role will honour your worth — and you’re more than worth it.</p>
    
            <p><strong>Girl Tech’s got your back 💼💖</strong></p>
        """
    }
}

# Instead of writing a separate route for every blog post (which gets messy), use one smart route: /blog/<slug>
# A slug is a human-readable, unique identifier, used to identify a resource
# It looks up the matching post in the dictionary based on the slug in the URL
# # Then it displays that post’s content dynamically
@app.route('/blog/<slug>')
def show_blog(slug):
    post = blog_posts.get(slug)
    home_url=url_for("home")
    return f"""
        <html>
            <head>
                <title>{post['title']} | {post['author']}</title>
                
                <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
            </head>
            <body style="font-family: Arial, sans-serif; max-width: 800px; margin: auto; padding: 2rem; line-height: 1.6;">
                <h1>{post['title']}</h1>
                <p><em>By {post['author']}</em></p>
                {post['body']}
                
                <a href="{home_url}"><button type="submit" class="btn btn-primary">Back to Home</button>
                         
                <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
            </body>
        </html>
    """


@app.route('/about')
def about():
    home_url = url_for("home")
    about_url = url_for("about")
    resources_url = url_for("resources")
    join_nav_url = url_for("join")
    return """
    <html>
        <head>
            <title>About the Team</title>
            
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
        </head>
        
        <body>
            <ul class="nav nav-tabs">
                <li class="nav-item">
                <a class="nav-link" href="{}">Home</a>
                </li>
                
                <li class="nav-item">
                <a class="nav-link active" aria-current="page" href="{}">About</a>
                </li>
            
                <li class="nav-item">
                <a class="nav-link" href="{}">Resources</a>
                </li>
                
                <li class="nav-item">
                <a class="nav-link" href="{}">Join</a>
                </li>
            </ul>
        
            <h1>Meet the team behind Girl Tech</h1>
            
            <p>We are ladies from a range of backgrounds and industries, all with one thing in common - a love of tech! </p>
            
            <p>Girl Tech is powered by a passionate team of women who believe in the future of tech being diverse, inclusive, and empowering. Sakeena, Reanna, Miranda, and Titi work together to bring this vision to life—creating a space where women can connect, learn, and lead.</p>
            <br>

            <img src="static/images/girltechgirls.jpeg" alt="Meet the team">
            
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
        </body>
    </html>
    """.format(home_url, about_url, resources_url, join_nav_url)


@app.route('/resources')
def resources():
    home_url = url_for("home")
    about_url = url_for("about")
    resources_url = url_for("resources")
    join_nav_url = url_for("join")
    return """
    <html>
        <head>
            <title>Girl Tech Resources</title>
            
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
        </head>
        
        <body>
            <ul class="nav nav-tabs">
                <li class="nav-item">
                <a class="nav-link" href="{}">Home</a>
                </li>
                
                <li class="nav-item">
                <a class="nav-link" href="{}">About</a>
                </li>
            
                <li class="nav-item">
                <a class="nav-link active" aria-current="page" href="{}">Resources</a>
                </li>
                
                <li class="nav-item">
                <a class="nav-link" href="{}">Join</a>
                </li>
            </ul>
            
            <h1>Discover our resources</h1>
            <p>Welcome to the Girl Tech Resources hub — your go-to space for tools, guides, and inspiration to fuel your journey in tech.</p>
            <p> Whether you're just starting out or looking to level up, you'll find curated content to help you learn, grow, and thrive. From coding tutorials to career advice and must-read articles, it's all here to support you.</p>

             
            <style>
            .card-img-top {{height: 300px; object-fit: cover;}}
            </style>

            <div class="row">
                <div class="col-md-4 mb-4">
                    <div class="card h-100 d-flex flex-column">
                        <img src="static/images/guide.png" class="card-img-top" alt="Resource guide">
                            <div class="card-body d-flex flex-column">
                                <h5 class="card-title">Employee resource groups</h5>
                                <a href="https://www.hiretechladies.com/blog/guide-to-employee-resource-groups-ergs" class="btn btn-primary mt-auto">Access guide</a>
                            </div>
                    </div>
                </div>

                <div class="col-md-4 mb-4">
                    <div class="card h-100 d-flex flex-column">
                        <img src="static/images/jobsearch.png" class="card-img-top" alt="Job search course">
                        <div class="card-body d-flex flex-column">
                            <h5 class="card-title">Ultimate job search course</h5>
                            <a href="https://www.hiretechladies.com/blog/the-ultimate-job-search-course-for-women-in-tech" class="btn btn-primary mt-auto">Explore course</a>
                        </div>
                    </div>
                </div>

                <div class="col-md-4 mb-4">
                    <div class="card h-100 d-flex flex-column">
                        <img src="static/images/salaryreport.jpg" class="card-img-top" alt="Salary report">
                        <div class="card-body d-flex flex-column">
                            <h5 class="card-title">Girl Tech 2024 salary report</h5>
                            <a href="https://www.hiretechladies.com/blog/salary-report-2024" class="btn btn-primary mt-auto">View the report</a>
                        </div>
                    </div>
                </div>
            </div>
             
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
        </body>
    </html>
    """.format(home_url, about_url, resources_url, join_nav_url)


@app.route('/submit', methods=["POST"])
def submit():
    home_url = url_for("home")
    first_name = request.form.get("first_name")
    return """
    Thanks for joining Girl Tech, {}!"
    <p><a href="{}">Back to Home</a></p>    
    """.format(first_name, home_url)


@app.route('/join')
def join():
    home_url = url_for("home")
    about_url = url_for("about")
    resources_url = url_for("resources")
    join_nav_url = url_for("join")
    submit_url = url_for("submit")
    return """
    <html>
        <head>
            <title>Join Us</title>
            
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
        </head>
        
        <body>
            <ul class="nav nav-tabs">
                <li class="nav-item">
                <a class="nav-link" href="{}">Home</a>
                </li>
                
                <li class="nav-item">
                <a class="nav-link" href="{}">About</a>
                </li>
            
                <li class="nav-item">
                <a class="nav-link" href="{}">Resources</a>
                </li>
                
                <li class="nav-item">
                <a class="nav-link active" aria-current="page" href="{}">Join</a>
                </li>
            </ul>
            
            <h1>Join Girl Tech</h1>
            
            <p>Become part of a vibrant community where women in tech share stories, insights, and inspiration. Whether you’re here to write, read, or connect — your voice matters. Join us and help shape the future of tech, one post at a time.</p>
            
            <h3>Benefits of joining Girl Tech</h3>
            <ul>
                <li>Online community of women in tech from around the world to find support, share ideas, and build new connections.</li>
                <li>Exclusive invitations to in-person and virtual events featuring industry leaders and inspiring experts.</li>
                <li>Best-in-class content including our weekly newsletter, original research, and insider industry insights.</li>
                <li>Access to our job board with top opportunities across the tech industry.</li>
            </ul>
            
            <p>Fill out the form below to get started!</p>

            <form method="POST" action="{}">

            <div class="form-group">
                <label for="firstName">First name*</label>
                <input type="text" class="form-control" id="firstName" name="first_name" required>
            </div>

            <div class="form-group">
                <label for="lastName">Last name*</label>
                <input type="text" class="form-control" id="lastName" name="last_name" required>
            </div>

            <div class="form-group">
                <label for="email">Email*</label>
                <input type="email" class="form-control" id="email" name="email" required>
            </div>

            <div class="form-group">
                <label for="country">Country*</label>
                <input type="text" class="form-control" id="country" name="country" required>
            </div>

            <div class="form-group">
                <label for="linkedin">Your LinkedIn Profile URL*</label>
                <input type="url" class="form-control" id="linkedin" name="linkedin" placeholder="Example: https://www.linkedin.com/in/jane-doe" required>
            </div>

            <div class="form-group">
                <label for="industry">Industry you are currently working in*</label>
                <select class="form-control" id="industry" name="industry" required>
                    <option value="" disabled selected>Please Select</option>
                    <option>Software Development</option>
                    <option>Data Science</option>
                    <option>Cybersecurity</option>
                    <option>Product Management</option>
                    <option>UX/UI Design</option>
                    <option>Other</option>
                </select>
            </div>

            <div class="form-group">
                <label for="experience">Years of experience in that industry?*</label>
                <select class="form-control" id="experience" name="experience" required>
                    <option value="" disabled selected>Please Select</option>
                    <option>0-1 years</option>
                    <option>2-3 years</option>
                    <option>4-6 years</option>
                    <option>7+ years</option>
                </select>
            </div>

            <div class="form-group">
                <label for="referral">How did you find Girl Tech?*</label>
                <select class="form-control" id="referral" name="referral" required>
                    <option value="" disabled selected>Please Select</option>
                    <option>LinkedIn</option>
                    <option>Twitter/X</option>
                    <option>Friend or colleague</option>
                    <option>Search engine</option>
                    <option>Tech conference</option>
                    <option>Other</option>
                </select>
            </div>

            <button type="submit" class="btn btn-primary">Join now</button>
            </form>

            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
        </body>
    </html>
    """.format(home_url, about_url, resources_url, join_nav_url, submit_url)


# main trick
if __name__ == "__main__":
    app.run(debug=True)

