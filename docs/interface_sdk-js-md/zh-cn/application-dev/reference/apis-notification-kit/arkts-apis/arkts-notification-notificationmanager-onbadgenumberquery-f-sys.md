# onBadgeNumberQuery（系统接口）

## 导入模块

```TypeScript
import { notificationManager } from 'kits/@kit.NotificationKit';
```

## onBadgeNumberQuery

```TypeScript
function onBadgeNumberQuery(callback: (bundle: BundleOption) => Promise<long>): void
```

注册应用角标数量查询回调。

**起始版本：** 22

**ArkTS模式：** ArkTS-Dyn起始版本为22；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notificationManager-function onBadgeNumberQuery(callback: (bundle: BundleOption) => Promise<long>): void--><!--Device-notificationManager-function onBadgeNumberQuery(callback: (bundle: BundleOption) => Promise<long>): void-End-->

**系统能力：** SystemCapability.Notification.Notification

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | ArkTS-Dyn: (bundle: BundleOption) =&gt; Promise&lt;number&gt;  <br>ArkTS-Sta：(bundle: BundleOption) =&gt; Promise&lt;long&gt; | 是 | 应用角标数量查询函数。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 1600001 | Internal error. |
| 202 | Not system application to call the interface. |
| 1600002 | Marshalling or unmarshalling error. |
| 1600003 | Failed to connect to the service. |

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

