import platform
import psutil
#using psutil for cpu, ram and disk statistics
#using platform for OS and hardware identification imformation
def system_info():
    memory=psutil.virtual_memory()
    disk=psutil.disk_usage("C:\\")
    return{
        "Operating System" : platform.system(),
        "Operating_System_Version" : platform.release(),
        "architecture": platform.machine(),
        "processor": platform.processor(),
        "cpu_cores": psutil.cpu_count(),
        "ram_total_gb": round(memory.total / (1024 ** 3), 2),
        "ram_used_percent": memory.percent,
        "disk_total_gb": round(disk.total / (1024 ** 3), 2),
        "disk_used_percent": disk.percent,
        "python_version": platform.python_version(),
    }
system_info()