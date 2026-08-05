# compare

## compare

```TypeScript
function compare(buf1: Buffer | Uint8Array, buf2: Buffer | Uint8Array): -1 | 0 | 1
```

Compares two **Buffer** objects. This API is used for sorting **Buffer** objects.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-buffer-function compare(buf1: Buffer | Uint8Array, buf2: Buffer | Uint8Array): -1 | 0 | 1--><!--Device-buffer-function compare(buf1: Buffer | Uint8Array, buf2: Buffer | Uint8Array): -1 | 0 | 1-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| buf1 | \_\_\_MD\_LINK\_USD\_0\_\_\_ \| Uint8Array | Yes | **Buffer** object to compare. |
| buf2 | \_\_\_MD\_LINK\_USD\_0\_\_\_ \| Uint8Array | Yes | **Buffer** object to compare. |

**Return value:**

| Type | Description |
| --- | --- |
| -1 | Returns **0** if **buf1** is the same as **buf2**. |

**Example**

```TypeScript
import { buffer } from '@kit.ArkTS';

let buf1 = buffer.from('1234');
let buf2 = buffer.from('0123');
let res = buffer.compare(buf1, buf2);

console.info(Number(res).toString());
// Output: 1
```


## compare

```TypeScript
function compare(buf1: Buffer | Uint8Array, buf2: Buffer | Uint8Array): int
```

Compares buf1 to buf2

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-buffer-function compare(buf1: Buffer | Uint8Array, buf2: Buffer | Uint8Array): int--><!--Device-buffer-function compare(buf1: Buffer | Uint8Array, buf2: Buffer | Uint8Array): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| buf1 | \_\_\_MD\_LINK\_USD\_0\_\_\_ \| Uint8Array | Yes | First buffer for comparison |
| buf2 | \_\_\_MD\_LINK\_USD\_0\_\_\_ \| Uint8Array | Yes | Second buffer for comparison |

**Return value:**

| Type | Description |
| --- | --- |
| int | 0 is returned if target is the same as buf |

