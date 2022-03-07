def filterMovieNames(movie_name):
    for index in range(len(movie_name)):
        movie_name[index] = movie_name[index].replace(' ', '')
    return movie_name


def filterJunkText(movie_time, movie_name):
    junk_text = ['pairedandDescriptiveServiceforthevisuallyim',
              'paired(CC/DS)3DATMOSULTRAAVXReclinerSeatsFAUTEUILSINCLINABLES(CC/DS)',
              'trailerClosedCaptionsforthehearingim', 'ClosedCaptionsforthehearingim',
              'Nopassestrailer3DATMOSULTRAAVXReclinerSeatsFAUTEUILSINCLINABLES', 'Nopassestrailer', '||', '|||',
              'trailer', 'Nopasses', '3DATMOSULTRAAVXReclinerSeatsFAUTEUILSINCLINABLES']
    extra_filters = filterMovieNames(movie_name)
    for index in range(len(extra_filters)):
        junk_text.append(extra_filters[index])
    for index in range(len(junk_text)):
        movie_time = movie_time.replace(junk_text[index], '')
    return movie_time


def filterJunkTime(movie_time):
    movie_time = movie_time.replace(' ', '')
    movie_time = movie_time.replace('0pm', '0pm|')
    movie_time = movie_time.replace('5pm', '5pm|')
    movie_time = movie_time.replace('0am', '0am|')
    movie_time = movie_time.replace('5am', '5am|')
    movie_time = movie_time.replace('SOLDOUT', '')
    return movie_time
