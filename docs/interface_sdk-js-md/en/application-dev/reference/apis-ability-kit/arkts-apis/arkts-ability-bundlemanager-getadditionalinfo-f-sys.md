# getAdditionalInfo (System API)

## Modules to Import

```TypeScript
import { bundleManager } from '@kit.AbilityKit';
```

## getAdditionalInfo

```TypeScript
function getAdditionalInfo(bundleName: string): string
```

Obtains additional information about a bundle in synchronous mode. The return value is the **additionalInfo** field value in [InstallParam](arkts-ability-installer-installparam-i-sys.md#InstallParam) passed when **install** is called.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

<!--Device-bundleManager-function getAdditionalInfo(bundleName: string): string--><!--Device-bundleManager-function getAdditionalInfo(bundleName: string): string-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundleName | string | Yes | Bundle name. |

**Return value:**

| Type | Description |
| --- | --- |
| string | Additional information about the bundle. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter bundleName is empty. |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission denied, non-system app called system api. |
| [17700001](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ability-kit/errorcode-bundle.md#17700001-bundle-name-does-not-exist) | The specified bundleName is not found. |

## Examples

```TypeScript
import { bundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let bundleName = "com.example.myapplication";

try {
  let info = bundleManager.getAdditionalInfo(bundleName);
  console.info('getAdditionalInfo successfully, additionInfo:' + info);
} catch (error) {
  let message = (error as BusinessError).message;
  console.error('getAdditionalInfo failed. Cause: ' + message);
}
```

