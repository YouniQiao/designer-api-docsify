# cleanBundleCacheFilesForSelf

## Modules to Import

```TypeScript
import { bundleManager } from '@kit.AbilityKit';
```

## cleanBundleCacheFilesForSelf

```TypeScript
function cleanBundleCacheFilesForSelf(): Promise<void>
```

Clears the application cache. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-bundleManager-function cleanBundleCacheFilesForSelf(): Promise<void>--><!--Device-bundleManager-function cleanBundleCacheFilesForSelf(): Promise<void>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

## Examples

```TypeScript
import { bundleManager } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

bundleManager.cleanBundleCacheFilesForSelf().then(() => {
  hilog.info(0x0000, 'testTag', 'cleanBundleCacheFilesForSelf complete.');
});
```
