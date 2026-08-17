# publishAsUser (System API)

## publishAsUser

```TypeScript
function publishAsUser(event: string, userId: number, callback: AsyncCallback<void>): void
```

Publishes a common event to a specific user. This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [publishAsUser](arkts-basicservices-commoneventmanager-publishasuser-f-sys.md#publishasuser)(event: string, userId: int, callback: AsyncCallback&lt;void&gt;)

<!--Device-commonEvent-function publishAsUser(event: string, userId: number, callback: AsyncCallback<void>): void--><!--Device-commonEvent-function publishAsUser(event: string, userId: number, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Notification.CommonEvent

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | string | Yes | Name of the common event to publish. |
| userId | number | Yes | ID of the user to whom the common event is published. |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback used to return the common event publication result. |

**Examples**

```TypeScript
import Base from '@ohos.base';

// Callback for common event publication
function publishCB(err:Base.BusinessError) {
    if (err.code) {
        console.error(`publishAsUser failed, code is ${err.code}`);
    } else {
        console.info("publishAsUser");
    }
}

// Specify the user to whom the common event will be published.
let userId = 100;

// Publish a common event.
commonEvent.publishAsUser("event", userId, publishCB);
```


## publishAsUser

```TypeScript
function publishAsUser(
    event: string,
    userId: number,
    options: CommonEventPublishData,
    callback: AsyncCallback<void>
  ): void
```

Publishes a common event with given properties to a specific user. This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [publishAsUser](arkts-basicservices-commoneventmanager-publishasuser-f-sys.md#publishasuser-system-api)( event: string, userId: int, options: CommonEventPublishData, callback: AsyncCallback&lt;void&gt; )

<!--Device-commonEvent-function publishAsUser(    event: string,    userId: number,    options: CommonEventPublishData,    callback: AsyncCallback<void>  ): void--><!--Device-commonEvent-function publishAsUser(    event: string,    userId: number,    options: CommonEventPublishData,    callback: AsyncCallback<void>  ): void-End-->

**System capability:** SystemCapability.Notification.CommonEvent

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | string | Yes | Name of the common event to publish. |
| userId | number | Yes | ID of the user to whom the common event is published. |
| options | [CommonEventPublishData](arkts-basicservices-commoneventpublishdata-commoneventpublishdata-i.md) | Yes | Properties of the common event to publish. |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback used to return the common event publication result. |

**Examples**

```TypeScript
import Base from '@ohos.base';
import CommonEventManager from '@ohos.commonEventManager';

// Information of a common event.
let options:CommonEventManager.CommonEventPublishData = {
    code: 0,             // Initial code of the common event.
    data: "initial data",// Initial data of the common event.
}

// Callback for common event publication
function publishCB(err:Base.BusinessError) {
    if (err.code) {
        console.error(`publishAsUser failed, code is ${err.code}`);
    } else {
        console.info("publishAsUser");
    }
}

// Specify the user to whom the common event will be published.
let userId = 100;

// Publish a common event.
commonEvent.publishAsUser("event", userId, options, publishCB);
```

```TypeScript
import Base from '@ohos.base';
import CommonEventManager from '@ohos.commonEventManager';

let subscriber:CommonEventManager.CommonEventSubscriber;    // Used to save the created subscriber object for subsequent subscription and unsubscription.

// Subscriber information.
let subscribeInfo:CommonEventManager.CommonEventSubscribeInfo = {
    events: ["event"]
};

// Callback for common event subscription.
function subscribeCB(err:Base.BusinessError, data:CommonEventManager.CommonEventData) {
    if (err.code) {
        console.error(`subscribe failed, code is ${err.code}`);
    } else {
        console.info("subscribe " + JSON.stringify(data));
    }
}

// Callback for subscriber creation.
function createCB(err:Base.BusinessError, commonEventSubscriber:CommonEventManager.CommonEventSubscriber) {
    if (err.code) {
        console.error(`createSubscriber failed, code is ${err.code}`);
    } else {
        console.info("createSubscriber");
        subscriber = commonEventSubscriber;
        // Subscribe to a common event.
        commonEvent.subscribe(subscriber, subscribeCB);
    }
}

// Callback for common event unsubscription.
function unsubscribeCB(err:Base.BusinessError) {
    if (err.code) {
        console.error(`unsubscribe failed, code is ${err.code}`);
    } else {
        console.info("unsubscribe");
    }
}

// Create a subscriber.
commonEvent.createSubscriber(subscribeInfo, createCB);

// Unsubscribe from the common event.
commonEvent.unsubscribe(subscriber, unsubscribeCB);
```

