# concat

## concat

```TypeScript
function concat(list: FastBuffer[] | Uint8Array[], totalLength?: number): FastBuffer
```

Returns a new \_\_\_INLINE\_CODE\_DESC\_USD\_0\_\_\_ which is the result of concatenating all the \_\_\_INLINE\_CODE\_DESC\_USD\_1\_\_\_instances in the \_\_\_INLINE\_CODE\_DESC\_USD\_2\_\_\_ together.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-fastbuffer-function concat(list: FastBuffer[] | Uint8Array[], totalLength?: number): FastBuffer--><!--Device-fastbuffer-function concat(list: FastBuffer[] | Uint8Array[], totalLength?: number): FastBuffer-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| list | FastBuffer[] \| Uint8Array[] | Yes | Array of FastBuffer or Uint8Array instances to concatenate |
| totalLength | number | No | Total length of the FastBuffer instances when concatenated |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | Return a new allocated FastBuffer |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [10200001](../errorcode-utils.md#10200001-value-out-of-range) | Range error. Possible causes:The value of the parameter is not within the specified range. |

**Example**

```TypeScript
import { fastbuffer } from '@kit.ArkTS';

let buf1 = fastbuffer.from("1234");
let buf2 = fastbuffer.from("abcd");
let buf = fastbuffer.concat([buf1, buf2]);
console.info(buf.toString('hex'));
// Output: 3132333461626364
```

