# getAppProvisionInfoSync (System API)

## Modules to Import

```TypeScript
import { bundleManager } from 'kits/@kit.AbilityKit';
```

## getAppProvisionInfoSync

```TypeScript
function getAppProvisionInfoSync(bundleName: string, userId?: int): AppProvisionInfo
```

以同步方法根据bundleName和userId获取应用的provision配置文件信息并返回结果。

获取调用方自身的信息时不需要权限。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

<!--Device-bundleManager-function getAppProvisionInfoSync(bundleName: string, userId?: int): AppProvisionInfo--><!--Device-bundleManager-function getAppProvisionInfoSync(bundleName: string, userId?: int): AppProvisionInfo-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundleName | string | Yes | 指定的bundleName。 |
| userId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | 表示用户ID，可以通过 [getOsAccountLocalId](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-osaccount-accountmanager-i.md/arkts-basicservices-osaccount-accountmanager-i.md#getosaccountlocalid) 获取，默认值：调用方所在用户，取值范围：大于等于0。 |

**Return value:**

| Type | Description |
| --- | --- |
| [AppProvisionInfo](arkts-ability-bundlemanager-appprovisioninfo-t-sys.md) | AppProvisionInfo对象，返回应用的provision配置文件信息。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter bundleName is empty. |
| 201 | Permission denied. |
| 202 | Permission denied, non-system app called system api. |
| 17700004 | The specified user ID is not found. |
| 17700001 | The specified bundleName is not found. |

## Examples

```TypeScript
import { bundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let bundleName = "com.ohos.myapplication";
let userId = 100;

try {
  let data = bundleManager.getAppProvisionInfoSync(bundleName);
  hilog.info(0x0000, 'testTag', 'getAppProvisionInfoSync successfully. Data: %{public}s', JSON.stringify(data));
} catch (err) {
  let message = (err as BusinessError).message;
  hilog.error(0x0000, 'testTag', 'getAppProvisionInfoSync failed. Cause: %{public}s', message);
}

try {
  let data = bundleManager.getAppProvisionInfoSync(bundleName, userId);
  hilog.info(0x0000, 'testTag', 'getAppProvisionInfoSync successfully. Data: %{public}s', JSON.stringify(data));
} catch (err) {
  let message = (err as BusinessError).message;
  hilog.error(0x0000, 'testTag', 'getAppProvisionInfoSync failed. Cause: %{public}s', message);
}
```

