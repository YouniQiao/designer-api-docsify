# getTotalSize

## Modules to Import

```TypeScript
import { storageStatistics } from '@kit.CoreFileKit';
```

## getTotalSize

```TypeScript
function getTotalSize(): Promise<long>
```

Get the total size.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-storageStatistics-function getTotalSize(): Promise<long>--><!--Device-storageStatistics-function getTotalSize(): Promise<long>-End-->

**System capability:** SystemCapability.FileManagement.StorageService.SpatialStatistics

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;long&gt; | return Promise (Unit: Byte) |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13600001 | IPC error. |
| 13900042 | Unknown error. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
storageStatistics.getTotalSize().then((number: number) => {
  console.info("getTotalSize successfully:" + JSON.stringify(number));
}).catch((err: BusinessError) => {
  console.error("getTotalSize failed with error:"+ JSON.stringify(err));
});
```

