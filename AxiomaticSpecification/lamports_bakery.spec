Pre-Conditions:
{id >= 0}
{count = 0}
{countGoal > 0}
{numberOfThreads >= 1}
{len(choosing) = numberOfThreads}
{len(ticket) = numberOfThreads}

Conditions while execution:
// id_{x} gets new ID for Thread X
{0 <= x < numberOfThreads} => {id_{x} < id_{x+1}; id_{x} >=0} 
// Getting new Ticket for Thread X with ID
{choosing[id_{x}] = true} => {ticket[id_{x}] = max(ticket)+1 && choosing[id_{x}] = false; max(ticket) > 0} = A_{1}
// Make sure no other Thread is getting new Ticket at this time
A_{1} => {choosing[id_{x}] = false; j = 0; j < numberOfThreads; j != id; choosing[j] == false;} => A_{2}
// Condition for continuing run on Thread X with ID
A_{2} => {ticket[j] != 0 && !(ticket[id_{x}] > ticket[j] || (ticket[id_{x}] == ticket[j] && id_{x} > j))} => A_{3}
// Trade section
A_{3} =>{count = count + 1; count <= countGoal; ticket[id_{x}] = 0}

Post-Conditions:
{count == numberOfThreads * countGoal}