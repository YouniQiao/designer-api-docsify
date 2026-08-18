# getBundleArchiveInfo

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

## getBundleArchiveInfo

```TypeScript
function getBundleArchiveInfo(hapFilePath: string, bundleFlags: number, callback: AsyncCallback<BundleInfo>): void
```

Obtains information about the bundles contained in a HAP file. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 9

<!--Device-bundle-function getBundleArchiveInfo(hapFilePath: string, bundleFlags: number, callback: AsyncCallback<BundleInfo>): void--><!--Device-bundle-function getBundleArchiveInfo(hapFilePath: string, bundleFlags: number, callback: AsyncCallback<BundleInfo>): void-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| hapFilePath | string | Yes | Path where the HAP file is stored. The absolute path of the application and the data directory sandbox path are supported. |
| bundleFlags | number | Yes | Flags used to specify information contained in the BundleInfo object that will be returned. For details about the available enumerated values, see the bundle information flags in [BundleFlag](arkts-ability-bundle-bundleflag-e.md). |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;[BundleInfo](arkts-ability-bundleinfo-bundleinfo-depr-i.md)&gt; | Yes | Callback used to return the information about the bundles. |


## getBundleArchiveInfo

```TypeScript
function getBundleArchiveInfo(hapFilePath: string, bundleFlags: number): Promise<BundleInfo>
```

Obtains information about the bundles contained in a HAP file. This API uses a promise to return the result.

**Since:** 7

**Deprecated since:** 9

<!--Device-bundle-function getBundleArchiveInfo(hapFilePath: string, bundleFlags: number): Promise<BundleInfo>--><!--Device-bundle-function getBundleArchiveInfo(hapFilePath: string, bundleFlags: number): Promise<BundleInfo>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| hapFilePath | string | Yes | Path where the HAP file is stored. The absolute path of the application and the data directory sandbox path are supported. |
| bundleFlags | number | Yes | Flags used to specify information contained in the BundleInfo object that will be returned. For details about the available enumerated values, see the bundle information flags in [BundleFlag](arkts-ability-bundle-bundleflag-e.md). |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[BundleInfo](arkts-ability-bundleinfo-bundleinfo-depr-i.md)&gt; | Returns the BundleInfo object. |

