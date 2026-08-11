# @ohos.util

The util module provides common utility functions,such as TextEncoder and TextDecoder for string encoding and decoding,RationalNumber8+ for rational number operations, LRUCache9+ for cache management, ScopeHelper9+ for range determination,Base64Helper9+ for Base64 encoding and decoding, types8+ for built-in object type check,and replacement on methods.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-declare namespace util--><!--Device-unnamed-declare namespace util-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { util } from 'kits/@kit.ArkTS';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [callbackWrapper](arkts-arkts-util-callbackwrapper-f.md#callbackwrapper) | Takes an async function (or a function that returns a Promise) and returns a function following the error-first callback style. |
| [errnoToString](arkts-arkts-util-errnotostring-f.md#errnotostring) | Get the string name of the system errno. |
| [format](arkts-arkts-util-format-f.md#format) | %s: String will be used to convert all values except BigInt, Object and -0. BigInt values will be represented with an n and Objects that have no user defined toString function are inspected using util.inspect() with options { depth: 0, colors: false, compact: 3 }.%d: Number will be used to convert all values except BigInt and Symbol.%i: parseInt(value, 10) is used for all values except BigInt and Symbol.%f: parseFloat(value) is used for all values except Bigint and Symbol.%j: JSON. Replaced with the string '[Circular]' if the argument contains circular references.%o: Object. A string representation of an object with generic JavaScript object formatting.Similar to util.inspect() with options { showHidden: true, showProxy: true}. This will show the full object including non-enumerable properties and proxies.%O: Object. A string representation of an object with generic JavaScript object formatting.%O: Object. A string representation of an object with generic JavaScript object formatting.Similar to util.inspect() without options. This will show the full object not including non-enumerable properties and proxies.%c: CSS. This specifier is ignored and will skip any CSS passed in.%%: single percent sign ('%'). This does not consume an argument.Returns: &lt;string&gt; The formatted string. |
| [generateRandomBinaryUUID](arkts-arkts-util-generaterandombinaryuuid-f.md#generaterandombinaryuuid) | Generate a random RFC 4122 version 4 binary UUID using a cryptographically secure random number generator. |
| [generateRandomUUID](arkts-arkts-util-generaterandomuuid-f.md#generaterandomuuid) | Generate a random RFC 4122 version 4 UUID using a cryptographically secure random number generator. |
| [getHash](arkts-arkts-util-gethash-f.md#gethash) | Get the hash code of an object. |
| [getMainThreadStackTrace](arkts-arkts-util-getmainthreadstacktrace-f.md#getmainthreadstacktrace) | Get stack trace of main thread. |
| [parseUUID](arkts-arkts-util-parseuuid-f.md#parseuuid) | Parse a UUID from the string standard representation as described in the RFC 4122 version 4. |
| [promisify](arkts-arkts-util-promisify-f.md#promisify) | Takes a function following the common error-first callback style, i.e taking an (err, value) =>callback as the last argument, and return a function that returns promises. |

### Classes

| Name | Description |
| --- | --- |
| [Base64Helper](arkts-arkts-util-base64helper-c.md) | Decodes a Base64 encoded String or input u8 array into a newly-allocated u8 array using the Base64 encoding scheme. |
| [LRUCache](arkts-arkts-util-lrucache-c.md) | Provides APIs to discard the least recently used data to make rooms for new elements when the cache is full.This class uses the Least Recently Used (LRU) algorithm,which believes that the recently used data may be accessed again in the near future and the least accessed data is the least valuable data and should be removed from the cache. |
| [RationalNumber](arkts-arkts-util-rationalnumber-c.md) | The rational number is mainly to compare rational numbers and obtain the numerator and denominator. |
| [ScopeHelper](arkts-arkts-util-scopehelper-c.md) | Provides APIs to define the valid range of a field. The constructor of this class creates comparable objects with lower and upper limits. |
| [StringDecoder](arkts-arkts-util-stringdecoder-c.md) | Provide the ability to decode binary streams into strings. The supported encoding types include: utf-8, iso-8859-2,koi8-r, macintosh, windows-1250, windows-1251, gbk, gb18030, big5, utf-16be, utf-16 le, etc. |
| [TextDecoder](arkts-arkts-util-textdecoder-c.md) | The TextDecoder represents a text decoder that accepts a string as input,decodes it in UTF-8 format, and outputs UTF-8 byte stream. |
| [TextEncoder](arkts-arkts-util-textencoder-c.md) | The TextEncoder interface represents a text encoder.The encoder takes the byte stream as the input and outputs the String string. |
| [types](arkts-arkts-util-types-c.md) | Check the type of parameter. |

### Interfaces

| Name | Description |
| --- | --- |
| [DecodeToStringOptions](arkts-arkts-util-decodetostringoptions-i.md) | Defines the decode with stream related options parameters. |
| [EncodeIntoUint8ArrayInfo](arkts-arkts-util-encodeintouint8arrayinfo-i.md) | Return encoded text. |
| [ScopeComparable](arkts-arkts-util-scopecomparable-i.md) | The ScopeComparable contains comparison methods. |
| [TextDecoderOptions](arkts-arkts-util-textdecoderoptions-i.md) | Defines the TextDecoder related options parameters. |

### Enums

| Name | Description |
| --- | --- |
| [Type](arkts-arkts-util-type-e.md) | The Type represents four different encoding formats for base64 |

### Types

| Name | Description |
| --- | --- |
| [PromisifiedFunc](arkts-arkts-util-promisifiedfunc-t.md) | The type of promisify return function |
| [ScopeType](arkts-arkts-util-scopetype-t.md) | A type used to denote ScopeComparable or number. |

