# IsoDepTag

Provides methods for accessing IsoDep tag.

**继承/实现关系：** IsoDepTag extends [TagSession](arkts-connectivity-tagsession-tagsession-i.md)

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

<!--Device-unnamed-export interface IsoDepTag extends TagSession--><!--Device-unnamed-export interface IsoDepTag extends TagSession-End-->

**系统能力：** SystemCapability.Communication.NFC.Tag

## getHiLayerResponse

ArkTS-Dyn:
```TypeScript
getHiLayerResponse(): number[]
```

ArkTS-Sta:
```TypeScript
getHiLayerResponse(): int[]
```

Gets IsoDep HiLayer Response bytes of the tag, which is based on NfcB RF technology.It could be null if not based on NfcB.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-IsoDepTag-getHiLayerResponse(): int[]--><!--Device-IsoDepTag-getHiLayerResponse(): int[]-End-->

**系统能力：** SystemCapability.Communication.NFC.Tag

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ArkTS-Dyn: number[]  <br>ArkTS-Sta：int[] | Returns HiLayer Response bytes, the length could be 0. |

## getHistoricalBytes

ArkTS-Dyn:
```TypeScript
getHistoricalBytes(): number[]
```

ArkTS-Sta:
```TypeScript
getHistoricalBytes(): int[]
```

Gets IsoDep Historical bytes of the tag, which is based on NfcA RF technology.It could be null if not based on NfcA.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-IsoDepTag-getHistoricalBytes(): int[]--><!--Device-IsoDepTag-getHistoricalBytes(): int[]-End-->

**系统能力：** SystemCapability.Communication.NFC.Tag

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ArkTS-Dyn: number[]  <br>ArkTS-Sta：int[] | Returns the Historical bytes, the length could be 0. |

## isExtendedApduSupported

```TypeScript
isExtendedApduSupported(): Promise<boolean>
```

Checks if extended apdu length supported or not.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.NFC_TAG

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-IsoDepTag-isExtendedApduSupported(): Promise<boolean>--><!--Device-IsoDepTag-isExtendedApduSupported(): Promise<boolean>-End-->

**系统能力：** SystemCapability.Communication.NFC.Tag

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;boolean&gt; | Returns true if extended apdu length supported, otherwise false. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |
| 3100204 | The tag I/O operation failed. |
| 3100201 | The tag running state is abnormal in the service. |
| 201 | Permission denied. |

## isExtendedApduSupported

```TypeScript
isExtendedApduSupported(callback: AsyncCallback<boolean>): void
```

Checks if extended apdu length supported or not.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.NFC_TAG

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-IsoDepTag-isExtendedApduSupported(callback: AsyncCallback<boolean>): void--><!--Device-IsoDepTag-isExtendedApduSupported(callback: AsyncCallback<boolean>): void-End-->

**系统能力：** SystemCapability.Communication.NFC.Tag

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 | The callback. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |
| 3100204 | The Tag I/O operation failed. |
| 3100201 | The tag running state is abnormal in the service. |
| 201 | Permission denied. |

