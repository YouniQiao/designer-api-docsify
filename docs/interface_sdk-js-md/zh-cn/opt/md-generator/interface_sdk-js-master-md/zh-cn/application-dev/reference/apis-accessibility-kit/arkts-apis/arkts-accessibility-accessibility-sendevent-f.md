# sendEvent

## sendEvent

```TypeScript
function sendEvent(event: EventInfo, callback: AsyncCallback<void>): void
```

发送无障碍事件，使用callback异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [accessibility.sendAccessibilityEvent](arkts-accessibility-accessibility-sendaccessibilityevent-f.md#sendaccessibilityevent)(event:

<!--Device-accessibility-function sendEvent(event: EventInfo, callback: AsyncCallback<void>): void--><!--Device-accessibility-function sendEvent(event: EventInfo, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | [EventInfo](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-update-eventinfo-i-sys.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## 示例

```TypeScript
import { accessibility } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let eventInfo: accessibility.EventInfo = ({
  type: 'click',
  bundleName: 'com.example.MyApplication',
  triggerAction: 'click',
});

accessibility.sendEvent(eventInfo, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to sendEvent. Code:${err.code}, message:${err.message}`);
    return;
  }
  console.info(`succeeded in sending event, eventInfo is ${eventInfo}`);
});
```


## sendEvent

```TypeScript
function sendEvent(event: EventInfo): Promise<void>
```

发送无障碍事件，使用Promise异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [accessibility.sendAccessibilityEvent](arkts-accessibility-accessibility-sendaccessibilityevent-f.md#sendaccessibilityevent)(event:

<!--Device-accessibility-function sendEvent(event: EventInfo): Promise<void>--><!--Device-accessibility-function sendEvent(event: EventInfo): Promise<void>-End-->

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | [EventInfo](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-update-eventinfo-i-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

## 示例

```TypeScript
import { accessibility } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let eventInfo: accessibility.EventInfo = ({
  type: 'click',
  bundleName: 'com.example.MyApplication',
  triggerAction: 'click',
});

accessibility.sendEvent(eventInfo).then(() => {
  console.info(`succeeded in sending event, eventInfo is ${eventInfo}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to sendEvent. Code:${err.code}, message:${err.message}`);
});
```
