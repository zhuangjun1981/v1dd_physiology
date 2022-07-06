
## Data Structure
The V1 deepdive "V1DD" database is organized the network share:  

`/allen/programs/mindscope/workgroups/surround/v1dd_in_vivo_new_segmentation/data`

and the entire database (except eye-tracking movies) is backed up in the network share:  

`/allen/programs/mindscope/workgroups/surround/v1dd_in_vivo_new_segmentation/data_backup`

The data were collected from four mice as listed below.

 | name  | mouse_id | genotype                          | comment                |   
 | ----- | -------- | --------------------------------- | ---------------------- |  
 | Slc2  | 409828   | Slc17a7-IRES2-Cre;Camk2a-tTA;Ai94 | with EM reconstruction | 
 | Teto1 | 416296   | TetO-GCaMP6s;Camk2a-tTA           |                        | 
 | Slc4  | 438833   | Slc17a7-IRES2-Cre;Camk2a-tTA;Ai94 |                        |  
 | Slc5  | 427836   | Slc17a7-IRES2-Cre;Camk2a-tTA;Ai94 |                        |  

Each sub-folder under the root directory contains as specific type of data.
 
#### Essential Sub-folders
 
 * **visual_area_maps**
    This folder contains the visual area maps as well as the field of view of each imaged column for each mouse. The information was summarized in the file: `v1dd_cortex_maps.pdf`


 * **nwbs**

    This is probably the most important folder of the database. It contains a list of .nwb files of all experiment sessions. Each nwb file contains the raw and first-order pre-processed the data of each imaging session, as well as the meta data of that particular session. The name convention is `M{mouseid}_{column}{volume}_{date}.nwb`. For example: `M409828_11_20181212.nwb` means this file contains the imaging session of column 1, volume 1 from the mouse 409828, and it is recorded on Dec. 12th, 2018. 

    For each mouse, five columns were recorded, marked as 1, 2, 3, 4, and 5, in which column 1 is at the center and column 2-5 were tiled at the four corners of column 1. For the detailed location of columns for each mouse, see `base folder/visual_area_maps/v1dd_cortex_maps.pdf`. For each columns, five volumes (volume 1 through 5 from superficial to deep) were recorded by DeepScope two-photon scope. Each volume expands 96 um in depth and contains 6 simultaneously recorded imaging planes.

    For the central column (column 1), the tissue below the five two-photon volumes was imaged by multiple single-plane three-photon sessions. The three-photon sessions were labeled as "16" (500 um), "17" (525 um), "18" (550 um), "19" (575 um), "1a" (600 um), "1b" (625 um), "1c" (650 um), "1d" (675 um), "1e" (700 um), "1f" (725 um).

    So in total, a complete dataset for each mouse will have 5 x 5 (two-photon) + 10 (three-photon) = 35 imaging sessions (nwb files). But not all mice have all the sessions due to experiment/process failures.  

    All nwb files were generated by the scripts in the `nwb_building` module.

 * **response_matrices** 

    list of .hdf5 containing second order analysis results (e.g., receptive fields, grating response tables, etc.)

    All response table files are generated by the scripts in the `response_talbe_building` module.
 
 * **roi_tables** 

    list of .csv files containing dataframes (roi x feature) for all rois. 

    All roi table files are generated by the scripts in the `roi_talbe_building` module. 
 
 * **stim_movies**

    The stimulus movies displayed during each imaging session. For "locally sparse noise" and "natural images", the index of each frame matched the display index saved in the nwb files.

 

#### Other Sub-folders
these are not essential folders for the database.

 * **eye\_tracking\_movies**
    
    This folder contains the eye-tracking movies and eye-tracking preprocess results for each imaging session. The eye-tracking moves recorded the right eye (which faces the display monitor) during imaging sessions.

    `*_eye.avi`: raw eye tracking movie.  
    `*_eyeDLC*.avi` : eye tracking movie marked by deeplabcut annotation.  
    `*_eye_ellipse.avi`: eye tracking movie marked by the ellipse fitting on deeplabcut annotation.  
    `*_eyeDLC*.h5`: deeplabcut annotation (pandas DataFrame saved as .h5 format).  
    `*_eye_ellipse.hdf5`: ellipse fitting results on deeplabcut annotation. These were saved in nwb files (path: `/processing/eye_trackig_right/PupilTracking/eyetracking`).

 * **stimulus_tables**
    
    This folder contains the intermediate data format conversion of displayed stimuli for each imaging session, which were saved in nwb files (path: `/stimulus/presentation`).   