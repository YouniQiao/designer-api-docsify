# setAlternateModuleEnabled (System API)

## Modules to Import

```TypeScript
import { bundleManager } from '@kit.AbilityKit';
```

## setAlternateModuleEnabled

```TypeScript
function setAlternateModuleEnabled(bundleName: string, moduleName: string, versionCode: number,
    isEnabled: boolean): Promise<void>
```

Enables or disables the standby module.

**Since:** 26.1.0

**Required permissions:** ohos.permission.INSTALL_BUNDLE

**Model restriction:** This API can be used only in the stage model.

<!--Device-bundleManager-function setAlternateModuleEnabled(bundleName: string, moduleName: string, versionCode: long,    isEnabled: boolean): Promise<void>--><!--Device-bundleManager-function setAlternateModuleEnabled(bundleName: string, moduleName: string, versionCode: long,    isEnabled: boolean): Promise<void>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundleName | string | Yes | Bundle name. |
| moduleName | string | Yes | Indicates the module name. |
| versionCode | number | Yes | Version number of a module. |
| isEnabled | boolean | Yes | **true** to enable the standby module; **false** to disable it. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise object. No result is returned. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |
| [17700001](../errorcode-bundle.md#17700001-bundle-name-does-not-exist) | The specified bundle is not found. |
| [17700002](../errorcode-bundle.md#17700002-module-name-does-not-exist) | The specified module is not existed. |
| 17700096 | The specified version of the module is not found. |
| [17700101](../errorcode-bundle.md#17700101-bundle-manager-service-abnormal) | Bundle manager service exception. |
