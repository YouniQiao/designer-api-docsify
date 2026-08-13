# byteLength

## Modules to Import

```TypeScript
import { buffer } from '@kit.ArkTS';
```

## byteLength

```TypeScript
function byteLength(
    string: string | Buffer | TypedArray | DataView | ArrayBuffer | SharedArrayBuffer,
    encoding?: BufferEncoding
  ): number
```

Obtains the number of bytes of a string based on the encoding format.

**Since:** 9

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-buffer-function byteLength(    string: string | Buffer | TypedArray | DataView | ArrayBuffer | SharedArrayBuffer,    encoding?: BufferEncoding  ): number--><!--Device-buffer-function byteLength(    string: string | Buffer | TypedArray | DataView | ArrayBuffer | SharedArrayBuffer,    encoding?: BufferEncoding  ): number-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| string | string \| [Buffer](arkts-arkts-buffer-buffer-c.md) \| TypedArray \| DataView \| ArrayBuffer \| [SharedArrayBuffer](../../apis-na/arkts-apis/arkts-na-lib-es2017-sharedmemory-sharedarraybuffer-i.md) | Yes |
| encoding | [BufferEncoding](arkts-arkts-fastbuffer-bufferencoding-t.md) | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |

## Examples

```TypeScript
import { buffer } from '@kit.ArkTS';

let str = '\u00bd + \u00bc = \u00be';
console.info(`${str}: ${str.length} characters, ${buffer.byteLength(str, 'utf-8')} bytes`);
// Output: ½ + ¼ = ¾: 9 characters, 12 bytes
```


## byteLength

```TypeScript
function byteLength(
    doc: string | Buffer | TypedArray | DataView | ArrayBuffer,
    encoding?: BufferEncoding
  ): number
```

Obtains the number of bytes of a string based on the encoding format.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-buffer-function byteLength(    doc: string | Buffer | TypedArray | DataView | ArrayBuffer,    encoding?: BufferEncoding  ): int--><!--Device-buffer-function byteLength(    doc: string | Buffer | TypedArray | DataView | ArrayBuffer,    encoding?: BufferEncoding  ): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| doc | string \| [Buffer](arkts-arkts-buffer-buffer-c.md) \| TypedArray \| DataView \| ArrayBuffer | Yes |
| encoding | [BufferEncoding](arkts-arkts-fastbuffer-bufferencoding-t.md) | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |
