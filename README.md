## Rasa Test of Custom Response Variations with Boolean Slots

Test intents:

```
/boolean_only
/boolean_only{"agent_queue_open":"true"}
/boolean_only{"agent_queue_open":"false"}

/boolean_action

/bot_challenge
/bot_challenge{"residence_status":"resident","phone_number_type":"mobile","agent_queue_open":"True"}
/bot_challenge{"residence_status":"resident","phone_number_type":"mobile","agent_queue_open":"true"}

/crv_works{"residence_status":"resident","phone_number_type":"mobile"}
/crv_works{"residence_status":"resident","phone_number_type":"other"}
/crv_works{"residence_status":"resident","phone_number_type":"mobile","agent_queue_open":"true"}
```