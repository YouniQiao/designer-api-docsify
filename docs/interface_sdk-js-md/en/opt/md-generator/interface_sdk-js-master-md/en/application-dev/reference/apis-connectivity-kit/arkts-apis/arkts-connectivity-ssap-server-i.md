# Server

Manages SSAP server. Before calling a SSAP server method, you must use [createServer](arkts-connectivity-ssap-createserver-f.md#createserver) to create a SSAP server instance.

**Since:** 26.0.0

<!--Device-ssap-interface Server--><!--Device-ssap-interface Server-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## Modules to Import

```TypeScript
```

## addService

```TypeScript
addService(service: Service): void
```

Adds a SSAP service.

**Since:** 26.0.0

**Required permissions:** ohos.permission.ACCESS_NEARLINK

**Model restriction:** This API can be used only in the stage model.

<!--Device-Server-addService(service: Service): void--><!--Device-Server-addService(service: Service): void-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [service](../../apis-calendar-kit/arkts-apis/arkts-calendar-calendarmanager-event-i.md) | [Service](arkts-connectivity-ssap-service-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 36100003 |
| 36100099 |
| [201](../../errorcode-universal.md#201-permission-denied) |
| 36100044 |
| 36100043 |

## close

```TypeScript
close(): void
```

Closes this {@code Server} object and unregisters its callbacks.

**Since:** 26.0.0

**Required permissions:** ohos.permission.ACCESS_NEARLINK

**Model restriction:** This API can be used only in the stage model.

<!--Device-Server-close(): void--><!--Device-Server-close(): void-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**Error codes:**

| Error Code ID |
| --- |
| 36100003 |
| 36100099 |
| [201](../../errorcode-universal.md#201-permission-denied) |

## notifyPropertyChanged

```TypeScript
notifyPropertyChanged(address: string, property: Property): Promise<void>
```

Notifies the client that the value of a property on the server has changed.

**Since:** 26.0.0

**Required permissions:** ohos.permission.ACCESS_NEARLINK

**Model restriction:** This API can be used only in the stage model.

<!--Device-Server-notifyPropertyChanged(address: string, property: Property): Promise<void>--><!--Device-Server-notifyPropertyChanged(address: string, property: Property): Promise<void>-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| address | string | Yes |
| property | [Property](arkts-connectivity-ssap-property-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| 36100003 |
| 36100099 |
| [201](../../errorcode-universal.md#201-permission-denied) |
| 36100044 |
| 36100043 |
| 36100041 |

## offConnectionStateChange

```TypeScript
offConnectionStateChange(callback?: Callback<ConnectionChangeState>): void
```

Unsubscribes from server connection state changed events.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-Server-offConnectionStateChange(callback?: Callback<ConnectionChangeState>): void--><!--Device-Server-offConnectionStateChange(callback?: Callback<ConnectionChangeState>): void-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[ConnectionChangeState](arkts-connectivity-ssap-connectionchangestate-i.md)&gt; | No |

## offMtuChange

```TypeScript
offMtuChange(callback?: Callback<number>): void
```

Unsubscribes from MTU changed events.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-Server-offMtuChange(callback?: Callback<int>): void--><!--Device-Server-offMtuChange(callback?: Callback<int>): void-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | No |

## offPropertyRead

```TypeScript
offPropertyRead(callback?: Callback<PropertyReadRequest>): void
```

Unsubscribes from property read events from the client.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-Server-offPropertyRead(callback?: Callback<PropertyReadRequest>): void--><!--Device-Server-offPropertyRead(callback?: Callback<PropertyReadRequest>): void-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[PropertyReadRequest](arkts-connectivity-ssap-propertyreadrequest-i.md)&gt; | No |

## offPropertyWrite

```TypeScript
offPropertyWrite(callback?: Callback<PropertyWriteRequest>): void
```

Unsubscribes from property write events from the client.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-Server-offPropertyWrite(callback?: Callback<PropertyWriteRequest>): void--><!--Device-Server-offPropertyWrite(callback?: Callback<PropertyWriteRequest>): void-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[PropertyWriteRequest](arkts-connectivity-ssap-propertywriterequest-i.md)&gt; | No |

## onConnectionStateChange

```TypeScript
onConnectionStateChange(callback: Callback<ConnectionChangeState>): void
```

Subscribes to server connection state changed events. This event is accessible only to applications that granted the ohos.permission.NEARLINK_ACCESS permission. If the application is granted the ohos.permission.GET_NEARLINK_PEER_MAC permission, the callback returns the real device address; otherwise, a random device address is returned.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-Server-onConnectionStateChange(callback: Callback<ConnectionChangeState>): void--><!--Device-Server-onConnectionStateChange(callback: Callback<ConnectionChangeState>): void-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[ConnectionChangeState](arkts-connectivity-ssap-connectionchangestate-i.md)&gt; | Yes |

## onMtuChange

```TypeScript
onMtuChange(callback: Callback<number>): void
```

Subscribes to MTU changed events. This event is accessible only to applications that granted the ohos.permission.NEARLINK_ACCESS permission.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-Server-onMtuChange(callback: Callback<int>): void--><!--Device-Server-onMtuChange(callback: Callback<int>): void-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | Yes |

## onPropertyRead

```TypeScript
onPropertyRead(callback: Callback<PropertyReadRequest>): void
```

Subscribes to property read events from the client. This event is accessible only to applications that granted the ohos.permission.NEARLINK_ACCESS permission. If the application is granted the ohos.permission.GET_NEARLINK_PEER_MAC permission, the callback returns the real device address; otherwise, a random device address is returned.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-Server-onPropertyRead(callback: Callback<PropertyReadRequest>): void--><!--Device-Server-onPropertyRead(callback: Callback<PropertyReadRequest>): void-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[PropertyReadRequest](arkts-connectivity-ssap-propertyreadrequest-i.md)&gt; | Yes |

## onPropertyWrite

```TypeScript
onPropertyWrite(callback: Callback<PropertyWriteRequest>): void
```

Subscribes to property write events from the client. This event is accessible only to applications that granted the ohos.permission.NEARLINK_ACCESS permission. If the application is granted the ohos.permission.GET_NEARLINK_PEER_MAC permission, the callback returns the real device address; otherwise, a random device address is returned.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-Server-onPropertyWrite(callback: Callback<PropertyWriteRequest>): void--><!--Device-Server-onPropertyWrite(callback: Callback<PropertyWriteRequest>): void-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[PropertyWriteRequest](arkts-connectivity-ssap-propertywriterequest-i.md)&gt; | Yes |

## removeService

```TypeScript
removeService(serviceUuid: string): void
```

Removes a specific SSAP service.

**Since:** 26.0.0

**Required permissions:** ohos.permission.ACCESS_NEARLINK

**Model restriction:** This API can be used only in the stage model.

<!--Device-Server-removeService(serviceUuid: string): void--><!--Device-Server-removeService(serviceUuid: string): void-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| serviceUuid | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 36100003 |
| 36100099 |
| [201](../../errorcode-universal.md#201-permission-denied) |
| 36100044 |
| 36100043 |

## sendResponse

```TypeScript
sendResponse(response: ServerResponse): void
```

Responds to read or write requests from the client.

**Since:** 26.0.0

**Required permissions:** ohos.permission.ACCESS_NEARLINK

**Model restriction:** This API can be used only in the stage model.

<!--Device-Server-sendResponse(response: ServerResponse): void--><!--Device-Server-sendResponse(response: ServerResponse): void-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| response | [ServerResponse](arkts-connectivity-bluetoothmanager-serverresponse-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 36100003 |
| 36100099 |
| [201](../../errorcode-universal.md#201-permission-denied) |
| 36100041 |
