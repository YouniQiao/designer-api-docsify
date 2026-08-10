# publish

## publish

```TypeScript
function publish(event: string, callback: AsyncCallback<void>): void
```

以回调形式发布公共事件。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [@ohos.commonEventManager:commonEventManager.publish](arkts-basicservices-commoneventmanager-publish-f.md#publish)(event:

<!--Device-commonEvent-function publish(event: string, callback: AsyncCallback<void>): void--><!--Device-commonEvent-function publish(event: string, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Notification.CommonEvent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | string | Yes | 表示要发布的公共事件。 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 表示发布公共事件的回调方法。 |

## Examples

```TypeScript
import Base from '@ohos.base';

// Callback for common event publication.
let publishCallBack = (err: Base.BusinessError) => {
    if (err.code) {
        console.error(`publish failed, code is ${err.code}, message is ${err.message}`);
    } else {
        console.info('publish');
    }
}

// Publish a common event.
commonEvent.publish("event", publishCallBack);
```


## publish

```TypeScript
function publish(event: string, options: CommonEventPublishData, callback: AsyncCallback<void>): void
```

以回调形式发布公共事件。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [@ohos.commonEventManager:commonEventManager.publish](arkts-basicservices-commoneventmanager-publish-f.md#publish)(event:

<!--Device-commonEvent-function publish(event: string, options: CommonEventPublishData, callback: AsyncCallback<void>): void--><!--Device-commonEvent-function publish(event: string, options: CommonEventPublishData, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Notification.CommonEvent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | string | Yes | 表示要发布的公共事件。 |
| options | [CommonEventPublishData](arkts-basicservices-commoneventpublishdata-commoneventpublishdata-i.md) | Yes | 表示发布公共事件的属性。 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 表示发布公共事件的回调方法。 |

## Examples

```TypeScript
import Base from '@ohos.base';
import CommonEventManager from '@ohos.commonEventManager';

// Information of a common event.
let options:CommonEventManager.CommonEventPublishData = {
    code: 0,             // Initial code of the common event.
    data: "initial data", // Initial data of the common event.
    isOrdered: true  // The common event is an ordered one.
};

// Callback for common event publication.
let publishCallBack = (err: Base.BusinessError) => {
    if (err.code) {
        console.error(`publish failed, code is ${err.code}, message is ${err.message}`);
    } else {
        console.info("publish");
    }
}

// Publish a common event.
commonEvent.publish("event", options, publishCallBack);
```

