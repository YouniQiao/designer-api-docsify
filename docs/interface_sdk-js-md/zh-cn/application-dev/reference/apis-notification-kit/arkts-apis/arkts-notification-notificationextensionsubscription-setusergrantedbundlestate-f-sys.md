# setUserGrantedBundleState（系统接口）

## 导入模块

```TypeScript
import { notificationExtensionSubscription } from 'kits/@kit.NotificationKit';
```

## setUserGrantedBundleState

```TypeScript
function setUserGrantedBundleState(targetBundle: BundleOption,
    enabledBundles: BundleOption[], enabled: boolean): Promise<void>
```

设置指定应用中“已获取的本机通知”的应用通知开关状态。使用Promise异步回调。

**起始版本：** 22

**需要权限：** ohos.permission.NOTIFICATION_CONTROLLER

**系统能力：** SystemCapability.Notification.Notification

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| targetBundle | [BundleOption](arkts-notification-notificationcommondef-bundleoption-i.md) | 是 |
| enabledBundles | [BundleOption[]](arkts-notification-notificationcommondef-bundleoption-i.md) | 是 |
| enabled | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [1600001](../errorcode-notification.md#1600001-内部错误) |
| [1600003](../errorcode-notification.md#1600003-连接通知服务失败) |
| [1600022](../errorcode-notification.md#1600022-无效的包信息) |
