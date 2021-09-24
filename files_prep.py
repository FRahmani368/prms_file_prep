import os
import shutil
import yaml
import pandas as pd


def control_file(site_no, args, main_path,
                 start_time=[2010,10,1], end_time=[2016,10,1]):
    # copy the sample file
    source = os.path.join(os.path.sep, main_path, "projects", "gages_II", "control", "sample_acf.control")
    destination = os.path.join(os.path.sep, main_path, "projects", "gages_II", "control", str(site_no) + ".control")
    shutil.copy(source, destination)



    # description of the control file
    with open(destination, 'r') as file:
        data = file.readlines()
    data[0] = str(site_no) + " control file" + '\n'
    with open(destination, "w") as file:
        file.writelines(data)

    # executable_model path
    with open(destination, 'r') as file:
        data = file.readlines()
    key = 'executable_model'
    for line_number, line in enumerate(data):
        if key in line:
            data[line_number + 3] = os.path.join(os.path.sep, os.path.sep, main_path, 'bin', 'prms') + '\n'
    with open(destination, "w") as file:
        file.writelines(data)


    #start_time
    with open(destination, 'r') as file:
        data = file.readlines()
    key = 'start_time'
    for line_number, line in enumerate(data):
        if key in line:
            data[line_number + 3] = str(start_time[0]) + '\n'
            data[line_number + 4] = str(start_time[1]) + '\n'
            data[line_number + 5] = str(start_time[2]) + '\n'
    with open(destination, "w") as file:
        file.writelines(data)

    # end_time
    with open(destination, 'r') as file:
        data = file.readlines()
    key = 'end_time'
    for line_number, line in enumerate(data):
        if key in line:
            data[line_number + 3] = str(start_time[0]) + '\n'
            data[line_number + 4] = str(start_time[1]) + '\n'
            data[line_number + 5] = str(start_time[2]) + '\n'
    with open(destination, "w") as file:
        file.writelines(data)

    # data_file
    with open(destination, 'r') as file:
        data = file.readlines()
    key = 'data_file'
    for line_number, line in enumerate(data):
        if key in line:
            data[line_number + 3] = os.path.join(os.path.sep, main_path, "projects", "gages_II", 'input', str(site_no) + ".data") + '\n'
    with open(destination, "w") as file:
        file.writelines(data)

    # param_file
    with open(destination, 'r') as file:
        data = file.readlines()
    key = 'data_file'
    for line_number, line in enumerate(data):
        if key in line:
            data[line_number + 3] = os.path.join(os.path.sep, main_path, "gages_II", 'input', str(site_no) + ".params") + '\n'
    with open(destination, "w") as file:
        file.writelines(data)

    # model_output_file
    with open(destination, 'r') as file:
        data = file.readlines()
    key = 'model_output_file'
    for line_number, line in enumerate(data):
        if key in line:
            data[line_number + 3] = os.path.join(os.path.sep, main_path, "projects", "gages_II", 'output', str(site_no) + ".data") + '\n'
    with open(destination, "w") as file:
        file.writelines(data)

    # stat_var_file
    with open(destination, 'r') as file:
        data = file.readlines()
    key = 'stat_var_file'
    for line_number, line in enumerate(data):
        if key in line:
            data[line_number + 3] = os.path.join(os.path.sep, main_path, "projects", "gages_II", "output", str(site_no) + ".statvar") + '\n'
    with open(destination, "w") as file:
        file.writelines(data)

    # ani_output_file
    with open(destination, 'r') as file:
        data = file.readlines()
    key = 'ani_output_file'
    for line_number, line in enumerate(data):
        if key in line:
            data[line_number + 3] = os.path.join(os.path.sep, main_path, "projects", "gages_II", "output",
                                                 str(site_no) + "_animation.out") + '\n'
    with open(destination, "w") as file:
        file.writelines(data)

    # nhruOutBaseFileName
    with open(destination, 'r') as file:
        data = file.readlines()
    key = 'nhruOutBaseFileName'
    for line_number, line in enumerate(data):
        if key in line:
            data[line_number + 3] = os.path.join(os.path.sep, main_path, "projects", "gages_II", "output",
                                                 str(site_no) + "_nhruOut_") + '\n'
    with open(destination, "w") as file:
        file.writelines(data)

    # basinOutBaseFileName
    with open(destination, 'r') as file:
        data = file.readlines()
    key = 'basinOutBaseFileName'
    for line_number, line in enumerate(data):
        if key in line:
            data[line_number + 3] = os.path.join(os.path.sep, main_path, "projects", "gages_II", "output",
                                                 str(site_no) + "_basinOut") + '\n'
    with open(destination, "w") as file:
        file.writelines(data)

    # tmax_day
    with open(destination, 'r') as file:
        data = file.readlines()
    key = 'tmax_day'
    for line_number, line in enumerate(data):
        if key in line:
            data[line_number + 3] = os.path.join(os.path.sep, main_path, "projects", "gages_II", "input",
                                                 str(site_no) + "_Tmax.data") + '\n'
    with open(destination, "w") as file:
        file.writelines(data)

    # tmin_day
    with open(destination, 'r') as file:
        data = file.readlines()
    key = 'tmin_day'
    for line_number, line in enumerate(data):
        if key in line:
            data[line_number + 3] = os.path.join(os.path.sep, main_path, "projects", "gages_II", "input",
                                                 str(site_no) + "_Tmin.data") + '\n'
    with open(destination, "w") as file:
        file.writelines(data)

    # precip_day
    with open(destination, 'r') as file:
        data = file.readlines()
    key = 'precip_day'
    for line_number, line in enumerate(data):
        if key in line:
            data[line_number + 3] = os.path.join(os.path.sep, main_path, "projects", "gages_II", "input",
                                                 str(site_no) + "_Prcp.data") + '\n'
    with open(destination, "w") as file:
        file.writelines(data)

    # potet_day
    with open(destination, 'r') as file:
        data = file.readlines()
    key = 'potet_day'
    for line_number, line in enumerate(data):
        if key in line:
            data[line_number + 3] = os.path.join(os.path.sep, main_path, "projects", "gages_II", "input",
                                                 str(site_no) + "_Ptet.data") + '\n'
    with open(destination, "w") as file:
        file.writelines(data)

    # swrad_day
    with open(destination, 'r') as file:
        data = file.readlines()
    key = 'swrad_day'
    for line_number, line in enumerate(data):
        if key in line:
            data[line_number + 3] = os.path.join(os.path.sep, main_path, "projects", "gages_II", "input",
                                                 str(site_no) + "_Orad.data") + '\n'
    with open(destination, "w") as file:
        file.writelines(data)

    # stats_output_file
    with open(destination, 'r') as file:
        data = file.readlines()
    key = 'stats_output_file'
    for line_number, line in enumerate(data):
        if key in line:
            data[line_number + 3] = os.path.join(os.path.sep, main_path, "projects", "gages_II", "output",
                                                 str(site_no) + ".statvar") + '\n'
    with open(destination, "w") as file:
        file.writelines(data)

    # csv_output_file
    with open(destination, 'r') as file:
        data = file.readlines()
    key = 'csv_output_file'
    for line_number, line in enumerate(data):
        if key in line:
            data[line_number + 3] = os.path.join(os.path.sep, main_path, "projects", "gages_II", "input",
                                                 str(site_no) + "_prms_summary.csv") + '\n'
    with open(destination, "w") as file:
        file.writelines(data)

    file.close()

