# requestSuspendDelay

## requestSuspendDelay

```TypeScript
function requestSuspendDelay(reason: string, callback: Callback<void>): DelaySuspendInfo
```

申请短时任务。

> **说明：**
> 
> 短时任务的申请和使用过程中的约束与限制请参考[指南](../../../task-management/transient-task.md#约束与限制)。

**起始版本：** 9

<!--Device-backgroundTaskManager-function requestSuspendDelay(reason: string, callback: Callback<void>): DelaySuspendInfo--><!--Device-backgroundTaskManager-function requestSuspendDelay(reason: string, callback: Callback<void>): DelaySuspendInfo-End-->

**系统能力：** SystemCapability.ResourceSchedule.BackgroundTaskManager.TransientTask

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| reason | string | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| [DelaySuspendInfo](arkts-backgroundtasks-backgroundtaskmanager-delaysuspendinfo-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [9800004](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-backgroundtasks-kit/errorcode-backgroundTaskMgr.md#9800004-系统服务失败) |
| [9800001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-backgroundtasks-kit/errorcode-backgroundTaskMgr.md#9800001-内存操作失败) |
| [9900002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-backgroundtasks-kit/errorcode-backgroundTaskMgr.md#9900002-短时任务校验失败) |
| [9800003](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-backgroundtasks-kit/errorcode-backgroundTaskMgr.md#9800003-ipc通信失败) |
| [9900001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-backgroundtasks-kit/errorcode-backgroundTaskMgr.md#9900001-短时任务调用方信息校验失败) |
| [9800002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-backgroundtasks-kit/errorcode-backgroundTaskMgr.md#9800002-parcel读写操作失败) |

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
