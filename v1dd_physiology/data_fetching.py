import h5py


# ========================== FETCHING DATA FROM NWB FILES ================================

def get_projection_images(nwb_f, plane_n, is_plot=False):
    """
    return mean projection and max projection of a given imaging plane

    Parameters
    ----------
    nwb_f : hdf5 File object
        should be in read-only mode
    plane_n : string
        "plane0", "plane1", ...
    is_plot : bool

    Returns
    -------
    mean_proj : 2d array
        mean projection 
    max_proj : 2d array
        max projection
    """

    if nwb_f.mode != 'r':
        raise OSError('The nwb file should be opened in read-only mode.')

    mean_proj = nwb_f['/processing/rois_and_traces_{}/ImageSegmentation' \
                      '/imaging_plane/reference_images/mean_projection' \
                      '/data'.format(plane_n)][()]
    max_proj = nwb_f['/processing/rois_and_traces_{}/ImageSegmentation' \
                      '/imaging_plane/reference_images/max_projection' \
                      '/data'.format(plane_n)][()]
    nwb_f.close()

    if is_plot:
        sl = 2 # plot saturation level [0-100]
        f = plt.figure(figsize=(10, 5))
        f.suptitle(plane_n)
        ax0 = f.add_subplot(121)
        ax0.set_title('mean_projection')
        ax0.set_axis_off()
        ax0.imshow(
            mean_proj, 
            vmin=np.percentile(mean_proj[:], sl),
            vmax=np.percentile(mean_proj[:], 100-sl), 
            cmap='gray', 
            interpolation='nearest'
            )

        ax1 = f.add_subplot(122)
        ax1.set_title('max_projection')
        ax1.set_axis_off()
        ax1.imshow(
            max_proj, 
            vmin=np.percentile(max_proj[:], sl),
            vmax=np.percentile(max_proj[:], 100-sl), 
            cmap='gray', 
            interpolation='nearest'
            )

    return mean_proj, max_proj


def get_vasculature_map(nwb_f,  type='wf', is_standard='False'):
    """
    get vasculature map of a particular session

    Parameters
    ----------
    nwb_f : hdf5 File object
        should be in read-only mode
    type : str, 
        'wf' for wide field or '2p' for 2p photon
    is_standard : bool
        if False, original image acquired;
        if True, rotated to match standard orientation 
        (up: anterior, left: lateral).
    
    Returns
    ------- 
    vasmap: 2d array
        vasculature_map
    """

    if nwb_f.mode != 'r':
        raise OSError('The nwb file should be opened in read-only mode.')

    vasmap_path = f'acquisition/images/vasmap_{type}'

    if is_standard:
        vasmap_path = f'{vasmap_path}_rotated'

    vasmap = nwb_f[vasmap_path][()]

    nwb_f.close()

    return vasmap


def get_session_id(nwb_f):
    """
    Parameters
    ----------
    nwb_f : hdf5 File object
        should be in read-only mode

    Returns
    -------
    sess_id : str
        LIMS ophys session id, unquie to every nwb file
    """
    return nwb_f['general/session_id'][()]


def get_windowed_grating_location(nwb_f):
    """
    return altitude and azimuth location of the center of windowed gratings

    Parameters
    ----------
    nwb_f : hdf5 File object
        should be in read-only mode

    Returns
    -------
    alt : float
        altitude of the windowed drifting grating circle in degrees
    azi : float
        azimuth of the windowed drifting grating circle in degrees
    """

    if nwb_f.mode != 'r':
        raise OSError('The nwb file should be opened in read-only mode.')

    alt = nwb_f['stimulus/presentation/drifting_gratings_windowed/center_alt'][()]
    azi = nwb_f['stimulus/presentation/drifting_gratings_windowed/center_azi'][()]
    nwb_f.close()
    return alt, azi


def get_windowed_grating_diameter(nwb_f):
    """
    return windowed drifting grating diameter in degrees 

    Parameters
    ----------
    nwb_f : hdf5 File object
        should be in read-only mode

    Returns
    -------
    dgcw_dia : float
        diameter of the windowed drifing grating circle in degrees
    """

    if nwb_f.mode != 'r':
        raise OSError('The nwb file should be opened in read-only mode.')

    dgcw_dia = nwb_f['stimulus/presentation/drifting_gratings_windowed/diameter_deg'][()]
    nwb_f.close()
    return dgcw_dia



# ========================== FETCHING DATA FROM NWB FILES ================================



# ==================== FETCHING DATA FROM RESPONSE METRICS FILES =========================


# ==================== FETCHING DATA FROM RESPONSE METRICS FILES =========================