# queryAllAutoStartupApplications

## Modules to Import

```TypeScript
import { autoStartupManager } from 'kits/@kit.AbilityKit';
```

## queryAllAutoStartupApplications

```TypeScript
function queryAllAutoStartupApplications(callback: AsyncCallback<Array<AutoStartupInfo>>): void
```

查询自启动应用组件信息。使用callback异步回调。从API version 18开始，该接口仅在2in1和Wearable设备中可正常调用，在其他设备上返回16000050错误码。对于API version 18之前版本，该接口仅在2in1设备中可正常调用，在其他设备上返回16000050错误码。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.MANAGE_APP_BOOT

**Model restriction:** This API can be used only in the stage model.

<!--Device-autoStartupManager-function queryAllAutoStartupApplications(callback: AsyncCallback<Array<AutoStartupInfo>>): void--><!--Device-autoStartupManager-function queryAllAutoStartupApplications(callback: AsyncCallback<Array<AutoStartupInfo>>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[AutoStartupInfo](arkts-ability-autostartupinfo-i-sys.md)&gt;&gt; | Yes | 回调函数。当查询自启动应用组件信息成功，err为undefined，data为获取到的Array&lt; [AutoStartupInfo](arkts-ability-autostartupinfo-i-sys.md)&gt;；否则为错误对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | The parameter check failed. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 16000050 | Failed to connect to the system service. |
| 201 | Permission denied, interface caller does not have permission "ohos.permission.MANAGE_APP_BOOT". |
| 202 | Permission denied, non-system app called system api. |


## queryAllAutoStartupApplications

```TypeScript
function queryAllAutoStartupApplications(): Promise<Array<AutoStartupInfo>>
```

查询自启动应用组件信息。使用Promise异步回调。从API version 18开始，该接口仅在2in1和Wearable设备中可正常调用，在其他设备上返回16000050错误码。对于API version 18之前版本，该接口仅在2in1设备中可正常调用，在其他设备上返回16000050错误码。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.MANAGE_APP_BOOT

**Model restriction:** This API can be used only in the stage model.

<!--Device-autoStartupManager-function queryAllAutoStartupApplications(): Promise<Array<AutoStartupInfo>>--><!--Device-autoStartupManager-function queryAllAutoStartupApplications(): Promise<Array<AutoStartupInfo>>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;[AutoStartupInfo](arkts-ability-autostartupinfo-i-sys.md)&gt;&gt; | Promise对象，返回自启动应用组件信息。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | The parameter check failed. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 16000050 | Failed to connect to the system service. |
| 201 | Permission denied, interface caller does not have permission "ohos.permission.MANAGE_APP_BOOT". |
| 202 | Permission denied, non-system app called system api. |

