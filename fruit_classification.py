#th_apple_radius è la media delle dimensioni delle mele
#th_orange_radius è la media delle dimensioni delle arance
#th_orange_red_intensity è la media dell'intensità di rosso delle arance - 0.07


def fruit_classification(detection: str, red_intensity, green_intensity, average_radius, th_apple_radius, 
                         th_orange_radius, th_orange_red_intensity):
    if detection == "Apple Class":
        if green_intensity > red_intensity:
            if average_radius > th_apple_radius:
                return "Green Large Apple"
            else:
                return "Green Small Apple"
        else:
            if average_radius > th_apple_radius:
                return "Red Large Apple"
            else:
                return "Red Small Apple"
    elif detection == "Orange Class":
        if average_radius > th_orange_radius:
            if red_intensity > th_orange_red_intensity:
                return "Large Sweet Orange"
            else:
                return "Large Sour Orange"
        elif average_radius < th_orange_radius:
            if red_intensity > th_orange_red_intensity:
                return "Small Sweet Orange"
            else:
                return "Small Sour Orange"