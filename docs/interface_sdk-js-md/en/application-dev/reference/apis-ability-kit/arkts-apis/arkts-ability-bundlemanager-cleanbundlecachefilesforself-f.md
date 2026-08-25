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

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 21.

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Examples**

```TypeScript
import { bundleManager } from '@kit.AbilityKit';

bundleManager.cleanBundleCacheFilesForSelf().then(() => {
  console.info('cleanBundleCacheFilesForSelf complete.');
});
```
