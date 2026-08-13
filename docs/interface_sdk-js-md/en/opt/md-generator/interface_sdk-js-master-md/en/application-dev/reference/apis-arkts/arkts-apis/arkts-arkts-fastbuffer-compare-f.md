# compare

## Modules to Import

```TypeScript
import { fastbuffer } from '@kit.ArkTS';
```

## compare

```TypeScript
function compare(buf1: FastBuffer | Uint8Array, buf2: FastBuffer | Uint8Array): -1 | 0 | 1
```

Compares buf1 to buf2

**Since:** 20

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-fastbuffer-function compare(buf1: FastBuffer | Uint8Array, buf2: FastBuffer | Uint8Array): -1 | 0 | 1--><!--Device-fastbuffer-function compare(buf1: FastBuffer | Uint8Array, buf2: FastBuffer | Uint8Array): -1 | 0 | 1-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| buf1 | [FastBuffer](arkts-arkts-fastbuffer-fastbuffer-c.md) \| Uint8Array | Yes |
| buf2 | [FastBuffer](arkts-arkts-fastbuffer-fastbuffer-c.md) \| Uint8Array | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| -1 |

**Error codes:**

| Error Code ID |
| --- |
| [10200068](../errorcode-utils.md#10200068-using-a-released-or-detached-arraybuffer) |

## Examples

```TypeScript
import { fastbuffer } from '@kit.ArkTS';

let buf1 = fastbuffer.from('1234');
let buf2 = fastbuffer.from('0123');
let res = fastbuffer.compare(buf1, buf2);

console.info(Number(res).toString());
// Output: 1
```
