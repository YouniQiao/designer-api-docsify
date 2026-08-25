# stopWork

## 导入模块

```TypeScript
import { workScheduler } from '@kit.BackgroundTasksKit';
```

## stopWork

```TypeScript
function stopWork(work: WorkInfo, needCancel?: boolean): void
```

取消延迟任务。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ResourceSchedule.WorkScheduler

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| work | [WorkInfo](arkts-backgroundtasks-workscheduler-workinfo-i.md) | 是 |
| needCancel | boolean | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9700001](../errorcode-workScheduler.md#9700001-内存操作失败) |
| [9700002](../errorcode-workScheduler.md#9700002-parcel读写操作失败) |
| [9700003](../errorcode-workScheduler.md#9700003-系统服务失败) |
| [9700004](../errorcode-workScheduler.md#9700004-参数校验失败) |

**示例**

ArkTS-Dyn示例：

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
  // 停止延迟任务，false表示只停止不移除任务
  workScheduler.stopWork(workInfo, false);
  console.info('workschedulerLog stopWork success');
} catch (error) {
  console.error(`workschedulerLog stopWork failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}`);
}
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { workScheduler } from '@kit.BackgroundTasksKit';

const parameter: Record<string, int | double | string | boolean> = {
  'mykey0': 1,
  'mykey1': 'string value',
  'mykey2': true,
  'mykey3': 1.5
};
let workInfo: workScheduler.WorkInfo = {
  workId: 1,
  batteryStatus: workScheduler.BatteryStatus.BATTERY_STATUS_LOW,
  isRepeat: false,
  isPersisted: true,
  bundleName: 'com.example.myapplication',
  abilityName: 'MyExtension',
  parameters: parameter
}
try {
  workScheduler.stopWork(workInfo, false);
  console.info('workschedulerLog stopWork success');
} catch (error) {
  console.error(`workschedulerLog stopWork failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}`);
}
```
