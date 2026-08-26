# getNameForUid

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

## getNameForUid

```TypeScript
function getNameForUid(uid: number, callback: AsyncCallback<string>): void
```

Obtains bundle name by the given uid.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [getBundleNameByUid](arkts-ability-bundlemanager-getbundlenamebyuid-f.md)

**System capability:** SystemCapability.BundleManager.BundleFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uid | number | Yes | Indicates the UID of an application. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes |  |

**Examples**

```TypeScript
import bundle from '@ohos.bundle';
import { BusinessError } from '@ohos.base';

let uid: number = 20010005;

bundle.getNameForUid(uid)
  .then((data) => {
    console.info('Operation successful. Data: ' + JSON.stringify(data));
  }).catch((error: BusinessError) => {
    console.error('Operation failed. Cause: ' + JSON.stringify(error));
  })
```


## getNameForUid

```TypeScript
function getNameForUid(uid: number): Promise<string>
```

Obtains the bundle name based on a UID. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** null

**System capability:** SystemCapability.BundleManager.BundleFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uid | number | Yes | UID based on which the bundle name is to obtain. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise & lt;string & gt; | Returns the bundle name. |

**Examples**

See [getNameForUid](#getnameforuid)
