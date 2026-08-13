# isEncoding

## Modules to Import

```TypeScript
import { buffer } from '@kit.ArkTS';
```

## isEncoding

```TypeScript
function isEncoding(encoding: string): boolean
```

Checks whether the encoding format is supported.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-buffer-function isEncoding(encoding: string): boolean--><!--Device-buffer-function isEncoding(encoding: string): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| encoding | string | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |

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
