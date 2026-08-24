# Base64

Decodes a string or Uint8Array containing Base64 data into a newly allocated Uint8Array.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [Base64Helper](../../apis-default/arkts-apis/arkts-util-base64helper-c.md)

<!--Device-util-class Base64--><!--Device-util-class Base64-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { util } from '@kit.ArkTS';
```

## constructor

```TypeScript
constructor()
```

A constructor used to create a **Base64** object.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [constructor](../../apis-default/arkts-apis/arkts-util-base64helper-c.md#constructor)

<!--Device-Base64-constructor()--><!--Device-Base64-constructor()-End-->

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

## decode

```TypeScript
decode(src: Uint8Array | string): Promise<Uint8Array>
```

Decodes the input content into a Uint8Array object. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [decode](../../apis-default/arkts-apis/arkts-util-base64helper-c.md#decode)

<!--Device-Base64-decode(src: Uint8Array | string): Promise<Uint8Array>--><!--Device-Base64-decode(src: Uint8Array | string): Promise<Uint8Array>-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| src | Uint8Array \| string | Yes | Uint8Array object or string to decode. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Uint8Array&gt; | Promise used to return the Uint8Array object obtained. |

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

## decodeSync

```TypeScript
decodeSync(src: Uint8Array | string): Uint8Array
```

Decodes the input content into a Uint8Array object.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [decodeSync](../../apis-default/arkts-apis/arkts-util-base64helper-c.md#decodesync)

<!--Device-Base64-decodeSync(src: Uint8Array | string): Uint8Array--><!--Device-Base64-decodeSync(src: Uint8Array | string): Uint8Array-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| src | Uint8Array \| string | Yes | Uint8Array object or string to decode. |

**Return value:**

| Type | Description |
| --- | --- |
| Uint8Array | Uint8Array object obtained. |

**Examples**

```TypeScript
let base64Helper = new util.Base64Helper();
let buff = 'TWFuaXNkaXN0aW5ndWlzaGVkbm90b25seWJ5aGlzcmVhc29uYnV0Ynl0aGlzc2luZ3VsYXJwYXNz\r\naW9uZnJvbW90aGVyYW5pbWFsc3doaWNoaXNhbHVzdG9mdGhlbWluZGV4Y2VlZHN0aGVzaG9ydHZl\r\naGVtZW5jZW9mYW55Y2FybmFscGxlYXN1cmU=\r\n';
let result = base64Helper.decodeSync(buff, util.Type.MIME);
console.info("result = " + result);
/*
Output: result = 77,97,110,105,115,100,105,115,116,105,110,103,117,105,115,104,101,100,110,111,116,111,110,108,121,98,121,104,105,115,114,101,97,115,111,110,98,117,116,98,121,116,104,105,115,115,105,110,103,117,108,97,114,112,97,115,115,105,111,110,102,114,111,109,111,116,104,101,114,97,110,105,109,97,108,115,119,104,105,99,104,105,115,97,108,117,115,116,111,102,116,104,101,109,105,110,100,101,120,99,101,101,100,115,116,104,101,115,104,111,114,116,118,101,104,101,109,101,110,99,101,111,102,97,110,121,99,97,114,110,97,108,112,108,101,97,115,117,114,101
*/
```

```TypeScript
let base64 = new util.Base64();
let buff = 'czEz';
let result = base64.decodeSync(buff);
console.info("result = " + result);
// Output: result = 115,49,51
```

## encode

```TypeScript
encode(src: Uint8Array): Promise<Uint8Array>
```

Encodes the input content into a Uint8Array object. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [encode](../../apis-default/arkts-apis/arkts-util-base64helper-c.md#encode)

<!--Device-Base64-encode(src: Uint8Array): Promise<Uint8Array>--><!--Device-Base64-encode(src: Uint8Array): Promise<Uint8Array>-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| src | Uint8Array | Yes | Uint8Array object to encode. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Uint8Array&gt; | Promise used to return the Uint8Array object obtained. |

**Examples**

```TypeScript
let textEncoder = new util.TextEncoder();
let result = textEncoder.encode("\uD800¥¥");
console.info("result = " + result);
// Output: result = 237,160,128,194,165,194,165
```

```TypeScript
let base64Helper = new util.Base64Helper();
let array = new Uint8Array([115,49,51]);
base64Helper.encode(array).then((val) => {
  console.info(val.toString());
  // Output: 99,122,69,122
})
```

```TypeScript
let base64 = new util.Base64();
let array = new Uint8Array([115,49,51]);
base64.encode(array).then((val) => {
  console.info(val.toString());
  // Output: 99,122,69,122
})
```

## encodeSync

```TypeScript
encodeSync(src: Uint8Array): Uint8Array
```

Performs Base64 encoding on the input Uint8Array byte array and returns the encoded Uint8Array.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [encodeSync](../../apis-default/arkts-apis/arkts-util-base64helper-c.md#encodesync)

<!--Device-Base64-encodeSync(src: Uint8Array): Uint8Array--><!--Device-Base64-encodeSync(src: Uint8Array): Uint8Array-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| src | Uint8Array | Yes | Uint8Array object to encode. |

**Return value:**

| Type | Description |
| --- | --- |
| Uint8Array | Uint8Array object obtained. |

**Examples**

```TypeScript
let base64Helper = new util.Base64Helper();
let array = new Uint8Array([115,49,51]);
let result = base64Helper.encodeSync(array);
console.info("result = " + result);
// Output: result = 99,122,69,122
```

```TypeScript
let base64 = new util.Base64();
let array = new Uint8Array([115,49,51]);
let result = base64.encodeSync(array);
console.info("result = " + result);
// Output: result = 99,122,69,122
```

## encodeToString

```TypeScript
encodeToString(src: Uint8Array): Promise<string>
```

Encodes the input content into a string. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [encodeToString](../../apis-default/arkts-apis/arkts-util-base64helper-c.md#encodetostring)

<!--Device-Base64-encodeToString(src: Uint8Array): Promise<string>--><!--Device-Base64-encodeToString(src: Uint8Array): Promise<string>-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| src | Uint8Array | Yes | Uint8Array object to encode. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;string&gt; | Promise used to return the string obtained. |

**Examples**

```TypeScript
let base64Helper = new util.Base64Helper();
let array = new Uint8Array([77,97,110,105,115,100,105,115,116,105,110,103,117,105,115,104,101,100,110,111,116,111,110,108,121,98,121,104,105,115,114,101,97,115,111,110,98,117,116,98,121,116,104,105,115,115,105,110,103,117,108,97,114,112,97,115,115,105,111,110,102,114,111,109,111,116,104,101,114,97,110,105,109,97,108,115,119,104,105,99,104,105,115,97,108,117,115,116,111,102,116,104,101,109,105,110,100,101,120,99,101,101,100,115,116,104,101,115,104,111,114,116,118,101,104,101,109,101,110,99,101,111,102,97,110,121,99,97,114,110,97,108,112,108,101,97,115,117,114,101]);
base64Helper.encodeToString(array, util.Type.MIME).then((val) => {
  console.info(val);
  /*
  Output: TWFuaXNkaXN0aW5ndWlzaGVkbm90b25seWJ5aGlzcmVhc29uYnV0Ynl0aGlzc2luZ3VsYXJwYXNz
  aW9uZnJvbW90aGVyYW5pbWFsc3doaWNoaXNhbHVzdG9mdGhlbWluZGV4Y2VlZHN0aGVzaG9ydHZl
  aGVtZW5jZW9mYW55Y2FybmFscGxlYXN1cmU=
  */

})
```

```TypeScript
let base64 = new util.Base64();
let array = new Uint8Array([115,49,51]);
base64.encodeToString(array).then((val) => {
    console.info(val);
    // Output: czEz
})
```

## encodeToStringSync

```TypeScript
encodeToStringSync(src: Uint8Array): string
```

Performs Base64 encoding on the input Uint8Array byte array and returns the encoded string.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [encodeToStringSync](../../apis-default/arkts-apis/arkts-util-base64helper-c.md#encodetostringsync)

<!--Device-Base64-encodeToStringSync(src: Uint8Array): string--><!--Device-Base64-encodeToStringSync(src: Uint8Array): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| src | Uint8Array | Yes | Uint8Array object to encode. |

**Return value:**

| Type | Description |
| --- | --- |
| string | String obtained. |

**Examples**

```TypeScript
// MIME encoding
let base64Helper = new util.Base64Helper();
let array =
  new Uint8Array([77, 97, 110, 105, 115, 100, 105, 115, 116, 105, 110, 103, 117, 105, 115, 104, 101, 100, 110, 111, 116,
    111, 110, 108, 121, 98, 121, 104, 105, 115, 114, 101, 97, 115, 111, 110, 98, 117, 116, 98, 121, 116, 104, 105, 115,
    115, 105, 110, 103, 117, 108, 97, 114, 112, 97, 115, 115, 105, 111, 110, 102, 114, 111, 109, 111, 116, 104, 101,
    114, 97, 110, 105, 109, 97, 108, 115, 119, 104, 105, 99, 104, 105, 115, 97, 108, 117, 115, 116, 111, 102, 116, 104,
    101, 109, 105, 110, 100, 101, 120, 99, 101, 101, 100, 115, 116, 104, 101, 115, 104, 111, 114, 116, 118, 101, 104,
    101, 109, 101, 110, 99, 101, 111, 102, 97, 110, 121, 99, 97, 114, 110, 97, 108, 112, 108, 101, 97, 115, 117, 114,
    101]);
