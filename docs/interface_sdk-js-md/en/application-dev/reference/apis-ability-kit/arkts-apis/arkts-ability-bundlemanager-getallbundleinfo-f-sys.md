# getAllBundleInfo (System API)

## Modules to Import

```TypeScript
import { bundleManager } from 'bundleManager';
```

## getAllBundleInfo

```TypeScript
function getAllBundleInfo(bundleFlags: int, callback: AsyncCallback<Array<BundleInfo>>): void
```

Obtains all the bundle information in the system based on the given bundle flags. This API uses an asynchronous callback to return the result.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Required permissions:** ohos.permission.GET_INSTALLED_BUNDLE_LIST

<!--Device-bundleManager-function getAllBundleInfo(bundleFlags: int, callback: AsyncCallback<Array<BundleInfo>>): void--><!--Device-bundleManager-function getAllBundleInfo(bundleFlags: int, callback: AsyncCallback<Array<BundleInfo>>): void-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundleFlags | int | Yes | Type of the bundle information to obtain. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;BundleInfo&gt;&gt; | Yes | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md#AsyncCallback) used to return the result. If the operation is successful, **err** is **null** and **data** is the array of bundle information obtained. Otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission denied, non-system app called system api. |

## Examples

```TypeScript
import { bundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let bundleFlags = bundleManager.BundleFlag.GET_BUNDLE_INFO_DEFAULT;

try {
  bundleManager.getAllBundleInfo(bundleFlags, (err, data) => {
    if (err) {
      hilog.error(0x0000, 'testTag', 'getAllBundleInfo failed: %{public}s', err.message);
    } else {
      hilog.info(0x0000, 'testTag', 'getAllBundleInfo successfully: %{public}s', JSON.stringify(data));
    }
  });
} catch (err) {
  let message = (err as BusinessError).message;
  hilog.error(0x0000, 'testTag', 'getAllBundleInfo failed: %{public}s', message);
}
```


## getAllBundleInfo

```TypeScript
function getAllBundleInfo(bundleFlags: int, userId: int, callback: AsyncCallback<Array<BundleInfo>>): void
```

Obtains all the bundle information in the system based on the given bundle flags and user ID. This API uses an asynchronous callback to return the result.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Required permissions:** ohos.permission.GET_INSTALLED_BUNDLE_LIST

<!--Device-bundleManager-function getAllBundleInfo(bundleFlags: int, userId: int, callback: AsyncCallback<Array<BundleInfo>>): void--><!--Device-bundleManager-function getAllBundleInfo(bundleFlags: int, userId: int, callback: AsyncCallback<Array<BundleInfo>>): void-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundleFlags | int | Yes | Type of the bundle information to obtain. |
| userId | int | Yes | User ID, which can be obtained by calling [getOsAccountLocalId](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-osaccount-accountmanager-i.md#getOsAccountLocalId) . |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;BundleInfo&gt;&gt; | Yes | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md#AsyncCallback) used to return the result. If the operation is successful, **err** is **null** and **data** is the array of bundle information obtained. Otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission denied, non-system app called system api. |
| [17700004](../errorcode-bundle.md#17700004-user-id-does-not-exist) | The specified user ID is not found. |

## Examples

```TypeScript
import { bundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let bundleFlags = bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_REQUESTED_PERMISSION;
let userId = 100;

try {
  bundleManager.getAllBundleInfo(bundleFlags, userId, (err, data) => {
    if (err) {
      hilog.error(0x0000, 'testTag', 'getAllBundleInfo failed: %{public}s', err.message);
    } else {
      hilog.info(0x0000, 'testTag', 'getAllBundleInfo successfully: %{public}s', JSON.stringify(data));
    }
  });
} catch (err) {
  let message = (err as BusinessError).message;
  hilog.error(0x0000, 'testTag', 'getAllBundleInfo failed: %{public}s', message);
}
```


## getAllBundleInfo

```TypeScript
function getAllBundleInfo(bundleFlags: int, userId?: int): Promise<Array<BundleInfo>>
```

Obtains all the bundle information in the system based on the given bundle flags and user ID. This API uses a promise to return the result.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Required permissions:** ohos.permission.GET_INSTALLED_BUNDLE_LIST

<!--Device-bundleManager-function getAllBundleInfo(bundleFlags: int, userId?: int): Promise<Array<BundleInfo>>--><!--Device-bundleManager-function getAllBundleInfo(bundleFlags: int, userId?: int): Promise<Array<BundleInfo>>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundleFlags | int | Yes | Type of the bundle information to obtain. |
| userId | int | No | User ID, which can be obtained by calling [getOsAccountLocalId](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-osaccount-accountmanager-i.md#getOsAccountLocalId) . The default value is the user ID of the caller. The value must be greater than or equal to 0. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;BundleInfo&gt;&gt; | Promise used to return an array of bundle information. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission denied, non-system app called system api. |
| [17700004](../errorcode-bundle.md#17700004-user-id-does-not-exist) | The specified user ID is not found. |

## Examples

```TypeScript
import { bundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let bundleFlags = bundleManager.BundleFlag.GET_BUNDLE_INFO_DEFAULT;

try {
  bundleManager.getAllBundleInfo(bundleFlags).then((data) => {
    hilog.info(0x0000, 'testTag', 'getAllBundleInfo successfully. Data: %{public}s', JSON.stringify(data));
  }).catch((err: BusinessError) => {
    hilog.error(0x0000, 'testTag', 'getAllBundleInfo failed. Cause: %{public}s', err.message);
  });
} catch (err) {
  let message = (err as BusinessError).message;
  hilog.error(0x0000, 'testTag', 'getAllBundleInfo failed. Cause: %{public}s', message);
}
```

