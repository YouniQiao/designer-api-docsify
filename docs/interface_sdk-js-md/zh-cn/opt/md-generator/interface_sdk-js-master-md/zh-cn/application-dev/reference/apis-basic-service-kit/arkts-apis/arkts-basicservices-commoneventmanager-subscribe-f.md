# subscribe

## subscribe

```TypeScript
function subscribe(subscriber: CommonEventSubscriber, callback: AsyncCallback<CommonEventData>): void
```

订阅公共事件。使用callback异步回调。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-commonEventManager-function subscribe(subscriber: CommonEventSubscriber, callback: AsyncCallback<CommonEventData>): void--><!--Device-commonEventManager-function subscribe(subscriber: CommonEventSubscriber, callback: AsyncCallback<CommonEventData>): void-End-->

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| subscriber | [CommonEventSubscriber](arkts-basicservices-commoneventsubscriber-commoneventsubscriber-i.md) | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;CommonEventData&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1500007](../../apis-basic-services-kit/errorcode-CommonEventService.md#1500007-ipc请求发送失败) |
| [1500010](../../apis-basic-services-kit/errorcode-CommonEventService.md#1500010-订阅者数量超限) |
| [1500008](../../apis-basic-services-kit/errorcode-CommonEventService.md#1500008-公共事件服务端初始化失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// 定义订阅者，用于保存创建成功的订阅者对象，后续使用其完成订阅及取消订阅的动作
let subscriber: commonEventManager.CommonEventSubscriber | null = null;
// 订阅者信息
let subscribeInfo: commonEventManager.CommonEventSubscribeInfo = {
  events: ['event']
};

// 创建订阅者
try {
  commonEventManager.createSubscriber(subscribeInfo,
    (err: BusinessError, commonEventSubscriber: commonEventManager.CommonEventSubscriber) => {
      if (!err) {
        console.info(`Succeeded in creating subscriber.`);
        subscriber = commonEventSubscriber;
        // 订阅公共事件
        try {
          commonEventManager.subscribe(subscriber, (err: BusinessError, data: commonEventManager.CommonEventData) => {
            if (err) {
              console.error(`Failed to subscribe. Code is ${err.code}, message is ${err.message}`);
              return;
            }
            console.info(`Succeeded in subscribing, data is ${JSON.stringify(data)}`);
          });
        } catch (error) {
          let err: BusinessError = error as BusinessError;
          console.error(`Failed to subscribe. Code is ${err.code}, message is ${err.message}`);
        }
        return;
      }
      console.error(`Failed to create subscriber. Code is ${err.code}, message is ${err.message}`);
    });
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(`Failed to create subscriber. Code is ${err.code}, message is ${err.message}`);
}
```
