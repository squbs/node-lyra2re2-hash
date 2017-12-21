node-lyra2re2-hash
===============

Lyra2re2 hashing function for node.js. Fori STRAKS digital currency.

Usage
-----

Install

    ~


Hash your data

    var lyra2re2 = require('lyra2re2-hash');

    var data = new Buffer('01234567890123456789012345678901234567890123456789012345678901234567890123456789');
    var hashed = lyra2re2.digest(data); //returns a 32 byte buffer

    console.log("data: ", data, "\nhashed: ", hashed, "\nhashed(hex): ", hashed.toString('hex'));
    // data:  <Buffer 30 31 32 33 34 35 36 37 38 39 30 31 32 33 34 35 36 37 38 39 30 31 32 33 34 35 36 37 38 39 30 31 32 33 34 35 36 37 38 39 30 31 32 33 34 35 36 37 38 39 ... >
    // hashed:  <Buffer 0f e0 c9 bd 25 d8 5c 20 3e 95 41 2f f6 d2 3e 19 82 41 1b e1 d9 5e a9 67 9f 90 b2 f0 a2 8f b1 3b>
    // hashed(hex):  0fe0c9bd25d85c203e95412ff6d23e1982411be1d95ea9679f90b2f0a28fb13b

