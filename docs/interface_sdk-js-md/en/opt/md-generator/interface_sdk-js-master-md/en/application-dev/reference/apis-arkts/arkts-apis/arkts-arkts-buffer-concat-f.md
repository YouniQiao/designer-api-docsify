# concat

## Modules to Import

```TypeScript
import { buffer } from 'kits/@kit.ArkTS';
```

## concat

```TypeScript
function concat(list: Buffer[] | Uint8Array[], totalLength?: number): Buffer
```

Concatenates an array of **Buffer** objects of the specified length into a new object.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-buffer-function concat(list: Buffer[] | Uint8Array[], totalLength?: int): Buffer--><!--Device-buffer-function concat(list: Buffer[] | Uint8Array[], totalLength?: int): Buffer-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| list | Buffer[] \| Uint8Array[] | Yes |
| totalLength | number | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Buffer](arkts-arkts-buffer-buffer-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-value-out-of-range) |

## Examples

```TypeScript
import { buffer } from '@kit.ArkTS';

let buf1 = buffer.from("1234");
let buf2 = buffer.from("abcd");
let buf = buffer.concat([buf1, buf2]);
console.info(buf.toString('hex'));
// Output: 3132333461626364
```
