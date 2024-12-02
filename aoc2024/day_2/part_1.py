# ----------- IMPORTS ------------ #
import os


def get_path(filename) -> str:
    __location__ = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(__location__, filename)


# ----------- SOLUTION ----------- #


async def solution(filename: str) -> int:
    safe_reports : int = 0
    
    def all_increasing(report: list[int]) -> bool:
        prev: int | None = None
        
        for level in report:
            if prev is not None and prev <= level:
                return False
            
            prev = level
        
        return True
            
    
    def all_decreasing(report: list[int]) -> bool:
        prev: int | None = None
        
        for level in report:
            if prev is not None and prev >= level:
                return False
            
            prev = level
            
        return True
    
    def differ_at_least_1_most_3(report: list[int]) -> bool:
        prev: int | None = None
        
        print(report)
        for level in report:
            if prev is not None and abs(prev - level) not in (1, 2, 3):
                print(f"{abs(prev - level)}")
                return False
            
            prev = level
            
        return True
    
    with open(get_path(filename), mode="r") as file:
        for report in file.readlines():
            report = report.split(" ")
            for idx, level in enumerate(report):
                report[idx] = int(level)
            
            if not all_increasing(report) and not all_decreasing(report):
                print(f"Rejecting {report}")
                continue
            
            if not differ_at_least_1_most_3(report):
                print(f"Rejecting {report}")
                continue
            
            safe_reports += 1

    return safe_reports
