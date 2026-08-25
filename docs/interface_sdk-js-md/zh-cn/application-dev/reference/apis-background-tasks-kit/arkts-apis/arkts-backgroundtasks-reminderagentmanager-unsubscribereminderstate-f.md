# unsubscribeReminderState

## 导入模块

```TypeScript
import { reminderAgentManager } from 'kits/@kit.BackgroundTasksKit';
```

## unsubscribeReminderState

```TypeScript
function unsubscribeReminderState(callback?: Callback<Array<ReminderState>>): Promise<void>
```

取消订阅代理提醒状态。使用Promise异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Notification.ReminderAgent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;[ReminderState](arkts-backgroundtasks-reminderagentmanager-reminderstate-i.md)&gt;&gt; | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [1700007](../errorcode-reminderAgentManager.md#1700007-参数错误) |
