# Client

Manages SSAP client. Before calling a SSAP client method, you must use [createClient](arkts-connectivity-ssap-createclient-f.md#createClient) to create a ssap client instance.

**Since:** 26.0.0

**Deprecated since:** -1

<!--Device-ssap-interface Client--><!--Device-ssap-interface Client-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## Modules to Import

```TypeScript
import { ssap } from '@kit.ConnectivityKit';
```

## callMethod

```TypeScript
callMethod(method: Method): Promise<Method>
```

Calls the method of a server.

**Since:** 26.0.0

**Deprecated since:** -1

**Required permissions:** ohos.permission.ACCESS_NEARLINK

**Model restriction:** This API can be used only in the stage model.

<!--Device-Client-callMethod(method: Method): Promise<Method>--><!--Device-Client-callMethod(method: Method): Promise<Method>-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| method | [Method](arkts-connectivity-ssap-method-i-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[Method](arkts-connectivity-ssap-method-i-sys.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| 36100003 |
| 36100099 |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 36100044 |
| 36100043 |

## offEventNotify

```TypeScript
offEventNotify(callback?: Callback<Event>): void
```

Unsubscribes from event notifications.

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Client-offEventNotify(callback?: Callback<Event>): void--><!--Device-Client-offEventNotify(callback?: Callback<Event>): void-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Event&gt; | No |

## onEventNotify

```TypeScript
onEventNotify(callback: Callback<Event>): void
```

Subscribes to event notifications. This event is accessible only to system applications that granted the ohos.permission.NEARLINK_ACCESS permission.

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Client-onEventNotify(callback: Callback<Event>): void--><!--Device-Client-onEventNotify(callback: Callback<Event>): void-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Event&gt; | Yes |

## readDescriptor

```TypeScript
readDescriptor(descriptor: PropertyDescriptor): Promise<PropertyDescriptor>
```

Reads the descriptor of a server.

**Since:** 26.0.0

**Deprecated since:** -1

**Required permissions:** ohos.permission.ACCESS_NEARLINK

**Model restriction:** This API can be used only in the stage model.

<!--Device-Client-readDescriptor(descriptor: PropertyDescriptor): Promise<PropertyDescriptor>--><!--Device-Client-readDescriptor(descriptor: PropertyDescriptor): Promise<PropertyDescriptor>-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| descriptor | [PropertyDescriptor](arkts-connectivity-ssap-propertydescriptor-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;PropertyDescriptor & gt; |

**Error codes:**

| Error Code ID |
| --- |
| 36100003 |
| 36100099 |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 36100044 |
| 36100043 |

## setPropertyIndication

```TypeScript
setPropertyIndication(property: Property, enable: boolean): Promise<void>
```

Enables or disables indication of a property when value changed.

**Since:** 26.0.0

**Deprecated since:** -1

**Required permissions:** ohos.permission.ACCESS_NEARLINK and ohos.permission.MANAGE_NEARLINK

**Model restriction:** This API can be used only in the stage model.

<!--Device-Client-setPropertyIndication(property: Property, enable: boolean): Promise<void>--><!--Device-Client-setPropertyIndication(property: Property, enable: boolean): Promise<void>-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| property | [Property](arkts-connectivity-ssap-property-i.md) | Yes |
| enable | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| 36100003 |
| 36100099 |
| 36100030 |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 36100044 |
| 36100043 |

## writeDescriptor

```TypeScript
writeDescriptor(descriptor: PropertyDescriptor): Promise<void>
```

Writes the descriptor of a server. This method does not support writing client property configuration descriptors. To write client property configuration descriptors, call [setPropertyNotification](arkts-connectivity-ssap-client-i.md#setPropertyNotification) or [setPropertyIndication](#setPropertyIndication) instead.

**Since:** 26.0.0

**Deprecated since:** -1

**Required permissions:** ohos.permission.ACCESS_NEARLINK

**Model restriction:** This API can be used only in the stage model.

<!--Device-Client-writeDescriptor(descriptor: PropertyDescriptor): Promise<void>--><!--Device-Client-writeDescriptor(descriptor: PropertyDescriptor): Promise<void>-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| descriptor | [PropertyDescriptor](arkts-connectivity-ssap-propertydescriptor-i.md) | Yes |

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
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 36100044 |
| 36100043 |
