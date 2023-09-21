import requests


def linkshrink(link, name):
    # Change the API Key below and this will work. Goto "https://cutt.ly/edit" and generate a new API"
    api_key = '25668bc30c641e9433fb9808afb110385b253'
    base_url = 'https://cutt.ly/api/api.php'

    payload = {'key': api_key, 'short': link, 'name': name}
    request = requests.get(base_url, params=payload)
    packets = request.json()

    print('')

    try:
        title = packets['url']['title']
        shrinklink = packets['url']['shortLink']

        print(f"Title: {title}\n"
              f"Link: {shrinklink}")

    except:
        status = packets['url']['status']
        print(f"Error Status: {status}")


print("All (*) fields are mandatory!")
inputLink = input("Enter the link here (*): ")
inputName = input("Enter your desired name: ")

linkshrink(inputLink, inputName)
