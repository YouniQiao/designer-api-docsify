# getRemainingDelayTime

## 导入模块

```TypeScript
```

## getRemainingDelayTime

```TypeScript
function getRemainingDelayTime(requestId: number, callback: AsyncCallback<number>): void
```

获取本次短时任务的剩余时间，使用callback异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [getRemainingDelayTime](arkts-backgroundtasks-backgroundtaskmanager-getremainingdelaytime-f.md)(requestId: int, callback: AsyncCallback&lt;int&gt;)

**系统能力：** SystemCapability.ResourceSchedule.BackgroundTaskManager.TransientTask

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| requestId | number | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |


## getRemainingDelayTime

```TypeScript
function getRemainingDelayTime(requestId: number): Promise<number>
```

获取本次短时任务的剩余时间，使用Promise异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [getRemainingDelayTime](arkts-backgroundtasks-backgroundtaskmanager-getremainingdelaytime-f.md)(requestId: int)

**系统能力：** SystemCapability.ResourceSchedule.BackgroundTaskManager.TransientTask

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| requestId | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |
