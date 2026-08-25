# getLauncherAbilityResourceInfoList (System API)

## Modules to Import

```TypeScript
import { bundleResourceManager } from 'kits/@kit.AbilityKit';
```

## getLauncherAbilityResourceInfoList

```TypeScript
function getLauncherAbilityResourceInfoList(optionsList: Array<BundleOptions>, resourceFlags: number): Promise<Array<LauncherAbilityResourceInfo>>
```

Obtains the launcher ability resource information of each application corresponding to the **BundleOptions** element in **optionsList**. This API uses a promise to return the result.

**Since:** 23

**Required permissions:** ohos.permission.GET_INSTALLED_BUNDLE_LIST and ohos.permission.GET_BUNDLE_RESOURCES

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.BundleManager.BundleFramework.Resource

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| optionsList | Array&lt;[BundleOptions](arkts-ability-bundleinfo-bundleoptions-i-sys.md)&gt; | Yes |
| resourceFlags | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Array & lt;LauncherAbilityResourceInfo & gt; & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [17700001](../errorcode-bundle.md#17700001-bundle-name-does-not-exist) |
| [17700002](../errorcode-bundle.md#17700002-module-name-does-not-exist) |
| [17700003](../errorcode-bundle.md#17700003-ability-name-does-not-exist) |
| [17700061](../errorcode-bundle.md#17700061-appindex-for-a-clone-is-invalid) |
