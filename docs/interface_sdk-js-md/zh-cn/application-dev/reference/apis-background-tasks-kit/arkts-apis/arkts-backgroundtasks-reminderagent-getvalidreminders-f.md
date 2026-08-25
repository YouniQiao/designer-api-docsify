# getValidReminders

## 导入模块

```TypeScript
import { reminderAgent } from 'kits/@kit.BackgroundTasksKit';
```

## getValidReminders

```TypeScript
function getValidReminders(callback: AsyncCallback<Array<ReminderRequest>>): void
```

获取当前应用已设置的所有有效（未过期）的提醒，使用回调的方式实现异步调用。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** getValidReminders

**系统能力：** SystemCapability.Notification.ReminderAgent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;ReminderRequest&gt;&gt; | 是 |


## getValidReminders

```TypeScript
function getValidReminders(): Promise<Array<ReminderRequest>>
```

获取当前应用已设置的所有有效（未过期）的提醒，使用Promise方式实现异步调用。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** getValidReminders

**系统能力：** SystemCapability.Notification.ReminderAgent

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;ReminderRequest & gt; & gt; |
