import camera_tracking as ct
import pose_graph_optimization as pgo
from loop_closure import *
from output_trajectory import return_trajectory


if __name__ == '__main__':

    pair_file_path = 'pairs_list.txt'  # RGB-D frame pairs
    absolute_pose_path = 'kf_pose_level4.txt'  # keyframe absolute pose
    keyframe_index_path = 'kf_index_level4.txt'  # keyframe index number
    loop_pair_file_path = 'loop_closure_pair.npy'  # loop closure pairs index

    # pair_file_path = 'rgbd_dataset_freiburg2_desk/results/pairs_list.txt'  # RGB-D frame pairs
    # absolute_pose_path = 'rgbd_dataset_freiburg2_desk/results/kf_pose_level4.txt'  # keyframe absolute pose
    # keyframe_index_path = 'rgbd_dataset_freiburg2_desk/results/kf_index_level4.txt'  # keyframe index number
    # loop_pair_file_path = 'rgbd_dataset_freiburg2_desk/results/loop_closure_pair.npy'  # loop closure pairs index

   
    # key-frame selection strategy: thresholds on the rotational and translational distance
    # ct.camera_tracking_with_rot_and_trans_thresh(pair_file_path=pair_file_path, level=4, rot_thresh=0.1,trans_thresh=0.1)

    # # automatic loop closure detection
    lc = automatic_loop_closure_detection_with_trans_dis(keyframe_index_path, absolute_pose_path, pair_file_path)
    print(len(lc))
    np.save('loop_closure_pair.npy', lc)
    

    # run pose graph optimization with automatic loop closure
    pgo.optimise_pose_graph_with_auto_loop_closure(pair_path=pair_file_path, pose_path=absolute_pose_path,
                                                           index_path=keyframe_index_path,
                                                           loop_pairs_path=loop_pair_file_path,
                                                           level=4)

    
    # output trajectory as txt file
    return_trajectory()