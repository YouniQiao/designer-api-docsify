# Session

A **Session** instance indicates a session created on an SE **Reader** instance. You can use [Reader.openSession](arkts-connectivity-omapi-reader-i.md#opensession) to obtain a **Session** instance.

**Since:** 10

**System capability:** SystemCapability.Communication.SecureElement

## Modules to Import

```TypeScript
import { omapi } from 'kits/@kit.ConnectivityKit';
```

## close

```TypeScript
close(): void
```

Closes the session with the SE. All channels opened by this session will be closed.

**Since:** 10

**System capability:** SystemCapability.Communication.SecureElement

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [3300101](../errorcode-se.md#3300101-abnormal-se-service-status) |

## closeChannels

```TypeScript
closeChannels(): void
```

Closes all channels opened on this session.

**Since:** 10

**System capability:** SystemCapability.Communication.SecureElement

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [3300101](../errorcode-se.md#3300101-abnormal-se-service-status) |

## getATR

```TypeScript
getATR(): number[]
```

Obtains the Answer to Reset (ATR) of this SE. If the ATR of this SE is not available, an empty array will be returned.

**Since:** 10

**System capability:** SystemCapability.Communication.SecureElement

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number[] |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [3300101](../errorcode-se.md#3300101-abnormal-se-service-status) |

## getReader

```TypeScript
getReader(): Reader
```

Obtains the reader that provides this session.

**Since:** 10

**System capability:** SystemCapability.Communication.SecureElement

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Reader](arkts-connectivity-omapi-reader-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |

## isClosed

```TypeScript
isClosed(): boolean
```

Check if this session is closed.

**Since:** 10

**System capability:** SystemCapability.Communication.SecureElement

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |

## openBasicChannel

```TypeScript
openBasicChannel(aid: number[]): Promise<Channel>
```

Opens a basic channel, as defined in ISO/IEC 7816-4. If the SE cannot provide the basic channel or the application does not have the permission to access the SE, null is returned. This API uses a promise to return the result.

**Since:** 10

**System capability:** SystemCapability.Communication.SecureElement

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| aid | number[] | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[Channel](arkts-connectivity-omapi-channel-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [3300101](../errorcode-se.md#3300101-abnormal-se-service-status) |
| [3300102](../errorcode-se.md#3300102-failed-to-find-the-desired-se) |
| [3300103](../errorcode-se.md#3300103-failed-to-obtain-the-access-rule) |
| [3300104](../errorcode-se.md#3300104-se-chip-io-exception) |

## openBasicChannel

```TypeScript
openBasicChannel(aid: number[], callback: AsyncCallback<Channel>): void
```

Opens a basic channel, as defined in ISO/IEC 7816-4. If the SE cannot provide the basic channel or the application does not have the permission to access the SE, null is returned. This API uses an asynchronous callback to return the result.

**Since:** 10

**System capability:** SystemCapability.Communication.SecureElement

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| aid | number[] | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[Channel](arkts-connectivity-omapi-channel-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [3300101](../errorcode-se.md#3300101-abnormal-se-service-status) |
| [3300102](../errorcode-se.md#3300102-failed-to-find-the-desired-se) |
| [3300103](../errorcode-se.md#3300103-failed-to-obtain-the-access-rule) |
| [3300104](../errorcode-se.md#3300104-se-chip-io-exception) |

## openBasicChannel

```TypeScript
openBasicChannel(aid: number[], p2: number): Promise<Channel>
```

Opens a basic channel, as defined in ISO/IEC 7816-4. If the SE cannot provide the basic channel or the application does not have the permission to access the SE, null is returned. This API uses a promise to return the result.

**Since:** 10

**System capability:** SystemCapability.Communication.SecureElement

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| aid | number[] | Yes |
| p2 | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[Channel](arkts-connectivity-omapi-channel-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [3300101](../errorcode-se.md#3300101-abnormal-se-service-status) |
| [3300102](../errorcode-se.md#3300102-failed-to-find-the-desired-se) |
| [3300103](../errorcode-se.md#3300103-failed-to-obtain-the-access-rule) |
| [3300104](../errorcode-se.md#3300104-se-chip-io-exception) |

## openBasicChannel

```TypeScript
openBasicChannel(aid: number[], p2: number, callback: AsyncCallback<Channel>): void
```

Opens a basic channel, as defined in ISO/IEC 7816-4. If the SE cannot provide the basic channel or the application does not have the permission to access the SE, null is returned. This API uses an asynchronous callback to return the result.

**Since:** 10

**System capability:** SystemCapability.Communication.SecureElement

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| aid | number[] | Yes |
| p2 | number | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[Channel](arkts-connectivity-omapi-channel-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [3300101](../errorcode-se.md#3300101-abnormal-se-service-status) |
| [3300102](../errorcode-se.md#3300102-failed-to-find-the-desired-se) |
| [3300103](../errorcode-se.md#3300103-failed-to-obtain-the-access-rule) |
| [3300104](../errorcode-se.md#3300104-se-chip-io-exception) |

## openLogicalChannel

```TypeScript
openLogicalChannel(aid: number[]): Promise<Channel>
```

Opens a logical channel, as defined in ISO/IEC 7816-4. If the SE cannot provide the logical channel or the application does not have the permission to access the SE, null is returned. This API uses a promise to return the result.

**Since:** 10

**System capability:** SystemCapability.Communication.SecureElement

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| aid | number[] | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[Channel](arkts-connectivity-omapi-channel-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [3300101](../errorcode-se.md#3300101-abnormal-se-service-status) |
| [3300102](../errorcode-se.md#3300102-failed-to-find-the-desired-se) |
| [3300103](../errorcode-se.md#3300103-failed-to-obtain-the-access-rule) |
| [3300104](../errorcode-se.md#3300104-se-chip-io-exception) |

## openLogicalChannel

```TypeScript
openLogicalChannel(aid: number[], callback: AsyncCallback<Channel>): void
```

Opens a logical channel, as defined in ISO/IEC 7816-4. If the SE cannot provide the logical channel or the application does not have the permission to access the SE, null is returned. This API uses an asynchronous callback to return the result.

**Since:** 10

**System capability:** SystemCapability.Communication.SecureElement

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| aid | number[] | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[Channel](arkts-connectivity-omapi-channel-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [3300101](../errorcode-se.md#3300101-abnormal-se-service-status) |
| [3300102](../errorcode-se.md#3300102-failed-to-find-the-desired-se) |
| [3300103](../errorcode-se.md#3300103-failed-to-obtain-the-access-rule) |
| [3300104](../errorcode-se.md#3300104-se-chip-io-exception) |

## openLogicalChannel

```TypeScript
openLogicalChannel(aid: number[], p2: number): Promise<Channel>
```

Opens a logical channel, as defined in ISO/IEC 7816-4. If the SE cannot provide the logical channel or the application does not have the permission to access the SE, null is returned. This API uses a promise to return the result.

**Since:** 10

**System capability:** SystemCapability.Communication.SecureElement

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| aid | number[] | Yes |
| p2 | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[Channel](arkts-connectivity-omapi-channel-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [3300101](../errorcode-se.md#3300101-abnormal-se-service-status) |
| [3300102](../errorcode-se.md#3300102-failed-to-find-the-desired-se) |
| [3300103](../errorcode-se.md#3300103-failed-to-obtain-the-access-rule) |
| [3300104](../errorcode-se.md#3300104-se-chip-io-exception) |

## openLogicalChannel

```TypeScript
openLogicalChannel(aid: number[], p2: number, callback: AsyncCallback<Channel>): void
```

Opens a logical channel, as defined in ISO/IEC 7816-4. If the SE cannot provide the logical channel or the application does not have the permission to access the SE, null is returned. This API uses an asynchronous callback to return the result.

**Since:** 10

**System capability:** SystemCapability.Communication.SecureElement

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| aid | number[] | Yes |
| p2 | number | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[Channel](arkts-connectivity-omapi-channel-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [3300101](../errorcode-se.md#3300101-abnormal-se-service-status) |
| [3300102](../errorcode-se.md#3300102-failed-to-find-the-desired-se) |
| [3300103](../errorcode-se.md#3300103-failed-to-obtain-the-access-rule) |
| [3300104](../errorcode-se.md#3300104-se-chip-io-exception) |
