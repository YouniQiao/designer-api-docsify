# getTotalSize

## Modules to Import

```TypeScript
import { storageStatistics } from '@kit.CoreFileKit';
```

## getTotalSize

```TypeScript
function getTotalSize(): Promise<number>
```

Get the total size.

**Since:** 23

**Deprecated since:** -1

<!--Device-storageStatistics-function getTotalSize(): Promise<long>--><!--Device-storageStatistics-function getTotalSize(): Promise<long>-End-->

**System capability:** SystemCapability.FileManagement.StorageService.SpatialStatistics

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| 13600001 |
| 13900042 |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
storageStatistics.getTotalSize().then((number: number) => {
  console.info("getTotalSize successfully:" + JSON.stringify(number));
}).catch((err: BusinessError) => {
  console.error("getTotalSize failed with error:"+ JSON.stringify(err));
});
```
