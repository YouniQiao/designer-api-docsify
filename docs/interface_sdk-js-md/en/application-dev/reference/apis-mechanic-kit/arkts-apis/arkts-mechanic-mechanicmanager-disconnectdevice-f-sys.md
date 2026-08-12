# disconnectDevice (System API)

## Modules to Import

```TypeScript
import { mechanicManager } from '@kit.MechanicKit';
```

## disconnectDevice

```TypeScript
function disconnectDevice(mechId: int): Promise<Result>
```

Disconnect a device with mechanic id.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Required permissions:** ohos.permission.CONNECT_MECHANIC_HARDWARE

**Model restriction:** This API can be used only in the stage model.

<!--Device-mechanicManager-function disconnectDevice(mechId: int): Promise<Result>--><!--Device-mechanicManager-function disconnectDevice(mechId: int): Promise<Result>-End-->

**System capability:** SystemCapability.Mechanic.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mechId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | mechanic device id. &lt;br&gt;The value should be an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Result&gt; | Promise used to return the execution result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not system application. |
| [33300001](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-mechanic-kit/errorcode-mechanic.md#33300001-system-error) | Service exception. |

