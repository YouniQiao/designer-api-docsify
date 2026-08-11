# getBundleInfoSync

## Modules to Import

```TypeScript
import { bundleManager } from 'kits/@kit.AbilityKit';
```

## getBundleInfoSync

```TypeScript
function getBundleInfoSync(bundleName: string, bundleFlags: int, userId: int): BundleInfo
```

Obtains the bundle information based on the given bundle name, bundle flags, and user ID. This API returns the result synchronously.

No permission is required for obtaining the caller's own information.

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED or ohos.permission.GET_BUNDLE_INFO

<!--Device-bundleManager-function getBundleInfoSync(bundleName: string, bundleFlags: int, userId: int): BundleInfo--><!--Device-bundleManager-function getBundleInfoSync(bundleName: string, bundleFlags: int, userId: int): BundleInfo-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundleName | string | Yes | Bundle name. |
| bundleFlags | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Type of the bundle information to obtain. |
| userId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | User ID, which can be obtained by calling [getOsAccountLocalId](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-osaccount-accountmanager-i.md/arkts-basicservices-osaccount-accountmanager-i.md#getosaccountlocalid) . |

**Return value:**

| Type | Description |
| --- | --- |
| [BundleInfo](arkts-ability-bundleinfo-i.md) | Bundle information obtained. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| [17700026](../errorcode-bundle.md#17700026-bundle-disabled) | The specified bundle is disabled. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [17700004](../errorcode-bundle.md#17700004-user-id-does-not-exist) | The specified user ID is not found. |
| [17700001](../errorcode-bundle.md#17700001-bundle-name-does-not-exist) | The specified bundleName is not found. |

## Examples

```TypeScript
import { bundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let bundleName = 'com.example.myapplication';
let bundleFlags = bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_REQUESTED_PERMISSION;
let userId = 100;

try {
  let data = bundleManager.getBundleInfoSync(bundleName, bundleFlags, userId);
  hilog.info(0x0000, 'testTag', 'getBundleInfoSync successfully: %{public}s', JSON.stringify(data));
} catch (err) {
  let message = (err as BusinessError).message;
  hilog.error(0x0000, 'testTag', 'getBundleInfoSync failed: %{public}s', message);
}
```

```TypeScript
import { bundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let bundleName = 'com.example.myapplication';
let bundleFlags = bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_REQUESTED_PERMISSION;
let userId = 100;

try {
  let data = bundleManager.getBundleInfoSync(bundleName, bundleFlags, userId);
  hilog.info(0x0000, 'testTag', 'getBundleInfoSync successfully: %{public}s', JSON.stringify(data));
} catch (err) {
  let message = (err as BusinessError).message;
  hilog.error(0x0000, 'testTag', 'getBundleInfoSync failed: %{public}s', message);
}
```


## getBundleInfoSync

```TypeScript
function getBundleInfoSync(bundleName: string, bundleFlags: int): BundleInfo
```

Obtains the bundle information for the caller's user based on the given bundle name and bundle flags. This API returns the result synchronously.

No permission is required for obtaining the caller's own information.

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED or ohos.permission.GET_BUNDLE_INFO

<!--Device-bundleManager-function getBundleInfoSync(bundleName: string, bundleFlags: int): BundleInfo--><!--Device-bundleManager-function getBundleInfoSync(bundleName: string, bundleFlags: int): BundleInfo-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundleName | string | Yes | Bundle name. |
| bundleFlags | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Type of the bundle information to obtain. |

**Return value:**

| Type | Description |
| --- | --- |
| [BundleInfo](arkts-ability-bundleinfo-i.md) | Bundle information obtained. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| [17700026](../errorcode-bundle.md#17700026-bundle-disabled) | The specified bundle is disabled. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [17700001](../errorcode-bundle.md#17700001-bundle-name-does-not-exist) | The specified bundleName is not found. |

## Examples

```TypeScript
import { bundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let bundleName = 'com.example.myapplication';
let bundleFlags = bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_REQUESTED_PERMISSION;
try {
  let data = bundleManager.getBundleInfoSync(bundleName, bundleFlags);
  hilog.info(0x0000, 'testTag', 'getBundleInfoSync successfully: %{public}s', JSON.stringify(data));
} catch (err) {
  let message = (err as BusinessError).message;
  hilog.error(0x0000, 'testTag', 'getBundleInfoSync failed: %{public}s', message);
}
```

```TypeScript
import { bundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let bundleName = 'com.example.myapplication';
let bundleFlags = bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_REQUESTED_PERMISSION;
try {
  let data = bundleManager.getBundleInfoSync(bundleName, bundleFlags);
  hilog.info(0x0000, 'testTag', 'getBundleInfoSync successfully: %{public}s', JSON.stringify(data));
} catch (err) {
  let message = (err as BusinessError).message;
  hilog.error(0x0000, 'testTag', 'getBundleInfoSync failed: %{public}s', message);
}
```

