# removeAll（系统接口）

## 导入模块

```TypeScript
import { notificationSubscribe } from '@kit.NotificationKit';
```

## removeAll

```TypeScript
function removeAll(bundle: BundleOption, callback: AsyncCallback<void>): void
```

删除指定应用的所有通知。使用callback异步回调。

**起始版本：** 9

**需要权限：** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notificationSubscribe-function removeAll(bundle: BundleOption, callback: AsyncCallback<void>): void--><!--Device-notificationSubscribe-function removeAll(bundle: BundleOption, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Notification.Notification

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundle | [BundleOption](arkts-notification-notificationcommondef-bundleoption-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [1600001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600001-内部错误) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |
| [1600002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600002-序列化或反序列化错误) |
| [1600003](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600003-连接通知服务失败) |
| [17700001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-bundle.md#17700001-指定的bundlename不存在) |

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

**需要权限：** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notificationSubscribe-function removeAll(callback: AsyncCallback<void>): void--><!--Device-notificationSubscribe-function removeAll(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Notification.Notification

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [1600001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600001-内部错误) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |
| [1600002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600002-序列化或反序列化错误) |
| [1600003](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600003-连接通知服务失败) |

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
function removeAll(userId: number, callback: AsyncCallback<void>): void
```

删除指定用户下的所有通知。使用callback异步回调。

**起始版本：** 9

**需要权限：** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notificationSubscribe-function removeAll(userId: int, callback: AsyncCallback<void>): void--><!--Device-notificationSubscribe-function removeAll(userId: int, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Notification.Notification

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| userId | number | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [1600008](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600008-用户不存在) |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [1600001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600001-内部错误) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |
| [1600002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600002-序列化或反序列化错误) |
| [1600003](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600003-连接通知服务失败) |

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
function removeAll(userId: number): Promise<void>
```

删除指定用户下的所有通知。使用Promise异步回调。

**起始版本：** 9

**需要权限：** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notificationSubscribe-function removeAll(userId: int): Promise<void>--><!--Device-notificationSubscribe-function removeAll(userId: int): Promise<void>-End-->

**系统能力：** SystemCapability.Notification.Notification

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| userId | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [1600008](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600008-用户不存在) |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [1600001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600001-内部错误) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |
| [1600002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600002-序列化或反序列化错误) |
| [1600003](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600003-连接通知服务失败) |

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

**需要权限：** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notificationSubscribe-function removeAll(bundle?: BundleOption): Promise<void>--><!--Device-notificationSubscribe-function removeAll(bundle?: BundleOption): Promise<void>-End-->

**系统能力：** SystemCapability.Notification.Notification

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundle | [BundleOption](arkts-notification-notificationcommondef-bundleoption-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [1600001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600001-内部错误) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |
| [1600002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600002-序列化或反序列化错误) |
| [1600003](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600003-连接通知服务失败) |
| [17700001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-bundle.md#17700001-指定的bundlename不存在) |

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
