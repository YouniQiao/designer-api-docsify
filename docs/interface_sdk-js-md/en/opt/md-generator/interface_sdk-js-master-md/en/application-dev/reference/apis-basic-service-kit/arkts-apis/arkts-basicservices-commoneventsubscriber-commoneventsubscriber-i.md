# CommonEventSubscriber

Represents the subscriber of a common event. The **CommonEventSubscriber** module provides the capabilities for processing ordered common events, including obtaining and setting the data and code transferred by events, checking whether the current common event is an ordered or sticky event, terminating an ordered common event or clearing the termination status, ending the processing of the current ordered common event, and obtaining subscription information of a subscriber. This module is applicable to data processing and process control of the received common event by the subscriber.

**Since:** 7

<!--Device-unnamed-export interface CommonEventSubscriber--><!--Device-unnamed-export interface CommonEventSubscriber-End-->

**System capability:** SystemCapability.Notification.CommonEvent

## abortCommonEvent

```TypeScript
abortCommonEvent(callback: AsyncCallback<void>): void
```

Aborts an ordered common event. This API is used with   
[finishCommonEvent](arkts-basicservices-commoneventsubscriber-commoneventsubscriber-i.md#finishcommonevent). After the abort,the common event is not sent to the next subscriber. This API uses an asynchronous callback to return the result.

**Since:** 7

<!--Device-CommonEventSubscriber-abortCommonEvent(callback: AsyncCallback<void>): void--><!--Device-CommonEventSubscriber-abortCommonEvent(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Notification.CommonEvent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## abortCommonEvent

```TypeScript
abortCommonEvent(): Promise<void>
```

Aborts an ordered common event. This API is used with  
[finishCommonEvent](arkts-basicservices-commoneventsubscriber-commoneventsubscriber-i.md#finishcommonevent). After the abort,the common event is not sent to the next subscriber. This API uses a promise to return the result.

**Since:** 7

<!--Device-CommonEventSubscriber-abortCommonEvent(): Promise<void>--><!--Device-CommonEventSubscriber-abortCommonEvent(): Promise<void>-End-->

**System capability:** SystemCapability.Notification.CommonEvent

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

## abortCommonEventSync

```TypeScript
abortCommonEventSync(): void
```

Aborts an ordered common event when used with  
[finishCommonEvent](arkts-basicservices-commoneventsubscriber-commoneventsubscriber-i.md#finishcommonevent). With the abort state, the common event is not sent to the next subscriber. This API returns the result synchronously.

**Since:** 10

<!--Device-CommonEventSubscriber-abortCommonEventSync(): void--><!--Device-CommonEventSubscriber-abortCommonEventSync(): void-End-->

**System capability:** SystemCapability.Notification.CommonEvent

## clearAbortCommonEvent

```TypeScript
clearAbortCommonEvent(callback: AsyncCallback<void>): void
```

Clears the abort state of an ordered common event. Use this API together with   
[finishCommonEvent](arkts-basicservices-commoneventsubscriber-commoneventsubscriber-i.md#finishcommonevent), and the common event can be passed to the next subscriber. This API uses an asynchronous callback to return the result.

**Since:** 7

<!--Device-CommonEventSubscriber-clearAbortCommonEvent(callback: AsyncCallback<void>): void--><!--Device-CommonEventSubscriber-clearAbortCommonEvent(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Notification.CommonEvent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## clearAbortCommonEvent

```TypeScript
clearAbortCommonEvent(): Promise<void>
```

Clears the abort state of this ordered common event. Use this API together with   
[finishCommonEvent](arkts-basicservices-commoneventsubscriber-commoneventsubscriber-i.md#finishcommonevent), and the common event can be passed to the next subscriber. This API uses a promise to return the result.

**Since:** 7

<!--Device-CommonEventSubscriber-clearAbortCommonEvent(): Promise<void>--><!--Device-CommonEventSubscriber-clearAbortCommonEvent(): Promise<void>-End-->

**System capability:** SystemCapability.Notification.CommonEvent

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

## clearAbortCommonEventSync

```TypeScript
clearAbortCommonEventSync(): void
```

Clears the abort state of an ordered common event when used with  
[finishCommonEvent](arkts-basicservices-commoneventsubscriber-commoneventsubscriber-i.md#finishcommonevent). After the clearance, the common event is sent to the next subscriber. This API returns the result synchronously.

**Since:** 10

<!--Device-CommonEventSubscriber-clearAbortCommonEventSync(): void--><!--Device-CommonEventSubscriber-clearAbortCommonEventSync(): void-End-->

**System capability:** SystemCapability.Notification.CommonEvent

## finishCommonEvent

```TypeScript
finishCommonEvent(callback: AsyncCallback<void>): void
```

Finishes this ordered common event. This API uses an asynchronous callback to return the result.

**Since:** 9

<!--Device-CommonEventSubscriber-finishCommonEvent(callback: AsyncCallback<void>): void--><!--Device-CommonEventSubscriber-finishCommonEvent(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Notification.CommonEvent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## finishCommonEvent

```TypeScript
finishCommonEvent(): Promise<void>
```

Finishes this ordered common event. This API uses a promise to return the result.

**Since:** 9

<!--Device-CommonEventSubscriber-finishCommonEvent(): Promise<void>--><!--Device-CommonEventSubscriber-finishCommonEvent(): Promise<void>-End-->

**System capability:** SystemCapability.Notification.CommonEvent

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

## getAbortCommonEvent

```TypeScript
getAbortCommonEvent(callback: AsyncCallback<boolean>): void
```

Checks whether this ordered common event should be aborted. This API uses an asynchronous callback to return the result.

**Since:** 7

<!--Device-CommonEventSubscriber-getAbortCommonEvent(callback: AsyncCallback<boolean>): void--><!--Device-CommonEventSubscriber-getAbortCommonEvent(callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.Notification.CommonEvent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## getAbortCommonEvent

```TypeScript
getAbortCommonEvent(): Promise<boolean>
```

Checks whether this ordered common event should be aborted. This API uses a promise to return the result.

**Since:** 7

<!--Device-CommonEventSubscriber-getAbortCommonEvent(): Promise<boolean>--><!--Device-CommonEventSubscriber-getAbortCommonEvent(): Promise<boolean>-End-->

**System capability:** SystemCapability.Notification.CommonEvent

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;boolean&gt; |

## getAbortCommonEventSync

```TypeScript
getAbortCommonEventSync(): boolean
```

Checks whether an ordered common event is aborted. This API returns the result synchronously.

**Since:** 10

<!--Device-CommonEventSubscriber-getAbortCommonEventSync(): boolean--><!--Device-CommonEventSubscriber-getAbortCommonEventSync(): boolean-End-->

**System capability:** SystemCapability.Notification.CommonEvent

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## getCode

```TypeScript
getCode(callback: AsyncCallback<number>): void
```

Obtains the result code of an ordered common event. This API uses an asynchronous callback to return the result.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-CommonEventSubscriber-getCode(callback: AsyncCallback<int>): void--><!--Device-CommonEventSubscriber-getCode(callback: AsyncCallback<int>): void-End-->

**System capability:** SystemCapability.Notification.CommonEvent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## getCode

```TypeScript
getCode(): Promise<number>
```

Obtains the result code of an ordered common event. This API uses a promise to return the result.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-CommonEventSubscriber-getCode(): Promise<int>--><!--Device-CommonEventSubscriber-getCode(): Promise<int>-End-->

**System capability:** SystemCapability.Notification.CommonEvent

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;number&gt; |

## getCodeSync

```TypeScript
getCodeSync(): number
```

Obtains the result code of an ordered common event. This API returns the result synchronously.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-CommonEventSubscriber-getCodeSync(): int--><!--Device-CommonEventSubscriber-getCodeSync(): int-End-->

**System capability:** SystemCapability.Notification.CommonEvent

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## getData

```TypeScript
getData(callback: AsyncCallback<string>): void
```

Obtains the data of an ordered common event. This API uses an asynchronous callback to return the result.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-CommonEventSubscriber-getData(callback: AsyncCallback<string>): void--><!--Device-CommonEventSubscriber-getData(callback: AsyncCallback<string>): void-End-->

**System capability:** SystemCapability.Notification.CommonEvent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## getData

```TypeScript
getData(): Promise<string>
```

Obtains the data of an ordered common event. This API uses a promise to return the result.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-CommonEventSubscriber-getData(): Promise<string>--><!--Device-CommonEventSubscriber-getData(): Promise<string>-End-->

**System capability:** SystemCapability.Notification.CommonEvent

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;string&gt; |

## getDataSync

```TypeScript
getDataSync(): string
```

Obtains the data of an ordered common event. This API returns the result synchronously.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-CommonEventSubscriber-getDataSync(): string--><!--Device-CommonEventSubscriber-getDataSync(): string-End-->

**System capability:** SystemCapability.Notification.CommonEvent

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## getSubscribeInfo

```TypeScript
getSubscribeInfo(callback: AsyncCallback<CommonEventSubscribeInfo>): void
```

Obtains the subscriber information. This API uses an asynchronous callback to return the result.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-CommonEventSubscriber-getSubscribeInfo(callback: AsyncCallback<CommonEventSubscribeInfo>): void--><!--Device-CommonEventSubscriber-getSubscribeInfo(callback: AsyncCallback<CommonEventSubscribeInfo>): void-End-->

**System capability:** SystemCapability.Notification.CommonEvent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;[CommonEventSubscribeInfo](arkts-basicservices-commoneventsubscribeinfo-commoneventsubscribeinfo-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## getSubscribeInfo

```TypeScript
getSubscribeInfo(): Promise<CommonEventSubscribeInfo>
```

Obtains the subscriber information. This API uses a promise to return the result.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-CommonEventSubscriber-getSubscribeInfo(): Promise<CommonEventSubscribeInfo>--><!--Device-CommonEventSubscriber-getSubscribeInfo(): Promise<CommonEventSubscribeInfo>-End-->

**System capability:** SystemCapability.Notification.CommonEvent

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[CommonEventSubscribeInfo](arkts-basicservices-commoneventsubscribeinfo-commoneventsubscribeinfo-i.md)&gt; |

## getSubscribeInfoSync

```TypeScript
getSubscribeInfoSync(): CommonEventSubscribeInfo
```

Obtains the subscriber information. This API returns the result synchronously.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-CommonEventSubscriber-getSubscribeInfoSync(): CommonEventSubscribeInfo--><!--Device-CommonEventSubscriber-getSubscribeInfoSync(): CommonEventSubscribeInfo-End-->

**System capability:** SystemCapability.Notification.CommonEvent

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [CommonEventSubscribeInfo](arkts-basicservices-commoneventsubscribeinfo-commoneventsubscribeinfo-i.md) |

## isOrderedCommonEvent

```TypeScript
isOrderedCommonEvent(callback: AsyncCallback<boolean>): void
```

Checks whether the current common event is an ordered common event. This API uses an asynchronous callback to return the result.

**Since:** 7

<!--Device-CommonEventSubscriber-isOrderedCommonEvent(callback: AsyncCallback<boolean>): void--><!--Device-CommonEventSubscriber-isOrderedCommonEvent(callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.Notification.CommonEvent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## isOrderedCommonEvent

```TypeScript
isOrderedCommonEvent(): Promise<boolean>
```

Checks whether the current common event is an ordered common event. This API uses a promise to return the result.

**Since:** 7

<!--Device-CommonEventSubscriber-isOrderedCommonEvent(): Promise<boolean>--><!--Device-CommonEventSubscriber-isOrderedCommonEvent(): Promise<boolean>-End-->

**System capability:** SystemCapability.Notification.CommonEvent

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;boolean&gt; |

## isOrderedCommonEventSync

```TypeScript
isOrderedCommonEventSync(): boolean
```

Checks whether a common event is an ordered one. This API returns the result synchronously.

**Since:** 10

<!--Device-CommonEventSubscriber-isOrderedCommonEventSync(): boolean--><!--Device-CommonEventSubscriber-isOrderedCommonEventSync(): boolean-End-->

**System capability:** SystemCapability.Notification.CommonEvent

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## isStickyCommonEvent

```TypeScript
isStickyCommonEvent(callback: AsyncCallback<boolean>): void
```

Checks whether the current common event is a sticky common event. This API uses an asynchronous callback to return the result.

**Since:** 7

<!--Device-CommonEventSubscriber-isStickyCommonEvent(callback: AsyncCallback<boolean>): void--><!--Device-CommonEventSubscriber-isStickyCommonEvent(callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.Notification.CommonEvent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## isStickyCommonEvent

```TypeScript
isStickyCommonEvent(): Promise<boolean>
```

Checks whether the current common event is a sticky common event. This API uses a promise to return the result.

**Since:** 7

<!--Device-CommonEventSubscriber-isStickyCommonEvent(): Promise<boolean>--><!--Device-CommonEventSubscriber-isStickyCommonEvent(): Promise<boolean>-End-->

**System capability:** SystemCapability.Notification.CommonEvent

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;boolean&gt; |

## isStickyCommonEventSync

```TypeScript
isStickyCommonEventSync(): boolean
```

Checks whether the current common event is a sticky common event. This API returns the result synchronously.

**Since:** 10

<!--Device-CommonEventSubscriber-isStickyCommonEventSync(): boolean--><!--Device-CommonEventSubscriber-isStickyCommonEventSync(): boolean-End-->

**System capability:** SystemCapability.Notification.CommonEvent

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## setCode

```TypeScript
setCode(code: number, callback: AsyncCallback<void>): void
```

Sets the code of an ordered common event. This API uses an asynchronous callback to return the result.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-CommonEventSubscriber-setCode(code: int, callback: AsyncCallback<void>): void--><!--Device-CommonEventSubscriber-setCode(code: int, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Notification.CommonEvent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| code | number | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## setCode

```TypeScript
setCode(code: number): Promise<void>
```

Sets the result code of an ordered common event. This API uses a promise to return the result.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-CommonEventSubscriber-setCode(code: int): Promise<void>--><!--Device-CommonEventSubscriber-setCode(code: int): Promise<void>-End-->

**System capability:** SystemCapability.Notification.CommonEvent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| code | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## setCodeAndData

```TypeScript
setCodeAndData(code: number, data: string, callback: AsyncCallback<void>): void
```

Sets the result code and data of an ordered common event. This API uses an asynchronous callback to return the result.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-CommonEventSubscriber-setCodeAndData(code: int, data: string, callback: AsyncCallback<void>): void--><!--Device-CommonEventSubscriber-setCodeAndData(code: int, data: string, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Notification.CommonEvent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| code | number | Yes |
| data | string | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## setCodeAndData

```TypeScript
setCodeAndData(code: number, data: string): Promise<void>
```

Sets the result code and data of an ordered common event. This API uses a promise to return the result.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-CommonEventSubscriber-setCodeAndData(code: int, data: string): Promise<void>--><!--Device-CommonEventSubscriber-setCodeAndData(code: int, data: string): Promise<void>-End-->

**System capability:** SystemCapability.Notification.CommonEvent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| code | number | Yes |
| data | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## setCodeAndDataSync

```TypeScript
setCodeAndDataSync(code: number, data: string): void
```

Sets the code and data of an ordered common event. This API returns the result synchronously.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-CommonEventSubscriber-setCodeAndDataSync(code: int, data: string): void--><!--Device-CommonEventSubscriber-setCodeAndDataSync(code: int, data: string): void-End-->

**System capability:** SystemCapability.Notification.CommonEvent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| code | number | Yes |
| data | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## setCodeSync

```TypeScript
setCodeSync(code: number): void
```

Sets the result code of an ordered common event. This API returns the result synchronously.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-CommonEventSubscriber-setCodeSync(code: int): void--><!--Device-CommonEventSubscriber-setCodeSync(code: int): void-End-->

**System capability:** SystemCapability.Notification.CommonEvent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| code | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## setData

```TypeScript
setData(data: string, callback: AsyncCallback<void>): void
```

Sets the data of an ordered common event. This API uses an asynchronous callback to return the result.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-CommonEventSubscriber-setData(data: string, callback: AsyncCallback<void>): void--><!--Device-CommonEventSubscriber-setData(data: string, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Notification.CommonEvent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| data | string | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## setData

```TypeScript
setData(data: string): Promise<void>
```

Sets the result data of an ordered common event. This API uses a promise to return the result.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-CommonEventSubscriber-setData(data: string): Promise<void>--><!--Device-CommonEventSubscriber-setData(data: string): Promise<void>-End-->

**System capability:** SystemCapability.Notification.CommonEvent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| data | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## setDataSync

```TypeScript
setDataSync(data: string): void
```

Sets the result data of an ordered common event. This API returns the result synchronously.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-CommonEventSubscriber-setDataSync(data: string): void--><!--Device-CommonEventSubscriber-setDataSync(data: string): void-End-->

**System capability:** SystemCapability.Notification.CommonEvent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| data | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
