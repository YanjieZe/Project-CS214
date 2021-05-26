from solver import Solver
from task_scheduler import TaskScheduler
from DAG_scheduler import DAGScheduler
from data_loader import DataLoader

def DepthBasedBaseline(file_path="../ToyData.xlsx"):
    """
    Depth Based Baseline, implemented by Yanjie Ze
    """
    task_scheduler = TaskScheduler(file_path=file_path)
    solver = Solver(file_path=file_path)
    cur_depth = 0
    max_depth = task_scheduler.max_depth

    data_center = None
    placement = None
    finish_time = None
    task_set = None
    task_set_new = None
    while(cur_depth<=max_depth):
        if cur_depth ==0:
            task_set = task_scheduler.get_taskset(cur_depth)
            data_center = task_scheduler.get_datacenter()
            placement, finish_time = solver.get_placement(task_set, data_center)
            cur_depth += 1
            continue

        task_set_new = task_scheduler.get_taskset(cur_depth)  
        new_data_center = solver.update_datacenter(placement, task_set_new, task_set, data_center)

        placement, finish_time = solver.get_placement(task_set_new, new_data_center)
        
        task_set = task_set_new

        cur_depth += 1
    
    print("Depth Based Baseline Finish.")

def JobStepBasedBaseline(file_path="../ToyData.xlsx", threshold=5):
    """
    Job Step Based Baseline, implemented by Yanjie Ze
    """
    task_scheduler = TaskScheduler(file_path=file_path, threshold=threshold)
    solver = Solver(file_path=file_path)
    cur_step = 0
    max_step = task_scheduler.max_step

    data_center = None
    placement = None
    finish_time = None
    task_set = None
    task_set_new = None
    while(cur_step<=max_step):
        if cur_step ==0:
            task_set = task_scheduler.get_taskset_jobbased(cur_step)
            data_center = task_scheduler.get_datacenter()
            placement, finish_time = solver.get_placement(task_set, data_center)
            cur_step += 1
            continue

        task_set_new = task_scheduler.get_taskset_jobbased(cur_step)  
        new_data_center = solver.update_datacenter(placement, task_set_new, task_set, data_center)

        placement, finish_time = solver.get_placement(task_set_new, new_data_center)
        
        task_set = task_set_new

        cur_step += 1
    
    print("Job Step Based Baseline Finish.")


if __name__=='__main__':
    print('----------------------------')
    DepthBasedBaseline()
    print('----------------------------')
    JobStepBasedBaseline()