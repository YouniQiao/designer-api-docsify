# requestSuspendDelay

## 导入模块

```TypeScript
import { backgroundTaskManager } from 'kits/@kit.BackgroundTasksKit';
```

## requestSuspendDelay

```TypeScript
function requestSuspendDelay(reason: string, callback: Callback<void>): DelaySuspendInfo
```

申请短时任务。

> **说明：**
> 
> 短时任务的申请和使用过程中的约束与限制请参考[指南](../../../task-management/transient-task.md#约束与限制)。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

<!--Device-backgroundTaskManager-function requestSuspendDelay(reason: string, callback: Callback<void>): DelaySuspendInfo--><!--Device-backgroundTaskManager-function requestSuspendDelay(reason: string, callback: Callback<void>): DelaySuspendInfo-End-->

**系统能力：** SystemCapability.ResourceSchedule.BackgroundTaskManager.TransientTask

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| reason | string | 是 | 申请短时任务的原因。 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | 是 | 短时任务即将超时的回调函数，一般在超时前6秒，通过此回调通知应用。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DelaySuspendInfo](arkts-backgroundtasks-backgroundtaskmanager-delaysuspendinfo-i.md) | 返回短时任务信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt; 2. Incorrect parameters types. |
| 9800004 | System service operation failed. |
| 9800001 | Memory operation failed. |
| 9900002 | Transient task verification failed. |
| 9800003 | Internal transaction failed. |
| 9900001 | Caller information verification failed for a transient task. |
| 9800002 | Failed to write data into parcel. Possible reasons: 1. Invalid parameters; &lt;br&gt; 2. Failed to apply for memory. |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { backgroundTaskManager } from '@kit.BackgroundTasksKit';

// 申请短时任务的原因
let delayReason = 'test requestSuspendDelay';
try {
  let delayInfo = backgroundTaskManager.requestSuspendDelay(delayReason, () => {
  // 回调函数。应用申请的短时任务即将超时，通过此函数回调应用，执行一些清理和标注工作，并取消短时任务
  // 此处回调与应用的业务功能不耦合，短时任务申请成功后，正常执行应用本身的业务
    console.info('Request suspension delay will time out.');
  })
  let requestId = delayInfo.requestId;
  let time = delayInfo.actualDelayTime;
  console.info('The requestId is: ' + requestId);
  console.info('The actualDelayTime is: ' + time);
} catch (error) {
  console.error(`requestSuspendDelay failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}`);
}
```

