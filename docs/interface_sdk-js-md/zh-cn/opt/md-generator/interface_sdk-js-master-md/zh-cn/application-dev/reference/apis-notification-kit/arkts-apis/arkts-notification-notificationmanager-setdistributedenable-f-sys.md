# setDistributedEnable（系统接口）

## 导入模块

```TypeScript
import { notificationManager } from '@kit.NotificationKit';
```

## setDistributedEnable

```TypeScript
function setDistributedEnable(enable: boolean, callback: AsyncCallback<void>): void
```

设置设备是否支持分布式通知。使用callback异步回调。

**起始版本：** 9

**废弃版本：** 26.0.0

**替代接口：** [setDistributedEnabled](notificationManager.setDistributedEnabled(enable:)

**需要权限：** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notificationManager-function setDistributedEnable(enable: boolean, callback: AsyncCallback<void>): void--><!--Device-notificationManager-function setDistributedEnable(enable: boolean, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Notification.Notification

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enable | boolean | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [801](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#801-该设备不支持此api) |
| [1600010](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600010-分布式操作失败) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [1600001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600001-内部错误) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |
| [1600002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600002-序列化或反序列化错误) |
| [1600003](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600003-连接通知服务失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let setDistributedEnableCallback = (err: BusinessError): void => {
    if (err) {
        console.error(`setDistributedEnable failed, code is ${err.code}, message is ${err.message}`);
    } else {
        console.info('setDistributedEnable success');
    }
};
let enable: boolean = true;
notificationManager.setDistributedEnable(enable, setDistributedEnableCallback);
```


## setDistributedEnable

```TypeScript
function setDistributedEnable(enable: boolean): Promise<void>
```

设置设备是否支持分布式通知。使用Promise异步回调。

**起始版本：** 9

**废弃版本：** 26.0.0

**替代接口：** [setDistributedEnabled](notificationManager.setDistributedEnabled(enable:)

**需要权限：** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notificationManager-function setDistributedEnable(enable: boolean): Promise<void>--><!--Device-notificationManager-function setDistributedEnable(enable: boolean): Promise<void>-End-->

**系统能力：** SystemCapability.Notification.Notification

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enable | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [801](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#801-该设备不支持此api) |
| [1600010](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600010-分布式操作失败) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [1600001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600001-内部错误) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |
| [1600002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600002-序列化或反序列化错误) |
| [1600003](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600003-连接通知服务失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let enable: boolean = true;
notificationManager.setDistributedEnable(enable).then(() => {
    console.info('setDistributedEnable success');
}).catch((err: BusinessError) => {
    console.error(`setDistributedEnable failed, code is ${err.code}, message is ${err.message}`);
});
```
