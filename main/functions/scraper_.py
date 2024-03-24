"""List.am scraper"""

# We need to scrap all list.am products.


import requests
from bs4 import BeautifulSoup
import time
import random
import re


class Scraper:
    """
        Waits as an input URL of product and will scraps all possible data from the website.

        attr: url(string)

    """

    cookies = {
        '__stripe_mid': '5609d0b6-25d2-497e-9a87-92033cabc672ae7986',
        '_gid': 'GA1.2.392915301.1668416499',
        '__stripe_sid': 'a126b9c1-39c1-4567-84ce-9644b8eba781390794',
        'lang': '0',
        '_ga_KVLP4BC4K8': 'GS1.1.1668416499.20.1.1668417668.0.0.0',
        '_ga': 'GA1.1.1201303053.1651760819',
    }

    headers = {
        'authority': 'www.list.am',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-US,en;q=0.9',
        'dnt': '1',
        'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
        'cookie': '__stripe_mid=5609d0b6-25d2-497e-9a87-92033cabc672ae7986; _gid=GA1.2.392915301.1668416499; __stripe_sid=a126b9c1-39c1-4567-84ce-9644b8eba781390794; lang=0; u=00066x72r8d84aed98660295500a12365cd3813be96640de18f3f59; _ga_KVLP4BC4K8=GS1.1.1668416499.20.1.1668418315.0.0.0; _ga=GA1.1.1201303053.1651760819',
    }

    params = {
        'w': '11',
        'i': '18056418',
    }

    scrap = {}

    def __init__(self, url):

        self.url = url

        self.url_en = "".join(
            ['https://www.list.am/en/item/', self.url.split('/')[-1]])
        self.url_am = "".join(
            ['https://www.list.am/am/item/', self.url.split('/')[-1]])

        time.sleep(random.randint(1, 5))

        self.response_en = requests.get(
            self.url_en, cookies=self.cookies, headers=self.headers, verify=False)
        self.html_soup_en = BeautifulSoup(self.response_en.text)

        self.response_am = requests.get(
            self.url_am, cookies=self.cookies, headers=self.headers, verify=False)
        self.html_soup_am = BeautifulSoup(self.response_am.text)

    def get_url(self):
        """Gets item url"""

        self.scrap['url'] = self.url

    def get_header(self):
        """Gets Item Title"""

        header = self.html_soup_am.find('h1', {'itemprop': "name"})

        if header:
            self.scrap['header'] = header.text

    def get_price(self):
        """Gets item price"""

        price_div = self.html_soup_en.find('div', {'class': 'price'})

        if price_div:
            price_spans = price_div.find_all('span')

            if price_spans:
                bool_ = False
                for pr in price_spans:
                    if re.search('֏', pr.text):
                        bool_ = True
                        break
                if bool_:
                    price = list(filter(lambda span: re.findall(
                        '֏$', span.text), price_spans))
                    
                    price_ = list(filter(lambda span: re.findall(
                        '֏', span.text), price_spans))
                    
                    if price:
                        self.scrap['price'] = price[0].text
                    elif price_:
                        self.scrap['price'] = price_[0].text

                    self.scrap['value'] = 'AMD'

    def get_image(self):
        """Gets item main image"""

        content = self.html_soup_en.find('div', {'id': 'pcontent'})

        if content:

            main_image = "".join(['https:', content.find('img')['src']])
            self.scrap['main_image'] = main_image

    def get_seller_info(self):
        """Gets information about seller"""

        seller = self.html_soup_en.find('div', {'id': 'uinfo'})

        seller_ = {}

        if seller:

            seller_link = seller.find('a')

            seller_link_ = "".join(['list.am', str(seller_link['href'])])

            seller_['list_url'] = seller_link_

            seller_name = seller_link.text

            seller_['name'] = seller_name

            seller_avatar = seller_link.find('img')['src']

            seller_['image'] = seller_avatar

            id = self.url.split('/')[-1]

            phone_req_url = "".join(['https://www.list.am/?w=12&&i=', id])

            time.sleep(random.randint(1, 5))

            phone_request = requests.get(
                phone_req_url, cookies=self.cookies, headers=self.headers, verify=False)

            html_soup_phone = BeautifulSoup(phone_request.text)

            tel = html_soup_phone.find_all('a')

            if tel:

                for t in tel:
                    if re.search('href="tel:', str(t)):
                        break

                seller_['phone'] = t.text

            self.scrap['seller'] = seller_

    def get_description(self):
        """Gets item description"""

        body_desc = self.html_soup_am.find('div', {'class': 'body'})

        if body_desc:

            description = body_desc.text

            self.scrap['description'] = description

    def get_type(self):
        """Gets item type"""

        type_ = self.html_soup_en.find('div', {'id': 'crumb'})

        if type_:

            crumb_span = type_.find_all('span', {'itemprop': 'name'})

            crumb_index = len(crumb_span) - (len(crumb_span) // 2) - 1

            type_item = crumb_span[crumb_index].text

            self.scrap['type'] = type_item

    def get_properties(self):
        """Gets item properties"""

        info = self.html_soup_en.find_all('div', {'class': 'attr'})
        information = self.html_soup_en.find_all('div', {'class': 'attr g'})
        information_am = self.html_soup_am.find_all('div', {'class': 'c'})

        if information or info:
            properties = {}
            t_ = self.html_soup_en.find_all('div', {'class': 't'})
            i_ = self.html_soup_am.find_all('div', {'class': 'i'})

            for i in range(len(t_)):
                properties[t_[i].text] = i_[i].text

            self.scrap['properties'] = properties

    def get_post_info(self):
        """Gets information about post"""

        footer = self.html_soup_en.find('div', {'class': 'footer'})

        if footer:

            footer_list = footer.find_all('span')

            if footer_list[0]:
                ad_id = footer_list[0].text.split()[2]
                self.scrap['ad_id'] = ad_id

            if len(footer_list) > 1:
                posted = footer_list[1].text.split()[1]
                self.scrap['posted'] = posted

            if len(footer_list) > 2:
                renewed = footer_list[2].text.split()[1]
                self.scrap['renewed'] = renewed

    def scrap_list_am(self):
        """Scraps all information"""

        if not re.search('https://www.list.am/', self.url) or (self.response_am.status_code != 200 or self.response_en.status_code != 200):
            return 'Wrong link'

        self.get_url()
        self.get_header()
        self.get_price()
        self.get_image()
        self.get_seller_info()
        self.get_description()
        self.get_type()
        self.get_properties()
        self.get_post_info()

        return self.scrap