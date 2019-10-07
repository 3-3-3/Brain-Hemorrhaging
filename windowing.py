import pydicom as dcm

#from See like a radiologist with systematic windowing
def window_image(img, window_center, window_width, intercept, slope):
    img = (img*slope + intercept)
    img_min = window_center - window_width // 2
    img_max = window_center + window_width // 2
    img[img<img_min] = img_min
    img[img>img_max] = img_max
    
    img = (img - img_min) / (img_max - img_min)
    return img

def get_windowing(data):
    dicom_fields = [data[('0028', '1050')].value, data[('0028', '1051')].value, 
                    data[('0028', '1052')].value, data[('0028', '1053')].value]
    int_fields = []
    for x in dicom_fields:
        if type(x) == dcm.multival.MultiValue:
            int_fields.append(int(x[0]))
        else:
            int_fields.append(int(x))
    return int_fields
