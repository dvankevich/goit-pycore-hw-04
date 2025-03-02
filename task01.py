from pathlib import Path

def total_salary(f_path):
    '''
    Returns the total and average salary of all employees. 
    Salary information is stored in a file in the format:
    Name,Salary
    Alex Korp,3000
    Nikita Borisenko,2000
    Sitarama Raju,1000
    Args:
        f_path (str): path to salary file
    Returns:
        (total (int), average(int)): a tuple of two numbers: the total amount of salaries and the average salary.
        Or None if error
    '''
    path = Path(f_path)
    if not path.exists() or path.is_dir():
        return None
    
    with open(f_path, "r") as fh:
        salary_sum = 0
        total_empl = 0
        for line in fh.readlines():
            salary_sum += int(line.strip().split(",")[1])
            total_empl += 1

        try:
            salary_avg = salary_sum / total_empl
        except:
            return None
            
    return (salary_sum, salary_avg)

def main():
    total, average = total_salary("salary.txt")
    assert total == 6000
    assert average == 2000

    assert total_salary("empty_file.txt") == None
    assert total_salary("nofile.txt") == None
    assert total_salary("salary.dir") == None

if __name__ == "__main__":
    main()
