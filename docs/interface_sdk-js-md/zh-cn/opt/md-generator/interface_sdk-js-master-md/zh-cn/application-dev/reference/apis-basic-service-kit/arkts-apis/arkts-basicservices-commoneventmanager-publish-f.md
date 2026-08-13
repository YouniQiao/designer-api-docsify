# publish

## publish

```TypeScript
function publish(event: string, callback: AsyncCallback<void>): void
```

发布公共事件。使用callback异步回调。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-commonEventManager-function publish(event: string, callback: AsyncCallback<void>): void--><!--Device-commonEventManager-function publish(event: string, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | string | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [1500007](../../apis-basic-services-kit/errorcode-CommonEventService.md#1500007-ipc请求发送失败) |
| [1500003](../../apis-basic-services-kit/errorcode-CommonEventService.md#1500003-公共事件发送频率过高) |
| [1500008](../../apis-basic-services-kit/errorcode-CommonEventService.md#1500008-公共事件服务端初始化失败) |
| [1500009](../../apis-basic-services-kit/errorcode-CommonEventService.md#1500009-获取系统参数失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// 发布公共事件
try {
  commonEventManager.publish('event', (err: BusinessError) => {
    if (err) {
      console.error(`Failed to publish common event. Code is ${err.code}, message is ${err.message}`);
      return;
    }
    console.info(`Succeeded in publishing common event.`);
  });
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(`Failed to publish common event. Code is ${err.code}, message is ${err.message}`);
}
```


## publish

```TypeScript
function publish(event: string, options: CommonEventPublishData, callback: AsyncCallback<void>): void
```

发布公共事件。使用callback异步回调。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-commonEventManager-function publish(event: string, options: CommonEventPublishData, callback: AsyncCallback<void>): void--><!--Device-commonEventManager-function publish(event: string, options: CommonEventPublishData, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | string | 是 |
| options | [CommonEventPublishData](arkts-basicservices-commoneventpublishdata-commoneventpublishdata-i.md) | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [1500007](../../apis-basic-services-kit/errorcode-CommonEventService.md#1500007-ipc请求发送失败) |
| [1500003](../../apis-basic-services-kit/errorcode-CommonEventService.md#1500003-公共事件发送频率过高) |
| [1500008](../../apis-basic-services-kit/errorcode-CommonEventService.md#1500008-公共事件服务端初始化失败) |
| [1500009](../../apis-basic-services-kit/errorcode-CommonEventService.md#1500009-获取系统参数失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// 公共事件相关信息，以发布有序公共事件为例
let options: commonEventManager.CommonEventPublishData = {
  code: 0,
  data: 'initial data',
  isOrdered: true // 有序公共事件
};

// 发布公共事件
try {
  commonEventManager.publish('event', options, (err: BusinessError) => {
    if (err) {
      console.error(`Failed to publish common event. Code is ${err.code}, message is ${err.message}`);
      return;
    }
    console.info(`Succeeded in publishing common event.`);
  });
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(`Failed to publish common event. Code is ${err.code}, message is ${err.message}`);
}
```
