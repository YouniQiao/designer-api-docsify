# doAction (System API)

## Modules to Import

```TypeScript
import { mechanicManager } from 'mechanicManager';
```

## doAction

```TypeScript
function doAction(mechId: int, actionType: ActionType): Promise<Result>
```

Execute an action sequence.

**Since:** 26.0.0

<!--Device-mechanicManager-function doAction(mechId: int, actionType: ActionType): Promise<Result>--><!--Device-mechanicManager-function doAction(mechId: int, actionType: ActionType): Promise<Result>-End-->

**System capability:** SystemCapability.Mechanic.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mechId | int | Yes | ID of the mechanical device. <br>The value should be an integer. |
| actionType | ActionType | Yes | Type of action sequence. |

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

