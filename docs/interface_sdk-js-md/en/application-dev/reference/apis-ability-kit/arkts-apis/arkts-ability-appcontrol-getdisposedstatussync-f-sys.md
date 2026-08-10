# getDisposedStatusSync (System API)

## Modules to Import

```TypeScript
import { appControl } from 'kits/@kit.AbilityKit';
```

## getDisposedStatusSync

```TypeScript
function getDisposedStatusSync(appId: string): Want
```

以同步方法获取指定应用已设置的处置状态。成功返回应用的处置状态，失败抛出对应异常。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.MANAGE_DISPOSED_APP_STATUS or ohos.permission.GET_DISPOSED_APP_STATUS

<!--Device-appControl-function getDisposedStatusSync(appId: string): Want--><!--Device-appControl-function getDisposedStatusSync(appId: string): Want-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.AppControl

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| appId | string | Yes | 要查询的应用的appId。&lt;br&gt; appId是应用的唯一标识，由应用Bundle名称和签名信息决定，获取方法参见 [获取应用的appId](../../../quick-start/common-problem-of-application.md#如何获取应用信息中的appid)。 |

**Return value:**

| Type | Description |
| --- | --- |
| [Want](arkts-ability-app-ability-want-want-c.md) | 返回应用的处置状态。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 201 | Permission denied. |
| 202 | Permission denied, non-system app called system api. |
| 17700005 | The specified app ID is empty string. |

## Examples

```TypeScript
import { appControl } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { Want } from '@kit.AbilityKit';

let appId: string = "com.example.myapplication_xxxxx";
let want: Want;

try {
  want = appControl.getDisposedStatusSync(appId);
} catch (error) {
  let message = (error as BusinessError).message;
  console.error('getDisposedStatusSync failed ' + message);
}
```

