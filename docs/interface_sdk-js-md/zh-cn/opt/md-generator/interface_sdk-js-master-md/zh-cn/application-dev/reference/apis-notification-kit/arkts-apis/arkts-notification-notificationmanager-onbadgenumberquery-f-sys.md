# onBadgeNumberQuery（系统接口）

## 导入模块

```TypeScript
import { notificationManager } from 'kits/@kit.NotificationKit';
```

## onBadgeNumberQuery

```TypeScript
function onBadgeNumberQuery(callback: (bundle: BundleOption) => Promise<number>): void
```

注册应用角标数量查询回调。

**起始版本：** 22

**需要权限：** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notificationManager-function onBadgeNumberQuery(callback: (bundle: BundleOption) => Promise<long>): void--><!--Device-notificationManager-function onBadgeNumberQuery(callback: (bundle: BundleOption) => Promise<long>): void-End-->

**系统能力：** SystemCapability.Notification.Notification

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | (bundle: BundleOption) =&gt; Promise&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [1600001](../errorcode-notification.md#1600001-内部错误) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [1600002](../errorcode-notification.md#1600002-序列化或反序列化错误) |
| [1600003](../errorcode-notification.md#1600003-连接通知服务失败) |

## 示例

```TypeScript
try{
    notificationManager.onBadgeNumberQuery(
        async (bundleOption: notificationManager.BundleOption) => {
            return 1;
        }
    );
} catch (err) {
    console.error(`OnBadgeNumberQuery failed, code is ${err.code}, message is ${err.message}`);
}
```
