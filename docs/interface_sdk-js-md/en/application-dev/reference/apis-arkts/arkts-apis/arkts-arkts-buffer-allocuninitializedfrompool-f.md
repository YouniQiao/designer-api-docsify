# allocUninitializedFromPool

## allocUninitializedFromPool

```TypeScript
function allocUninitializedFromPool(size: int): Buffer
```

Creates a **Buffer** object of the specified size from the buffer pool, without initializing it.You need to use [fill()]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ to initialize the **Buffer** object created.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-buffer-function allocUninitializedFromPool(size: int): Buffer--><!--Device-buffer-function allocUninitializedFromPool(size: int): Buffer-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| size | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：int | Yes | Size of the **Buffer** object to create, in bytes. |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | Uninitialized **Buffer** object. |

**Example**

```TypeScript
import { buffer, JSON } from '@kit.ArkTS';

let buf = buffer.allocUninitializedFromPool(10);
buf.fill(0);
console.info(JSON.stringify(buf)); // {"type":"Buffer","data":[0,0,0,0,0,0,0,0,0,0]}
```

