# moveBySpeed (System API)

## Modules to Import

```TypeScript
import { mechanicManager } from '@kit.MechanicKit';
```

## moveBySpeed

```TypeScript
function moveBySpeed(mechId: int, params: SpeedParams, duration: int): Promise<Result>
```

Move a mechanical device at the specified speed.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-mechanicManager-function moveBySpeed(mechId: int, params: SpeedParams, duration: int): Promise<Result>--><!--Device-mechanicManager-function moveBySpeed(mechId: int, params: SpeedParams, duration: int): Promise<Result>-End-->

**System capability:** SystemCapability.Mechanic.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mechId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | ID of the mechanical device. &lt;br&gt;The value should be an integer. |
| params | [SpeedParams](arkts-mechanic-mechanicmanager-speedparams-i-sys.md) | Yes | Parameters to use when moving. |
| duration | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Duration of movement, in ms. &lt;br&gt;The value should be an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Result&gt; | Promise that returns the execution result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not system application. |
| [33300001](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-mechanic-kit/errorcode-mechanic.md#33300001-system-error) | Service exception. |
| [33300002](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-mechanic-kit/errorcode-mechanic.md#33300002-device-not-connected) | Device not connected. |
| [33300003](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-mechanic-kit/errorcode-mechanic.md#33300003-function-not-supported) | Feature not supported. |

