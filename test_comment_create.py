
def test_add_comment(app, login_user):
    test_text = "Shit happens!!!:("
    expected_text = test_text

    app.create_comment(test_text)
    # Verifications
    comment_elements = app.get_comments()
    assert comment_elements[0].text == expected_text

