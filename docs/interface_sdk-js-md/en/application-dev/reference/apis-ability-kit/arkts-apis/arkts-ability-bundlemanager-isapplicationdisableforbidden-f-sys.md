# isApplicationDisableForbidden (System API)

## Modules to Import

```TypeScript
import { bundleManager } from 'kits/@kit.AbilityKit';
```

## isApplicationDisableForbidden

```TypeScript
function isApplicationDisableForbidden(bundleName: string, userId: int, appIndex: int): boolean
```

以同步方法查询指定用户下指定应用或分身应用是否被设置禁止停用。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Required permissions:** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED or (ohos.permission.GET_BUNDLE_INFO_PRIVILEGED and ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS)

**Model restriction:** This API can be used only in the stage model.

<!--Device-bundleManager-function isApplicationDisableForbidden(bundleName: string, userId: int, appIndex: int): boolean--><!--Device-bundleManager-function isApplicationDisableForbidden(bundleName: string, userId: int, appIndex: int): boolean-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundleName | string | Yes | 表示应用的包名。 |
| userId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 表示用户ID，可以通过 [getOsAccountLocalId](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-osaccount-accountmanager-i.md/arkts-basicservices-osaccount-accountmanager-i.md#getosaccountlocalid) 获取，取值范围：大于等于0。 |
| appIndex | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 表示应用索引。取值范围0~5，取值为0表示主应用，取值1~5表示分身应用的索引。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 指定应用是否被设置禁止停用。&lt;br/&gt;返回true表示指定应用已被设置禁止停用，返回false表示指定应用没有被设置禁止停用。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 17700061 | The specified app index is invalid. |
| 201 | Permission denied. |
| 202 | Permission denied. Non-system APP calling system API. |
| 17700004 | The specified user ID is not found. |
| 17700001 | The specified bundle is not found. |

## Examples

```TypeScript
import { bundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let bundleName: string = 'com.example.myapplication';
let userId: number = 100;
let appIndex: number = 0;

try {
  let data = bundleManager.isApplicationDisableForbidden(bundleName, userId, appIndex);
  hilog.info(0x0000, 'testTag', 'isApplicationDisableForbidden successfully: %{public}s', JSON.stringify(data));
} catch (err) {
  let message = (err as BusinessError).message;
  hilog.error(0x0000, 'testTag', 'isApplicationDisableForbidden failed: %{public}s', message);
}
```

