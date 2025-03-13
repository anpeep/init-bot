if message.content.startswith("?"):
    await client.process_commands(message)
    return
elif message.author.id != client.user.id:  # If you are done with task 2, remove this and the following line
    await message.channel.send("Hello")  # Add in between these brackets the response to the message, for example "Hello!"