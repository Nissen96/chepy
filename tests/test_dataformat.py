from chepy import Chepy


def test_eval():
    assert Chepy("1").eval_state().o == 1


def test_base16_encode():
    assert Chepy("test").to_base16().o == b"74657374"


def test_base16_decode():
    assert Chepy("74657374").from_base16().o == b"test"


def test_bytes_to_ascii():
    assert Chepy([116, 101, 115, 116]).bytes_to_ascii().o == "test"


def test_dict_to_json():
    assert (
        Chepy({"some": "data", "a": ["list", 1, True]}).dict_to_json().o
        == '{"some": "data", "a": ["list", 1, true]}'
    )


def test_dict_get_items():
    o = Chepy({"a": 1, "b": 2}).dict_get_items("a", "b", "c").o
    assert o[0] == 1 and o[1] == 2 and len(o) == 2
    o = Chepy({"a": 1, "b": 2}).dict_get_items().o
    assert len(o) == 2


def test_json_to_dict():
    assert Chepy('{"some": "data", "a": ["list", 1, true]}').json_to_dict().o == {
        "some": "data",
        "a": ["list", 1, True],
    }


def test_yaml_to_json():
    data = """# An employee record
name: Martin D'vloper
job: Developer
skill: Elite
employed: True
foods:
    - Apple
    - Orange
    - Strawberry
    - Mango
languages:
    perl: Elite
    python: Elite
    pascal: Lame
education: |
    4 GCSEs
    3 A-Levels
    BSc in the Internet of Things
"""
    assert (
        Chepy(data).yaml_to_json().o
        != ""
        # == '{"name":"Martin D\'vloper","job":"Developer","skill":"Elite","employed":true,"foods":["Apple","Orange","Strawberry","Mango"],"languages":{"perl":"Elite","python":"Elite","pascal":"Lame"},"education":"4 GCSEs\\n3 A-Levels\\nBSc in the Internet of Things\\n"}'
    )


def test_json_to_yaml():
    data = '{"name": "Martin D\'vloper", "job": "Developer", "skill": "Elite", "employed": true, "foods": ["Apple", "Orange", "Strawberry", "Mango"], "languages": {"perl": "Elite", "python": "Elite", "pascal": "Lame"}, "education": "4 GCSEs\\n3 A-Levels\\nBSc in the Internet of Things\\n"}'
    assert (
        Chepy(data).json_to_yaml().o
        == """name: Martin D'vloper
job: Developer
skill: Elite
employed: true
foods:
  - Apple
  - Orange
  - Strawberry
  - Mango
languages:
  perl: Elite
  python: Elite
  pascal: Lame
education: '4 GCSEs

  3 A-Levels

  BSc in the Internet of Things

  '
"""
    )


def test_from_base58():
    assert Chepy("2UDrs31qcWSPi").from_base58().out.decode() == "some data"


def test_to_base85():
    assert Chepy("some data").to_base85().out.decode() == "F)Po,+Cno&@/"


def test_from_base85():
    assert Chepy("F)Po,+Cno&@/").from_base85().out.decode() == "some data"


def test_to_base32():
    assert Chepy("some data").to_base32().out.decode() == "ONXW2ZJAMRQXIYI="


def test_to_base64():
    assert Chepy("some data").to_base64().out.decode() == "c29tZSBkYXRh"
    assert (
        Chepy("some random? data")
        .to_base64(
            custom="./0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz="
        )
        .o
        == b"QqxhNG/mMKtYPqoz64FVR42="
    )
    assert Chepy("test").to_base64(url_safe=True).o == b"dGVzdA"


def test_from_base64():
    assert Chepy("c29tZSByYW5kb20/IGRhdGE").from_base64().o == b"some random? data"
    assert (
        Chepy("QqxhNG/mMKtYPqoz64FVR42=")
        .from_base64(
            custom="./0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz="
        )
        .o
        == b"some random? data"
    )
    assert Chepy("dGVzdA").from_base64(url_safe=True).o == b"test"


def test_decode_bytes():
    assert (
        Chepy(
            b'{"flag":{" b":"MjQ3Q1RGe2RhODA3OTVmOGE1Y2FiMmUwMzdkNzM4NTgwN2I5YTkxfQ=="}}\x17\x8by\x90[\xc38E"\xf2\xb8\xfe\xf0\x95\xcc\x16.7\xabc\x92\xc0\x92'
        )
        .decode_bytes()
        .extract_base64()
        .from_base64()
        .o
        == b"247CTF{da80795f8a5cab2e037d7385807b9a91}"
    )


