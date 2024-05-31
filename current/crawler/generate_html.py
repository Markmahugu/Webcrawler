import json

def generate_html(json_file, output_html):
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    html_content = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Team Scores</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                background-color: #f4f4f4;
            }
            .container {
                width: 80%;
                margin: auto;
                overflow: hidden;
            }
            header {
                background: #333;
                color: #fff;
                padding-top: 30px;
                min-height: 70px;
                border-bottom: #77aaff 3px solid;
            }
            header a {
                color: #fff;
                text-decoration: none;
                text-transform: uppercase;
                font-size: 16px;
            }
            header ul {
                padding: 0;
                list-style: none;
            }
            header li {
                display: inline;
                padding: 0 20px 0 20px;
            }
            header #branding {
                float: left;
            }
            header #branding h1 {
                margin: 0;
            }
            header nav {
                float: right;
                margin-top: 10px;
            }
            .showcase {
                min-height: 400px;
                background: url('showcase.jpg') no-repeat 0 -400px;
                text-align: center;
                color: #fff;
            }
            .showcase h1 {
                margin-top: 100px;
                font-size: 55px;
                margin-bottom: 10px;
            }
            .showcase p {
                font-size: 20px;
            }
            .main-content {
                padding: 20px;
                background: #fff;
                margin-top: 20px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            }
            .team {
                margin-bottom: 20px;
            }
            .team h2 {
                color: #333;
                margin-bottom: 10px;
            }
            .team p {
                color: #666;
            }
            footer {
                background: #333;
                color: #fff;
                text-align: center;
                padding: 10px 0;
                margin-top: 20px;
            }
        </style>
    </head>
    <body>
        <header>
            <div class="container">
                <div id="branding">
                    <h1>Team Scores</h1>
                </div>
                <nav>
                    <ul>
                        <li><a href="#">Home</a></li>
                    </ul>
                </nav>
            </div>
        </header>
        <section class="main-content container">
    '''

    for item in data:
        html_content += f'''
        <div class="team">
            <h2>{item['team_name']}</h2>
            <p>{'<br>'.join(item['team_stats'])}</p>
        </div>
        '''

    html_content += '''
        </section>
        <footer>
            <p>Scraped Data &copy; 2024</p>
        </footer>
    </body>
    </html>
    '''

    with open(output_html, 'w', encoding='utf-8') as f:
        f.write(html_content)

# Generate the HTML page
generate_html('output.json', 'output.html')
