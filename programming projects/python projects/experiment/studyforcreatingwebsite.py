import requests
from bs4 import BeautifulSoup
from time import sleep
from pyfiglet import figlet_format
from random import choice
from termcolor import colored

# --------------------------- Print ASCII Art Title -------------------------- #
# Pyfiglet colors:
eBayColors = ("red", "blue", "yellow", "green")


def print_art(msg, color):
    ascii_art = figlet_format(msg)
    colored_ascii = colored(ascii_art, color=color)
    print(colored_ascii)


print_art("eBay Search And Scrape!!!", choice(eBayColors))

# -------------------------------- List setup -------------------------------- #
# List to send unfiltered results to:
roughResults = []
# Set list for final search results:
searchResults = []

# Messages:
yesOrNo = "Enter either Y or N!!!"
nahFam = "Nah, that's not an option, fam."


# ---------------------------------------------------------------------------- #
#                              MAIN LOGIC FUNCTION                             #
# ---------------------------------------------------------------------------- #
def programLoop():
    program_loop_stop = False
    while program_loop_stop == False:
        # -------------------------------- User Inputs ------------------------------- #
        # Ask user what they want to search for:
        search_for = input("What do you want to search eBay for: ")
        # Ask max price:
        max_price_prompt = input("Would you like to set a maximum price? (Y/N): ")
        maxLoopStop = False
        while maxLoopStop == False:
            if max_price_prompt.lower() == "n":
                max_price = 10000000
                maxLoopStop = True
            elif max_price_prompt.lower() == "y":
                max_price = input("What is the most you are willing to spend: $")
                max_price = int(max_price)
                maxLoopStop = True
            else:
                print(" ")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~")
                print(yesOrNo)
                print("~~~~~~~~~~~~~~~~~~~~~~~~~")
                print(" ")
                max_price_prompt = input("Would you like to set a maximum price? (Y/N): ")
        # Ask min price:
        min_price_prompt = input("Would you like to set a minimum price? (Y/N): ")
        minLoopStop = False
        while minLoopStop == False:
            if min_price_prompt.lower() == "n":
                min_price = 0
                minLoopStop = True
            elif min_price_prompt.lower() == "y":
                min_price = input("Enter your minimum price: $")
                min_price = int(min_price)
                minLoopStop = True
            else:
                print(" ")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~")
                print(yesOrNo)
                print("~~~~~~~~~~~~~~~~~~~~~~~~~")
                print(" ")
                min_price_prompt = input("Would you like to set a minimum price? (Y/N): ")
        # Ask how many pages to scrape:
        pages_to_scrape = input("How many pages would you like to scrape?: ")

        try:
            pages_to_scrape = int(pages_to_scrape)
        except ValueError:
            try:
                print(" ")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("You have to enter an integer!")
                print("Try one more time!")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print(" ")
                pages_to_scrape = input("How many pages would you like to scrape?: ")
                pages_to_scrape = int(pages_to_scrape)
            except ValueError:
                print(" ")
                print(" ")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("You broke me because you didn't listen! Enter an integer next time!")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print(" ")
                print(" ")

        reverse_check_prompt = input(
            "In what order would you like your results? ('a' for Ascending/'d' for Descending): ")
        reverse_prompt_loop_stop = False
        while reverse_prompt_loop_stop == False:
            if reverse_check_prompt.lower() == "a" or reverse_check_prompt.lower() == "d":
                reverse_prompt_loop_stop = True
            else:
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print(nahFam)
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                reverse_check_prompt = input("In what order would you like your results? (Ascending/Descending): ")

        # --------------------------------- Functions -------------------------------- #
        # Scraper function:
        def scrapeIt(num_of_pages=pages_to_scrape, search_for=search_for):
            # Base url to scrape:
            baseURL = "https://www.ebay.com"
            # Search url (/sch/) with Buy It Now (&LH_BIN=1) and page-url beginning:
            searchURL = f"/sch/{search_for}&LH_BIN=1&_pgn="
            pageNum = "1"
            # URL all put together:
            url = f"{baseURL}{searchURL}{pageNum}"
            # Page count:
            count = pages_to_scrape
            while count > 0:
                # Increase page number
                def pageNumPlus(num):
                    num = int(num)
                    num += 1
                    return str(num)

                # Make http request:
                response = requests.get(f"{url}")
                print(f"Now scraping: {url}")
                print(" ")
                # Send through Beautiful Soup:
                soup = BeautifulSoup(response.text, "html.parser")
                # Search Results
                results = soup.find_all(class_="s-item")

                # Assign Keys:
                for result in results:
                    try:
                        # Send to list:
                        roughResults.append({
                            "title": result.find(class_="s-item__title").get_text(),
                            "price": result.find(class_="s-item__price").get_text(),
                            "link": result.find(class_="s-item__link")["href"]
                        })
                    # Catch AttrErrors and pass by:
                    except AttributeError:
                        pass

                # Increase page number:
                pageNum = pageNumPlus(pageNum)
                # Reset url:
                url = f"{baseURL}{searchURL}{pageNum}"
                count -= 1
                # Give ten seconds before requesting next page
                sleep(10)

            return roughResults

        # Filter out results with range of prices:
        def removeResultsWithRange(lst=roughResults):
            for result in roughResults:
                to = "to"
                price = result['price']
                if to not in price:
                    searchResults.append(result)
            return searchResults

        # Sort the results and print to command line:
        def sortAndShow(list_of_results=searchResults, order=reverse_check_prompt, max_price=max_price,
                        min_price=min_price, search_for=search_for):
            # If there are search results:
            if len(list_of_results) > 0:
                for eachDict in list_of_results:
                    # Remove '$' and ',' from price string to change to float for sorting:
                    eachDict['price'] = eachDict['price'].replace("$", "")
                    eachDict['price'] = eachDict['price'].replace(",", "")

            # Choose ascending or descending:
            if order.lower() == "d":
                list_of_results = sorted(list_of_results, reverse=True, key=lambda i: float(i['price']))
            else:
                list_of_results = sorted(list_of_results, key=lambda i: float(i['price']))

            # List of acceptable prices:
            acceptablePrices = []
            # Clear acceptablePrices list in between searches:
            del acceptablePrices[:]
            # Go through search results:
            for item in list_of_results:
                # Keep search between price parameters:
                if float(item['price']) <= int(max_price) and float(item['price']) >= int(min_price):
                    acceptablePrices.append(item)

            if len(acceptablePrices) == 0:
                print(f"No results for '{search_for}' in the range of ${min_price} and ${max_price}")
            else:
                for item in acceptablePrices:
                    print(item['title'])
                    print(item['price'])
                    print(item['link'])
                    print(" ")

        # ------------------------------ Function Calls ------------------------------ #
        scrapeIt()
        removeResultsWithRange()
        sortAndShow()

        # ------------------------------- Search Again? ------------------------------ #
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        search_again_loop_stop = False
        while search_again_loop_stop == False:
            search_again = input("Would you like to search again? (Y/N): ")
            if search_again.lower() == "n":
                program_loop_stop = True
                search_again_loop_stop = True
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("Ok... See you later, bruv!")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            elif search_again.lower() == "y":
                program_loop_stop = False
                search_again_loop_stop = True
            else:
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print(nahFam)
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


# ---------------------------------------------------------------------------- #
#                          END OF MAIN LOGIC FUNCTION                          #
# ---------------------------------------------------------------------------- #

# Let's run this thing!
programLoop()