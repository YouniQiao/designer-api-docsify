# compare

## Modules to Import

```TypeScript
import { buffer } from '@kit.ArkTS';
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

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| buf1 | Buffer \| Uint8Array | Yes | Buffer** object to compare. |
| buf2 | Buffer \| Uint8Array | Yes | Buffer** object to compare. |

**Return value:**

| Type | Description |
| --- | --- |
| -1 \| 0 \| 1 | Returns **0** if **buf1** is the same as **buf2**. <br>Returns **1** if **buf1** comes after **buf2** when sorted. <br>Returns **-1** if **buf1** comes before **buf2** when sorted. |

**Examples**

```TypeScript
import { buffer } from '@kit.ArkTS';

let buf1 = buffer.from('1234');
let buf2 = buffer.from('0123');
let res = buffer.compare(buf1, buf2);

console.info(Number(res).toString());
// Output: 1
```

```TypeScript
import { buffer } from '@kit.ArkTS';

let buf1 = buffer.from([1, 2, 3, 4, 5, 6, 7, 8, 9]);
let buf2 = buffer.from([5, 6, 7, 8, 9, 1, 2, 3, 4]);

console.info(buf1.compare(buf2, 5, 9, 0, 4).toString());
// Output: 0
console.info(buf1.compare(buf2, 0, 6, 4).toString());
// Output: -1
console.info(buf1.compare(buf2, 5, 6, 5).toString());
// Output: 1
```


## compare

```TypeScript
function compare(buf1: Buffer | Uint8Array, buf2: Buffer | Uint8Array): int
```

Compares buf1 to buf2

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-buffer-function compare(buf1: Buffer | Uint8Array, buf2: Buffer | Uint8Array): int--><!--Device-buffer-function compare(buf1: Buffer | Uint8Array, buf2: Buffer | Uint8Array): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| buf1 | Buffer \| Uint8Array | Yes | First buffer for comparison |
| buf2 | Buffer \| Uint8Array | Yes | Second buffer for comparison |

**Return value:**

| Type | Description |
| --- | --- |
| int | 0 is returned if target is the same as buf 1 is returned if target should come before buf when sorted. -1 is returned if target should come after buf when sorted. |

**Examples**

See [compare](#compare)

