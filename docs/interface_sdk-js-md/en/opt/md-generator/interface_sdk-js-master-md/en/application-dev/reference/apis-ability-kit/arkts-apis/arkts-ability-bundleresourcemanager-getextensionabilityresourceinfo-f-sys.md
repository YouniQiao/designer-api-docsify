# getExtensionAbilityResourceInfo (System API)

## Modules to Import

```TypeScript
import { bundleResourceManager } from 'kits/@kit.AbilityKit';
```

## getExtensionAbilityResourceInfo

```TypeScript
function getExtensionAbilityResourceInfo(bundleName: string, extensionAbilityType: bundleManager.ExtensionAbilityType, resourceFlags: number, appIndex?: number): Array<LauncherAbilityResourceInfo>
```

Obtains the ExtensionAbility resource information of an application based on the bundle name, ExtensionAbility type, resource flags, and clone ID. This API returns the result synchronously.

**Since:** 20

**Required permissions:** ohos.permission.GET_BUNDLE_RESOURCES

<!--Device-bundleResourceManager-function getExtensionAbilityResourceInfo(bundleName: string, extensionAbilityType: bundleManager.ExtensionAbilityType, resourceFlags: int, appIndex?: int): Array<LauncherAbilityResourceInfo>--><!--Device-bundleResourceManager-function getExtensionAbilityResourceInfo(bundleName: string, extensionAbilityType: bundleManager.ExtensionAbilityType, resourceFlags: int, appIndex?: int): Array<LauncherAbilityResourceInfo>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Resource

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |
| extensionAbilityType | bundleManager.ExtensionAbilityType | Yes |
| resourceFlags | number | Yes |
| appIndex | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array&lt;LauncherAbilityResourceInfo&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [17700061](../errorcode-bundle.md#17700061-appindex-for-a-clone-is-invalid) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [17700001](../errorcode-bundle.md#17700001-bundle-name-does-not-exist) |

## Examples

```TypeScript
import { bundleManager, bundleResourceManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let bundleName = "com.example.myapplication";
let extensionAbilityType = bundleManager.ExtensionAbilityType.INPUT_METHOD;
let resourceFlag = bundleResourceManager.ResourceFlag.GET_RESOURCE_INFO_ALL;
try {
  let resourceInfo =
    bundleResourceManager.getExtensionAbilityResourceInfo(bundleName, extensionAbilityType, resourceFlag);
  console.info('getExtensionAbilityResourceInfo successfully. Data label: ' + JSON.stringify(resourceInfo[0].label));
} catch (err) {
  let message = (err as BusinessError).message;
  let code = (err as BusinessError).code;
  console.error(`getExtensionAbilityResourceInfo failed, err code:${code}, err msg: ${message}`);
}
```
