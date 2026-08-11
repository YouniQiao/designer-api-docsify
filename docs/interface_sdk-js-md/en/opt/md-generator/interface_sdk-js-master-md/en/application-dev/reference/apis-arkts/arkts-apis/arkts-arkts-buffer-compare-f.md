# compare

## Modules to Import

```TypeScript
import { buffer } from 'kits/@kit.ArkTS';
```

## compare

```TypeScript
function compare(buf1: Buffer | Uint8Array, buf2: Buffer | Uint8Array): -1 | 0 | 1
```

Compares two **Buffer** objects. This API is used for sorting **Buffer** objects.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-buffer-function compare(buf1: Buffer | Uint8Array, buf2: Buffer | Uint8Array): -1 | 0 | 1--><!--Device-buffer-function compare(buf1: Buffer | Uint8Array, buf2: Buffer | Uint8Array): -1 | 0 | 1-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| buf1 | [Buffer](arkts-arkts-buffer-buffer-c.md) \| Uint8Array | Yes |
| buf2 | [Buffer](arkts-arkts-buffer-buffer-c.md) \| Uint8Array | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| -1 |

## Examples

```TypeScript
import { buffer } from '@kit.ArkTS';

let buf1 = buffer.from('1234');
let buf2 = buffer.from('0123');
let res = buffer.compare(buf1, buf2);

console.info(Number(res).toString());
// Output: 1
```
