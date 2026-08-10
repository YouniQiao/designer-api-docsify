# isEncoding

## Modules to Import

```TypeScript
import { buffer } from 'kits/@kit.ArkTS';
```

## isEncoding

```TypeScript
function isEncoding(encoding: string): boolean
```

判断`encoding`是否为支持的编码格式。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-buffer-function isEncoding(encoding: string): boolean--><!--Device-buffer-function isEncoding(encoding: string): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| encoding | string | Yes | 编码格式，支持的格式范围为[BufferEncoding](arkts-arkts-buffer-bufferencoding-t.md)。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 是支持的编码格式返回true，反之则返回false。 |

## Examples

```TypeScript
import { buffer } from '@kit.ArkTS';

console.info(buffer.isEncoding('utf-8').toString());
// Output: true
console.info(buffer.isEncoding('hex').toString());
// Output: true
console.info(buffer.isEncoding('utf/8').toString());
// Output: false
console.info(buffer.isEncoding('').toString());
// Output: false
```

