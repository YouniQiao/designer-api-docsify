# cancelSuspendDelay

## cancelSuspendDelay

```TypeScript
function cancelSuspendDelay(requestId: number): void
```

Cancels the suspension delay.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [@ohos.resourceschedule.backgroundTaskManager:backgroundTaskManager.cancelSuspendDelay](arkts-backgroundtasks-backgroundtaskmanager-cancelsuspenddelay-depr-f.md#cancelsuspenddelay)

<!--Device-backgroundTaskManager-function cancelSuspendDelay(requestId: number): void--><!--Device-backgroundTaskManager-function cancelSuspendDelay(requestId: number): void-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.TransientTask

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| requestId | number | Yes |

## Examples

```TypeScript
let delayInfo = backgroundTaskManager.requestSuspendDelay("test", () => {});
backgroundTaskManager.cancelSuspendDelay(delayInfo.requestId);
```
