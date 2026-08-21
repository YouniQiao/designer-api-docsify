# getLaunchWantForBundle

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

## getLaunchWantForBundle

```TypeScript
function getLaunchWantForBundle(bundleName: string, callback: AsyncCallback<Want>): void
```

Obtains the Want object that launches the specified application. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 9

**Required permissions:** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

<!--Device-bundle-function getLaunchWantForBundle(bundleName: string, callback: AsyncCallback<Want>): void--><!--Device-bundle-function getLaunchWantForBundle(bundleName: string, callback: AsyncCallback<Want>): void-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundleName | string | Yes | Bundle name. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;[Want](arkts-ability-appabilitywant-want-c.md)&gt; | Yes | Callback used to return the Want object. |


## getLaunchWantForBundle

```TypeScript
function getLaunchWantForBundle(bundleName: string): Promise<Want>
```

Obtains the Want object that launches the specified application. This API uses a promise to return the result.

**Since:** 7

**Deprecated since:** 9

**Required permissions:** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

<!--Device-bundle-function getLaunchWantForBundle(bundleName: string): Promise<Want>--><!--Device-bundle-function getLaunchWantForBundle(bundleName: string): Promise<Want>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundleName | string | Yes | Bundle name. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[Want](arkts-ability-appabilitywant-want-c.md)&gt; | Returns the Want for starting the application's main ability if any. |

