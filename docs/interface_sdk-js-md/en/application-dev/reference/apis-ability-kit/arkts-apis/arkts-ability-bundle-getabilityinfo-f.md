# getAbilityInfo

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

## getAbilityInfo

```TypeScript
function getAbilityInfo(bundleName: string, abilityName: string, callback: AsyncCallback<AbilityInfo>): void
```

Obtains the ability information based on a given bundle name and ability name. This API uses an asynchronous callback to return the result. No permission is required for obtaining the caller's own information.

**Since:** 7

**Deprecated since:** 9

**Required permissions:** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED or ohos.permission.GET_BUNDLE_INFO

<!--Device-bundle-function getAbilityInfo(bundleName: string, abilityName: string, callback: AsyncCallback<AbilityInfo>): void--><!--Device-bundle-function getAbilityInfo(bundleName: string, abilityName: string, callback: AsyncCallback<AbilityInfo>): void-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundleName | string | Yes | Bundle name. |
| abilityName | string | Yes | Ability name. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;[AbilityInfo](arkts-ability-abilityinfo-abilityinfo-depr-i.md)&gt; | Yes | Callback used to return the ability information. |


## getAbilityInfo

```TypeScript
function getAbilityInfo(bundleName: string, abilityName: string): Promise<AbilityInfo>
```

Obtains the ability information based on a given bundle name and ability name. This API uses a promise to return the result. No permission is required for obtaining the caller's own information.

**Since:** 7

**Deprecated since:** 9

**Required permissions:** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED or ohos.permission.GET_BUNDLE_INFO

<!--Device-bundle-function getAbilityInfo(bundleName: string, abilityName: string): Promise<AbilityInfo>--><!--Device-bundle-function getAbilityInfo(bundleName: string, abilityName: string): Promise<AbilityInfo>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundleName | string | Yes | Bundle name. |
| abilityName | string | Yes | Ability name. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[AbilityInfo](arkts-ability-abilityinfo-abilityinfo-depr-i.md)&gt; | Promise used to return the ability information. |

