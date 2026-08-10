# byteLength

## Modules to Import

```TypeScript
import { buffer } from 'kits/@kit.ArkTS';
```

## byteLength

```TypeScript
function byteLength(
    string: string | Buffer | TypedArray | DataView | ArrayBuffer | SharedArrayBuffer,
    encoding?: BufferEncoding
  ): number
```

根据不同的编码格式，返回指定数据的字节数。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-buffer-function byteLength(    string: string | Buffer | TypedArray | DataView | ArrayBuffer | SharedArrayBuffer,    encoding?: BufferEncoding  ): number--><!--Device-buffer-function byteLength(    string: string | Buffer | TypedArray | DataView | ArrayBuffer | SharedArrayBuffer,    encoding?: BufferEncoding  ): number-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| string | string \| Buffer \| TypedArray \| DataView \| ArrayBuffer \| SharedArrayBuffer | Yes | 要计算字节长度的字符串或其他数据对象。 |
| encoding | [BufferEncoding](arkts-arkts-fastbuffer-bufferencoding-t.md) | No | 编码格式（string参数为string类型时才有意义）。默认值：'utf8'。 |

**Return value:**

| Type | Description |
| --- | --- |
| number | 返回指定字符串的字节数。 |

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

根据不同的编码格式，返回指定字符串的字节数。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-buffer-function byteLength(    doc: string | Buffer | TypedArray | DataView | ArrayBuffer,    encoding?: BufferEncoding  ): int--><!--Device-buffer-function byteLength(    doc: string | Buffer | TypedArray | DataView | ArrayBuffer,    encoding?: BufferEncoding  ): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| doc | string \| Buffer \| TypedArray \| DataView \| ArrayBuffer | Yes | 指定字符串。 |
| encoding | [BufferEncoding](arkts-arkts-fastbuffer-bufferencoding-t.md) | No | 编码格式。默认值：'utf8'。 |

**Return value:**

| Type | Description |
| --- | --- |
| int | 返回指定字符串的字节数 |