let result = base64Helper.encodeToStringSync(array, util.Type.MIME);
console.info("result = " + result);
/*
// Output: result = TWFuaXNkaXN0aW5ndWlzaGVkbm90b25seWJ5aGlzcmVhc29uYnV0Ynl0aGlzc2luZ3VsYXJwYXNz
aW9uZnJvbW90aGVyYW5pbWFsc3doaWNoaXNhbHVzdG9mdGhlbWluZGV4Y2VlZHN0aGVzaG9ydHZl
aGVtZW5jZW9mYW55Y2FybmFscGxlYXN1cmU=
*/

// BASIC encoding
let base64Helper = new util.Base64Helper();
let array =
  new Uint8Array([77, 97, 110, 105, 115, 100, 105, 115, 116, 105, 110, 103, 117, 105, 115, 104, 101, 100, 110, 111, 116,
    111, 110, 108, 121, 98, 121, 104, 105, 115, 114, 101, 97, 115, 111, 110, 98, 117, 116, 98, 121, 116, 104, 105, 115,
    115, 105, 110, 103, 117, 108, 97, 114, 112, 97, 115, 115, 105, 111, 110, 102, 114, 111, 109, 111, 116, 104, 101,
    114, 97, 110, 105, 109, 97, 108, 115, 119, 104, 105, 99, 104, 105, 115, 97, 108, 117, 115, 116, 111, 102, 116, 104,
    101, 109, 105, 110, 100, 101, 120, 99, 101, 101, 100, 115, 116, 104, 101, 115, 104, 111, 114, 116, 118, 101, 104,
    101, 109, 101, 110, 99, 101, 111, 102, 97, 110, 121, 99, 97, 114, 110, 97, 108, 112, 108, 101, 97, 115, 117, 114,
    101]);
