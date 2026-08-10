# isNotificationEnabledSync

## Modules to Import

```TypeScript
import { notificationManager } from 'kits/@kit.NotificationKit';
```

## isNotificationEnabledSync

```TypeScript
function isNotificationEnabledSync(): boolean
```

同步查询当前应用通知授权状态。

用于在发布通知前快速检查当前应用是否被允许发送通知。此接口为同步接口，调用后立即返回结果，适用于需要在同步代码流程中获取使能状态的场景。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-notificationManager-function isNotificationEnabledSync(): boolean--><!--Device-notificationManager-function isNotificationEnabledSync(): boolean-End-->

**System capability:** SystemCapability.Notification.Notification

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 返回查询通知使能状态的结果。返回true，表示允许发布通知；返回false，表示禁止发布通知。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 1600001 | Internal error. |
| 1600002 | Marshalling or unmarshalling error. |
| 1600003 | Failed to connect to the service. |

## Examples

```TypeScript
let enabled: boolean = notificationManager.isNotificationEnabledSync();
console.info(`isNotificationEnabledSync success, data is : ${JSON.stringify(enabled)}`);
```

