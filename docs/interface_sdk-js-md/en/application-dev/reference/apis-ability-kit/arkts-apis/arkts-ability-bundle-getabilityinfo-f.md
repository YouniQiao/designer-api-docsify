# getAbilityInfo

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

## getAbilityInfo

```TypeScript
function getAbilityInfo(bundleName: string, abilityName: string, callback: AsyncCallback<AbilityInfo>): void
```

Obtains the ability information based on a given bundle name and ability name. This API uses an asynchronous callback to return the result.No permission is required for obtaining the caller's own information.

**Since:** 7

**Deprecated since:** 9

**Required permissions:** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED or ohos.permission.GET_BUNDLE_INFO

**System capability:** SystemCapability.BundleManager.BundleFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundleName | string | Yes | Bundle name. |
| abilityName | string | Yes | Ability name. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[AbilityInfo](arkts-ability-abilityinfo-abilityinfo-depr-i.md)&gt; | Yes | Callback used to return the ability information. |

**Examples**

```TypeScript
import bundle from '@ohos.bundle';
import { BusinessError } from '@ohos.base';

let bundleName: string = "com.example.myapplication";
let abilityName: string = "EntryAbility";

bundle.getAbilityInfo(bundleName, abilityName)
  .then((data) => {
    console.info('Operation successful. Data: ' + JSON.stringify(data));
  }).catch((error: BusinessError) => {
    console.error('Operation failed. Cause: ' + JSON.stringify(error));
  })
```

```TypeScript
import bundle from '@ohos.bundle';

let bundleName: string = "com.example.myapplication";
let abilityName: string = "EntryAbility";

bundle.getAbilityInfo(bundleName, abilityName, (err, data) => {
  if (err) {
    console.error('Operation failed. Cause: ' + JSON.stringify(err));
    return;
  }
  console.info('Operation successful. Data:' + JSON.stringify(data));
})
```


## getAbilityInfo

```TypeScript
function getAbilityInfo(bundleName: string, abilityName: string): Promise<AbilityInfo>
```

Obtains the ability information based on a given bundle name and ability name. This API uses a promise to return the result.No permission is required for obtaining the caller's own information.

**Since:** 7

**Deprecated since:** 9

**Required permissions:** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED or ohos.permission.GET_BUNDLE_INFO

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

**Examples**

See [getAbilityInfo](#getabilityinfo)
