# requestSuspendDelay

## 导入模块

```TypeScript
```

## requestSuspendDelay

```TypeScript
function requestSuspendDelay(reason: string, callback: Callback<void>): DelaySuspendInfo
```

后台应用申请延迟挂起。延迟挂起时间一般情况下默认值为3分钟，低电量（依据系统低电量广播）时默认值为1分钟。

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为7。

**废弃版本：** 9

**替代接口：** [requestSuspendDelay](arkts-backgroundtasks-backgroundtaskmanager-requestsuspenddelay-f.md)

**系统能力：** SystemCapability.ResourceSchedule.BackgroundTaskManager.TransientTask

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| reason | string | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| [DelaySuspendInfo](arkts-backgroundtasks-backgroundtaskmanager-delaysuspendinfo-i.md) |

**示例**

```TypeScript
import backgroundTaskManager from '@ohos.backgroundTaskManager';

// 设置延迟任务挂起的原因
let myReason = 'test requestSuspendDelay';
// 申请延迟任务
let delayInfo = backgroundTaskManager.requestSuspendDelay(myReason, () => {
  console.info('Request suspension delay will time out.');
})
// 打印延迟任务信息
let id = delayInfo.requestId;
let time = delayInfo.actualDelayTime;
console.info('The requestId is: ' + id);
console.info('The actualDelayTime is: ' + time);
```
