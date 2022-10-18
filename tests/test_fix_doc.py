from codegen.fix_doc import fix_settings_doc


def test_fix_settings_doc():
    old_doc = """Menu to define the rotor pitch and flapping angles.
 - blade-pitch-collective    : ,
 - blade-pitch-cyclic-sin    : ,
 - blade-pitch-cyclic-cos    : ,
For more details please consult the help option of the corresponding menu or TUI command."""
    new_doc = fix_settings_doc(old_doc)
    assert (
        new_doc
        == """Menu to define the rotor pitch and flapping angles.

 - blade-pitch-collective    : ,
 - blade-pitch-cyclic-sin    : ,
 - blade-pitch-cyclic-cos    : ,

For more details please consult the help option of the corresponding menu or TUI command."""
    )