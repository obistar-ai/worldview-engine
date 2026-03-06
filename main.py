from event import Event
import rules
import actions
import ledger

event = Event("temperature", 90)

decision = rules.evaluate(event)

if decision:
    actions.execute()

ledger.record(event, decision)