def input_params(site_no, args, attr, main_path):
    # copy the sample file
    source = os.path.join(os.path.sep, main_path, "projects", "gages_II", "input", "acf.params")
    destination = os.path.join(os.path.sep, main_path, "projects", "gages_II", "input", str(site_no) + ".params")
    shutil.copy(source, destination)

    # description of the control file
    with open(destination, 'r') as file:
        data = file.readlines()
    data[0] = str(site_no) + " params file" + '\n'
    with open(destination, "w") as file:
        file.writelines(data)

    # number of prcp measurement stations
    with open(destination, 'r') as file:
        data = file.readlines()
    key = 'nrain'
    for line_number, line in enumerate(data):
        if key in line:
            data[line_number + 1] = str(1) + '\n'
    with open(destination, "w") as file:
        file.writelines(data)

    # number of air temperature measurement stations
    with open(destination, 'r') as file:
        data = file.readlines()
    key = 'ntemp'
    for line_number, line in enumerate(data):
        if key in line:
            data[line_number + 1] = str(1) + '\n'
    with open(destination, "w") as file:
        file.writelines(data)

    # number of number of subsurface reservoirs
    with open(destination, 'r') as file:
        data = file.readlines()
    key = 'nssr'
    for line_number, line in enumerate(data):
        if key in line:
            data[line_number + 1] = str(1) + '\n'
    with open(destination, "w") as file:
        file.writelines(data)

    # number of segments
    with open(destination, 'r') as file:
        data = file.readlines()
    key = 'nssr'
    for line_number, line in enumerate(data):
        if key in line:
            data[line_number + 1] = str(1) + '\n'
    with open(destination, "w") as file:
        file.writelines(data)

    # number of snow depletion curves
    with open(destination, 'r') as file:
        data = file.readlines()
    key = 'ndepl'
    for line_number, line in enumerate(data):
        if key in line:
            data[line_number + 1] = str(1) + '\n'
            ndepl = int(data[line_number + 1])
    with open(destination, "w") as file:
        file.writelines(data)

    # number of streamflow-measurement stations
    with open(destination, 'r') as file:
        data = file.readlines()
    key = 'nobs'
    for line_number, line in enumerate(data):
        if key in line:
            data[line_number + 1] = str(1) + '\n'
    with open(destination, "w") as file:
        file.writelines(data)

    # number of values in all snow depletion curve, set to ndepl * 11
    with open(destination, 'r') as file:
        data = file.readlines()
    key = 'ndeplval'
    for line_number, line in enumerate(data):
        if key in line:
            data[line_number + 1] = str(ndepl * 11) + '\n'
    with open(destination, "w") as file:
        file.writelines(data)


    # number of HRUs
    with open(destination, 'r') as file:
        data = file.readlines()
    key = 'nhru'
    for line_number, line in enumerate(data):
        if key in line:
            data[line_number + 1] = str(1) + '\n'
    with open(destination, "w") as file:
        file.writelines(data)

    # number of groundwater reservoirs
    with open(destination, 'r') as file:
        data = file.readlines()
    key = 'nobs'
    for line_number, line in enumerate(data):
        if key in line:
            data[line_number + 1] = str(1) + '\n'
    with open(destination, "w") as file:
        file.writelines(data)

    # Coefficient in non-linear contributing area algorithm for each HRU
    # according to PRMS table, it is between 0.0 - 5.0 . default = 0.3
    with open(destination, 'r') as file:
        data = file.readlines()
    key = 'smidx_exp'
    for line_number, line in enumerate(data):
        if key in line:
            key2 = "####"
            data[line_number + 3] = str(1) + '\n'
            # just to copy the next parameters
            for line_number2, line2 in enumerate(data[line_number:]):
                if key2 in line2:
                    datatemp = data[line_number + line_number2:]
                    break
            data[line_number + 5] = str(args['params']['smidx_exp']) + '\n'
            data = data[0:line_number + 6] + datatemp
    with open(destination, "w") as file:
        file.writelines(data)


