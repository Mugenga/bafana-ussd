session_id = request.values.get("sessionId", None)
serviceCode = request.values.get("serviceCode", None)
phone_number = request.values.get("phoneNumber", None)
text = request.values.get("text", "default")

if text == "":
    response = "CON Urakaza neza kuri Bafana. Injiza code yuwo wenda gutera inkunga"
    # Insert Session Id, Current State, and Next State
else:
    # Get State From Recent Session
    if next_state == 2:
        # Verify Team

        # If team correct
        response = "CON Ugiye gutera inkuga [Insert] . Injiza inkuga ushaka gutanga."

        # Update state
        # If team not correct
        response = "CON Kode winjije ntango ariyo. Injiza code yuwo wenda gutera inkunga"
    elif next_state == 3:
        response = "END Urakoze gutanga inkuga kuri APR FC. Emeza kuri Mobile Money."

return response

