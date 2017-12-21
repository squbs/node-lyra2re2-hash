{
    "targets": [
        {
            "target_name": "lyra2re2hash",
            "sources": [
                "lyra2re2hash.cc",
                "crypto/Lyra2RE.c",
                "crypto/Lyra2RE.h",
                "crypto/Sponge.c",
                "crypto/Lyra2.c",
                "crypto/blake.c",
                "crypto/keccak.c",
                "crypto/skein.c",
                "crypto/cubehash.c",
                "crypto/bmw.c"
            ],
            "include_dirs" : [
                "<!(node -e \"require('nan')\")"
            ]
        }
    ]
}
