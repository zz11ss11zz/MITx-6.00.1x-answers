def decrypt_story():
    a = get_story_string()
    c = CiphertextMessage(a)
    return c.decrypt_message()   