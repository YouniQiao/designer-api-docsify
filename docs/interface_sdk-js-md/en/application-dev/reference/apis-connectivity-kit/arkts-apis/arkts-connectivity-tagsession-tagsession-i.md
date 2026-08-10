# TagSession

Controls tag read and write.&lt;p&gt;Classes for different types of tags inherit from this abstract class to control connections to tags, read data from tags, and write data to tags.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-unnamed-export interface TagSession--><!--Device-unnamed-export interface TagSession-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

## connect

```TypeScript
connect(): void
```

Connects to a tag. Must be called before data is read from or written to the tag.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.NFC_TAG

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TagSession-connect(): void--><!--Device-TagSession-connect(): void-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported. |
| 3100201 | The tag running state is abnormal in the service. |
| 201 | Permission denied. |

## connectTag

```TypeScript
connectTag(): boolean
```

Connects to a tag.&lt;p&gt;This method must be called before data is read from or written to the tag.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** tagSession.TagSession#connect

**Required permissions:** ohos.permission.NFC_TAG

<!--Device-TagSession-connectTag(): boolean--><!--Device-TagSession-connectTag(): boolean-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns { |

## getMaxSendLength

```TypeScript
getMaxSendLength(): number
```

Queries the maximum length of data that can be sent to a tag.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** tagSession.TagSession#getMaxTransmitSize

**Required permissions:** ohos.permission.NFC_TAG

<!--Device-TagSession-getMaxSendLength(): number--><!--Device-TagSession-getMaxSendLength(): number-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Return value:**

| Type | Description |
| --- | --- |
| number | Returns the maximum length of the data to be sent to the tag. |

## getMaxTransmitSize

ArkTS-Dyn:
```TypeScript
getMaxTransmitSize(): number
```

ArkTS-Sta:
```TypeScript
getMaxTransmitSize(): int
```

Obtains the maximum length of data that can be sent to a tag.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.NFC_TAG

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TagSession-getMaxTransmitSize(): int--><!--Device-TagSession-getMaxTransmitSize(): int-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：int | Returns the maximum length of the data to be sent to the tag. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported. |
| 3100201 | The tag running state is abnormal in the service. |
| 201 | Permission denied. |

## getSendDataTimeout

```TypeScript
getSendDataTimeout(): number
```

Queries the timeout duration (ms) for sending data to a tag.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** tagSession.TagSession#getTimeout

**Required permissions:** ohos.permission.NFC_TAG

<!--Device-TagSession-getSendDataTimeout(): number--><!--Device-TagSession-getSendDataTimeout(): number-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Return value:**

| Type | Description |
| --- | --- |
| number | Returns the timeout duration. |

## getTagInfo

```TypeScript
getTagInfo(): tag.TagInfo
```

Obtains the tag information.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.nfc.tag/tag#getTagInfo

**Required permissions:** ohos.permission.NFC_TAG

<!--Device-TagSession-getTagInfo(): tag.TagInfo--><!--Device-TagSession-getTagInfo(): tag.TagInfo-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Return value:**

| Type | Description |
| --- | --- |
| tag.TagInfo | Returns the tag information, which is a { |

## getTimeout

ArkTS-Dyn:
```TypeScript
getTimeout(): number
```

ArkTS-Sta:
```TypeScript
getTimeout(): int
```

Obtains the timeout duration (ms) for sending data to a tag.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.NFC_TAG

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TagSession-getTimeout(): int--><!--Device-TagSession-getTimeout(): int-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：int | Returns the timeout duration. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported. |
| 3100201 | The tag running state is abnormal in the service. |
| 201 | Permission denied. |

## isConnected

```TypeScript
isConnected(): boolean
```

Checks whether a connection has been set up with a tag.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TagSession-isConnected(): boolean--><!--Device-TagSession-isConnected(): boolean-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns true if tag connected, otherwise false. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported. |

## isTagConnected

```TypeScript
isTagConnected(): boolean
```

Checks whether a connection has been set up with a tag.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** tagSession.TagSession#isConnected

<!--Device-TagSession-isTagConnected(): boolean--><!--Device-TagSession-isTagConnected(): boolean-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns { |

## reset

```TypeScript
reset(): void
```

Resets a connection with a tag and restores the default timeout duration for writing data to the tag.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** tagSession.TagSession#resetConnection

**Required permissions:** ohos.permission.NFC_TAG

<!--Device-TagSession-reset(): void--><!--Device-TagSession-reset(): void-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

## resetConnection

```TypeScript
resetConnection(): void
```

Resets a connection with a tag and restores the default timeout duration for writing data to the tag.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.NFC_TAG

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TagSession-resetConnection(): void--><!--Device-TagSession-resetConnection(): void-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported. |
| 3100201 | The tag running state is abnormal in the service. |
| 201 | Permission denied. |

## sendData

```TypeScript
sendData(data: number[]): Promise<number[]>
```

Writes data to a tag.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** tagSession.TagSession#transmit

**Required permissions:** ohos.permission.NFC_TAG

<!--Device-TagSession-sendData(data: number[]): Promise<number[]>--><!--Device-TagSession-sendData(data: number[]): Promise<number[]>-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | number[] | Yes | Indicates the data to be written to the tag. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;number[]&gt; | Returns bytes received in response. Or bytes with a length of 0 if the data fails to be written to the tag. |

## sendData

```TypeScript
sendData(data: number[], callback: AsyncCallback<number[]>): void
```

Writes data to a tag.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** tagSession.TagSession#transmit

**Required permissions:** ohos.permission.NFC_TAG

<!--Device-TagSession-sendData(data: number[], callback: AsyncCallback<number[]>): void--><!--Device-TagSession-sendData(data: number[], callback: AsyncCallback<number[]>): void-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | number[] | Yes | Indicates the data to be written to the tag. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number[]&gt; | Yes | The callback. data fails to be written to the tag. |

## setSendDataTimeout

```TypeScript
setSendDataTimeout(timeout: number): boolean
```

Sets the timeout duration (ms) for sending data to a tag.&lt;p&gt;If data is not sent to the tag within the duration, data sending fails.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** tagSession.TagSession#setTimeout

**Required permissions:** ohos.permission.NFC_TAG

<!--Device-TagSession-setSendDataTimeout(timeout: number): boolean--><!--Device-TagSession-setSendDataTimeout(timeout: number): boolean-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| timeout | number | Yes | Indicates the timeout duration to be set. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns { |

## setTimeout

ArkTS-Dyn:
```TypeScript
setTimeout(timeout: number): void
```

ArkTS-Sta:
```TypeScript
setTimeout(timeout: int): void
```

Sets the timeout duration (ms) for sending data to a tag.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.NFC_TAG

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TagSession-setTimeout(timeout: int): void--><!--Device-TagSession-setTimeout(timeout: int): void-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| timeout | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Indicates the timeout duration to be set. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | The parameter check failed. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 3100201 | The tag running state is abnormal in the service. |
| 201 | Permission denied. |

## transmit

ArkTS-Dyn:
```TypeScript
transmit(data: number[]): Promise<number[]>
```

ArkTS-Sta:
```TypeScript
transmit(data: int[]): Promise<int[]>
```

Writes data to a tag.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.NFC_TAG

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TagSession-transmit(data: int[]): Promise<int[]>--><!--Device-TagSession-transmit(data: int[]): Promise<int[]>-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | ArkTS-Dyn: number[]  <br>ArkTS-Sta：int[] | Yes | Indicates the data to be written to the tag. |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: Promise&lt;number[]&gt;  <br>ArkTS-Sta：Promise&lt;int[]&gt; | Returns bytes received in response. Or bytes with a length of 0 if the data fails to be written to the tag. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | The parameter check failed. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 3100204 | The tag I/O operation failed. |
| 3100201 | The tag running state is abnormal in the service. |
| 201 | Permission denied. |

## transmit

ArkTS-Dyn:
```TypeScript
transmit(data: number[], callback: AsyncCallback<number[]>): void
```

ArkTS-Sta:
```TypeScript
transmit(data: int[], callback: AsyncCallback<int[]>): void
```

Writes data to a tag.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.NFC_TAG

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TagSession-transmit(data: int[], callback: AsyncCallback<int[]>): void--><!--Device-TagSession-transmit(data: int[], callback: AsyncCallback<int[]>): void-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | ArkTS-Dyn: number[]  <br>ArkTS-Sta：int[] | Yes | Indicates the data to be written to the tag. |
| callback | ArkTS-Dyn: [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number[]&gt;  <br>ArkTS-Sta：[AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;int[]&gt; | Yes | The callback. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | The parameter check failed. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 3100204 | The tag I/O operation failed. |
| 3100201 | The tag running state is abnormal in the service. |
| 201 | Permission denied. |

