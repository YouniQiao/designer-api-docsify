# cleanBundleCacheFiles (System API)

## Modules to Import

```TypeScript
import { appControl } from '@kit.AbilityKit';
import { bundleManager } from '@kit.AbilityKit';
import { bundleMonitor } from '@kit.AbilityKit';
import { bundleResourceManager } from '@kit.AbilityKit';
import { bundle } from '@kit.AbilityKit';
import { defaultAppManager } from '@kit.AbilityKit';
import { distributedBundleManager } from '@kit.AbilityKit';
import { freeInstall } from '@kit.AbilityKit';
import { innerBundleManager, BundleStatusCallback } from '@kit.AbilityKit';
import { installer } from '@kit.AbilityKit';
import { launcherBundleManager } from '@kit.AbilityKit';
import { overlay } from '@kit.AbilityKit';
import { shortcutManager } from '@kit.AbilityKit';
import { skillManager } from '@kit.AbilityKit';
import { appDomainVerify } from '@kit.AbilityKit';
import { pluginBundleManager } from '@kit.AbilityKit';
```

## cleanBundleCacheFiles

```TypeScript
function cleanBundleCacheFiles(bundleName: string, callback: AsyncCallback<void>): void
```

Clears the cache data of an application. This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** null

**Required permissions:** ohos.permission.REMOVE_CACHE_FILES

<!--Device-bundle-function cleanBundleCacheFiles(bundleName: string, callback: AsyncCallback<void>): void--><!--Device-bundle-function cleanBundleCacheFiles(bundleName: string, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundleName | string | Yes | Bundle name. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback used to return the result. |

**Examples**

```TypeScript
import bundle from '@ohos.bundle';

let bundleName: string = "com.example.myapplication";

bundle.cleanBundleCacheFiles(bundleName, err => {
  if (err) {
    console.error('cleanBundleCacheFiles failed.');
  } else {
    console.info('cleanBundleCacheFiles successfully.');
  }
});
```

```TypeScript
import bundle from '@ohos.bundle';
import { BusinessError } from '@ohos.base';

let bundleName: string = "com.example.myapplication";

bundle.cleanBundleCacheFiles(bundleName).then(() => {
  console.info('cleanBundleCacheFiles successfully.');
}).catch((error: BusinessError) => {
  console.error('cleanBundleCacheFiles failed.');
});
```


## cleanBundleCacheFiles

```TypeScript
function cleanBundleCacheFiles(bundleName: string): Promise<void>
```

Clears the cache data of an application. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** null

**Required permissions:** ohos.permission.REMOVE_CACHE_FILES

<!--Device-bundle-function cleanBundleCacheFiles(bundleName: string): Promise<void>--><!--Device-bundle-function cleanBundleCacheFiles(bundleName: string): Promise<void>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundleName | string | Yes | Bundle name. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Examples**

See [cleanBundleCacheFiles](#cleanbundlecachefiles)

