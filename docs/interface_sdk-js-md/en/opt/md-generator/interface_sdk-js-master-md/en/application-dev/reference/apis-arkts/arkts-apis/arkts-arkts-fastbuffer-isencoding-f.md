# isEncoding

## Modules to Import

```TypeScript
import { fastbuffer } from 'kits/@kit.ArkTS';
```

## isEncoding

```TypeScript
function isEncoding(encoding: string): boolean
```

Returns true if encoding is the name of a supported character encoding, or false otherwise.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-fastbuffer-function isEncoding(encoding: string): boolean--><!--Device-fastbuffer-function isEncoding(encoding: string): boolean-End-->

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
import { fastbuffer } from '@kit.ArkTS';

console.info(fastbuffer.isEncoding('utf-8').toString());
// Output: true
console.info(fastbuffer.isEncoding('hex').toString());
// Output: true
console.info(fastbuffer.isEncoding('utf/8').toString());
// Output: false
console.info(fastbuffer.isEncoding('').toString());
// Output: false
```
