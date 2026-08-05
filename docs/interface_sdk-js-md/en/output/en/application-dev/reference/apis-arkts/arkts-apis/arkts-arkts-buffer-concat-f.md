# concat

## concat

```TypeScript
function concat(list: Buffer[] | Uint8Array[], totalLength?: int): Buffer
```

Concatenates an array of **Buffer** objects of the specified length into a new object.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-buffer-function concat(list: Buffer[] | Uint8Array[], totalLength?: int): Buffer--><!--Device-buffer-function concat(list: Buffer[] | Uint8Array[], totalLength?: int): Buffer-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| list | Buffer[] \| Uint8Array[] | Yes | Array of objects to concatenate. |
| totalLength | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：int | No | Total length of bytes to be copied. The default value is **0**. |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | **Buffer** object created. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [10200001](../errorcode-utils.md#10200001-value-out-of-range) | The value of "length" is out of range. It must be >= 0 and <= uint32 max.Received value is: [length] |

**Example**

```TypeScript
import { buffer } from '@kit.ArkTS';

let buf1 = buffer.from("1234");
let buf2 = buffer.from("abcd");
let buf = buffer.concat([buf1, buf2]);
console.info(buf.toString('hex'));
// Output: 3132333461626364
```

