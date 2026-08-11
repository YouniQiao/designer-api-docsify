# setStaticSubscriberState（系统接口）

## setStaticSubscriberState

```TypeScript
function setStaticSubscriberState(enable: boolean, callback: AsyncCallback<void>): void
```

为当前应用设置静态订阅事件使能或去使能状态。使用callback异步回调。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-commonEventManager-function setStaticSubscriberState(enable: boolean, callback: AsyncCallback<void>): void--><!--Device-commonEventManager-function setStaticSubscriberState(enable: boolean, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Notification.CommonEvent

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enable | boolean | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [1500007](../../apis-basic-services-kit/errorcode-CommonEventService.md#1500007-ipc请求发送失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [1500008](../../apis-basic-services-kit/errorcode-CommonEventService.md#1500008-公共事件服务端初始化失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

commonEventManager.setStaticSubscriberState(true, (err: BusinessError) => {
  if (err.code != 0) {
    console.error(`setStaticSubscriberState failed, errCode: ${err.code}, errMsg: ${err.message}`);
    return;
  }
  console.info(`setStaticSubscriberState success`);
});
```


## setStaticSubscriberState

```TypeScript
function setStaticSubscriberState(enable: boolean): Promise<void>
```

为当前应用设置静态订阅事件使能或去使能状态。使用Promise异步回调。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-commonEventManager-function setStaticSubscriberState(enable: boolean): Promise<void>--><!--Device-commonEventManager-function setStaticSubscriberState(enable: boolean): Promise<void>-End-->

**系统能力：** SystemCapability.Notification.CommonEvent

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enable | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [1500007](../../apis-basic-services-kit/errorcode-CommonEventService.md#1500007-ipc请求发送失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [1500008](../../apis-basic-services-kit/errorcode-CommonEventService.md#1500008-公共事件服务端初始化失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

commonEventManager.setStaticSubscriberState(false).then(() => {
  console.info(`setStaticSubscriberState success`);
}).catch((err: BusinessError) => {
  console.error(`setStaticSubscriberState failed, errCode: ${err.code}, errMsg: ${err.message}`);
});
```


## setStaticSubscriberState

```TypeScript
function setStaticSubscriberState(enable: boolean, events?: Array<string>): Promise<void>
```

设置当前应用的静态订阅公共事件的使能状态。使用Promise异步回调。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-commonEventManager-function setStaticSubscriberState(enable: boolean, events?: Array<string>): Promise<void>--><!--Device-commonEventManager-function setStaticSubscriberState(enable: boolean, events?: Array<string>): Promise<void>-End-->

**系统能力：** SystemCapability.Notification.CommonEvent

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enable | boolean | 是 |
| events | Array&lt;string&gt; | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [1500007](../../apis-basic-services-kit/errorcode-CommonEventService.md#1500007-ipc请求发送失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [1500008](../../apis-basic-services-kit/errorcode-CommonEventService.md#1500008-公共事件服务端初始化失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let eventName: string[] = ['usual.event.SEND_DATA'];
commonEventManager.setStaticSubscriberState(true, eventName).then(() => {
  console.info(`setStaticSubscriberState success`);
}).catch((err: BusinessError) => {
  console.error(`setStaticSubscriberState failed, errCode: ${err.code}, errMsg: ${err.message}`);
});
```
