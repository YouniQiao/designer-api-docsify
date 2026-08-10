# removeAll（系统接口）

## 导入模块

```TypeScript
import { notificationSubscribe } from 'kits/@kit.NotificationKit';
```

## removeAll

```TypeScript
function removeAll(bundle: BundleOption, callback: AsyncCallback<void>): void
```

删除指定应用的所有通知。使用callback异步回调。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notificationSubscribe-function removeAll(bundle: BundleOption, callback: AsyncCallback<void>): void--><!--Device-notificationSubscribe-function removeAll(bundle: BundleOption, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Notification.Notification

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| bundle | [BundleOption](arkts-notification-notificationextensionsubscription-bundleoption-t.md) | 是 | 指定应用的包信息。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 | 删除指定应用的所有通知回调函数。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 201 | Permission denied. |
| 1600001 | Internal error. |
| 202 | Not system application to call the interface. |
| 1600002 | Marshalling or unmarshalling error. |
| 1600003 | Failed to connect to the service. |
| 17700001 | The specified bundle name was not found. |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let removeAllCallback = (err: BusinessError) => {
  if (err) {
    console.error(`removeAll failed, code is ${err.code}, message is ${err.message}`);
  } else {
    console.info('removeAll success');
  }
}
let bundle: notificationSubscribe.BundleOption = {
  bundle: 'bundleName1',
};
notificationSubscribe.removeAll(bundle, removeAllCallback);
```


## removeAll

```TypeScript
function removeAll(callback: AsyncCallback<void>): void
```

删除所有通知。使用callback异步回调。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notificationSubscribe-function removeAll(callback: AsyncCallback<void>): void--><!--Device-notificationSubscribe-function removeAll(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Notification.Notification

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 | 删除所有通知回调函数。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 201 | Permission denied. |
| 1600001 | Internal error. |
| 202 | Not system application to call the interface. |
| 1600002 | Marshalling or unmarshalling error. |
| 1600003 | Failed to connect to the service. |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let removeAllCallback = (err: BusinessError) => {
    if (err) {
        console.error(`removeAll failed, code is ${err.code}, message is ${err.message}`);
    } else {
        console.info('removeAll success');
    }
}
notificationSubscribe.removeAll(removeAllCallback);
```


## removeAll

```TypeScript
function removeAll(userId: int, callback: AsyncCallback<void>): void
```

删除指定用户下的所有通知。使用callback异步回调。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notificationSubscribe-function removeAll(userId: int, callback: AsyncCallback<void>): void--><!--Device-notificationSubscribe-function removeAll(userId: int, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Notification.Notification

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| userId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 是 | 用户ID。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 | 删除指定用户所有通知回调函数。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 1600008 | The user does not exist. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 201 | Permission denied. |
| 1600001 | Internal error. |
| 202 | Not system application to call the interface. |
| 1600002 | Marshalling or unmarshalling error. |
| 1600003 | Failed to connect to the service. |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let removeAllCallback = (err: BusinessError) => {
  if (err) {
    console.error(`removeAll failed, code is ${err.code}, message is ${err.message}`);
  } else {
    console.info('removeAll success');
  }
}
// 用户ID，使用时需替换为真实的userId。
let userId: number = 1;
notificationSubscribe.removeAll(userId, removeAllCallback);
```


## removeAll

```TypeScript
function removeAll(userId: int): Promise<void>
```

删除指定用户下的所有通知。使用Promise异步回调。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notificationSubscribe-function removeAll(userId: int): Promise<void>--><!--Device-notificationSubscribe-function removeAll(userId: int): Promise<void>-End-->

**系统能力：** SystemCapability.Notification.Notification

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| userId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 是 | 用户ID。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | 无返回结果的Promise对象。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 1600008 | The user does not exist. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 201 | Permission denied. |
| 1600001 | Internal error. |
| 202 | Not system application to call the interface. |
| 1600002 | Marshalling or unmarshalling error. |
| 1600003 | Failed to connect to the service. |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let userId: number = 1;
notificationSubscribe.removeAll(userId).then(() => {
  console.info('removeAll success');
}).catch((err: BusinessError) => {
  console.error(`removeAll fail, code is ${err.code}, message is ${err.message}`);
});
```


## removeAll

```TypeScript
function removeAll(bundle?: BundleOption): Promise<void>
```

删除指定应用的所有通知。使用Promise异步回调。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notificationSubscribe-function removeAll(bundle?: BundleOption): Promise<void>--><!--Device-notificationSubscribe-function removeAll(bundle?: BundleOption): Promise<void>-End-->

**系统能力：** SystemCapability.Notification.Notification

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| bundle | [BundleOption](arkts-notification-notificationextensionsubscription-bundleoption-t.md) | 否 | 指定应用的包信息。默认为空，表示删除所有通知。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | 无返回结果的Promise对象。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 201 | Permission denied. |
| 1600001 | Internal error. |
| 202 | Not system application to call the interface. |
| 1600002 | Marshalling or unmarshalling error. |
| 1600003 | Failed to connect to the service. |
| 17700001 | The specified bundle name was not found. |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// 不指定应用时，删除所有通知
notificationSubscribe.removeAll().then(() => {
  console.info('removeAll success');
}).catch((err: BusinessError) => {
  console.error(`removeAll fail, code is ${err.code}, message is ${err.message}`);
});
```

