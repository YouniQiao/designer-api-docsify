# sendEvent

## Modules to Import

```TypeScript
import { config } from '@kit.AccessibilityKit';
import { accessibility } from '@kit.AccessibilityKit';
import { AccessibilityEventType, AccessibilityAction, FocusMoveResultCode, InjectActionType, AccessibilityFocusScene, FocusRuleType, OperateVirtualNodeResult, AccessibilitySourceType } from '@kit.AccessibilityKit';
import { GesturePath } from '@kit.AccessibilityKit';
import { GesturePoint } from '@kit.AccessibilityKit';
```

## sendEvent

```TypeScript
function sendEvent(event: EventInfo, callback: AsyncCallback<void>): void
```

Sends an accessibility event. The event will be distributed to registered accessibility extension applications that match the event type for response. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [sendAccessibilityEvent](arkts-accessibility-accessibility-sendaccessibilityevent-f.md)(event: EventInfo, callback: AsyncCallback&lt;void&gt;)

<!--Device-accessibility-function sendEvent(event: EventInfo, callback: AsyncCallback<void>): void--><!--Device-accessibility-function sendEvent(event: EventInfo, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | EventInfo | Yes | Accessibility event object. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback used to return the result. If the accessibility event is sent successfully, err is undefined; otherwise, err is an error object. |

**Examples**

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
    console.error(`failed to sendEvent, Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info(`Succeeded in sendEvent, eventInfo is ${eventInfo}`);
});
```


## sendEvent

```TypeScript
function sendEvent(event: EventInfo): Promise<void>
```

Sends an accessibility event. The event will be distributed to registered accessibility extension applications that match the event type for response. This API uses a promise to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [sendAccessibilityEvent](arkts-accessibility-accessibility-sendaccessibilityevent-f.md)(event: EventInfo)

<!--Device-accessibility-function sendEvent(event: EventInfo): Promise<void>--><!--Device-accessibility-function sendEvent(event: EventInfo): Promise<void>-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | EventInfo | Yes | Accessibility event. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Examples**

```TypeScript
import { accessibility } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let eventInfo: accessibility.EventInfo = ({
  type: 'click',
  bundleName: 'com.example.MyApplication',
  triggerAction: 'click',
});

accessibility.sendEvent(eventInfo).then(() => {
  console.info(`Succeeded in send event,eventInfo is ${eventInfo}`);
}).catch((err: BusinessError) => {
  console.error(`failed to sendEvent, Code is ${err.code}, message is ${err.message}`);
});
```

