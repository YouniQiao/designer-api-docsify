# getApplicationInfos (System API)

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

## getApplicationInfos

```TypeScript
function getApplicationInfos(bundleFlags: number, userId: number, callback: AsyncCallback<Array<ApplicationInfo>>): void
```

Obtains information about all installed apps for a specified user. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 8

**Substitutes:** getAllApplicationInfo

**Required permissions:** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

<!--Device-bundle-function getApplicationInfos(bundleFlags: number, userId: number, callback: AsyncCallback<Array<ApplicationInfo>>): void--><!--Device-bundle-function getApplicationInfos(bundleFlags: number, userId: number, callback: AsyncCallback<Array<ApplicationInfo>>): void-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundleFlags | number | Yes | Flag used to specify the information contained in the returned application information object. Value range: see the application information related flags in BundleFlag. |
| userId | number | Yes | User ID. Value range: greater than or equal to 0. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[ApplicationInfo](arkts-ability-applicationinfo-applicationinfo-depr-i.md)&gt;&gt; | Yes | Callback used to return the result. If getApplicationInfos is successful, **err** is **undefined**, and the list of app information as the input parameter at program startup. Otherwise, **err** is an error object. |


## getApplicationInfos

```TypeScript
function getApplicationInfos(bundleFlags: number, callback: AsyncCallback<Array<ApplicationInfo>>): void
```

Obtains information about installed apps for the user to which the caller belongs. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 8

**Substitutes:** getAllApplicationInfo

**Required permissions:** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

<!--Device-bundle-function getApplicationInfos(bundleFlags: number, callback: AsyncCallback<Array<ApplicationInfo>>): void--><!--Device-bundle-function getApplicationInfos(bundleFlags: number, callback: AsyncCallback<Array<ApplicationInfo>>): void-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundleFlags | number | Yes | Flag used to specify the information contained in the returned application information object. Value range: see the application information related flags in BundleFlag. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[ApplicationInfo](arkts-ability-applicationinfo-applicationinfo-depr-i.md)&gt;&gt; | Yes | Callback used to return the result. If getApplicationInfos is successful, **err** is **undefined**, and the list of app information as the input parameter at program startup. Otherwise, **err** is an error object. |


## getApplicationInfos

```TypeScript
function getApplicationInfos(bundleFlags: number, userId?: number): Promise<Array<ApplicationInfo>>
```

Obtains information about all installed apps for a specified user. This API uses a promise to return the result.

**Since:** 7

**Deprecated since:** 8

**Substitutes:** getAllApplicationInfo

**Required permissions:** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

<!--Device-bundle-function getApplicationInfos(bundleFlags: number, userId?: number): Promise<Array<ApplicationInfo>>--><!--Device-bundle-function getApplicationInfos(bundleFlags: number, userId?: number): Promise<Array<ApplicationInfo>>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundleFlags | number | Yes | Flag used to specify the information contained in the returned application information object. Value range: see the application information related flags in BundleFlag. |
| userId | number | No | User ID. Default value: the user to which the caller belongs. Value range: greater than or equal to 0. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;[ApplicationInfo](arkts-ability-applicationinfo-applicationinfo-depr-i.md)&gt;&gt; | Promise used to return the list of app information when obtained successfully. |

