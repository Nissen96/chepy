from chepy import Chepy


def test_sha1():
    assert Chepy("A").sha1().out == b"6dcd4ce23d88e2ee9568ba546c007c63d9131c1b"


def test_sha2_256():
    assert (
        Chepy("A").sha2_256().out
        == b"559aead08264d5795d3909718cdd05abd49572e84fe55590eef31a88a08fdffd"
    )


def test_sha2_512():
    assert (
        Chepy("A").sha2_512().out
        == b"21b4f4bd9e64ed355c3eb676a28ebedaf6d8f17bdc365995b319097153044080516bd083bfcce66121a3072646994c8430cc382b8dc543e84880183bf856cff5"
    )


def test_sha2_384():
    assert (
        Chepy("A").sha2_384().out
        == b"ad14aaf25020bef2fd4e3eb5ec0c50272cdfd66074b0ed037c9a11254321aac0729985374beeaa5b80a504d048be1864"
    )


def test_sha2_224():
    assert (
        Chepy("A").sha2_224().out
        == b"5cfe2cddbb9940fb4d8505e25ea77e763a0077693dbb01b1a6aa94f2"
    )


def test_sha2_512_truncate():
    assert (
        Chepy("abc").sha2_512_truncate().out
        == b"53048e2681941ef99b2e29b76b4c7dabe4c2d0c634fc6d46e0e2f13107e7af23"
    )


def test_sha3_512():
    assert (
        Chepy("A").sha3_512().out
        == b"f5f0eaa9ca3fd0c4e0d72a3471e4b71edaabe2d01c4b25e16715004ed91e663a1750707cc9f04430f19b995f4aba21b0ec878fc5c4eb838a18df5bf9fdc949df"
    )


def test_sha3_256():
    assert (
        Chepy("A").sha3_256().out
        == b"1c9ebd6caf02840a5b2b7f0fc870ec1db154886ae9fe621b822b14fd0bf513d6"
    )


def test_sha3_384():
    assert (
        Chepy("A").sha3_384().out
        == b"15000d20f59aa483b5eac0a1f33abe8e09dea1054d173d3e7443c68035b99240b50f7abdb9553baf220320384c6b1cd6"
    )


def test_sha3_224():
    assert (
        Chepy("A").sha3_224().out
        == b"97e2f98c0938943ab1a18a1721a04dff922ecc1ad14d4bbf905c02ca"
    )


def test_md2():
    assert Chepy("A").md2().out == b"08e2a3810d8426443ecacaf47aeedd17"


def test_md4():
    assert Chepy("A").md4().out == b"d5ef20eeb3f75679f86cf57f93ed0ffe"


def test_md5():
    assert Chepy("A").md5().out == b"7fc56270e7a70fa81a5935b72eacbe29"


def test_keccak_384():
    assert (
        Chepy("A").keccak_384().out
        == b"5c744cf4b4e3fb8967189e9744261a74f0ef31cdd8850554c737803585ac109039b73c22c50ea866c94debf1061f37a4"
    )


def test_keccak_256():
    assert (
        Chepy("A").keccak_256().out
        == b"03783fac2efed8fbc9ad443e592ee30e61d65f471140c10ca155e937b435b760"
    )


def test_keccak_224():
    assert (
        Chepy("A").keccak_224().out
        == b"ef40b16ff375c834e91412489889f36538748c5454f4b02ba750b65e"
    )


def test_keccak_512():
    assert (
        Chepy("A").keccak_512().out
        == b"421a35a60054e5f383b6137e43d44e998f496748cc77258240ccfaa8730b51f40cf47c1bc09c728a8cd4f096731298d51463f15af89543fed478053346260c38"
    )


def test_shake_256():
    assert (
        Chepy("A").shake_256().out
        == b"5e6812c0bbaaee6440dcc8b81ca6809645f7512e06cf5acb57bd16dc3a2bfc57dc2bf9e6d8941950594bef5191d8394691f86edffcad6c5ebad9365f282f37a8"
    )


