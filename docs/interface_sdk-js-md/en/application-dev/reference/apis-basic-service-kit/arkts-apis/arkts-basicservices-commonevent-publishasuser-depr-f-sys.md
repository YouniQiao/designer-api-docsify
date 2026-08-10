# publishAsUser (System API)

## publishAsUser

```TypeScript
function publishAsUser(event: string, userId: number, callback: AsyncCallback<void>): void
```

以回调的形式向指定用户发布公共事件。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [@ohos.commonEventManager:commonEventManager.publishAsUser](arkts-basicservices-commoneventmanager-publishasuser-f-sys.md#publishasuser)(event:

<!--Device-commonEvent-function publishAsUser(event: string, userId: number, callback: AsyncCallback<void>): void--><!--Device-commonEvent-function publishAsUser(event: string, userId: number, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Notification.CommonEvent

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | string | Yes | 表示要发布的公共事件。 |
| userId | number | Yes | 表示指定向该用户ID发布此公共事件。 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 公共事件发布结果的回调方法。 |

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

以回调形式向指定用户发布公共事件并指定发布信息。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [@ohos.commonEventManager:commonEventManager.publishAsUser](arkts-basicservices-commoneventmanager-publishasuser-f-sys.md#publishasuser)(

<!--Device-commonEvent-function publishAsUser(    event: string,    userId: number,    options: CommonEventPublishData,    callback: AsyncCallback<void>  ): void--><!--Device-commonEvent-function publishAsUser(    event: string,    userId: number,    options: CommonEventPublishData,    callback: AsyncCallback<void>  ): void-End-->

**System capability:** SystemCapability.Notification.CommonEvent

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | string | Yes | 表示要发布的公共事件。 |
| userId | number | Yes | 表示指定向该用户ID发布此公共事件。 |
| options | [CommonEventPublishData](arkts-basicservices-commoneventpublishdata-commoneventpublishdata-i.md) | Yes | 表示发布公共事件的属性。 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 公共事件发布结果的回调方法。 |

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

