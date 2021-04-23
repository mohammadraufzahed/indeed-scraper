import requests
from bs4 import BeautifulSoup


def get_jobs() -> list:
    # Take the job title and location from user
    job_title = input("Please enter the job title (Python,Javascript) > ")
    location = input("Please enter where you are (USA,Germany) > ")
    # Prepare the url
    url = f"https://www.indeed.com/jobs?q={job_title}&l={location}"
    # Send a request
    r = requests.get(url).text
    # Parse the html page
    soup = BeautifulSoup(r, "lxml")
    # Export data from parsed html
    jobs_table = soup.find("table", id='pageContent')
    jobs_box = jobs_table.find("td", id="resultsCol")
    all_jobs = jobs_box.find_all("div", class_="jobsearch-SerpJobCard")
    for job in all_jobs:
        # Return the received data
        yield {
            "title": job.h2.text.strip(),
            "company": job.find("span", class_="company").text.strip(),
            # "salary": job.find("span", class_="salary").text,
            "summery": job.find("div", class_="summary").text.strip()

        }


if __name__ == "__main__":
    jobs = get_jobs()
    for job in jobs:
        job_title = job["title"]
        job_company = job["company"]
        # job_salary = job["salary"]

        print("*"*10)
        print(f"Title: {job_title}")
        print(f"Company: {job_company}")
        # print(f"Salary: {job_salary}")
        print("*"*10)
