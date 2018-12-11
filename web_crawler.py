''' Extracting Video Title from a youtube playlists '''
import time  # to calculate the execution time
from main import PlotFrame

t1 = time.time()


import requests


def writeSourceContentToTextFile(response_content_list):
    # writing the source content to a text file
    with open('page_source.txt', 'w') as file:
        for i in response_content_list:
            file.write(i + '\n')
        file.close()


def extractTilesFromSourceContent(response_content_list):
    titles = []
    # with open('page_source.txt', 'r') as file_r:
    for line in response_content_list:
        f_index = line.find("data-title=")  # > 3000
        if f_index != -1:
            start_index = f_index + 12
            req_str = ''
            while line[start_index] != '"':
                req_str = req_str + line[start_index]
                start_index += 1

            titles.append(req_str)
    return titles


def getSourceContent(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    response = requests.get(url, headers=headers)
    response_content = response.content
    response_content_list = str(response_content).split('\\n')
    # print('Number of lines in the SourceFile: ', len(response_content_list))

    return response_content_list




''' returns list of titles of the passed url '''
def extract(url):
    # if url == '':
    #     PlotFrame().setStatusToEnterCorrectUrl()
    # gets the source content of the passed url in string format
    response_content_list = getSourceContent(url)

    # -----------------------------
    # writes the source content to a text file

    # writeSourceContentToTextFile(response_content_list)

    # -----------------------------
    ''' Extracting the titles '''
    titles = extractTilesFromSourceContent(response_content_list)

    print('Number of videos: ', len(titles))

    # writing the extracted titles to a text file
    # with open('extracted_titles.txt', 'w') as file_w:
    #     file_w.write('url= ' + url + '\n\n')
    #     for count, value in enumerate(titles):
    #         file_w.write(str(count + 1) + "  " + value)
    #
    #         file_w.write('\n')

    return titles

    # print("\nCheck 'source_1_titles.txt' file for list the of titles!")
    # print('It took {} sec(s) to complete the task!'.format(round(time.time() - t1)))
