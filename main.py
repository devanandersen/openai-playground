from gpt import *

my_gpt = GPTConversation("You are ChatGPT, a large language model trained by OpenAI. Follow the user's instructions carefully. Respond using markdown.")

prompt = """
I need a parser written in Python using LARK. In this parser, make sure:
* It can parse address strings into:
  * Building Number, Street, and Unit Number components
* Unit number is optional
* Apartments can handle different formats like apt, apartment, unit, #, etc
* Unit number must be able to handle values like (3, 3a, a, etc).
* Street can be multiple words long
  * Likewise, it can take terms like "42nd Street"
* Handle spacing in all of these cases:
  * Unit numbers can optionally have a space between the unit designator and the unit number/value
  * Street will have WS between words if it is more than one word long

Here are some test cases to add in, with their corresponding annotations:

* 123 fake st
  * building_number: 123, street: fake st, unit_number: None
* 123 fake st apt 1
  * building_number: 123, street: fake st, unit_number: apt 1
* 456 blah lane
  * building_number: 456, street: blah lane, unit_number: None
* 888 w cherry rose road #2
  * building_number: 888, street: w cherry rose road, unit_number: #2
* 302 east mulberry lane
  * building_number: 302, street: east mulberry lane, unit_number: None
* 220 n hampton way unit 3a
  * building_number: 220, street: n hampton way, unit_number: unit 3a
* 123 fake st apt1
  * building_number: 123, street: fake st, unit_number: apt1
* 123 fake st # 1
  * building_number: 123, street: fake st, unit_number: # 1
* 123 fake st #1
  * building_number: 123, street: fake st, unit_number: #1
"""

my_gpt.chat(prompt)
