import plivo

client = plivo.RestClient("MAMGI5OTMXZTI0MMVMOG","ZThmMzRjN2I1Y2U0ZWY2MDRkOTUxNTMzZjYzMzlh")
call_made = client.calls.create(
    from_='1234567',
    to_='919106054324', #sip:Digvijay180412125753@phone.plivo.com
    answer_url='https://s3.amazonaws.com/plivocloud/Trumpet.mp3',
    answer_method = 'GET'
)
print call_made
