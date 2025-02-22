
import re
import argparse

def html_part1(title = ''):
    html = f"""
    <html lang="jp">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>{title}</title>
        <style>
        .container {{
            display: flex;
            align-items: flex-start;
            line-height: 2em;
            font-size: 14pt;
            gap: 2em;
        }}

        rt {{
            font-size: 7pt;
        }}

        .col {{
            width: 53%;
            height: 100vh;
        }}
        </style>
    </head>
    <body>
        <div class="container">
        <div class="col">
            {title}<br /><br />
    """

    return html

def remove_wrapper(input):
    modified = input[22:]       # remove '<div class="hiragana">'
    modified = modified[:-6]    # remove '</div>'
    return modified


def transform(input):
    regex1 = r'\s{2,}'
    input = re.sub(regex1, '', input)

    regex2 = r'<span class=ruby>\s*<span class=rb>([^<]+)<\/span>\s*<span class=rt>([^<]+)<\/span>\s*<\/span>'
    input = re.sub(regex2, r'<ruby><rb>\1</rb><rt>\2</rt></ruby>', input)

    return input

def html_part2():
    html = """
        </div>
        </div>
    </body>
    </html>
    """

    return html


def main(args):
    # get song title name from input arguments
    title = args.title or 'Song'

    # transform input lyrics into code format
    result = remove_wrapper(args.input)
    result = transform(result)

    with open(f"{title}.html", 'w') as f:

        # output html structure
        f.write(html_part1(args.title))

        # output transformed lyrics
        f.write(result)

        # output html structure
        f.write(html_part2())
        f.close
    

# this script is used to transform the lyrics from utaten
# first, find the .hiragana part on website and copy the content
# then execute this script by command: 'python lyris_transform.py --input "copied content" --title "song title"'
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process input arguments.")
    parser.add_argument("--input", type=str, required=True, help="Input string")
    parser.add_argument("--title", type=str, default="", help="Title of the song")
    args = parser.parse_args()
    main(args)
