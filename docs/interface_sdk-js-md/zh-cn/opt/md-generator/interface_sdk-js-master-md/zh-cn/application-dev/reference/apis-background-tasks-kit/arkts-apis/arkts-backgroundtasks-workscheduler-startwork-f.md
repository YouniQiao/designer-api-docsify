# startWork

## startWork

```TypeScript
function startWork(work: WorkInfo): void
```

申请延迟任务，成功后会把任务添加到执行队列，满足触发条件后由系统调度执行。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-workScheduler-function startWork(work: WorkInfo): void--><!--Device-workScheduler-function startWork(work: WorkInfo): void-End-->

**系统能力：** SystemCapability.ResourceSchedule.WorkScheduler

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| work | [WorkInfo](arkts-backgroundtasks-workscheduler-workinfo-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [9700004](../../apis-backgroundtasks-kit/errorcode-workScheduler.md#9700004-workinfo校验失败) |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [9700005](../../apis-backgroundtasks-kit/errorcode-workScheduler.md#9700005-startwork失败) |
| [9700001](../../apis-backgroundtasks-kit/errorcode-workScheduler.md#9700001-内存操作失败) |
| [9700002](../../apis-backgroundtasks-kit/errorcode-workScheduler.md#9700002-parcel读写操作失败) |
| [9700003](../../apis-backgroundtasks-kit/errorcode-workScheduler.md#9700003-系统服务失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { workScheduler } from '@kit.BackgroundTasksKit';

let workInfo: workScheduler.WorkInfo = {
  workId: 1,
  batteryStatus: workScheduler.BatteryStatus.BATTERY_STATUS_LOW,
  isRepeat: false,
  isPersisted: true,
  bundleName: 'com.example.myapplication',
  abilityName: 'MyExtension',
  parameters: {
    intValue: 1,
    stringValue: 'string value',
    booleanValue: true,
    floatValue: 1.5
  }
}
try {
  workScheduler.startWork(workInfo);
  console.info('workschedulerLog startWork success');
} catch (error) {
  console.error(`workschedulerLog startwork failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}`);
}
```
