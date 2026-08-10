# publishAsUser (System API)

## Modules to Import

```TypeScript
import { commonEventManager } from 'kits/@kit.BasicServicesKit';
```

## publishAsUser

```TypeScript
function publishAsUser(event: string, userId: int, callback: AsyncCallback<void>): void
```

向指定用户发布公共事件。使用callback异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-commonEventManager-function publishAsUser(event: string, userId: int, callback: AsyncCallback<void>): void--><!--Device-commonEventManager-function publishAsUser(event: string, userId: int, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Notification.CommonEvent

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | string | Yes | 表示要发布的公共事件。 |
| userId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 表示指定接收此公共事件的用户ID。 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 回调函数。当公共事件发布成功，err为undefined，否则为错误对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 1500006 | Invalid userId.<br>**Applicable version:** 21 and later |
| 1500007 | Failed to send the message to the common event service. |
| 1500003 | The common event sending frequency too high.<br>**Applicable version:** 20 and later |
| 202 | Permission verification failed. A non-system application calls a system API. |
| 1500008 | Failed to initialize the common event service. |
| 1500009 | Failed to obtain system parameters. |

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
    userId: int,
    options: CommonEventPublishData,
    callback: AsyncCallback<void>
  ): void
```

向指定用户发布公共事件并指定发布信息。使用callback异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-commonEventManager-function publishAsUser(    event: string,    userId: int,    options: CommonEventPublishData,    callback: AsyncCallback<void>  ): void--><!--Device-commonEventManager-function publishAsUser(    event: string,    userId: int,    options: CommonEventPublishData,    callback: AsyncCallback<void>  ): void-End-->

**System capability:** SystemCapability.Notification.CommonEvent

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | string | Yes | 表示要发布的公共事件。 |
| userId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 表示指定接收此公共事件的用户ID。 |
| options | [CommonEventPublishData](arkts-basicservices-commoneventmanager-commoneventpublishdata-t.md) | Yes | 表示发布公共事件的属性。 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 回调函数。当公共事件发布成功，err为undefined，否则为错误对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 1500006 | Invalid userId.<br>**Applicable version:** 21 and later |
| 1500007 | Failed to send the message to the common event service. |
| 1500003 | The common event sending frequency too high.<br>**Applicable version:** 20 and later |
| 202 | Permission verification failed. A non-system application calls a system API. |
| 1500008 | Failed to initialize the common event service. |
| 1500009 | Failed to obtain system parameters. |

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

