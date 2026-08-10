# deleteExcludeDates

## Modules to Import

```TypeScript
import { reminderAgentManager } from 'kits/@kit.BackgroundTasksKit';
```

## deleteExcludeDates

```TypeScript
function deleteExcludeDates(reminderId: int): Promise<void>
```

为指定id的周期性的日历提醒，删除设置的所有不提醒日期。使用Promise异步回调。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-reminderAgentManager-function deleteExcludeDates(reminderId: int): Promise<void>--><!--Device-reminderAgentManager-function deleteExcludeDates(reminderId: int): Promise<void>-End-->

**System capability:** SystemCapability.Notification.ReminderAgent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| reminderId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 需要删除不提醒日期的代理提醒id。 代理提醒id会在 [发布代理提醒](arkts-backgroundtasks-reminderagentmanager-publishreminder-f.md#publishreminder) 时作为返回值返回。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | 无返回结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 201 | Permission denied |
| 1700003 | The reminder does not exist. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { reminderAgentManager } from '@kit.BackgroundTasksKit';

let reminderId: number = 1;
reminderAgentManager.deleteExcludeDates(reminderId).then(() => {
  console.info("deleteExcludeDates promise");
}).catch((err: BusinessError) => {
  console.error("promise err code:" + err.code + " message:" + err.message);
});
```

