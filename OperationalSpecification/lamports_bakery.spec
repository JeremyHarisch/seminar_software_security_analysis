Possible States:
- Start
- Lock
- Waiting
- Trade
- Unlock
- End

Next-State-Relations:
- {Start|init()} => {checkGoalReached()|Check}
- {Check|} => {lock()|Lock}
- {Check|} => {|End}
- {Lock|} => {waiting()|Waiting}
- {Waiting|} => {enterTrade()|Trade}
- {Trade|leaveTrade()} => {|Unlock}
- {Unlock|} => {|Check}


Actions:

@Start-Main
def init():
    count = 0;
    countGoal = 500;
    for i in range(len(threads)):
        threads[i].startAndRunThread();

@Thread-Start
def checkGoalReached():
    if count == countGoal:
        trigger(end)
    else:
    count ++
        trigger(lock)

def lock():
    this.choosingTicket = true;
    this.ticket.id = getNewId();
    this.choosingTicket = false;

def unlock():
    this.ticket.id = 0

def waiting():
    for thread in threads and thread != this.thread:
        // Waiting for thread to choose new Ticket Number
        while thread.choosingTicket: { }
        // Waiting until it is the turn of this threads ticket
        while thread.ticket.id != 0 and (this.ticket.id > thread.ticketid. or (this.ticket.id == thread.ticket.id && this.id > thread.id)) { }

def enterTrade():
    /* Include actions when entering Trade-State*/
    pass

def leaveTrade():
    /* Include actions when leaving Trade-State*/
    pass


