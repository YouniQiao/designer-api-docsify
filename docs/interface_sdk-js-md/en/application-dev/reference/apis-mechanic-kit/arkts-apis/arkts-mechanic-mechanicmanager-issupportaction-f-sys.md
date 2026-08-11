# isSupportAction (System API)

## Modules to Import

```TypeScript
import { mechanicManager } from 'kits/@kit.MechanicKit';
```

## isSupportAction

```TypeScript
function isSupportAction(mechId: int, actionType: ActionType): boolean
```

Check whether the specific action type is supported.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-mechanicManager-function isSupportAction(mechId: int, actionType: ActionType): boolean--><!--Device-mechanicManager-function isSupportAction(mechId: int, actionType: ActionType): boolean-End-->

**System capability:** SystemCapability.Mechanic.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mechId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | ID of the mechanical device. &lt;br&gt;The value should be an integer. |
| actionType | [ActionType](../../apis-avsession-kit/arkts-apis/arkts-avsession-avmusictemplate-actiontype-t.md) | Yes | Type of action sequence. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Indicates whether the action type is supported. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not system application. |
| [33300001](../errorcode-mechanic.md#33300001-system-error) | Service exception. |
| [33300002](../errorcode-mechanic.md#33300002-device-not-connected) | Device not connected. |

