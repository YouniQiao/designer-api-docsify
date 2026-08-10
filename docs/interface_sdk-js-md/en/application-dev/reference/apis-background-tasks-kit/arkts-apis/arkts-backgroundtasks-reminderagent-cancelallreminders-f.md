# cancelAllReminders

## Modules to Import

```TypeScript
import { reminderAgent } from 'kits/@kit.BackgroundTasksKit';
```

## cancelAllReminders

```TypeScript
function cancelAllReminders(callback: AsyncCallback<void>): void
```

取消当前应用所有的提醒，使用回调的方式实现异步调用。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [reminderAgentManager.cancelAllReminders](arkts-backgroundtasks-reminderagentmanager-cancelallreminders-f.md#cancelallreminders)

<!--Device-reminderAgent-function cancelAllReminders(callback: AsyncCallback<void>): void--><!--Device-reminderAgent-function cancelAllReminders(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Notification.ReminderAgent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 异步回调。 |

## Examples

```TypeScript
import { BusinessError } from '@ohos.base';
import reminderAgent from '@ohos.reminderAgent';

reminderAgent.cancelAllReminders((err: BusinessError, data: void) =>{
  console.info("cancelAllReminders callback")
})
```


## cancelAllReminders

```TypeScript
function cancelAllReminders(): Promise<void>
```

取消当前应用所有的提醒，使用Promise方式实现异步调用。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [reminderAgentManager.cancelAllReminders](arkts-backgroundtasks-reminderagentmanager-cancelallreminders-f.md#cancelallreminders)

<!--Device-reminderAgent-function cancelAllReminders(): Promise<void>--><!--Device-reminderAgent-function cancelAllReminders(): Promise<void>-End-->

**System capability:** SystemCapability.Notification.ReminderAgent

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise类型异步回调。 |

## Examples

```TypeScript
import reminderAgent from '@ohos.reminderAgent';

reminderAgent.cancelAllReminders().then(() => {
    console.info("cancelAllReminders promise")
})
```

