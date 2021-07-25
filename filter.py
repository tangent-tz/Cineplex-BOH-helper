

def filtermovienames(movie_name):
    for i in range(len(movie_name)):
        movie_name[i]=movie_name[i].replace(' ','')
    return movie_name

def filterjunk(movie_time,movie_name):
    filter=['pairedandDescriptiveServiceforthevisuallyim','paired(CC/DS)3DATMOSULTRAAVXReclinerSeatsFAUTEUILSINCLINABLES(CC/DS)','trailerClosedCaptionsforthehearingim','ClosedCaptionsforthehearingim','Nopassestrailer3DATMOSULTRAAVXReclinerSeatsFAUTEUILSINCLINABLES','Nopassestrailer','||','|||','trailer','Nopasses','3DATMOSULTRAAVXReclinerSeatsFAUTEUILSINCLINABLES']
    extrafilters=filtermovienames(movie_name)
    for i in range(len(extrafilters)):
        filter.append(extrafilters[i])
    for i in range(len(filter)):
        movie_time=movie_time.replace(filter[i],'')
    return movie_time

def filtertime(movie_time):
    movie_time=movie_time.replace(' ','')
    movie_time=movie_time.replace('0pm','0pm|')
    movie_time=movie_time.replace('5pm','5pm|')
    movie_time=movie_time.replace('0am','0am|')
    movie_time=movie_time.replace('5am','5am|')
    return movie_time