# turnBySpeed (System API)

## Modules to Import

```TypeScript
import { mechanicManager } from 'mechanicManager';
```

## turnBySpeed

```TypeScript
function turnBySpeed(mechId: int, angleSpeed: double, duration: int): Promise<Result>
```

Rotate in place according to the speed.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

<!--Device-mechanicManager-function turnBySpeed(mechId: int, angleSpeed: double, duration: int): Promise<Result>--><!--Device-mechanicManager-function turnBySpeed(mechId: int, angleSpeed: double, duration: int): Promise<Result>-End-->

**System capability:** SystemCapability.Mechanic.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mechId | int | Yes | ID of the mechanical device. <br>The value should be an integer. |
| angleSpeed | double | Yes | angular velocity. |
| duration | int | Yes | Duration of movement, unit ms. <br>The value should be an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Result&gt; | Promise that returns the execution result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not system application. |
| [33300001](../errorcode-mechanic.md#33300001-system-error) | Service exception. |
| [33300002](../errorcode-mechanic.md#33300002-device-not-connected) | Device not connected. |
| [33300003](../errorcode-mechanic.md#33300003-function-not-supported) | Feature not supported. |

