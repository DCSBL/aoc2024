# ----------- IMPORTS ------------ #
import os
import copy


def get_path(filename) -> str:
    __location__ = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(__location__, filename)


# ----------- SOLUTION ----------- #


async def solution(filename: str) -> int:
    safe_reports : int = 0
    
    def all_increasing(report: list[int]) -> bool:
        prev: int | None = None
        
        for idx, level in enumerate(report):
            if prev is not None and not (prev <= level or prev >= level):
                raise ValueError(f"not increasing - {report}", idx)
            
            prev = level
    
    def differ_at_least_1_most_3(report: list[int]) -> bool:
        prev: int | None = None
        
        for idx, level in enumerate(report):
            if prev is not None and abs(prev - level) not in (1, 2, 3):
                raise ValueError(f"not in range - {report}", idx)
            
            prev = level
    
    with open(get_path(filename), mode="r") as file:
        for report in file.readlines():
            report = report.split(" ")
            for idx, level in enumerate(report):
                report[idx] = int(level)
            
            try:
                all_increasing(report) 
                differ_at_least_1_most_3(report)
            except ValueError as e:
                report_copy = copy.deepcopy(report)
                del report_copy[e.args[1]]
                
                try:
                    all_increasing(report_copy) 
                    differ_at_least_1_most_3(report_copy)
                except ValueError as e:
                    continue
            
            safe_reports += 1

    return safe_reports