# soil moisture
    with open(destination, 'r') as file:
        data = file.readlines()
    key = 'soil_moist_init_frac'
    for line_number, line in enumerate(data):
        if key in line:
            key2 = "####"
            data[line_number + 3] = str(1) + '\n'
            # just to copy the next parameters
            for line_number2, line2 in enumerate(data[line_number:]):
                if key2 in line2:
                    datatemp = data[line_number + line_number2:]
                    break
            data[line_number + 5] = str(args['params']['soil_moist_init_frac']) + '\n'
            data = data[0:line_number + 6] + datatemp
    with open(destination, "w") as file:
        file.writelines(data)

    # fraction of impervious surface runoff that flows into surface-depression storage;
    # the remainders flows to a stream network for each HRU
    with open(destination, 'r') as file:
        data = file.readlines()
    key = 'sro_to_dprst_imperv'
    for line_number, line in enumerate(data):
        if key in line:
            key2 = "####"
            data[line_number + 3] = str(1) + '\n'
            # just to copy the next parameters
            for line_number2, line2 in enumerate(data[line_number:]):
                if key2 in line2:
                    datatemp = data[line_number + line_number2:]
                    break
            data[line_number + 5] = str(args['params']['sro_to_dprst_imperv']) + '\n'
            data = data[0:line_number + 6] + datatemp
    with open(destination, "w") as file:
        file.writelines(data)

    # initial fraction of water available in gravity and preferential flow
    # reservoirs (fraction of sat_threshold) for each HRU
    with open(destination, 'r') as file:
        data = file.readlines()
    key = 'ssstor_init_frac'
    for line_number, line in enumerate(data):
        if key in line:
            key2 = "####"
            data[line_number + 3] = str(1) + '\n'
            # just to copy the next parameters
            for line_number2, line2 in enumerate(data[line_number:]):
                if key2 in line2:
                    datatemp = data[line_number + line_number2:]
                    break
            data[line_number + 5] = str(args['params']['ssstor_init_frac']) + '\n'
            data = data[0:line_number + 6] + datatemp
    with open(destination, "w") as file:
        file.writelines(data)

    # latitude for each hru
    with open(destination, 'r') as file:
        data = file.readlines()
    key = 'hru_lat'
    for line_number, line in enumerate(data):
        if key in line:
            key2 = "####"
            data[line_number + 3] = str(1) + '\n'
            # just to copy the next parameters
            for line_number2, line2 in enumerate(data[line_number:]):
                if key2 in line2:
                    datatemp = data[line_number + line_number2:]
                    break
            data[line_number + 5] = str(attr.loc[attr['site_no']==site_no, 'lat'][0]) + '\n'
            data = data[0:line_number + 6] + datatemp
    with open(destination, "w") as file:
        file.writelines(data)

    # Julian date to force snowpack to spring snowmelt stage, varies with region depending on length of time that
    # permanent  snowpack exist for each hru - default is 140
    with open(destination, 'r') as file:
        data = file.readlines()
    key = 'melt_force'
    for line_number, line in enumerate(data):
        if key in line:
            key2 = "####"
            data[line_number + 3] = str(1) + '\n'
            data[line_number + 5] = str(args['params']['melt_force']) + '\n'
    with open(destination, "w") as file:
        file.writelines(data)

    # maximum possible area contributing to surface runoff expressed as a portion of the HRU area
    with open(destination, 'r') as file:
        data = file.readlines()
    key = 'carea_max'
    for line_number, line in enumerate(data):
        if key in line:
            key2 = "####"
            data[line_number + 3] = str(1) + '\n'
            # just to copy the next parameters
            for line_number2, line2 in enumerate(data[line_number:]):
                if key2 in line2:
                    datatemp = data[line_number + line_number2:]
                    break
            data[line_number + 5] = str(args['params']['carea_max']) + '\n'
            data = data[0:line_number + 6] + datatemp
    with open(destination, "w") as file:
        file.writelines(data)

    # HRU slope
    with open(destination, 'r') as file:
        data = file.readlines()
    key = 'hru_slope'
    for line_number, line in enumerate(data):
        if key in line:
            key2 = "####"
            data[line_number + 3] = str(1) + '\n'
            # just to copy the next parameters
            for line_number2, line2 in enumerate(data[line_number:]):
                if key2 in line2:
                    datatemp = data[line_number + line_number2:]
                    break
            data[line_number + 5] = str(attr.loc[attr['site_no']==site_no, 'slope_mean'][0]) + '\n'
            data = data[0:line_number + 6] + datatemp
    with open(destination, "w") as file:
        file.writelines(data)


    # fraction of the soil zone in which preferential flow occurs for each HRU
    with open(destination, 'r') as file:
        data = file.readlines()
    key = 'pref_flow_den'
    for line_number, line in enumerate(data):
        if key in line:
            key2 = "####"
            data[line_number + 3] = str(1) + '\n'
            # just to copy the next parameters
            for line_number2, line2 in enumerate(data[line_number:]):
                if key2 in line2:
                    datatemp = data[line_number + line_number2:]
                    break
            data[line_number + 5] = str(0) + '\n'
            data = data[0:line_number + 6] + datatemp
    with open(destination, "w") as file:
        file.writelines(data)


    # index of measured streamflow station that replaces inflow to a segment
    with open(destination, 'r') as file:
        data = file.readlines()
    key = 'obsin_segment'
    for line_number, line in enumerate(data):
        if key in line:
            key2 = "####"
            data[line_number + 3] = str(1) + '\n'
            # just to copy the next parameters
            for line_number2, line2 in enumerate(data[line_number:]):
                if key2 in line2:
                    datatemp = data[line_number + line_number2:]
                    break
            data[line_number + 5] = str(0) + '\n'
            data = data[0:line_number + 6] + datatemp
    with open(destination, "w") as file:
        file.writelines(data)


    file.close()


if __name__=="__main__":
    stream = open("config.yaml", 'r')
    args = yaml.load(stream)
    attr = pd.read_feather(args['path']['attr'])
    control_file(1101344, args, main_path=r"/home/fzr5082/GitHub/prms5.2.0_linux")
    input_params(site_no = '01013500', args, attr, main_path=r"/home/fzr5082/GitHub/prms5.2.0_linux")
