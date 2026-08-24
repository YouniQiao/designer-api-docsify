# TextDecoder

Provides APIs to decode byte arrays into strings. It supports multiple formats, including UTF-8, UTF-16LE, UTF-16BE, ISO-8859, and Windows-1251.

**Since:** 7

<!--Device-util-class TextDecoder--><!--Device-util-class TextDecoder-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { util } from '@kit.ArkTS';
```

## constructor

```TypeScript
constructor()
```

A constructor used to create a **TextDecoder** object.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TextDecoder-constructor()--><!--Device-TextDecoder-constructor()-End-->

**System capability:** SystemCapability.Utils.Lang

**Examples**

```TypeScript
let textDecoder = new util.TextDecoder();
let retStr = textDecoder.encoding;
console.info('retStr = ' + retStr);
// Output: retStr = utf-8
```

```TypeScript
let textDecoder = new util.TextDecoder("utf-8",{ignoreBOM: true});
```

```TypeScript
let textEncoder = new util.TextEncoder();
```

```TypeScript
let textEncoder = new util.TextEncoder("utf-8");
```

```TypeScript
let rationalNumber = new util.RationalNumber();
```

```TypeScript
let rationalNumber = new util.RationalNumber(1,2);
```

```TypeScript
let pro = new util.LRUCache<number, number>();
```

```TypeScript
class Temperature implements util.ScopeComparable {
  private readonly _temp: number;

  constructor(value: number) {
    this._temp = value;
  }

  compareTo(value: Temperature) {
    return this._temp >= value.getTemp();
  }

  getTemp() {
    return this._temp;
  }

  toString(): string {
    return this._temp.toString();
  }
}
let tempLower = new Temperature(30);
let tempUpper = new Temperature(40);
let range = new util.ScopeHelper(tempLower, tempUpper);
console.info("range = " + range);
// Output: range = [30, 40]
```

```TypeScript
let base64 = new util.Base64Helper();
```

```TypeScript
let decoder = new util.StringDecoder();
```

```TypeScript
let type = new util.types();
```

```TypeScript
let pro : util.LruBuffer<number,number> = new util.LruBuffer();
```

```TypeScript
class Temperature implements util.ScopeComparable {
  private readonly _temp: number;

  constructor(value: number) {
    this._temp = value;
  }

  compareTo(value: Temperature) {
    return this._temp >= value.getTemp();
  }

  getTemp() {
    return this._temp;
  }

  toString(): string {
    return this._temp.toString();
  }
}

