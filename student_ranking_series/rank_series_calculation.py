

Total_marks = list()
def total_marks_calculation():
    with open('output.txt','w') as file_out :
        with open('input.txt','r') as file_in:
            lines = file_in.readlines()
            for line in lines:
                line = line.rstrip('\n')
                all_marks = 0
                for i in range(1,len(line.split(','))):
                    marks = int(line.split(',')[i])
                    all_marks+= marks
                file_out.write(line+',' + 'Total:' + str(all_marks)+'\n')
                Total_marks.append(all_marks)
                    
                    

def ranking_series_evaluation():
    with open('output.txt','r') as file_in:
        lines = file_in.readlines()
        with open('output.txt','w+') as file_out:
            for line in lines:
                line = line.rstrip('\n')
                marks = int(line.split(':')[1])
                rank = Total_marks.index(marks)+1
                file_out.write(line + ',' + 'Rank:' + str(rank) + '\n')





if __name__ == "__main__":
    total_marks_calculation()
    Total_marks = list(set(Total_marks))
    Total_marks.sort(reverse=True)
    ranking_series_evaluation()









