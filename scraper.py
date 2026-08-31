import logging
from config import HEADERS
import requests
from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)

def fetch_page(url):
    try:
        response = requests.get(url, timeout=30, headers=HEADERS)

        response.raise_for_status()

        logger.info(f"successfully fetched: {url}")
        soup = BeautifulSoup(response.text, "html.parser")
        return soup
    except requests.RequestException as error:
        logger.error(f"Failed to fetch: {url}")
        raise


def scrape_abu(url):
    soup = fetch_page(url)
    records = []
    university_name = "Ahmadu Bello University"
    Faculty = soup.find("div", class_="department-label text-left")
    Faculty = Faculty.find("h3").text
    staff_section = soup.find("section", class_="team-style2 section")
    staffs_tag = staff_section.find_all("div", class_="col-lg-3 col-md-6 col-12")
    for staff in staffs_tag:
        if staff is not None:
            name_tag = staff.find("h4", class_="name")
        position_tag = name_tag.find("span")

        if name_tag is None:
            logger.warning("Skipping one staff entry - no name tag found")
            continue
        name = name_tag.contents[0].strip()

        position = ""
        if position_tag is not None:
            position = position_tag.text.strip()

        image_tag = staff.find("img")
        if image_tag is not None:
            image_url = image_tag["src"]
            image_url = (f"https://engineering.abu.edu.ng/{image_url}")

        if image_url == "https://engineering.abu.edu.ng/assets/images/staff/20.jpeg":
            logger.warning(f"Blank image detected for {name}, marking image_url as not Found")
            image_url = "Image not Found"

        record = {
            "University": university_name,
            "Faculty": Faculty,
            "Department": "not Specified",
            "Name": name,
            "Position": position,
            "Image_url": image_url

        }

        records.append(record)
    return records

def scrape_Unilorin(url):
    soup = fetch_page(url)
    records = []
    university_name = "University of illorin"
    Department = soup.find("div", class_="header-sitename").text
    Faculty_tag = soup.find("div", class_="breadcrumb")
    Faculty_tag = Faculty_tag.find_all("a")
    Faculty_name = Faculty_tag[1].text.strip()
    staffs_tag = soup.find_all("div", class_="col-lg-2 col-md-6 col-sm-6")

    for staff in staffs_tag:
        staffs = staff.find("div", class_="campus-content")
        if staffs is not None:
            name_tag = staffs.find("a")

        if name_tag is None:
            logger.warning("Skipping one staff entry - no name tag found")
            continue

        name = name_tag.find("h2").text

        position_tag = staff.find("h4")

        position = "N/A"
        if position_tag is None:
            logger.warning("position tag not Found")
        else:
            position = position_tag.text

        image_url = "Image not Found"
        image_tag = staff.find("div", class_="img")
        if image_tag is not None:
            image_tag = image_tag.find("img")
            if image_tag is not None:
                image_url = image_tag["src"]
        else:
            logger.warning(f"Blank image detected for {name}, marking image_url as not Found")
            image_url = "Image not Found"

        record = {
            "University": university_name,
            "Faculty": Faculty_name,
            "Department": Department,
            "Name": name,
            "Position": position,
            "Image_url": image_url
        }

        records.append(record)
    return records


def  scrape_university(university,url):
    university = university.strip().lower()
    if university == "ahmadu bello university":
        return scrape_abu(url)
    elif university == "university of illorin":
        return scrape_Unilorin(url)
    else:
        logger.warning(f"No scraper available for {university}")


    return []