let tempLower = new Temperature(30);
let tempUpper = new Temperature(40);
let range = new util.Scope(tempLower, tempUpper);
console.info("range = " + range);
// Output: range = [30, 40]
```

```TypeScript
let base64 = new  util.Base64();
```

## constructor

```TypeScript
constructor(encoding?: string, options?: { fatal?: boolean; ignoreBOM?: boolean })
```

A constructor used to create a **TextDecoder** object.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [create](../../apis-default/arkts-apis/arkts-util-textdecoder-c.md#create)

<!--Device-TextDecoder-constructor(encoding?: string, options?: { fatal?: boolean; ignoreBOM?: boolean })--><!--Device-TextDecoder-constructor(encoding?: string, options?: { fatal?: boolean; ignoreBOM?: boolean })-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| encoding | string | No | Encoding format. The default format is **'utf-8'**. |
| options | { fatal?: boolean; ignoreBOM?: boolean } | No | Decoding-related options, which include **fatal** and **ignoreBOM**. |

**Examples**

See [constructor](#constructor)

## create

```TypeScript
static create(encoding?: string, options?: TextDecoderOptions): TextDecoder
```

Creates a **TextDecoder** object. It provides the same function as the deprecated argument constructor.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-TextDecoder-static create(encoding?: string, options?: TextDecoderOptions): TextDecoder--><!--Device-TextDecoder-static create(encoding?: string, options?: TextDecoderOptions): TextDecoder-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| encoding | string | No | Encoding format. The default format is **'utf-8'**.<br>**Since:** 11 |
| options | [TextDecoderOptions](../../apis-default/arkts-apis/arkts-util-textdecoderoptions-i.md) | No | Decoding-related options, which include **fatal** and **ignoreBOM**.<br>**Since:** 11 |

**Return value:**

| Type | Description |
| --- | --- |
| [TextDecoder](../../apis-default/arkts-apis/arkts-util-textdecoder-c.md) | TextDecoder** object created. |

**Examples**

```TypeScript
let textDecoderOptions: util.TextDecoderOptions = {
  fatal: false,
  ignoreBOM : true
}
let textDecoder = util.TextDecoder.create('utf-8', textDecoderOptions);
let retStr = textDecoder.encoding;
console.info('retStr = ' + retStr);
// Output: retStr = utf-8
```

```TypeScript
let textEncoder = util.TextEncoder.create("utf-8");
```

## decode

```TypeScript
decode(input: Uint8Array, options?: { stream?: false }): string
```

Decodes the input content into a string.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [decodeToString](../../apis-default/arkts-apis/arkts-util-textdecoder-c.md#decodetostring)

<!--Device-TextDecoder-decode(input: Uint8Array, options?: { stream?: false }): string--><!--Device-TextDecoder-decode(input: Uint8Array, options?: { stream?: false }): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| input | Uint8Array | Yes | Uint8Array object to decode. |
| options | { stream?: false } | No | Decoding-related options. |

**Return value:**

| Type | Description |
| --- | --- |
| string | String obtained. |

**Examples**

```TypeScript
let textDecoder = new util.TextDecoder("utf-8",{ignoreBOM: true});
let uint8 = new Uint8Array(6);
uint8[0] = 0xEF;
uint8[1] = 0xBB;
uint8[2] = 0xBF;
uint8[3] = 0x61;
uint8[4] = 0x62;
uint8[5] = 0x63;
console.info("input num:");
let retStr = textDecoder.decode(uint8, {stream: false});
console.info("retStr = " + retStr);
// Output: retStr = abc
```

```TypeScript
let base64Helper = new util.Base64Helper();
let array = 'TWFuaXNkaXN0aW5ndWlzaGVkbm90b25seWJ5aGlzcmVhc29uYnV0Ynl0aGlzc2luZ3VsYXJwYXNz\r\naW9uZnJvbW90aGVyYW5pbWFsc3doaWNoaXNhbHVzdG9mdGhlbWluZGV4Y2VlZHN0aGVzaG9ydHZl\r\naGVtZW5jZW9mYW55Y2FybmFscGxlYXN1cmU=\r\n';
base64Helper.decode(array, util.Type.MIME).then((val) => {
  console.info(val.toString());
  /*
  Output: 77,97,110,105,115,100,105,115,116,105,110,103,117,105,115,104,101,100,110,111,116,111,110,108,121,98,121,104,105,115,114,101,97,115,111,110,98,117,116,98,121,116,104,105,115,115,105,110,103,117,108,97,114,112,97,115,115,105,111,110,102,114,111,109,111,116,104,101,114,97,110,105,109,97,108,115,119,104,105,99,104,105,115,97,108,117,115,116,111,102,116,104,101,109,105,110,100,101,120,99,101,101,100,115,116,104,101,115,104,111,114,116,118,101,104,101,109,101,110,99,101,111,102,97,110,121,99,97,114,110,97,108,112,108,101,97,115,117,114,101
  */
})
```

```TypeScript
let base64 = new util.Base64();
let array = new Uint8Array([99,122,69,122]);
base64.decode(array).then((val) => {
  console.info(val.toString());
  // Output: 115,49,51
})
```

## decodeToString

```TypeScript
decodeToString(input: Uint8Array, options?: DecodeToStringOptions): string
```

Decodes the input content into a string.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TextDecoder-decodeToString(input: Uint8Array, options?: DecodeToStringOptions): string--><!--Device-TextDecoder-decodeToString(input: Uint8Array, options?: DecodeToStringOptions): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| input | Uint8Array | Yes | Uint8Array object to decode. |
| options | [DecodeToStringOptions](../../apis-default/arkts-apis/arkts-util-decodetostringoptions-i.md) | No | Decoding-related options. The default value is **undefined**. |

**Return value:**

| Type | Description |
| --- | --- |
| string | String obtained. |

**Examples**

```TypeScript
let textDecoderOptions: util.TextDecoderOptions = {
  fatal: false,
  ignoreBOM : true
}
let decodeToStringOptions: util.DecodeToStringOptions = {
  stream: false
}
let textDecoder = util.TextDecoder.create('utf-8', textDecoderOptions);
let uint8 = new Uint8Array([0xEF, 0xBB, 0xBF, 0x61, 0x62, 0x63]);
let retStr = textDecoder.decodeToString(uint8, decodeToStringOptions);
console.info("retStr = " + retStr);
// Output: retStr = abc
```

## decodeWithStream

```TypeScript
decodeWithStream(input: Uint8Array, options?: DecodeWithStreamOptions): string
```

Decodes the input content into a string. If **input** is an empty array, **undefined** is returned.

**Since:** 9

**Deprecated since:** 12

**Substitutes:** [decodeToString](../../apis-default/arkts-apis/arkts-util-textdecoder-c.md#decodetostring)

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-TextDecoder-decodeWithStream(input: Uint8Array, options?: DecodeWithStreamOptions): string--><!--Device-TextDecoder-decodeWithStream(input: Uint8Array, options?: DecodeWithStreamOptions): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| input | Uint8Array | Yes | Uint8Array object to decode. |
| options | [DecodeWithStreamOptions](arkts-arkts-util-decodewithstreamoptions-i.md) | No | Decoding-related options.<br>**Since:** 11 |

**Return value:**

| Type | Description |
| --- | --- |
| string | String obtained. |

**Examples**

```TypeScript
let textDecoderOptions: util.TextDecoderOptions = {
  fatal: false,
  ignoreBOM : true
}
let decodeWithStreamOptions: util.DecodeWithStreamOptions = {
  stream: false
}
let textDecoder = util.TextDecoder.create('utf-8', textDecoderOptions);
let uint8 = new Uint8Array(6);
uint8[0] = 0xEF;
uint8[1] = 0xBB;
uint8[2] = 0xBF;
uint8[3] = 0x61;
uint8[4] = 0x62;
uint8[5] = 0x63;
console.info("input num:");
let retStr = textDecoder.decodeWithStream(uint8, decodeWithStreamOptions);
console.info("retStr = " + retStr);
// Output: retStr = abc
```

## encoding

```TypeScript
readonly encoding: string
```

Encoding format.<br>The following formats are supported: utf-8, ibm866, iso-8859-2, iso-8859-3, iso-8859-4, iso-8 859-5, iso-8859-6, iso-8859-7, iso-8859-8, iso-8859-8-i, iso-8859-10, iso-8859-13, iso-8859-14, iso-8859-15, koi8 -r, koi8-u, macintosh, windows-874, windows-1250, windows-1251, windows-1252, windows-1253, windows-1254, windows -1255, windows-1256, windows-1257, windows-1258, x-mac-cyrillic, gbk, gb18030, big5, euc-jp, iso-2022-jp, shift_jis, euc-kr, utf-16be, utf-16le, gb2312, and iso-8859-1.

**Type:** string

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TextDecoder-readonly encoding: string--><!--Device-TextDecoder-readonly encoding: string-End-->

**System capability:** SystemCapability.Utils.Lang

## fatal

```TypeScript
readonly fatal: boolean
```

Whether to display fatal errors. The value **true** means to display fatal errors, and **false** means the opposite.

**Type:** boolean

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TextDecoder-readonly fatal: boolean--><!--Device-TextDecoder-readonly fatal: boolean-End-->

**System capability:** SystemCapability.Utils.Lang

## ignoreBOM

```TypeScript
readonly ignoreBOM = false
```

Whether to ignore the byte order marker (BOM). The default value is **false**, which indicates that the result contains the BOM.

**Type:** false

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TextDecoder-readonly ignoreBOM = false--><!--Device-TextDecoder-readonly ignoreBOM = false-End-->

**System capability:** SystemCapability.Utils.Lang

