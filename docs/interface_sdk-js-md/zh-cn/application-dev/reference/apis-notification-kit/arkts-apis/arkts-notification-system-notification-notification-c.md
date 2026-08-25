# Notification

提供通知管理的能力。

**起始版本：** 3

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为3。

**废弃版本：** 7

**替代接口：** [notification/notification](arkts-notification.md)

**系统能力：** SystemCapability.Notification.Notification

## 导入模块

```TypeScript
import { Notification, ActionResult, ShowNotificationOptions } from '@kit.NotificationKit';
```

## show

```TypeScript
static show(options?: ShowNotificationOptions): void
```

显示通知。

**起始版本：** 3

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为3。

**废弃版本：** 7

**替代接口：** [notification/notification](arkts-notification.md)

**系统能力：** SystemCapability.Notification.Notification

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [ShowNotificationOptions](arkts-notification-system-notification-shownotificationoptions-i.md) | 否 |

**示例**

```TypeScript
let notificationObj: notification = {
  show() {
    notification.show({
      contentTitle: 'title info',
      contentText: 'text',
      clickAction: {
        bundleName: 'com.example.testapp',
        abilityName: 'notificationDemo',
        uri: '/path/to/notification'
      }
    });
  }
}
```
