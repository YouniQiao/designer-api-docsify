# setAbilityEnabled (System API)

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

## setAbilityEnabled

```TypeScript
function setAbilityEnabled(info: AbilityInfo, isEnable: boolean, callback: AsyncCallback<void>): void
```

Sets whether to enable an ability. This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** null

**Required permissions:** ohos.permission.CHANGE_ABILITY_ENABLED_STATE

<!--Device-bundle-function setAbilityEnabled(info: AbilityInfo, isEnable: boolean, callback: AsyncCallback<void>): void--><!--Device-bundle-function setAbilityEnabled(info: AbilityInfo, isEnable: boolean, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| info | [AbilityInfo](arkts-ability-abilityinfo-abilityinfo-depr-i.md) | Yes | Ability information. |
| isEnable | boolean | Yes | Whether to enable the application. **true** to enable, **false** otherwise. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback used to return the result. |


## setAbilityEnabled

```TypeScript
function setAbilityEnabled(info: AbilityInfo, isEnable: boolean): Promise<void>
```

Sets whether to enable an ability. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** null

**Required permissions:** ohos.permission.CHANGE_ABILITY_ENABLED_STATE

<!--Device-bundle-function setAbilityEnabled(info: AbilityInfo, isEnable: boolean): Promise<void>--><!--Device-bundle-function setAbilityEnabled(info: AbilityInfo, isEnable: boolean): Promise<void>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| info | [AbilityInfo](arkts-ability-abilityinfo-abilityinfo-depr-i.md) | Yes | Ability information. |
| isEnable | boolean | Yes | Whether to enable the application. **true** to enable, **false** otherwise. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

