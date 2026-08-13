# getCurrentBundleInodes

## Modules to Import

```TypeScript
import { storageStatistics } from '@kit.CoreFileKit';
```

## getCurrentBundleInodes

```TypeScript
function getCurrentBundleInodes(): Promise<number>
```

Get the current bundle inodes.

**Since:** 24

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-storageStatistics-function getCurrentBundleInodes(): Promise<long>--><!--Device-storageStatistics-function getCurrentBundleInodes(): Promise<long>-End-->

**System capability:** SystemCapability.FileManagement.StorageService.SpatialStatistics

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| 13600002 |
| 13600001 |
| 13600017 |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

storageStatistics.getCurrentBundleInodes().then((curInodes: number) => {
  console.info("getCurrentBundleInodes successfully: " + curInodes);
}).catch((err: BusinessError) => {
  console.error(`getCurrentBundleInodes failed. Code: ${err.code}, Message: ${err.message}`);
});
```
