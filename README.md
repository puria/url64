<h1 align="center">
  url64 <br>
  <sub>🐍 base64url decode/encode for python</sub>
</h1>

<p align="center">
  <a href="https://travis-ci.com/puria/url64">
    <img src="https://travis-ci.com/puria/url64.svg?branch=master" alt="Build Status">
  </a>
  <a href="https://codecov.io/gh/puria/url64">
    <img src="https://codecov.io/gh/puria/url64/branch/master/graph/badge.svg" alt="coverage"/>
  </a>
  <a href="https://pypi.org/project/url64/">
    <img alt="PyPI" src="https://img.shields.io/pypi/v/url64.svg" alt="Latest release">
  </a>
</p>

<br><br>

<h4 align="center">
  <a href="#-install">💾 Install</a>
  <span> • </span>
  <a href="#-quick-start">🎮 Quick start</a>
  <span> • </span>
  <a href="#-links">🌐 Links</a>
  <span> • </span>
  <a href="#-contributing">👤 Contributing</a>
  <span> • </span>
  <a href="#-license">💼 License</a>
</h4>


`url64` is the common name for the `base64url` described in the
 [RFC4648 §5](https://tools.ietf.org/html/rfc4648#section-5).
 Since the original base64 alphabet contains invalid characters for URLs a safe
 base64 for url is suggested, replacing the 62nd (plus sign +) and 63rd
 (slash /) with new chars respectively the minus `-` and underscore `_` and
 removing also the padding that is represented with the equal sign `=`.

 This a handy small utility to encode/decode strings in url64 with python3
 very useful for JWT

<details>
 <summary><strong>🚩 Table of Contents</strong> (click to expand)</summary>

* [Install](#-install)
* [Quick start](#-quick-start)
* [Links](#-links)
* [Contributing](#-contributing)
* [License](#-license)
</details>

***
## 💾 Install
```pip install url64```

***
## 🎮 Quick start

### encode

```python

import url64

encoded = url64.encode('Hello world!')
print(encoded)  # SGVsbG8gd29ybGQh

dict_exncode = url64.encode(dict(alg="HS256", typ="JWT"))
print(dict_exncode) # eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9
```

### decode

```python

import url64

decoded = url64.decode('SGVsbG8gd29ybGQh')
print(decoded)  # Hello world!

dict_decoded = url64.decode('eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9')
print(dict_decoded) # {"alg": "HS256", "typ": "JWT"}
```

***
## 🌐 Links

https://tools.ietf.org/html/rfc4648#section-5

https://en.wikipedia.org/wiki/Base64#URL_applications

https://base64.guru/standards/base64url

***
## 👤 Contributing

1.  🔀 [FORK IT](../../fork)
2.  Create your feature branch `git checkout -b feature/branch`
3.  Commit your changes `git commit -am 'Add some fooBar'`
4.  Push to the branch `git push origin feature/branch`
5.  Create a new Pull Request
6.  🙏 Thank you


***
## 💼 License

    Copyright (c) 2019 Puria Nafisi Azizi

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
