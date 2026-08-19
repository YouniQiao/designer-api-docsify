# getAllBundleInfo

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

## getAllBundleInfo

```TypeScript
function getAllBundleInfo(bundleFlag: BundleFlag, userId: number, callback: AsyncCallback<Array<BundleInfo>>): void
```

Obtains the information of all bundles of the specified user. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 9

**Required permissions:** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

<!--Device-bundle-function getAllBundleInfo(bundleFlag: BundleFlag, userId: number, callback: AsyncCallback<Array<BundleInfo>>): void--><!--Device-bundle-function getAllBundleInfo(bundleFlag: BundleFlag, userId: number, callback: AsyncCallback<Array<BundleInfo>>): void-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundleFlag | BundleFlag | Yes | Type of information that will be returned. For details about the available enumerated values, see the bundle information flags in [BundleFlag](arkts-ability-bundle-bundleflag-e.md). |
| userId | number | Yes | User ID. The default value is the user ID of the caller. The value must be greater than or equal to 0. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[BundleInfo](arkts-ability-bundleinfo-bundleinfo-depr-i.md)&gt;&gt; | Yes | Callback used to return the information of all bundles. |


## getAllBundleInfo

```TypeScript
function getAllBundleInfo(bundleFlag: BundleFlag, callback: AsyncCallback<Array<BundleInfo>>): void
```

Obtains the information of all bundles of the current user. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 9

**Required permissions:** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

<!--Device-bundle-function getAllBundleInfo(bundleFlag: BundleFlag, callback: AsyncCallback<Array<BundleInfo>>): void--><!--Device-bundle-function getAllBundleInfo(bundleFlag: BundleFlag, callback: AsyncCallback<Array<BundleInfo>>): void-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundleFlag | BundleFlag | Yes | Type of information that will be returned. For details about the available enumerated values, see the bundle information flags in [BundleFlag](arkts-ability-bundle-bundleflag-e.md). |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[BundleInfo](arkts-ability-bundleinfo-bundleinfo-depr-i.md)&gt;&gt; | Yes | Callback used to return the information of all bundles. |


## getAllBundleInfo

```TypeScript
function getAllBundleInfo(bundleFlag: BundleFlag, userId?: number): Promise<Array<BundleInfo>>
```

Obtains the information of all bundles of the specified user. This API uses a promise to return the result.

**Since:** 7

**Deprecated since:** 9

**Required permissions:** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

<!--Device-bundle-function getAllBundleInfo(bundleFlag: BundleFlag, userId?: number): Promise<Array<BundleInfo>>--><!--Device-bundle-function getAllBundleInfo(bundleFlag: BundleFlag, userId?: number): Promise<Array<BundleInfo>>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundleFlag | BundleFlag | Yes | Type of information that will be returned. For details about the available enumerated values, see the bundle information flags in [BundleFlag](arkts-ability-bundle-bundleflag-e.md). |
| userId | number | No | User ID. The default value is the user ID of the caller. The value must be greater than or equal to 0. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;[BundleInfo](arkts-ability-bundleinfo-bundleinfo-depr-i.md)&gt;&gt; | Promise used to return the information of all bundles. |

