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

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-bundleManager-function cleanBundleCacheFilesForSelf(): Promise<void>--><!--Device-bundleManager-function cleanBundleCacheFilesForSelf(): Promise<void>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Examples**

```TypeScript
import { bundleManager } from '@kit.AbilityKit';

bundleManager.cleanBundleCacheFilesForSelf().then(() => {
  console.info('cleanBundleCacheFilesForSelf complete.');
});
```

