# Client

Manages SSAP client. Before calling a SSAP client method,you must use {@link createClient} to create a ssap client instance.

**Since:** 26.0.0

<!--Device-ssap-interface Client--><!--Device-ssap-interface Client-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## Modules to Import

```TypeScript
import { ssap } from 'kits/@kit.ConnectivityKit';
```

## close

```TypeScript
close(): void
```

Closes the client.

**Since:** 26.0.0

**Required permissions:** ohos.permission.ACCESS_NEARLINK

**Model restriction:** This API can be used only in the stage model.

<!--Device-Client-close(): void--><!--Device-Client-close(): void-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**Error codes:**

| Error Code ID |
| --- |
| 36100003 |
| 36100099 |
| [201](../../errorcode-universal.md#201-permission-denied) |

## connect

```TypeScript
connect(): Promise<void>
```

Connects to the server.

**Since:** 26.0.0

**Required permissions:** ohos.permission.ACCESS_NEARLINK

**Model restriction:** This API can be used only in the stage model.

<!--Device-Client-connect(): Promise<void>--><!--Device-Client-connect(): Promise<void>-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| 36100003 |
| 36100099 |
| [201](../../errorcode-universal.md#201-permission-denied) |

## disconnect

```TypeScript
disconnect(): Promise<void>
```

Disconnects from or stops an ongoing connection to a server.

**Since:** 26.0.0

**Required permissions:** ohos.permission.ACCESS_NEARLINK

**Model restriction:** This API can be used only in the stage model.

<!--Device-Client-disconnect(): Promise<void>--><!--Device-Client-disconnect(): Promise<void>-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| 36100003 |
| 36100099 |
| [201](../../errorcode-universal.md#201-permission-denied) |

## getServices

```TypeScript
getServices(): Promise<Service[]>
```

Starts discovering all services on server.

**Since:** 26.0.0

**Required permissions:** ohos.permission.ACCESS_NEARLINK

**Model restriction:** This API can be used only in the stage model.

<!--Device-Client-getServices(): Promise<Service[]>--><!--Device-Client-getServices(): Promise<Service[]>-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Service[]&gt; |

**Error codes:**

| Error Code ID |
| --- |
| 36100003 |
| 36100099 |
| [201](../../errorcode-universal.md#201-permission-denied) |

## offConnectionStateChange

```TypeScript
offConnectionStateChange(callback?: Callback<ConnectionChangeState>): void
```

Unsubscribes from client connection state changed events.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-Client-offConnectionStateChange(callback?: Callback<ConnectionChangeState>): void--><!--Device-Client-offConnectionStateChange(callback?: Callback<ConnectionChangeState>): void-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;ConnectionChangeState&gt; | No |

## offMtuChange

```TypeScript
offMtuChange(callback?: Callback<number>): void
```

Unsubscribes from MTU changed events.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-Client-offMtuChange(callback?: Callback<int>): void--><!--Device-Client-offMtuChange(callback?: Callback<int>): void-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | No |

## offPropertyChange

```TypeScript
offPropertyChange(callback?: Callback<Property>): void
```

Unsubscribe property value changed event.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-Client-offPropertyChange(callback?: Callback<Property>): void--><!--Device-Client-offPropertyChange(callback?: Callback<Property>): void-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Property&gt; | No |

## onConnectionStateChange

```TypeScript
onConnectionStateChange(callback: Callback<ConnectionChangeState>): void
```

Subscribes to client connection state changed events.

This event is accessible only to applications that granted the ohos.permission.NEARLINK_ACCESS permission.If the application is granted the ohos.permission.GET_NEARLINK_PEER_MAC permission,the callback returns the real device address; otherwise, a random device address is returned.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-Client-onConnectionStateChange(callback: Callback<ConnectionChangeState>): void--><!--Device-Client-onConnectionStateChange(callback: Callback<ConnectionChangeState>): void-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;ConnectionChangeState&gt; | Yes |

## onMtuChange

```TypeScript
onMtuChange(callback: Callback<number>): void
```

Subscribes to MTU changed events.

This event is accessible only to applications that granted the ohos.permission.NEARLINK_ACCESS permission.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-Client-onMtuChange(callback: Callback<int>): void--><!--Device-Client-onMtuChange(callback: Callback<int>): void-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | Yes |

## onPropertyChange

```TypeScript
onPropertyChange(callback: Callback<Property>): void
```

Subscribe property value changed event.

This event is accessible only to applications that granted the ohos.permission.NEARLINK_ACCESS permission.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-Client-onPropertyChange(callback: Callback<Property>): void--><!--Device-Client-onPropertyChange(callback: Callback<Property>): void-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Property&gt; | Yes |

## readProperty

```TypeScript
readProperty(property: Property): Promise<Property>
```

Reads the property of a server.

**Since:** 26.0.0

**Required permissions:** ohos.permission.ACCESS_NEARLINK

**Model restriction:** This API can be used only in the stage model.

<!--Device-Client-readProperty(property: Property): Promise<Property>--><!--Device-Client-readProperty(property: Property): Promise<Property>-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| property | [Property](arkts-connectivity-ssap-property-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Property&gt; |

**Error codes:**

| Error Code ID |
| --- |
| 36100003 |
| 36100099 |
| [201](../../errorcode-universal.md#201-permission-denied) |
| 36100044 |
| 36100043 |

## requestMtuSize

```TypeScript
requestMtuSize(mtu: number): Promise<void>
```

Negotiate the MTU size with server.The negotiation result needs to be obtained by subscribing to MTU event.

**Since:** 26.0.0

**Required permissions:** ohos.permission.ACCESS_NEARLINK

**Model restriction:** This API can be used only in the stage model.

<!--Device-Client-requestMtuSize(mtu: int): Promise<void>--><!--Device-Client-requestMtuSize(mtu: int): Promise<void>-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mtu | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| 36100003 |
| 36100099 |
| [201](../../errorcode-universal.md#201-permission-denied) |

## setPropertyNotification

```TypeScript
setPropertyNotification(property: Property, enable: boolean): Promise<void>
```

Enables or disables notification of a property when value changed.

**Since:** 26.0.0

**Required permissions:** ohos.permission.ACCESS_NEARLINK

**Model restriction:** This API can be used only in the stage model.

<!--Device-Client-setPropertyNotification(property: Property, enable: boolean): Promise<void>--><!--Device-Client-setPropertyNotification(property: Property, enable: boolean): Promise<void>-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| property | [Property](arkts-connectivity-ssap-property-i.md) | Yes |
| enable | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| 36100003 |
| 36100099 |
| [201](../../errorcode-universal.md#201-permission-denied) |
| 36100044 |
| 36100043 |

## writeProperty

```TypeScript
writeProperty(property: Property, writeType: PropertyWriteType): Promise<void>
```

Writes the property of a server.

**Since:** 26.0.0

**Required permissions:** ohos.permission.ACCESS_NEARLINK

**Model restriction:** This API can be used only in the stage model.

<!--Device-Client-writeProperty(property: Property, writeType: PropertyWriteType): Promise<void>--><!--Device-Client-writeProperty(property: Property, writeType: PropertyWriteType): Promise<void>-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| property | [Property](arkts-connectivity-ssap-property-i.md) | Yes |
| writeType | [PropertyWriteType](arkts-connectivity-ssap-propertywritetype-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| 36100003 |
| 36100099 |
| [201](../../errorcode-universal.md#201-permission-denied) |
| 36100044 |
| 36100043 |