let result = base64Helper.encodeToStringSync(array, util.Type.BASIC);
console.info("result = " + result);
/*
Output: result = TWFuaXNkaXN0aW5ndWlzaGVkbm90b25seWJ5aGlzcmVhc29uYnV0Ynl0aGlzc2luZ3VsYXJwYXNzaW9uZnJvbW90aGVyYW5pbWFsc3doaWNoaXNhbHVzdG9mdGhlbWluZGV4Y2VlZHN0aGVzaG9ydHZlaGVtZW5jZW9mYW55Y2FybmFscGxlYXN1cmU=
*/

// MIME_URL_SAFE encoding
let base64Helper = new util.Base64Helper();
let array =
  new Uint8Array([77, 97, 110, 105, 115, 100, 105, 115, 116, 105, 110, 103, 117, 105, 115, 104, 101, 100, 110, 111, 116,
    111, 110, 108, 121, 98, 121, 104, 105, 115, 114, 101, 97, 115, 111, 110, 98, 117, 116, 98, 121, 116, 104, 105, 115,
    115, 105, 110, 103, 117, 108, 97, 114, 112, 97, 115, 115, 105, 111, 110, 102, 114, 111, 109, 111, 116, 104, 101,
    114, 97, 110, 105, 109, 97, 108, 115, 119, 104, 105, 99, 104, 105, 115, 97, 108, 117, 115, 116, 111, 102, 116, 104,
    101, 109, 105, 110, 100, 101, 120, 99, 101, 101, 100, 115, 116, 104, 101, 115, 104, 111, 114, 116, 118, 101, 104,
    101, 109, 101, 110, 99, 101, 111, 102, 97, 110, 121, 99, 97, 114, 110, 97, 108, 112, 108, 101, 97, 115, 117, 114,
    101]);
