# publishAsUser (System API)

## publishAsUser

```TypeScript
function publishAsUser(event: string, userId: number, callback: AsyncCallback<void>): void
```

Publishes a common event to a specific user. This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [@ohos.commonEventManager:commonEventManager.publishAsUser](arkts-basicservices-commoneventmanager-publishasuser-f-sys.md#publishasuser)(event:

<!--Device-commonEvent-function publishAsUser(event: string, userId: number, callback: AsyncCallback<void>): void--><!--Device-commonEvent-function publishAsUser(event: string, userId: number, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Notification.CommonEvent

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | string | Yes |
| userId | number | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## Examples

```TypeScript
import Base from '@ohos.base';

// Callback for common event publication
let publishCallBack = (err:Base.BusinessError) => {
    if (err.code) {
        console.error(`Failed to publishAsUser. Code: ${err.code}, message: ${err.message}`);
    } else {
        console.info('publishAsUser');
    }
}

// Specify the user to whom the common event will be published.
const userId = 100;

// Publish a common event.
commonEvent.publishAsUser('event', userId, publishCallBack);
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

**Substitutes:** [@ohos.commonEventManager:commonEventManager.publishAsUser](arkts-basicservices-commoneventmanager-publishasuser-f-sys.md#publishasuser)(

<!--Device-commonEvent-function publishAsUser(    event: string,    userId: number,    options: CommonEventPublishData,    callback: AsyncCallback<void>  ): void--><!--Device-commonEvent-function publishAsUser(    event: string,    userId: number,    options: CommonEventPublishData,    callback: AsyncCallback<void>  ): void-End-->

**System capability:** SystemCapability.Notification.CommonEvent

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | string | Yes |
| userId | number | Yes |
| options | [CommonEventPublishData](arkts-basicservices-commoneventpublishdata-commoneventpublishdata-i.md) | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## Examples

```TypeScript
import Base from '@ohos.base';
import CommonEventManager from '@ohos.commonEventManager';

// Information of a common event.
let options:CommonEventManager.CommonEventPublishData = {
    code: 0,              // Initial code of the common event.
    data: 'initial data', // Initial data of the common event.
};

// Callback for common event publication
let publishCallBack = (err:Base.BusinessError) => {
    if (err.code) {
        console.error(`Failed to publishAsUser. Code: ${err.code}, message: ${err.message}`);
    } else {
        console.info('publishAsUser');
    }
}

// Specify the user to whom the common event will be published.
let userId = 100;

// Publish a common event.
commonEvent.publishAsUser('event', userId, options, publishCallBack);
```
