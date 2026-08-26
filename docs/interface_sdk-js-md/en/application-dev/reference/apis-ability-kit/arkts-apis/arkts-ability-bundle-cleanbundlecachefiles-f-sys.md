# cleanBundleCacheFiles (System API)

## Modules to Import

```TypeScript
import appControl from '@kit.AbilityKit.appControl';
import bundleManager from '@kit.AbilityKit.bundleManager';
import bundleMonitor from '@kit.AbilityKit.bundleMonitor';
import bundleResourceManager from '@kit.AbilityKit.bundleResourceManager';
import bundle from '@kit.AbilityKit';
import defaultAppManager from '@kit.AbilityKit.defaultAppManager';
import distributedBundleManager from '@kit.AbilityKit.distributedBundleManager';
import freeInstall from '@kit.AbilityKit.freeInstall';
import innerBundleManager, { BundleStatusCallback } from '@kit.AbilityKit.innerBundleManager';
import installer from '@kit.AbilityKit.installer';
import launcherBundleManager from '@kit.AbilityKit.launcherBundleManager';
import overlay from '@kit.AbilityKit.overlay';
import shortcutManager from '@kit.AbilityKit.shortcutManager';
import skillManager from '@kit.AbilityKit.skillManager';
import appDomainVerify from '@kit.AbilityKit.appDomainVerify';
import pluginBundleManager from '@kit.AbilityKit.pluginBundleManager';
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

**System capability:** SystemCapability.BundleManager.BundleFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundleName | string | Yes | Bundle name. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise & lt;void & gt; | Promise that returns no value. |

**Examples**

See [cleanBundleCacheFiles](#cleanbundlecachefiles)
