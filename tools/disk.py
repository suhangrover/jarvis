import shutil
#to get drive's storage stats
def get_disk_usage(drive="C:\\"):
    usage=shutil.disk_usage(drive)
    total_gb = usage.total / (1024 ** 3)
    used_gb= usage.total - usage.free
    used_gb /= 1024 ** 3
    free_gb=usage.free/(1024**3) #conversion of bytes to gigabytes
    return {
        "drive":drive,
        "total_gb":round(total_gb,2),
        "used_gb":round(used_gb,2),
        "free_gb":round(free_gb, 2),
        "used_percent":round((usage.total-usage.free)/usage.total*100,1),

    }