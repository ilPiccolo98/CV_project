def fruit_recognition(green_intensity, red_intensity, average_radius, th_green_intensity, th_lower_radius, 
                      th_upper_radius, th_lower_intensity_diff, th_upper_intensity_diff):
    if green_intensity > red_intensity:
        if green_intensity < th_green_intensity:
            return "Orange Class"
        else:
            return "Apple Class"
    else:
        if th_lower_radius <= average_radius and average_radius <= th_upper_radius and th_lower_intensity_diff <= red_intensity - green_intensity and red_intensity - green_intensity <= th_upper_intensity_diff:
            return "Orange Class"
        else:
            return "Apple Class"