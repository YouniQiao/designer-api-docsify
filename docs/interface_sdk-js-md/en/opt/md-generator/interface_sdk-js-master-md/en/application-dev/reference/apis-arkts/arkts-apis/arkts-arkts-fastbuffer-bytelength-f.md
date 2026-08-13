# byteLength

## Modules to Import

```TypeScript
import { fastbuffer } from '@kit.ArkTS';
```

## byteLength

```TypeScript
function byteLength(value: string | FastBuffer | TypedArray | DataView | ArrayBuffer | SharedArrayBuffer, encoding?: BufferEncoding): number
```

Returns the byte length of a string when encoded using `encoding`. This is not the same as [`String.prototype.length`], which does not account for the encoding that is used to convert the string into bytes.

**Since:** 20

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-fastbuffer-function byteLength(value: string | FastBuffer | TypedArray | DataView | ArrayBuffer | SharedArrayBuffer, encoding?: BufferEncoding): number--><!--Device-fastbuffer-function byteLength(value: string | FastBuffer | TypedArray | DataView | ArrayBuffer | SharedArrayBuffer, encoding?: BufferEncoding): number-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | string \| [FastBuffer](arkts-arkts-fastbuffer-fastbuffer-c.md) \| TypedArray \| DataView \| ArrayBuffer \| [SharedArrayBuffer](../../apis-na/arkts-apis/arkts-na-lib-es2017-sharedmemory-sharedarraybuffer-i.md) | Yes |
| encoding | [BufferEncoding](arkts-arkts-fastbuffer-bufferencoding-t.md) | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |

## Examples

```TypeScript
import { fastbuffer } from '@kit.ArkTS';

let str = 'hello world';
console.info(`${str}: ${str.length} characters, ${fastbuffer.byteLength(str, 'utf-8')} bytes`);
// Output: hello world: 11 characters, 11 bytes

str = '\u00bd + \u00bc = \u00be';
console.info(`${str}: ${str.length} characters, ${fastbuffer.byteLength(str, 'utf-8')} bytes`);
// Output: ½ + ¼ = ¾: 9 characters, 12 bytes
```
