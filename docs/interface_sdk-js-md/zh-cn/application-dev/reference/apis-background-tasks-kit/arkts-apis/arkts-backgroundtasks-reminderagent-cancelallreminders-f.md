# cancelAllReminders

## 导入模块

```TypeScript
import { reminderAgent } from 'kits/@kit.BackgroundTasksKit';
```

## cancelAllReminders

```TypeScript
function cancelAllReminders(callback: AsyncCallback<void>): void
```

取消当前应用所有的提醒，使用回调的方式实现异步调用。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** cancelAllReminders

**系统能力：** SystemCapability.Notification.ReminderAgent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |


## cancelAllReminders

```TypeScript
function cancelAllReminders(): Promise<void>
```

取消当前应用所有的提醒，使用Promise方式实现异步调用。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** cancelAllReminders

**系统能力：** SystemCapability.Notification.ReminderAgent

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |
