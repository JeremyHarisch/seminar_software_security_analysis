Pre-Conditions:
{id >= 0}
{count = 0}
{countGoal > 0}
{numberOfThreads >= 1}
{len(choosing) = numberOfThreads}
{len(ticket) = numberOfThreads}

Conditions while execution:
{0 <= x < numberOfThreads} => {id_{x} < id_{x+1}; id_{x} >=0} //id_{x} ID of Thread x
{choosing[id_{x}] = true} => {ticket[id_{x}] = max(ticket)+1 && choosing[id_{x}] = false; max(ticket) > 0} = A_{1}
A_{1} => {choosing[id_{x}] = false; j = 0; j < numberOfThreads; j != id; choosing[j] == false; ticket[j] != 0 && (ticket[id_{x}] > ticket[j] || (ticket[id_{x}] == ticket[j] && id_{x} > j))} => A_{2}
A_{2} => {count = count + 1; count <= countGoal; ticket[id_{x}] = 0}

Post-Conditions:
{count == countGoal}