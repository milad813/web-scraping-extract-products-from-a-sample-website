# ############ Category ############
def get_category(soup):
    category = soup.find(name="span", class_='navigation_page').text.split(">")
    category = "".join(category[1:len(category) - 1])
    return category


# ############ Content ############
def get_content(soup):
    try:
        content = soup.select_one("#descriptionTab").text.replace("\n", " ").replace("\t", " ")
    except:
        content = ""

    return content


# ############ Details ############
def get_details(soup):
    try:
        details = ""
        t_col = soup.select("td.first-row")
        t_spec = soup.select("td.row")
        if len(t_col) == len(t_spec):
            for _ in range(len(t_col)):
                details += f"{t_col[_].text}\t{t_spec[_].text}\t"
        else:
            new_col = []
            junk_col = []
            for item in t_col:
                try:
                    row_span = int(item.get('rowspan'))
                    for i in range(row_span):
                        new_text = item.getText()
                        new_text += f"({t_col[t_col.index(item) + i + 1].getText()})"
                        new_col.append(new_text)
                        junk_col.append(t_col[t_col.index(item) + i + 1])
                except:
                    if item not in junk_col:
                        new_col.append(item.text)

            for _ in range(len(new_col)):
                details += f"{new_col[_]}\t{t_spec[_].text}\t"
    except:
        details = ""
    return details


# ############ Details ############
def get_guaranty(soup):
    try:
        guaranty_title = soup.find(name="p", class_="guarantee-title").text
        guaranty_title = f"گارانتی\t{guaranty_title}"
    except:
        guaranty_title = ""
    try:
        guaranty_text = soup.find(name="li", class_="guarantee").text
        guaranty_text = f"گارانتی\t{guaranty_text}"
    except:
        guaranty_text = ""

    return guaranty_title, guaranty_text


# ############ Images ############
def get_images(soup, folder_name):
    images = soup.find_all(name="a", class_="fancybox")
    image_urls = [item.get("href") for item in images]
    image_list = []
    for url in image_urls:
        image_name = image_urls.index(url) + 1
        image_list.append(f"https://damava.ir/wp-content/uploads/2022/new/sarmayesh/{folder_name}/{image_name}.jpg")
        # os.mkdir(f"garmayesh/images/{folder_name}")
        # image = requests.get(url=url).content
        # with open(f"./garmayesh/images/{folder_name}/{image_name}.jpg", "wb") as data_file:
        #     data_file.write(image)

    image_urls = ",".join(image_list)

    return image_urls


# ############ Price ############
def get_price(soup):
    display = soup.find(name="div", class_="price").get("style")
    if display == "display: none;":
        price = ""
    else:
        price = soup.select_one("#our_price_display").get("content")

    return price


# ############ Short desc ############
def get_short_desc(soup):
    desc = soup.find_all(name="li", class_="feature-list")
    short_desc = ""
    for item in desc[:len(desc) - 1]:
        short_desc += f"<li>{str(item.text)}</li>"
    short_desc = f"<ol>{short_desc}</ol>"
    return short_desc
