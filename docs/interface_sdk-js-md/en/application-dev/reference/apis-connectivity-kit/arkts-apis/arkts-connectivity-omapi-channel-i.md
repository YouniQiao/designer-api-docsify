# Channel

A **Channel** instance indicates a channel set up by a **Session** instance. The channel can be a basic channel or a logical channel. You can use [Session.openBasicChannel](arkts-connectivity-omapi-session-i.md#openbasicchannel) or [Session.openLogicalChannel](arkts-connectivity-omapi-session-i.md#openlogicalchannel) to obtain a channel instance.

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

Closes this channel.

**Since:** 10

**System capability:** SystemCapability.Communication.SecureElement

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |

## getSelectResponse

```TypeScript
getSelectResponse(): number[]
```

Obtains the response data including the status word of **SELECT Applet**.

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

## getSession

```TypeScript
getSession(): Session
```

Obtains the session used to open this channel.

**Since:** 10

**System capability:** SystemCapability.Communication.SecureElement

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Session](../../apis-camera-kit/arkts-apis/arkts-camera-camera-session-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |

## isBasicChannel

```TypeScript
isBasicChannel(): boolean
```

Checks whether this channel is a basic channel.

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

## isClosed

```TypeScript
isClosed(): boolean
```

Checks whether this channel is closed.

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

## transmit

```TypeScript
transmit(command: number[]): Promise<number[]>
```

Transmits APDU data (as per ISO/IEC 7816) to the SE. This API uses a promise to return the result.

**Since:** 10

**System capability:** SystemCapability.Communication.SecureElement

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| command | number[] | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number[] & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [3300101](../errorcode-se.md#3300101-abnormal-se-service-status) |
| [3300103](../errorcode-se.md#3300103-failed-to-obtain-the-access-rule) |
| [3300104](../errorcode-se.md#3300104-se-chip-io-exception) |

## transmit

```TypeScript
transmit(command: number[], callback: AsyncCallback<number[]>): void
```

Transmits APDU data (as per ISO/IEC 7816) to the SE. This API uses an asynchronous callback to return the result.

**Since:** 10

**System capability:** SystemCapability.Communication.SecureElement

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| command | number[] | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number[]&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [3300101](../errorcode-se.md#3300101-abnormal-se-service-status) |
| [3300103](../errorcode-se.md#3300103-failed-to-obtain-the-access-rule) |
| [3300104](../errorcode-se.md#3300104-se-chip-io-exception) |
