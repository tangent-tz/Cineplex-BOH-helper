def filter_movie_names(movie_name):
    for index in range(len(movie_name)):
        movie_name[index] = movie_name[index].replace(' ', '')
    return movie_name


def filter_extra_info(movie_time, movie_name):
    tofilter = ['pairedandDescriptiveServiceforthevisuallyim',
              'paired(CC/DS)3DATMOSULTRAAVXReclinerSeatsFAUTEUILSINCLINABLES(CC/DS)',
              'trailerClosedCaptionsforthehearingim', 'ClosedCaptionsforthehearingim',
              'Nopassestrailer3DATMOSULTRAAVXReclinerSeatsFAUTEUILSINCLINABLES', 'Nopassestrailer', '||', '|||',
              'trailer', 'Nopasses', '3DATMOSULTRAAVXReclinerSeatsFAUTEUILSINCLINABLES']
    extra_filters = filter_movie_names(movie_name)
    for index in range(len(extra_filters)):
        tofilter.append(extra_filters[index])
    for index in range(len(tofilter)):
        movie_time = movie_time.replace(tofilter[index], '')
    return movie_time


def filter_movie_time_data(movie_time):
    movie_time = movie_time.replace(' ', '')
    movie_time = movie_time.replace('0pm', '0pm|')
    movie_time = movie_time.replace('5pm', '5pm|')
    movie_time = movie_time.replace('0am', '0am|')
    movie_time = movie_time.replace('5am', '5am|')
    movie_time = movie_time.replace('SOLDOUT', '')
    return movie_time
