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
            
            <div class="row">
                <div class="col-md-4">
                    <div class="card" style="width: 18rem;">
                        <img src="static/images/girltechcareers.jpeg" class="card-img-top" alt="Tech careers">
                        <div class="card-body">
                            <h5 class="card-title">Tech Careers You Have Never Heard Of But Could Totally Rock</h5>
                            <p class="card-text">Discover exciting, lesser-known tech careers where creativity and curiosity thrive — and women are leading the way.</p>
                            <a href="{}" class="btn btn-primary">Read more</a>
                        </div>
                    </div>
                </div>
            
                <div class="col-md-4">
                    <div class="card" style="width: 18rem;">
                        <img src="static/images/networking.jpeg" class="card-img-top" alt="Networking">
                        <div class="card-body">
                            <h5 class="card-title">Conquer The Crowd: Networking Like a Pro</h5>
                            <p class="card-text">A beginner-friendly guide to confidently navigating your first tech networking event, from prep to follow-up.</p>
                            <a href="{}" class="btn btn-primary">Read more</a>
                        </div>
                    </div>
                </div>
            
                <div class="col-md-4">
                    <div class="card" style="width: 18rem;">
                        <img src="static/images/salary.jpg" class="card-img-top" alt="Salary">
                        <div class="card-body">
                            <h5 class="card-title">Navigating the Numbers: Salary Talk for New Girls in Tech</h5>
                            <p class="card-text">Learn how to handle salary conversations with confidence and strategy as a newcomer in tech.</p>
                            <a href="{}" class="btn btn-primary">Read more</a>
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
    home_url = url_for("home")
    name = request.form.get("name")
    return """Thanks for subscribing to our newsletter, {}. 
    <p><a href="{}">Back to Home</a></p>    
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
        <p>If you’re the kind of person who notices when an app feels clunky or a website just <em>works</em>, UX design might be your thing...</p>

        <h2>🔐 Cybersecurity Analyst</h2>
        <p>Love solving puzzles or spotting when something feels off? Cybersecurity is about protecting data...</p>

        <h2>🧠 Data Ethics Specialist</h2>
        <p>As tech gets smarter (think AI and big data), we need people who can ask, "Is this the right thing to do?"...</p>

        <h2>🤖 AI Prompt Engineer</h2>
        <p>This one's new — and super cool. Prompt engineers write clever instructions for AI tools like ChatGPT...</p>

        <h2>📈 Product Manager</h2>
        <p>Think of this as the CEO of a product. Product managers work with designers, developers, and marketers...</p>

        <p><strong>The future of tech is diverse — and we want you in it.</strong></p>
        """
    },

    "networking-tips": {
        "title": "Conquer the Crowd: Networking Like a Pro (New Girl in Tech Edition!)",
        "author": "Girl Tech",
        "body": """
        <p>You’re new to tech. You’ve got your first networking event coming up. And if we’re being real? The idea of entering a room full of confident, experienced professionals is… intimidating. But don’t panic — this is your chance to shine, learn, and start building your tribe in tech!</p>

        <h2>🔍 Before You Go: Prep Like a Pro</h2>
        <p>Think of this as your mission briefing. Start by researching the event...</p>

        <h2>🌟 At the Event: Dive In</h2>
        <p>Take a breath. You belong here. Everyone started somewhere...</p>

        <h2>📩 After the Event: Keep the Spark Alive</h2>
        <p>Networking doesn’t stop at the venue doors. Follow up within a couple of days...</p>

        <p><strong>Girl Tech’s got your back 💻💪</strong></p>
        """
    },

    "salary-talk": {
        "title": "Navigating the Numbers: Salary Talk for New Girls in Tech",
        "author": "Girl Tech",
        "body": """
        <p>Ah, the salary question — the moment that can make even the most confident tech newbie sweat. “What are your salary expectations?” or worse, “What are you currently making?” Cue the internal panic. But guess what? You’ve got this.</p>

        <h2>📊 Know Your Worth</h2>
        <p>Before you walk into any interview, come armed with knowledge...</p>

        <h2>🚫 Skip the Salary History Trap</h2>
        <p>In many places, it’s illegal to ask about your past pay...</p>

        <h2>💬 Talk Ranges, Not Exact Numbers</h2>
        <p>Instead of locking yourself into a single figure, offer a well-researched range...</p>

        <h2>🌟 Lead with Value</h2>
        <p>Don’t just talk about what you want — talk about what you bring...</p>

        <p><strong>Girl Tech’s got your back 💼💖</strong></p>
        """
    }
}


# A slug is a human-readable, unique identifier, used to identify a resource
# You use a slug when you want to refer to an item while preserving the ability to see, at a glance, what the item is
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

             <p>
                <h2>Employee resource groups</h2>
                <a href="https://www.hiretechladies.com/blog/guide-to-employee-resource-groups-ergs">Access the guide</a>
             </p>

             <p>
                <h2>Ultimate job search course</h2>
                <a href="https://www.hiretechladies.com/blog/the-ultimate-job-search-course-for-women-in-tech">Learn about the course</a>
                </p>

             <p>
                <h2>Girl Tech 2024 salary report</h2>
                <a href="https://www.hiretechladies.com/blog/the-ultimate-job-search-course-for-women-in-tech">View the report</a>
            </p>
           
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

