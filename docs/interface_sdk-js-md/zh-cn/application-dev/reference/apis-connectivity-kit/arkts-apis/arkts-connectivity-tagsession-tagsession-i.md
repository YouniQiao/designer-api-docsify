# TagSession

Controls tag read and write.&lt;p&gt;Classes for different types of tags inherit from this abstract class to control connections to tags, read data from tags, and write data to tags.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

<!--Device-unnamed-export interface TagSession--><!--Device-unnamed-export interface TagSession-End-->

**系统能力：** SystemCapability.Communication.NFC.Tag

## connect

```TypeScript
connect(): void
```

Connects to a tag. Must be called before data is read from or written to the tag.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.NFC_TAG

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-TagSession-connect(): void--><!--Device-TagSession-connect(): void-End-->

**系统能力：** SystemCapability.Communication.NFC.Tag

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |
| 3100201 | The tag running state is abnormal in the service. |
| 201 | Permission denied. |

## connectTag

```TypeScript
connectTag(): boolean
```

Connects to a tag.&lt;p&gt;This method must be called before data is read from or written to the tag.

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为7。

**废弃版本：** 9

**替代接口：** tagSession.TagSession#connect

**需要权限：** ohos.permission.NFC_TAG

<!--Device-TagSession-connectTag(): boolean--><!--Device-TagSession-connectTag(): boolean-End-->