let result = base64Helper.encodeToStringSync(array, util.Type.BASIC_URL_SAFE);
console.info("result = " + result);
/*
Output: result = TWFuaXNkaXN0aW5ndWlzaGVkbm90b25seWJ5aGlzcmVhc29uYnV0Ynl0aGlzc2luZ3VsYXJwYXNzaW9uZnJvbW90aGVyYW5pbWFsc3doaWNoaXNhbHVzdG9mdGhlbWluZGV4Y2VlZHN0aGVzaG9ydHZlaGVtZW5jZW9mYW55Y2FybmFscGxlYXN1cmU
*/
// MIME_URL_SAFE encoding
let base64Helper = new util.Base64Helper();
let array =
  new Uint8Array([77, 97, 110, 105, 115, 100, 105, 115, 116, 105, 110, 103, 117, 105, 115, 104, 101, 100, 110, 111, 116,
    111, 110, 108, 121, 98, 121, 104, 105, 115, 114, 101, 97, 115, 111, 110, 98, 117, 116, 98, 121, 116, 104, 105, 115,
    115, 105, 110, 103, 117, 108, 97, 114, 112, 97, 115, 115, 105, 111, 110, 102, 114, 111, 109, 111, 116, 104, 101,
    114, 97, 110, 105, 109, 97, 108, 115, 119, 104, 105, 99, 104, 105, 115, 97, 108, 117, 115, 116, 111, 102, 116, 104,
    101, 109, 105, 110, 100, 101, 120, 99, 101, 101, 100, 115, 116, 104, 101, 115, 104, 111, 114, 116, 118, 101, 104,
    101, 109, 101, 110, 99, 101, 111, 102, 97, 110, 121, 99, 97, 114, 110, 97, 108, 112, 108, 101, 97, 115, 117, 114,
    101]);
let result = base64Helper.encodeToStringSync(array, util.Type.MIME_URL_SAFE);
console.info("result = " + result);
/*
// Output: result = TWFuaXNkaXN0aW5ndWlzaGVkbm90b25seWJ5aGlzcmVhc29uYnV0Ynl0aGlzc2luZ3VsYXJwYXNz
aW9uZnJvbW90aGVyYW5pbWFsc3doaWNoaXNhbHVzdG9mdGhlbWluZGV4Y2VlZHN0aGVzaG9ydHZl
aGVtZW5jZW9mYW55Y2FybmFscGxlYXN1cmU
*/
```

```TypeScript
let base64 = new util.Base64();
let array = new Uint8Array([115,49,51]);
let result = base64.encodeToStringSync(array);
console.info("result = " + result);
// Output: result = czEz
```

