# TagSession

The **tagSession** module provides common APIs for establishing connections and transferring data.

> **NOTE：**&gt;
> If an error is reported while importing the tag module editor, the capabilities of a specific device model may
> exceed the capability set defined for the default device. To use these capabilities, configure a custom SysCap by
> following instructions in
> [SystemCapability](https://developer.huawei.com/consumer/en/doc/harmonyos-references/syscap).

**Since:** 7

**System capability:** SystemCapability.Communication.NFC.Tag

## connect

```TypeScript
connect(): void
```

Connects to this tag. Call this API to set up a connection before reading data from or writing data to a tag.

**Since:** 9

**Required permissions:** ohos.permission.NFC_TAG

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Communication.NFC.Tag

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [3100201](../errorcode-nfc.md#3100201-tag-readwrite-error) |

## connectTag

```TypeScript
connectTag(): boolean
```

Connects to this tag. Call this API to set up a connection before reading data from or writing data to a tag.

> **NOTE：**&gt;
> This API is supported since API version 7 and deprecated since API version 9. Use
> [tagSession.connect](#connect) instead.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** connect

**Required permissions:** ohos.permission.NFC_TAG

**System capability:** SystemCapability.Communication.NFC.Tag

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## getMaxSendLength

```TypeScript
getMaxSendLength(): number
```

Obtains the maximum length of the data that can be sent to this tag.

> **NOTE：**&gt;
> This API is supported since API version 7 and deprecated since API version 9. Use
> [tagSession.getMaxTransmitSize](#getmaxtransmitsize) instead.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [getMaxTransmitSize](#getmaxtransmitsize)

**Required permissions:** ohos.permission.NFC_TAG

**System capability:** SystemCapability.Communication.NFC.Tag

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## getMaxTransmitSize

```TypeScript
getMaxTransmitSize(): number
```

Obtains the maximum length of the data that can be sent to this tag.

**Since:** 9

**Required permissions:** ohos.permission.NFC_TAG

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Communication.NFC.Tag

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [3100201](../errorcode-nfc.md#3100201-tag-readwrite-error) |

## getSendDataTimeout

```TypeScript
getSendDataTimeout(): number
```

Obtains the timeout period for sending data to this tag, in milliseconds.

> **NOTE：**&gt;
> This API is supported since API version 7 and deprecated since API version 9. Use
> [tagSession.getTimeout](#gettimeout) instead.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [getTimeout](#gettimeout)

**Required permissions:** ohos.permission.NFC_TAG

**System capability:** SystemCapability.Communication.NFC.Tag

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## getTagInfo

```TypeScript
getTagInfo(): tag.TagInfo
```

Obtains the **tagInfo** object provided by the NFC service when the tag is dispatched.

> **NOTE：**&gt;
> This API is supported since API version 7 and deprecated since API version 9. Use
> [tag.getTagInfo](arkts-connectivity-tag-gettaginfo-f.md) instead.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [getTagInfo](arkts-connectivity-tag-gettaginfo-f.md)

**Required permissions:** ohos.permission.NFC_TAG

**System capability:** SystemCapability.Communication.NFC.Tag

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| tag.TagInfo |

## getTimeout

```TypeScript
getTimeout(): number
```

Obtains the timeout period for sending data to this tag, in milliseconds.

**Since:** 9

**Required permissions:** ohos.permission.NFC_TAG

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Communication.NFC.Tag

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [3100201](../errorcode-nfc.md#3100201-tag-readwrite-error) |

## isConnected

```TypeScript
isConnected(): boolean
```

Checks whether the tag is connected. If you receive a message indicating that the tag has not been connected, call [tagSession.connect](#connect) to connect the tag.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Communication.NFC.Tag

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |

## isTagConnected

```TypeScript
isTagConnected(): boolean
```

Checks whether the tag is connected.

> **NOTE：**&gt;
> This API is supported since API version 7 and deprecated since API version 9. Use
> [tagSession.isConnected](#isconnected) instead.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** isConnected

**System capability:** SystemCapability.Communication.NFC.Tag

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## reset

```TypeScript
reset(): void
```

Resets the connection to this tag.

> **NOTE：**&gt;
> This API is supported since API version 7 and deprecated since API version 9. Use
> [tagSession.resetConnection](#resetconnection) instead.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [resetConnection](#resetconnection)

**Required permissions:** ohos.permission.NFC_TAG

**System capability:** SystemCapability.Communication.NFC.Tag

## resetConnection

```TypeScript
resetConnection(): void
```

Resets the connection to this tag.

**Since:** 9

**Required permissions:** ohos.permission.NFC_TAG

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Communication.NFC.Tag

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [3100201](../errorcode-nfc.md#3100201-tag-readwrite-error) |

## sendData

```TypeScript
sendData(data: number[]): Promise<number[]>
```

Sends data to the tag. This API uses a promise to return the result.

> **NOTE：**&gt;
> This API is supported since API version 7 and deprecated since API version 9. Use
> [tagSession.transmit](#transmit) instead.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** transmit

**Required permissions:** ohos.permission.NFC_TAG

**System capability:** SystemCapability.Communication.NFC.Tag

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| data | number[] | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number[] & gt; |

## sendData

```TypeScript
sendData(data: number[], callback: AsyncCallback<number[]>): void
```

Sends data to the tag. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> This parameter is supported since API version 7 and deprecated since API version 9. Use
> [tagSession.transmit](#transmit) instead.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** transmit

**Required permissions:** ohos.permission.NFC_TAG

**System capability:** SystemCapability.Communication.NFC.Tag

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| data | number[] | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number[]&gt; | Yes |

## setSendDataTimeout

```TypeScript
setSendDataTimeout(timeout: number): boolean
```

Sets the maximum time allowed for sending data to this tag, in ms.

> **NOTE：**&gt;
> This API is supported since API version 7 and deprecated since API version 9. Use
> [tagSession.setTimeout](#settimeout) instead.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** setTimeout

**Required permissions:** ohos.permission.NFC_TAG

**System capability:** SystemCapability.Communication.NFC.Tag

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| timeout | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## setTimeout

```TypeScript
setTimeout(timeout: number): void
```

Sets the maximum time allowed for sending data to this tag, in ms.

**Since:** 9

**Required permissions:** ohos.permission.NFC_TAG

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Communication.NFC.Tag

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| timeout | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [3100201](../errorcode-nfc.md#3100201-tag-readwrite-error) |

## transmit

```TypeScript
transmit(data: number[]): Promise<number[]>
```

Sends data to the tag. This API uses a promise to return the result.

**Since:** 9

**Required permissions:** ohos.permission.NFC_TAG

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Communication.NFC.Tag

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| data | number[] | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number[] & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [3100201](../errorcode-nfc.md#3100201-tag-readwrite-error) |
| [3100204](../errorcode-nfc.md#3100204-nfc-chip-io-exception) |

## transmit

```TypeScript
transmit(data: number[], callback: AsyncCallback<number[]>): void
```

Sends data to the tag. This API uses an asynchronous callback to return the result.

**Since:** 9

**Required permissions:** ohos.permission.NFC_TAG

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Communication.NFC.Tag

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| data | number[] | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number[]&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [3100201](../errorcode-nfc.md#3100201-tag-readwrite-error) |
| [3100204](../errorcode-nfc.md#3100204-nfc-chip-io-exception) |