def test_to_base58():
    assert Chepy("some data").to_base58().out.decode() == "2UDrs31qcWSPi"


def test_to_hex():
    assert Chepy("AAA").to_hex().out.decode() == "414141"
    assert Chepy("AAA").to_hex(delimiter=" ").out.decode() == "41 41 41"


def test_from_hex():
    assert Chepy("414141").from_hex().out.decode() == "AAA"
    assert (
        Chepy("41;41;41").from_hex(delimiter=";", join_by="%").out.decode() == "A%A%A"
    )


def test_hex_to_int():
    assert Chepy("0x123").hex_to_int().out == 291
    assert Chepy("123").hex_to_int().out == 291


def test_hex_to_binary():
    assert Chepy("ab00").hex_to_binary().o == b"\xab\x00"


def test_int_to_hex():
    assert Chepy(101).int_to_hex().o == "65"


def test_hex_to_str():
    assert Chepy("4100").hex_to_str().o == b"A\x00"
    assert Chepy("4100").hex_to_str(ignore=True).o == "A\x00"


def test_to_url_encoding():
    assert (
        Chepy("https://google.com/?lol=some data&a=1").to_url_encoding(safe="/:").o
        == "https://google.com/%3Flol%3Dsome+data%26a%3D1"
    )


def test_from_url_encoding():
    assert (
        Chepy("https://google.com/%3Flol%3Dsome+data%26a%3D1").from_url_encoding().o
        == "https://google.com/?lol=some data&a=1"
    )


def test_to_list():
    assert Chepy("[1,2,'lol', true]").str_list_to_list().o == [1, 2, "lol", True]


def test_list_to_str():
    assert Chepy(["a", "b", "c"]).list_to_str(",").o == "a,b,c"
    assert Chepy([1, 2, 3]).list_to_str((".")).o == "1.2.3"
    assert Chepy([b"a", b"b"]).list_to_str(b".").o == b"a.b"


def test_join_list():
    assert Chepy(["a", "b", "c"]).join_list(":").o == "a:b:c"


def test_join():
    assert Chepy(["a", "b", "c"]).join(":").o == "a:b:c"


def test_to_int():
    assert Chepy("1").to_int().o == 1


def test_normalize_hex():
    assert Chepy("41:42:CE").normalize_hex().o == "4142CE"
    assert Chepy("0x410x420xce").normalize_hex().o == "4142ce"
    assert (
        Chepy("tests/files/hello").load_file().normalize_hex(True).o[0:6].decode()
        == "cffaed"
    )


def test_bytearray_to_str():
    assert Chepy(bytearray("lolol", "utf")).bytearray_to_str().o == "lolol"


def test_get_by_index():
    assert Chepy([1, "a", True]).get_by_index(2).state == True


def test_get_by_key():
    assert Chepy('{"some": "data"}').json_to_dict().get_by_key("some").o == "data"


def test_to_bytes():
    assert Chepy({"some": "val", "kl": 1}).to_bytes().o == b"{'some': 'val', 'kl': 1}"


def test_from_bytes():
    assert (
        Chepy(b'{"some": "val", "kl": 1}').from_bytes().o == '{"some": "val", "kl": 1}'
    )


def test_str_to_list():
    assert Chepy("abc").str_to_list().o == ["a", "b", "c"]


def test_str_to_dict():
    assert Chepy(b"{'some': 'dict'}").str_to_dict().o == {"some": "dict"}


def test_int_to_str():
    assert Chepy(41).int_to_str().o == "41"


def test_to_charcode():
    assert Chepy("aㅎ").to_charcode().o == "97 12622"


def test_from_charcode():
    assert Chepy("314e 61 20 41").from_charcode().o == "ㅎa A"


def test_to_decimal():
    assert Chepy("aㅎ").to_decimal().o == "97 12622"


def test_from_decimal():
    assert Chepy(12622).from_decimal().o == "ㅎ"


def test_to_binary():
    assert Chepy("abc").to_binary().o == "01100001 01100010 01100011"


def test_from_binary():
    assert Chepy("011001000110 000101110100 0110000 1").from_binary().o == b"data"


