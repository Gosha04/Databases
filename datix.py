import requests as requests
from bs4 import BeautifulSoup


def retrieve(docURL):
    response = requests.get(url=docURL)
    assert response.status_code == 200, 'Wrong status code'

    soup = BeautifulSoup(response.text, 'html.parser')
    
    # with open("google_doc.html", "w", encoding="utf-8") as f:
    #     f.write(soup.prettify())
    
    table = soup.find('table')

    coords = []
    rows = table.find_all('tr')
    for i, row in enumerate(rows):
        if i == 0:
            continue
        cells = row.find_all(['td', 'th'])

        x = cells[0].get_text(strip=True)
        char = cells[1].get_text(strip=True)
        y = cells[2].get_text(strip=True)
        coords.append((x, char, y))
    return coords

def printTable(coords):
    max_x = max(int(x) for x, _, _ in coords)
    max_y = max(int(y) for _, _, y in coords)

    grid = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    for x, char, y in coords:
        x = int(x)
        y = int(y)
        grid[y][x] = char

    for row in reversed(grid):
        print(''.join(row))

def main(docUrl):
    coords = retrieve(docUrl)
    printTable(coords)

main('https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub')