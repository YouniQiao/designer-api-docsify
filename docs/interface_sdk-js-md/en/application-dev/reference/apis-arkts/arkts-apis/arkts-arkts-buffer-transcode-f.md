# transcode

## Modules to Import

```TypeScript
import { buffer } from 'kits/@kit.ArkTS';
```

## transcode

```TypeScript
function transcode(source: Buffer | Uint8Array, fromEnc: string, toEnc: string): Buffer
```

将Buffer或Uint8Array对象从一种字符编码重新编码为另一种。适用于需要在不同编码格式之间转换已有Buffer数据的场景。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-buffer-function transcode(source: Buffer | Uint8Array, fromEnc: string, toEnc: string): Buffer--><!--Device-buffer-function transcode(source: Buffer | Uint8Array, fromEnc: string, toEnc: string): Buffer-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| source | [Buffer](arkts-arkts-buffer-buffer-c.md) \| Uint8Array | Yes | 待转码的Buffer或Uint8Array实例，提供需要重新编码的源数据。 |
| fromEnc | string | Yes | 当前编码。 支持的格式范围为[BufferEncoding](arkts-arkts-buffer-bufferencoding-t.md)。 |
| toEnc | string | Yes | 目标编码。 支持的格式范围为[BufferEncoding](arkts-arkts-buffer-bufferencoding-t.md)。 |

**Return value:**

| Type | Description |
| --- | --- |
| [Buffer](arkts-arkts-buffer-buffer-c.md) | 将当前编码转换成目标编码，并返回一个新的Buffer对象。 |

## Examples

```TypeScript
import { buffer } from '@kit.ArkTS';

let newBuf = buffer.transcode(buffer.from('€'), 'utf-8', 'ascii');
console.info("newBuf = " + newBuf.toString('ascii'));
// Output: newBuf = ,
```

