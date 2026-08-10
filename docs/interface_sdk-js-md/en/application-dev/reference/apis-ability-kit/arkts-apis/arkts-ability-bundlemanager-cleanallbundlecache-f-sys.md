# cleanAllBundleCache (System API)

## Modules to Import

```TypeScript
import { bundleManager } from 'kits/@kit.AbilityKit';
```

## cleanAllBundleCache

```TypeScript
function cleanAllBundleCache(): Promise<void>
```

清理全局缓存。使用Promise异步回调。

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.REMOVE_CACHE_FILES

<!--Device-bundleManager-function cleanAllBundleCache(): Promise<void>--><!--Device-bundleManager-function cleanAllBundleCache(): Promise<void>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 201 | Permission denied. |
| 202 | Permission denied, non-system app called system api. |

## Examples

```TypeScript
import { bundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  bundleManager.cleanAllBundleCache().then((data) => {
    hilog.info(0x0000, 'testTag', 'cleanAllBundleCache successful.');
  }).catch((err: BusinessError) => {
    hilog.error(0x0000, 'testTag', 'cleanAllBundleCache failed: %{public}s', err.message);
  });
} catch (err) {
  let message = (err as BusinessError).message;
  hilog.error(0x0000, 'testTag', 'cleanAllBundleCache failed: %{public}s', message);
}
```

