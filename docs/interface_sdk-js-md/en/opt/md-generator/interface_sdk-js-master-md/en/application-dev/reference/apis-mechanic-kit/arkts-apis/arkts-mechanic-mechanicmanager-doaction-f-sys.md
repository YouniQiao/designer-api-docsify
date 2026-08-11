# doAction (System API)

## Modules to Import

```TypeScript
import { mechanicManager } from 'kits/@kit.MechanicKit';
```

## doAction

```TypeScript
function doAction(mechId: number, actionType: ActionType): Promise<Result>
```

Execute an action sequence.

**Since:** 26.0.0

<!--Device-mechanicManager-function doAction(mechId: int, actionType: ActionType): Promise<Result>--><!--Device-mechanicManager-function doAction(mechId: int, actionType: ActionType): Promise<Result>-End-->

**System capability:** SystemCapability.Mechanic.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mechId | number | Yes |
| actionType | [ActionType](../../apis-data-protection-kit/arkts-apis/arkts-dataprotection-dlppermission-actiontype-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Result&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [33300001](../errorcode-mechanic.md#33300001-system-error) |
| [33300002](../errorcode-mechanic.md#33300002-device-not-connected) |
| [33300003](../errorcode-mechanic.md#33300003-function-not-supported) |
