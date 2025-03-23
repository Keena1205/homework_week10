from flask import Flask, request, url_for

app = Flask(__name__)


@app.route('/home')
def home_from_flask():
    url = url_for("join_from_flask")
    return """
    <html>
        <head>
            <title>Girl Tech</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
        </head>
        <body>
            <h1>Girl Tech Blog</h1>
            <p>Welcome to this blog where you can find resources for women in technology.</p>
            <p>Interested in joining our community? Join now!</p>
            <hr>
            <a href="{}">Join Now!</a>
            <h2><button type="button" class="btn">Subscribe</button></h2>
            <form method="POST" action="{{ url_for('subscribe') }}">
            <form method="POST" action="{{ url_for('subscribe') }}">
            <div class="form-group">
            <label for="exampleInputEmail1">Email address</label>
            <input type="email" class="form-control" id="exampleInputEmail1" name="email" placeholder="Enter email" required>
            <small id="emailHelp" class="form-text text-muted">We'll never share your email with anyone else.</small>
            </div>
            <button type="submit" class="btn btn-primary">Subscribe</button>
            </form>
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
        </body>
    </html>
    """.format(url)


@app.route('/about')
def about_from_flask():
    return """
    <html>
        <head>
            <title>About Girls in Tech</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
        </head>
        <body>
            <h1>About Us</h1>
            <p>We are ladies from a range of backgrounds and industries, all with one thing in common - a love of tech! </p>
            <p>We’re here to celebrate, inspire, and empower women in technology. From coding breakthroughs to industry insights, we share stories, advice, and resources to help girls and women thrive in the tech world. Whether you're a beginner, a pro, or just curious about tech, this is your space to learn, connect, and grow.</p>
            <p>We support 140,000+ women in all areas of tech, including engineering, design, product management, marketing, and more. Women in the technology industry often feel like they’re on an island, facing unique obstacles and lacking support.</p>
            
            <p>Girl Tech is a safe space to share experiences, while also recognizing and celebrating our differences. Join forces with our incredible community, where fellow women in tech around the world share challenges, celebrate successes, and swap best practices for professional and personal growth!</p>
            <img src="{{ url_for('static', filename='girltechimage/girl_tech.png') }}" alt="About Us">
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
        </body>
    </html>
    """


@app.route('/resources')
def resources_from_flask():
    return """
    <html>
        <head>
            <title>Girls in Tech Resources</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
        </head>
        <body>
            <h1>Discover the Best Resources for Girls in Tech</h1>
            <p>We support 140,000+ women in all areas of tech, including engineering, design, product management, marketing, and more to build their dream career. Explore our resources below</p>
            
             <p><a href="https://www.hiretechladies.com/blog/guide-to-employee-resource-groups-ergs" target="_blank">Guide to Employee Resource Groups (ERGS)</a></p>
             
             <p><a href="https://www.hiretechladies.com/blog/the-ultimate-job-search-course-for-women-in-tech" target="_blank">Ultimate Job Search Course for Women in Tech</a></p>
             
             <p><a href="https://www.hiretechladies.com/blog/the-ultimate-job-search-course-for-women-in-tech" target="_blank">Tech Ladies Salary Report 2024</a></p>
            
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
        </body>
    </html>
    """


@app.route('/join')
def join_from_flask():
    return """
    <html>
        <head>
            <title>Join Us!</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
        </head>
        <body>
            <h1>Join Girl Tech</h1>
            <p>Online community of other women in tech all over the world to find support, ideas, and new connections.</p>

            <p>Exclusive invitations to in-person and virtual events featuring industry leaders and other experts.</p>

            <p>Best-in-class content including our weekly newsletters, proprietary research, and other industry intel.</p>

            <p>Access to our job board with the best jobs in technology.</p>
                        
            <form method="POST" action="{{ url_for('submit') }}">
            
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

            <button type="submit" class="btn btn-primary">Join Now</button>
            </form>
   
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
        </body>
    </html>
    """




#main trick
if __name__ == "__main__":
    app.run(debug=True)