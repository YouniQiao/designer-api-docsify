# getApplicationInfoSync (System API)

## Modules to Import

```TypeScript
import { bundleManager } from 'kits/@kit.AbilityKit';
```

## getApplicationInfoSync

```TypeScript
function getApplicationInfoSync(bundleName: string, applicationFlags: int, userId: int) : ApplicationInfo
```

以同步方法根据给定的bundleName、applicationFlags和userId获取ApplicationInfo。

获取调用方自身的信息时不需要权限。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED or ohos.permission.GET_BUNDLE_INFO

<!--Device-bundleManager-function getApplicationInfoSync(bundleName: string, applicationFlags: int, userId: int) : ApplicationInfo--><!--Device-bundleManager-function getApplicationInfoSync(bundleName: string, applicationFlags: int, userId: int) : ApplicationInfo-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundleName | string | Yes | 表示应用程序的bundleName。 |
| applicationFlags | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 表示用于指定将返回的ApplicationInfo对象中包含的信息，具体取值及不同含义参考 [ApplicationFlag](arkts-ability-bundlemanager-applicationflag-e-sys.md)。 |
| userId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 表示用户ID，可以通过 [getOsAccountLocalId](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-osaccount-accountmanager-i.md/arkts-basicservices-osaccount-accountmanager-i.md#getosaccountlocalid) 获取。 |

**Return value:**

| Type | Description |
| --- | --- |
| [ApplicationInfo](arkts-ability-bundlemanager-applicationinfo-t.md) | 返回ApplicationInfo对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 17700026 | The specified bundle is disabled. |
| 201 | Permission denied. |
| 202 | Permission denied, non-system app called system api. |
| 17700004 | The specified user ID is not found. |
| 17700001 | The specified bundleName is not found. |

## Examples

```TypeScript
import { bundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let bundleName = 'com.example.myapplication';
let applicationFlags = bundleManager.ApplicationFlag.GET_APPLICATION_INFO_DEFAULT;
let userId = 100;

try {
  let data = bundleManager.getApplicationInfoSync(bundleName, applicationFlags, userId);
  hilog.info(0x0000, 'testTag', 'getApplicationInfoSync successfully: %{public}s', JSON.stringify(data));
} catch (err) {
  let message = (err as BusinessError).message;
  hilog.error(0x0000, 'testTag', 'getApplicationInfoSync failed: %{public}s', message);
}
```


## getApplicationInfoSync

```TypeScript
function getApplicationInfoSync(bundleName: string, applicationFlags: int) : ApplicationInfo
```

以同步方法根据给定的bundleName、applicationFlags获取ApplicationInfo。

获取调用方自身的信息时不需要权限。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED or ohos.permission.GET_BUNDLE_INFO

<!--Device-bundleManager-function getApplicationInfoSync(bundleName: string, applicationFlags: int) : ApplicationInfo--><!--Device-bundleManager-function getApplicationInfoSync(bundleName: string, applicationFlags: int) : ApplicationInfo-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundleName | string | Yes | 表示应用程序的bundleName。 |
| applicationFlags | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 表示用于指定将返回的ApplicationInfo对象中包含的信息，具体取值及不同含义参考 [ApplicationFlag](arkts-ability-bundlemanager-applicationflag-e-sys.md)。 |

**Return value:**

| Type | Description |
| --- | --- |
| [ApplicationInfo](arkts-ability-bundlemanager-applicationinfo-t.md) | 返回ApplicationInfo对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 17700026 | The specified bundle is disabled. |
| 201 | Permission denied. |
| 202 | Permission denied, non-system app called system api. |
| 17700001 | The specified bundleName is not found. |

## Examples

```TypeScript
import { bundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let bundleName = 'com.example.myapplication';
let applicationFlags = bundleManager.ApplicationFlag.GET_APPLICATION_INFO_DEFAULT;

try {
  let data = bundleManager.getApplicationInfoSync(bundleName, applicationFlags);
  hilog.info(0x0000, 'testTag', 'getApplicationInfoSync successfully: %{public}s', JSON.stringify(data));
} catch (err) {
  let message = (err as BusinessError).message;
  hilog.error(0x0000, 'testTag', 'getApplicationInfoSync failed: %{public}s', message);
}
```

