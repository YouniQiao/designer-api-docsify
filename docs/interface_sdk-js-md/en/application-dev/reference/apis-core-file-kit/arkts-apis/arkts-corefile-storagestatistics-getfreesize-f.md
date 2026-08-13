# getFreeSize

## Modules to Import

```TypeScript
import { storageStatistics } from '@kit.CoreFileKit';
```

## getFreeSize

```TypeScript
function getFreeSize(): Promise<long>
```

Get the free size.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-storageStatistics-function getFreeSize(): Promise<long>--><!--Device-storageStatistics-function getFreeSize(): Promise<long>-End-->

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
storageStatistics.getFreeSize().then((number: number) => {
  console.info("getFreeSize successfully:" + JSON.stringify(number));
}).catch((err: BusinessError) => {
  console.error("getFreeSize failed with error:" + JSON.stringify(err));
});
```

