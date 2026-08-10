# getUserGrantedEnabledBundles (System API)

## Modules to Import

```TypeScript
import { notificationExtensionSubscription } from 'kits/@kit.NotificationKit';
```

## getUserGrantedEnabledBundles

```TypeScript
function getUserGrantedEnabledBundles(targetBundle: BundleOption): Promise<BundleOption[]>
```

获取指定应用中“已获取的本机通知”通知开关开启的应用列表。使用Promise异步回调。

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notificationExtensionSubscription-function getUserGrantedEnabledBundles(targetBundle: BundleOption): Promise<BundleOption[]>--><!--Device-notificationExtensionSubscription-function getUserGrantedEnabledBundles(targetBundle: BundleOption): Promise<BundleOption[]>-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| targetBundle | [BundleOption](arkts-notification-notificationextensionsubscription-bundleoption-t.md) | Yes | 需要查询的目标应用信息。应用需要具有ohos.permission.SUBSCRIBE_NOTIFICATION权限， 并且实现[NotificationSubscriberExtensionAbility](arkts-notification-application-notificationsubscriberextensionability-notificationsubscriberextensionability-c.md)， 否则返回1600022错误码。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;BundleOption[]&gt; | Promise对象，返回指定应用中“已获取的本机通知”通知开关开启的应用列表。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 201 | Permission denied. |
| 1600001 | Internal error. |
| 202 | Not system application to call the interface. |
| 1600003 | Failed to connect to the service. |
| 1600022 | The specified bundle is invalid. |

## Examples

```TypeScript
let targetBundle: notificationExtensionSubscription.BundleOption =
{
  // Use the actual target application information.
  bundle: 'com.example.testnotification',
};
notificationExtensionSubscription.getUserGrantedEnabledBundles(targetBundle).then((data: notificationExtensionSubscription.BundleOption[]) => {
  console.info(`getUserGrantedEnabledBundles successfully. Data: ${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
  console.error(`getUserGrantedEnabledBundles fail, code is ${err.code}, message is ${err.message}`);
});
```

