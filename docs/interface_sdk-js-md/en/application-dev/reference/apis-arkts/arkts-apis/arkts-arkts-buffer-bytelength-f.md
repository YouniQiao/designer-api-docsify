# byteLength

## Modules to Import

```TypeScript
import { buffer } from 'buffer';
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

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-buffer-function byteLength(    string: string | Buffer | TypedArray | DataView | ArrayBuffer | SharedArrayBuffer,    encoding?: BufferEncoding  ): number--><!--Device-buffer-function byteLength(    string: string | Buffer | TypedArray | DataView | ArrayBuffer | SharedArrayBuffer,    encoding?: BufferEncoding  ): number-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| string | string \| [Buffer](arkts-arkts-buffer-buffer-c.md) \| TypedArray \| DataView \| ArrayBuffer \| SharedArrayBuffer | Yes | Target string. |
| encoding | BufferEncoding | No | Encoding format. The default value is **'utf8'**. |

**Return value:**

| Type | Description |
| --- | --- |
| number | Number of bytes of the string. |

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
  ): int
```

Obtains the number of bytes of a string based on the encoding format.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-buffer-function byteLength(    doc: string | Buffer | TypedArray | DataView | ArrayBuffer,    encoding?: BufferEncoding  ): int--><!--Device-buffer-function byteLength(    doc: string | Buffer | TypedArray | DataView | ArrayBuffer,    encoding?: BufferEncoding  ): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| doc | string \| [Buffer](arkts-arkts-buffer-buffer-c.md) \| TypedArray \| DataView \| ArrayBuffer | Yes | Target string. |
| encoding | BufferEncoding | No | Encoding format of the string. The default value is 'utf8'. |

**Return value:**

| Type | Description |
| --- | --- |
| int | The number of bytes contained within `string` |

