# publishAsUser (System API)

## Modules to Import

```TypeScript
import { commonEventManager } from '@kit.BasicServicesKit';
```

## publishAsUser

```TypeScript
function publishAsUser(event: string, userId: number, callback: AsyncCallback<void>): void
```

Publishes a common event to a specified user. This API uses an asynchronous callback to return the result.

**Since:** 23

**Deprecated since:** -1

<!--Device-commonEventManager-function publishAsUser(event: string, userId: int, callback: AsyncCallback<void>): void--><!--Device-commonEventManager-function publishAsUser(event: string, userId: int, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Notification.CommonEvent

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | string | Yes |
| userId | number | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [1500006](../../apis-basic-services-kit/errorcode-CommonEventService.md#1500006-invalid-user-id) |
| [1500007](../../apis-basic-services-kit/errorcode-CommonEventService.md#1500007-failed-to-send-a-request-through-ipc) |
| [1500003](../../apis-basic-services-kit/errorcode-CommonEventService.md#1500003-common-event-sending-frequency-is-too-high) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [1500008](../../apis-basic-services-kit/errorcode-CommonEventService.md#1500008-failed-to-initialize-the-common-event-service) |
| [1500009](../../apis-basic-services-kit/errorcode-CommonEventService.md#1500009-failed-to-obtain-system-parameters) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// Specify the user to whom the common event will be published.
let userId = 100;

// Publish a common event.
try {
    commonEventManager.publishAsUser('event', userId, (err: BusinessError) => {
      if (err) {
        console.error(`publishAsUser failed, code is ${err.code}, message is ${err.message}`);
        return;
      }
      console.info('publishAsUser');
    });
} catch (error) {
    let err: BusinessError = error as BusinessError;
    console.error(`publishAsUser failed, code is ${err.code}, message is ${err.message}`);
}
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

Publishes a common event to a specified user and specifies the information to be published. This API uses an asynchronous callback to return the result.

**Since:** 23

**Deprecated since:** -1

<!--Device-commonEventManager-function publishAsUser(    event: string,    userId: int,    options: CommonEventPublishData,    callback: AsyncCallback<void>  ): void--><!--Device-commonEventManager-function publishAsUser(    event: string,    userId: int,    options: CommonEventPublishData,    callback: AsyncCallback<void>  ): void-End-->

**System capability:** SystemCapability.Notification.CommonEvent

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | string | Yes |
| userId | number | Yes |
| options | [CommonEventPublishData](arkts-basicservices-commoneventmanager-commoneventpublishdata-t.md) | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [1500006](../../apis-basic-services-kit/errorcode-CommonEventService.md#1500006-invalid-user-id) |
| [1500007](../../apis-basic-services-kit/errorcode-CommonEventService.md#1500007-failed-to-send-a-request-through-ipc) |
| [1500003](../../apis-basic-services-kit/errorcode-CommonEventService.md#1500003-common-event-sending-frequency-is-too-high) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [1500008](../../apis-basic-services-kit/errorcode-CommonEventService.md#1500008-failed-to-initialize-the-common-event-service) |
| [1500009](../../apis-basic-services-kit/errorcode-CommonEventService.md#1500009-failed-to-obtain-system-parameters) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// Information of the common event.
let options: commonEventManager.CommonEventPublishData = {
  code: 0,       // Initial code of the common event.
  data: 'initial data', // Initial data of the common event.
};

// Specify the user to whom the common event will be published.
let userId = 100;
// Publish a common event.
try {
  commonEventManager.publishAsUser('event', userId, options, (err: BusinessError) => {
    if (err) {
      console.error(`publishAsUser failed, code is ${err.code}, message is ${err.message}`);
      return;
    }
    console.info('publishAsUser');
  });
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(`publishAsUser failed, code is ${err.code}, message is ${err.message}`);
}
```
