# resetDefaultApplicationSync (System API)

## Modules to Import

```TypeScript
import { defaultAppManager } from '@kit.AbilityKit';
```

## resetDefaultApplicationSync

```TypeScript
function resetDefaultApplicationSync(type: string, userId?: int): void
```

Resets the default application based on a system-defined application type, a file type that complies with the media type format (either specified by **type** or **subtype**), or a  
[uniform data type](../../apis-arkdata/arkts-apis/arkts-data-uniformtypedescriptor.md#uniformTypeDescriptor). This API returns the result synchronously.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.SET_DEFAULT_APPLICATION

<!--Device-defaultAppManager-function resetDefaultApplicationSync(type: string, userId?: int): void--><!--Device-defaultAppManager-function resetDefaultApplicationSync(type: string, userId?: int): void-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.DefaultApp

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | string | Yes | Type of the target application. It must be set to a value defined by [ApplicationType](arkts-ability-defaultappmanager-applicationtype-e.md#ApplicationType), a file type that complies with the media type format, or a value defined by [UniformDataType](../../apis-arkdata/arkts-apis/arkts-data-uniformtypedescriptor.md#uniformTypeDescriptor). |
| userId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | User ID, which can be obtained by calling [getOsAccountLocalId](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-osaccount-accountmanager-i.md#getOsAccountLocalId) . The default value is the user ID of the caller. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| [801](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. |
| [17700025](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ability-kit/errorcode-bundle.md#17700025-invalid-type) | The specified type is invalid. |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission denied, non-system app called system api. |
| [17700004](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ability-kit/errorcode-bundle.md#17700004-user-id-does-not-exist) | The specified user ID is not found. |

## Examples

```TypeScript
import { defaultAppManager } from '@kit.AbilityKit';
import { uniformTypeDescriptor } from '@kit.ArkData';

let userId = 100;
try {
  defaultAppManager.resetDefaultApplicationSync(defaultAppManager.ApplicationType.BROWSER, userId);
  console.info('Operation successful.');
} catch (error) {
  console.error('Operation failed. Cause: ' + JSON.stringify(error));
};

try {
  defaultAppManager.resetDefaultApplicationSync("image/png", userId);
  console.info('Operation successful.');
} catch (error) {
  console.error('Operation failed. Cause: ' + JSON.stringify(error));
};

try {
  defaultAppManager.resetDefaultApplicationSync(uniformTypeDescriptor.UniformDataType.AVI, userId);
  console.info('Operation successful.');
} catch (error) {
  console.error('Operation failed. Cause: ' + JSON.stringify(error));
};
```