def test_shake_128():
    assert (
        Chepy("A").shake_128(128).out
        == b"a5ba3aeee1525b4ae5439e54cd711f14850251e02c5999a53f61374c0ae089ef905a30c6abe132988c3eb233aaa2a79737fd245f87eda8b635a53720865a8604512a7ca47defb8993adae051e8390881d86968edf631d97f00b4ebef58ad183dc49d97dacc1e6bf1f38a99784dcfe517e4aa3b22401a9b35fd184c19626b8b53"
    )


def test_ripemd_160():
    assert Chepy("A").ripemd_160().out == b"ddadef707ba62c166051b9e3cd0294c27515f2bc"


def test_blake_2b():
    assert (
        Chepy("A").blake_2b(bits=128, key="key").out
        == b"6d2e4cba3bc564e02d1a76f585a6795d"
    )


def test_blake_2s():
    assert (
        Chepy("A").blake_2s(bits=128, key="key").out
        == b"4e33cc702e9d08c28a5e9691f23bc66a"
    )


def test_crc8_checksum():
    assert Chepy("abc").crc8_checksum().out == b"5f"


def test_crc16_checksum():
    assert Chepy("a").crc16_checksum().out == b"e8c1"


def test_crc32_checksum():
    assert Chepy("a").crc32_checksum().out == b"e8b7be43"


def test_hmac_hash():
    assert Chepy("abc").hmac_hash("", "md5").out == b"dd2701993d29fdd0b032c233cec63403"
    assert (
        Chepy("abc").hmac_hash("", "sha1").out
        == b"9b4a918f398d74d3e367970aba3cbe54e4d2b5d9"
    )
    assert (
        Chepy("abc").hmac_hash("", "sha256").out
        == b"fd7adb152c05ef80dccf50a1fa4c05d5a3ec6da95575fc312ae7c5d091836351"
    )
    assert (
        Chepy("abc").hmac_hash("", "sha512").out
        == b"29689f6b79a8dd686068c2eeae97fd8769ad3ba65cb5381f838358a8045a358ee3ba1739c689c7805e31734fb6072f87261d1256995370d55725cba00d10bdd0"
    )


def test_bcrypt_hash():
    assert Chepy("abc").bcrypt_hash().out.decode().startswith("$2a$10")


def test_bcrypt_compare():
    assert Chepy("abc").bcrypt_compare(
        "$2a$10$SpXMRnrQ4IQqC710xMHfAu0BBr4nJkuPqDvzhiAACnykgn87iE2S2"
    )


def test_scrypt_hash():
    assert (
        Chepy("abc").scrypt_hash(salt="", key_length=16).out
        == b"f352f3374cf4e344dde4108b96985248"
    )


def test_derive_pbkdf2_key():
    assert (
        Chepy(".")
        .derive_pbkdf2_key(
            "mR3m", "d9016d44c374f5fb62604683f4d61578", show_full_key=True
        )
        .o[:10]
        == b"7c8898f222"
    )
    assert (
        Chepy(".").derive_pbkdf2_key("mR3m", "d9016d44c374f5fb62604683f4d61578").o
        == b"7c8898f22239ce49aad28e6d16266b8dc1d681f86d2a56c76ebad5cfac1b0dd6"
    )
    assert (
        Chepy(".")
        .derive_pbkdf2_key("mR3m", "d9016d44c374f5fb62604683f4d61578", hash_type="md5")
        .o[:10]
        == b"f7918edc04"
    )
    assert (
        Chepy(".")
        .derive_pbkdf2_key(
            "mR3m", "d9016d44c374f5fb62604683f4d61578", hash_type="sha256"
        )
        .o[:10]
        == b"16b0a769cb"
    )
    assert (
        Chepy(".")
        .derive_pbkdf2_key(
            "mR3m", "d9016d44c374f5fb62604683f4d61578", hash_type="sha512"
        )
        .o[:10]
        == b"6d2a9c4b24"
    )


def test_password_hashing():
    password = "lol"
    assert (
        Chepy(password).password_hashing("lmhash").o
        == b"7d0fbaebf878e771aad3b435b51404ee"
    )
    assert (
        Chepy(password).password_hashing("msdcc", user="lol").o
        == b"5a487b0cda9a56e7e25464d81da162a2"
    )