**系统能力：** SystemCapability.Communication.NFC.Tag

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | Returns { |

## getMaxSendLength

```TypeScript
getMaxSendLength(): number
```

Queries the maximum length of data that can be sent to a tag.

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为7。

**废弃版本：** 9

**替代接口：** tagSession.TagSession#getMaxTransmitSize

**需要权限：** ohos.permission.NFC_TAG

<!--Device-TagSession-getMaxSendLength(): number--><!--Device-TagSession-getMaxSendLength(): number-End-->

**系统能力：** SystemCapability.Communication.NFC.Tag

**返回值：**

| 类型 | 说明 |
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

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.NFC_TAG

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-TagSession-getMaxTransmitSize(): int--><!--Device-TagSession-getMaxTransmitSize(): int-End-->

**系统能力：** SystemCapability.Communication.NFC.Tag

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：int | Returns the maximum length of the data to be sent to the tag. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |
| 3100201 | The tag running state is abnormal in the service. |
| 201 | Permission denied. |

## getSendDataTimeout

```TypeScript
getSendDataTimeout(): number
```

Queries the timeout duration (ms) for sending data to a tag.

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为7。

**废弃版本：** 9

**替代接口：** tagSession.TagSession#getTimeout

**需要权限：** ohos.permission.NFC_TAG

<!--Device-TagSession-getSendDataTimeout(): number--><!--Device-TagSession-getSendDataTimeout(): number-End-->

**系统能力：** SystemCapability.Communication.NFC.Tag

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | Returns the timeout duration. |

## getTagInfo

```TypeScript
getTagInfo(): tag.TagInfo
```

Obtains the tag information.

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为7。

**废弃版本：** 9

**替代接口：** ohos.nfc.tag/tag#getTagInfo

**需要权限：** ohos.permission.NFC_TAG

<!--Device-TagSession-getTagInfo(): tag.TagInfo--><!--Device-TagSession-getTagInfo(): tag.TagInfo-End-->

**系统能力：** SystemCapability.Communication.NFC.Tag

**返回值：**

| 类型 | 说明 |
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

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.NFC_TAG

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-TagSession-getTimeout(): int--><!--Device-TagSession-getTimeout(): int-End-->

**系统能力：** SystemCapability.Communication.NFC.Tag

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：int | Returns the timeout duration. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |
| 3100201 | The tag running state is abnormal in the service. |
| 201 | Permission denied. |

## isConnected

```TypeScript
isConnected(): boolean
```

Checks whether a connection has been set up with a tag.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-TagSession-isConnected(): boolean--><!--Device-TagSession-isConnected(): boolean-End-->

**系统能力：** SystemCapability.Communication.NFC.Tag

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | Returns true if tag connected, otherwise false. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |

## isTagConnected

```TypeScript
isTagConnected(): boolean
```

Checks whether a connection has been set up with a tag.

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为7。

**废弃版本：** 9

**替代接口：** tagSession.TagSession#isConnected

<!--Device-TagSession-isTagConnected(): boolean--><!--Device-TagSession-isTagConnected(): boolean-End-->

**系统能力：** SystemCapability.Communication.NFC.Tag

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | Returns { |

## reset

```TypeScript
reset(): void
```

Resets a connection with a tag and restores the default timeout duration for writing data to the tag.

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为7。

**废弃版本：** 9

**替代接口：** tagSession.TagSession#resetConnection

**需要权限：** ohos.permission.NFC_TAG

<!--Device-TagSession-reset(): void--><!--Device-TagSession-reset(): void-End-->

**系统能力：** SystemCapability.Communication.NFC.Tag

## resetConnection

```TypeScript
resetConnection(): void
```

Resets a connection with a tag and restores the default timeout duration for writing data to the tag.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.NFC_TAG

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-TagSession-resetConnection(): void--><!--Device-TagSession-resetConnection(): void-End-->

**系统能力：** SystemCapability.Communication.NFC.Tag

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |
| 3100201 | The tag running state is abnormal in the service. |
| 201 | Permission denied. |

## sendData

```TypeScript
sendData(data: number[]): Promise<number[]>
```

Writes data to a tag.

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为7。

**废弃版本：** 9

**替代接口：** tagSession.TagSession#transmit

**需要权限：** ohos.permission.NFC_TAG

<!--Device-TagSession-sendData(data: number[]): Promise<number[]>--><!--Device-TagSession-sendData(data: number[]): Promise<number[]>-End-->

**系统能力：** SystemCapability.Communication.NFC.Tag

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | number[] | 是 | Indicates the data to be written to the tag. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;number[]&gt; | Returns bytes received in response. Or bytes with a length of 0 if the data fails to be written to the tag. |

## sendData

```TypeScript
sendData(data: number[], callback: AsyncCallback<number[]>): void
```

Writes data to a tag.

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为7。

**废弃版本：** 9

**替代接口：** tagSession.TagSession#transmit

**需要权限：** ohos.permission.NFC_TAG

<!--Device-TagSession-sendData(data: number[], callback: AsyncCallback<number[]>): void--><!--Device-TagSession-sendData(data: number[], callback: AsyncCallback<number[]>): void-End-->

**系统能力：** SystemCapability.Communication.NFC.Tag

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | number[] | 是 | Indicates the data to be written to the tag. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number[]&gt; | 是 | The callback. data fails to be written to the tag. |

## setSendDataTimeout

```TypeScript
setSendDataTimeout(timeout: number): boolean
```

Sets the timeout duration (ms) for sending data to a tag.&lt;p&gt;If data is not sent to the tag within the duration, data sending fails.

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为7。

**废弃版本：** 9

**替代接口：** tagSession.TagSession#setTimeout

**需要权限：** ohos.permission.NFC_TAG

<!--Device-TagSession-setSendDataTimeout(timeout: number): boolean--><!--Device-TagSession-setSendDataTimeout(timeout: number): boolean-End-->

**系统能力：** SystemCapability.Communication.NFC.Tag

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| timeout | number | 是 | Indicates the timeout duration to be set. |

**返回值：**

| 类型 | 说明 |
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

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.NFC_TAG

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-TagSession-setTimeout(timeout: int): void--><!--Device-TagSession-setTimeout(timeout: int): void-End-->

**系统能力：** SystemCapability.Communication.NFC.Tag

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| timeout | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 是 | Indicates the timeout duration to be set. |

**错误码：**

| 错误码ID | 错误信息 |
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

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.NFC_TAG

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-TagSession-transmit(data: int[]): Promise<int[]>--><!--Device-TagSession-transmit(data: int[]): Promise<int[]>-End-->

**系统能力：** SystemCapability.Communication.NFC.Tag

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | ArkTS-Dyn: number[]  <br>ArkTS-Sta：int[] | 是 | Indicates the data to be written to the tag. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ArkTS-Dyn: Promise&lt;number[]&gt;  <br>ArkTS-Sta：Promise&lt;int[]&gt; | Returns bytes received in response. Or bytes with a length of 0 if the data fails to be written to the tag. |

**错误码：**

| 错误码ID | 错误信息 |
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

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.NFC_TAG

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-TagSession-transmit(data: int[], callback: AsyncCallback<int[]>): void--><!--Device-TagSession-transmit(data: int[], callback: AsyncCallback<int[]>): void-End-->

**系统能力：** SystemCapability.Communication.NFC.Tag

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | ArkTS-Dyn: number[]  <br>ArkTS-Sta：int[] | 是 | Indicates the data to be written to the tag. |
| callback | ArkTS-Dyn: [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number[]&gt;  <br>ArkTS-Sta：[AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;int[]&gt; | 是 | The callback. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 3100204 | The tag I/O operation failed. |
| 3100201 | The tag running state is abnormal in the service. |
| 201 | Permission denied. |

