# setDisposedStatusSync (System API)

## Modules to Import

```TypeScript
import { appControl } from 'kits/@kit.AbilityKit';
```

## setDisposedStatusSync

```TypeScript
function setDisposedStatusSync(appId: string, disposedWant: Want): void
```

以同步方法设置应用的处置状态。成功返回null，失败抛出对应异常。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.MANAGE_DISPOSED_APP_STATUS

<!--Device-appControl-function setDisposedStatusSync(appId: string, disposedWant: Want): void--><!--Device-appControl-function setDisposedStatusSync(appId: string, disposedWant: Want): void-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.AppControl

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| appId | string | Yes | 需要设置处置的应用的appId。&lt;br&gt; appId是应用的唯一标识，由应用Bundle名称和签名信息决定，获取方法参见 [获取应用的appId](../../../quick-start/common-problem-of-application.md#如何获取应用信息中的appid)。 |
| disposedWant | [Want](arkts-ability-app-ability-want-want-c.md) | Yes | 对应用的处置意图。 |

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
let want: Want = { bundleName: 'com.example.myapplication' };

try {
  appControl.setDisposedStatusSync(appId, want);
} catch (error) {
  let message = (error as BusinessError).message;
  console.error('setDisposedStatusSync failed ' + message);
}
```

