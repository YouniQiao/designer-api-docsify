# openNotificationSettings

## 导入模块

```TypeScript
import { notificationManager } from 'kits/@kit.NotificationKit';
```

## openNotificationSettings

```TypeScript
function openNotificationSettings(context: UIAbilityContext): Promise<void>
```

拉起应用的通知设置界面，该页面以半模态形式呈现，可用于设置通知开关、 通知提醒方式等。使用Promise异步回调。适用于用户需要手动修改通知设置的场景，如用户拒绝授权后二次申请，或需要 修改通知提醒方式（振动、响铃等）。当requestEnableNotification弹窗被 用户拒绝后，开发者可调用此接口引导用户前往通知设置页面手动开启。

**起始版本：** 13

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Notification.NotificationSettings

**参见：**

requestEnableNotification 请求通知使能。

isNotificationEnabled 查询当前应用通知授权状态。

getNotificationSetting 获取应用的通知设置状态。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [UIAbilityContext](../../apis-ability-kit/arkts-apis/arkts-ability-uiabilitycontext-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1600001](../errorcode-notification.md#1600001-内部错误) |
| [1600003](../errorcode-notification.md#1600003-连接通知服务失败) |
| [1600018](../errorcode-notification.md#1600018-通知设置页面已经拉起) |
