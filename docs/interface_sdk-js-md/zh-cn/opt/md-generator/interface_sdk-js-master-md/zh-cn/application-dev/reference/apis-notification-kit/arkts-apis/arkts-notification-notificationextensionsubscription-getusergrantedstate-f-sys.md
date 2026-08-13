# getUserGrantedState（系统接口）

## 导入模块

```TypeScript
import { notificationExtensionSubscription } from '@kit.NotificationKit';
```

## getUserGrantedState

```TypeScript
function getUserGrantedState(targetBundle: BundleOption): Promise<boolean>
```

查询指定应用的“允许获取本机通知”的开关状态。使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notificationExtensionSubscription-function getUserGrantedState(targetBundle: BundleOption): Promise<boolean>--><!--Device-notificationExtensionSubscription-function getUserGrantedState(targetBundle: BundleOption): Promise<boolean>-End-->

**系统能力：** SystemCapability.Notification.Notification

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| targetBundle | [BundleOption](arkts-notification-notificationcommondef-bundleoption-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [1600001](../errorcode-notification.md#1600001-内部错误) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [1600003](../errorcode-notification.md#1600003-连接通知服务失败) |
| [1600022](../errorcode-notification.md#1600022-无效的包信息) |

## 示例

```TypeScript
let targetBundle: notificationExtensionSubscription.BundleOption =
{
  // 应改为开发者需要查询的目标应用信息
  bundle: 'com.example.testnotification',
};
notificationExtensionSubscription.getUserGrantedState(targetBundle).then((isOpen: boolean) => {
  if (isOpen) {
    console.info('GrantedState true');
  } else {
    console.info('GrantedState false');
  }
}).catch((err: BusinessError) => {
  console.error(`getUserGrantedState fail, code is ${err.code}, message is ${err.message}`);
});
```