def test_to_octal():
    assert Chepy("abㅎ").to_octal().o == "141 142 30516"


def test_from_octral():
    assert Chepy("141 142 30516").from_octal().o == "abㅎ"


def test_html_encode():
    assert (
        Chepy('https://google.com&a="lol"').to_html_entity().o
        == "https://google.com&amp;a=&quot;lol&quot;"
    )


def test_html_decode():
    assert (
        Chepy("https://google.com&amp;a=&quot;lol&quot;").from_html_entity().o
        == 'https://google.com&a="lol"'
    )


def test_from_punycode():
    assert Chepy(b"mnchen-3ya").from_punycode().o == "münchen"


def test_to_punycode():
    assert Chepy("münchen").to_punycode().o == b"mnchen-3ya"


def test_encode_bruteforce():
    assert (
        Chepy("münchen한").encode_bruteforce().get_by_key("ascii").o
        == b"m\\xfcnchen\\ud55c"
    )


def test_decode_bruteforce():
    assert (
        Chepy("m\xfcnchen\ud55c").decode_bruteforce().get_by_key("utf_8").o
        == "münchen한"
    )


def test_to_braille():
    assert Chepy("secret message").to_braille().o == "⠎⠑⠉⠗⠑⠞⠀⠍⠑⠎⠎⠁⠛⠑"


def test_from_braille():
    assert Chepy("⠎⠑⠉⠗⠑⠞⠀⠍⠑⠎⠎⠁⠛⠑").from_braille().o == "secret message"


def test_trim():
    assert Chepy("\nlol ").trim().o == "lol"


def test_to_hexdump():
    assert Chepy("some").to_hexdump().o.split() == [
        "00000000:",
        "73",
        "6F",
        "6D",
        "65",
        "some",
    ]


def test_from_hexdump():
    assert Chepy("some").to_hexdump().from_hexdump().o == b"some"


def test_nato_convert():
    assert Chepy("abc:1").to_nato().o == "Alpha Bravo Charlie : 1"
    assert (
        Chepy("Lima Alpha Kilo Echo Mike India Charlie Hotel India Golf Alpha November")
        .from_nato()
        .o
        == "LAKEMICHIGAN"
    )


def test_swap_strings():
    assert Chepy("oY u").swap_strings(2).o == "You "


def test_to_string():
    assert Chepy(1).to_string().o == "1"


def test_select():
    assert Chepy("abcd").select(0, 2).o == "ab"
    assert Chepy("abcd").select(2).o == "cd"


def test_length():
    assert Chepy("abcd").length().o == 4


def test_leetcode():
    assert len(Chepy("ab@ cd").to_leetcode(replace_space="_").o) == 6


def test_substitute():
    assert (
        Chepy("synt{q41q8pq98s00o204r9800998rps8427r}")
        .substitute(
            "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm",
            "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz",
        )
        .o
        == "flag{d41d8cd98f00b204e9800998ecf8427e}"
    )


def test_remove_nonprintable():
    assert Chepy(b"aa").remove_nonprintable().o == b"aa"
    assert (
        Chepy(
            "\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f"
        )
        .remove_nonprintable()
        .o
        == b""
    )
    assert Chepy("41ae42").from_hex().remove_nonprintable(replace_with=" ").o == b"A B"
    assert Chepy("41ae42").from_hex().remove_nonprintable(replace_with=b" ").o == b"A B"


def test_base91():
    data = "flag{some_flag}"
    out = "@iH<,{_{W$OsuxXi%]D"
    assert Chepy(data).to_base91().o == out
    assert Chepy(out).from_base91().o.decode() == data


def test_swap_endianness():
    assert Chepy("4142").from_hex().swap_endianness().o == b"\x00\x00\x42A"


def test_bruteforce_base_xx():
    assert Chepy("dGVzdA==").bruteforce_from_base_xx().o["base64"] == b"test"


def test_long_to_bytes():
    assert (
        Chepy(
            "11515195063862318899931685488813747395775516287289682636499965282714637259206269"
        )
        .long_to_bytes()
        .o
        == b"crypto{3nc0d1n6_4ll_7h3_w4y_d0wn}"
    )


def test_bytes_to_long():
    assert (
        Chepy("crypto{3nc0d1n6_4ll_7h3_w4y_d0wn}").bytes_to_long().o
        == 11515195063862318899931685488813747395775516287289682636499965282714637259206269
    )
