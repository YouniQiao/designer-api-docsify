# isNotificationEnabled

## 导入模块

```TypeScript
import { notificationManager } from 'kits/@kit.NotificationKit';
```

## isNotificationEnabled

```TypeScript
function isNotificationEnabled(callback: AsyncCallback<boolean>): void
```

查询当前应用通知授权状态。使用callback异步回调。

用于在发布通知前检查当前应用是否被允许发送通知，避免在通知授权关闭时发布导致失败。

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**需要权限：** 
- API版本9 - 10：ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notificationManager-function isNotificationEnabled(callback: AsyncCallback<boolean>): void--><!--Device-notificationManager-function isNotificationEnabled(callback: AsyncCallback<boolean>): void-End-->

**系统能力：** SystemCapability.Notification.Notification

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 | 回调函数。返回true，表示允许发布通知；返回false，表示禁止发布通知；调用失败返回错误对象。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 1600008 | The user does not exist.<br>**适用版本：** 11+ |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 201 | Permission denied.<br>**适用版本：** 9 - 10 |
| 1600001 | Internal error. |
| 202 | Not system application to call the interface.<br>**适用版本：** 9 - 10 |
| 1600002 | Marshalling or unmarshalling error. |
| 1600003 | Failed to connect to the service. |
| 17700001 | The specified bundle name was not found.<br>**适用版本：** 11+ |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let isNotificationEnabledCallback = (err: BusinessError, data: boolean): void => {
  if (err) {
    console.error(`isNotificationEnabled failed, code is ${err.code}, message is ${err.message}`);
  } else {
    console.info(`isNotificationEnabled success, data is ${JSON.stringify(data)}`);
  }
}

notificationManager.isNotificationEnabled(isNotificationEnabledCallback);
```


## isNotificationEnabled

```TypeScript
function isNotificationEnabled(): Promise<boolean>
```

查询当前应用通知授权状态。使用Promise异步回调。

用于在发布通知前检查当前应用是否被允许发送通知，避免在通知使能关闭时发布导致失败。

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**需要权限：** 
- API版本9 - 10：ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notificationManager-function isNotificationEnabled(): Promise<boolean>--><!--Device-notificationManager-function isNotificationEnabled(): Promise<boolean>-End-->

**系统能力：** SystemCapability.Notification.Notification

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;boolean&gt; | Promise对象。返回true，表示允许发布通知；返回false，表示禁止发布通知。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 1600008 | The user does not exist.<br>**适用版本：** 11+ |
| 201 | Permission denied.<br>**适用版本：** 9 - 10 |
| 1600001 | Internal error. |
| 202 | Not system application to call the interface.<br>**适用版本：** 9 - 10 |
| 1600002 | Marshalling or unmarshalling error. |
| 1600003 | Failed to connect to the service. |
| 17700001 | The specified bundle name was not found.<br>**适用版本：** 11+ |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

notificationManager.isNotificationEnabled().then((data: boolean) => {
  console.info(`isNotificationEnabled success, data: ${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
  console.error(`isNotificationEnabled failed, code is ${err.code}, message is ${err.message}`);
});
```

