# MifareClassicTag

Provides methods for accessing MifareClassic tag.

**继承/实现关系：** MifareClassicTag extends [TagSession](arkts-connectivity-tagsession-tagsession-i.md)

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

<!--Device-unnamed-export interface MifareClassicTag extends TagSession--><!--Device-unnamed-export interface MifareClassicTag extends TagSession-End-->

**系统能力：** SystemCapability.Communication.NFC.Tag

## authenticateSector

ArkTS-Dyn:
```TypeScript
authenticateSector(sectorIndex: number, key: number[], isKeyA: boolean): Promise<void>
```

ArkTS-Sta:
```TypeScript
authenticateSector(sectorIndex: int, key: int[], isKeyA: boolean): Promise<void>
```

Authenticates a sector with the key. Only successful authentication sector can be operated.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.NFC_TAG

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-MifareClassicTag-authenticateSector(sectorIndex: int, key: int[], isKeyA: boolean): Promise<void>--><!--Device-MifareClassicTag-authenticateSector(sectorIndex: int, key: int[], isKeyA: boolean): Promise<void>-End-->

**系统能力：** SystemCapability.Communication.NFC.Tag

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sectorIndex | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 是 | Index of sector to authenticate. |
| key | ArkTS-Dyn: number[]  <br>ArkTS-Sta：int[] | 是 | The key(6-bytes) to authenticate. |
| isKeyA | boolean | 是 | KeyA flag. true means KeyA, otherwise KeyB. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | The void |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |
| 3100204 | The tag I/O operation failed. |
| 3100201 | The tag running state is abnormal in the service. |
| 201 | Permission denied. |

## authenticateSector

ArkTS-Dyn:
```TypeScript
authenticateSector(sectorIndex: number, key: number[], isKeyA: boolean, callback: AsyncCallback<void>): void
```

ArkTS-Sta:
```TypeScript
authenticateSector(sectorIndex: int, key: int[], isKeyA: boolean, callback: AsyncCallback<void>): void
```

Authenticates a sector with the key. Only successful authentication sector can be operated.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.NFC_TAG

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-MifareClassicTag-authenticateSector(sectorIndex: int, key: int[], isKeyA: boolean, callback: AsyncCallback<void>): void--><!--Device-MifareClassicTag-authenticateSector(sectorIndex: int, key: int[], isKeyA: boolean, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Communication.NFC.Tag

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sectorIndex | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 是 | Index of sector to authenticate. |
| key | ArkTS-Dyn: number[]  <br>ArkTS-Sta：int[] | 是 | The key(6-bytes) to authenticate. |
| isKeyA | boolean | 是 | KeyA flag. true means KeyA, otherwise KeyB. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 | The callback. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |
| 3100204 | The Tag I/O operation failed. |
| 3100201 | The tag running state is abnormal in the service. |
| 201 | Permission denied. |

## decrementBlock

ArkTS-Dyn:
```TypeScript
decrementBlock(blockIndex: number, value: number): Promise<void>
```

ArkTS-Sta:
```TypeScript
decrementBlock(blockIndex: int, value: int): Promise<void>
```

Decreases the contents of a block, and stores the result in the internal transfer buffer.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.NFC_TAG

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-MifareClassicTag-decrementBlock(blockIndex: int, value: int): Promise<void>--><!--Device-MifareClassicTag-decrementBlock(blockIndex: int, value: int): Promise<void>-End-->

**系统能力：** SystemCapability.Communication.NFC.Tag

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| blockIndex | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 是 | The index of block to decrease. |
| value | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 是 | The value to decrease, non-negative. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | The void |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |
| 3100204 | The tag I/O operation failed. |
| 3100201 | The tag running state is abnormal in the service. |
| 201 | Permission denied. |

## decrementBlock

ArkTS-Dyn:
```TypeScript
decrementBlock(blockIndex: number, value: number, callback: AsyncCallback<void>): void
```

ArkTS-Sta:
```TypeScript
decrementBlock(blockIndex: int, value: int, callback: AsyncCallback<void>): void
```

Decreases the contents of a block, and stores the result in the internal transfer buffer.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.NFC_TAG

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-MifareClassicTag-decrementBlock(blockIndex: int, value: int, callback: AsyncCallback<void>): void--><!--Device-MifareClassicTag-decrementBlock(blockIndex: int, value: int, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Communication.NFC.Tag

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| blockIndex | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 是 | The index of block to decrease. |
| value | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 是 | The value to decrease, non-negative. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 | The callback. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |
| 3100204 | The Tag I/O operation failed. |
| 3100201 | The tag running state is abnormal in the service. |
| 201 | Permission denied. |

## getBlockCountInSector

ArkTS-Dyn:
```TypeScript
getBlockCountInSector(sectorIndex: number): number
```

ArkTS-Sta:
```TypeScript
getBlockCountInSector(sectorIndex: int): int
```

Gets the number of blocks in the sector.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-MifareClassicTag-getBlockCountInSector(sectorIndex: int): int--><!--Device-MifareClassicTag-getBlockCountInSector(sectorIndex: int): int-End-->

**系统能力：** SystemCapability.Communication.NFC.Tag

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sectorIndex | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 是 | The index of sector. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：int | Returns the number of blocks. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |

## getBlockIndex

ArkTS-Dyn:
```TypeScript
getBlockIndex(sectorIndex: number): number
```

ArkTS-Sta:
```TypeScript
getBlockIndex(sectorIndex: int): int
```

Gets the first block of the specific sector.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-MifareClassicTag-getBlockIndex(sectorIndex: int): int--><!--Device-MifareClassicTag-getBlockIndex(sectorIndex: int): int-End-->

**系统能力：** SystemCapability.Communication.NFC.Tag

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sectorIndex | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 是 | The index of sector. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：int | Returns index of first block in the sector. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |

## getSectorCount

ArkTS-Dyn:
```TypeScript
getSectorCount(): number
```

ArkTS-Sta:
```TypeScript
getSectorCount(): int
```

Gets the number of sectors in MifareClassic tag.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-MifareClassicTag-getSectorCount(): int--><!--Device-MifareClassicTag-getSectorCount(): int-End-->

**系统能力：** SystemCapability.Communication.NFC.Tag

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：int | Returns the number of sectors. |

## getSectorIndex

ArkTS-Dyn:
```TypeScript
getSectorIndex(blockIndex: number): number
```

ArkTS-Sta:
```TypeScript
getSectorIndex(blockIndex: int): int
```

Gets the sector index, that the sector contains the specific block.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-MifareClassicTag-getSectorIndex(blockIndex: int): int--><!--Device-MifareClassicTag-getSectorIndex(blockIndex: int): int-End-->

**系统能力：** SystemCapability.Communication.NFC.Tag

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| blockIndex | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 是 | The index of block. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：int | Returns the sector index. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |

## getTagSize

ArkTS-Dyn:
```TypeScript
getTagSize(): number
```

ArkTS-Sta:
```TypeScript
getTagSize(): int
```

Gets size of the tag in bytes.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-MifareClassicTag-getTagSize(): int--><!--Device-MifareClassicTag-getTagSize(): int-End-->

**系统能力：** SystemCapability.Communication.NFC.Tag

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：int | Returns the size of the tag. |

## getType

```TypeScript
getType(): tag.MifareClassicType
```

Gets the type of the MifareClassic tag.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-MifareClassicTag-getType(): tag.MifareClassicType--><!--Device-MifareClassicTag-getType(): tag.MifareClassicType-End-->

**系统能力：** SystemCapability.Communication.NFC.Tag

**返回值：**

| 类型 | 说明 |
| --- | --- |
| tag.MifareClassicType | Returns type of MifareClassic tag. |

## incrementBlock

ArkTS-Dyn:
```TypeScript
incrementBlock(blockIndex: number, value: number): Promise<void>
```

ArkTS-Sta:
```TypeScript
incrementBlock(blockIndex: int, value: int): Promise<void>
```

Increments the contents of a block, and stores the result in the internal transfer buffer.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.NFC_TAG

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-MifareClassicTag-incrementBlock(blockIndex: int, value: int): Promise<void>--><!--Device-MifareClassicTag-incrementBlock(blockIndex: int, value: int): Promise<void>-End-->

**系统能力：** SystemCapability.Communication.NFC.Tag

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| blockIndex | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 是 | The index of block to increment. |
| value | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 是 | The value to increment, non-negative. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | The void |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |
| 3100204 | The tag I/O operation failed. |
| 3100201 | The tag running state is abnormal in the service. |
| 201 | Permission denied. |

## incrementBlock

ArkTS-Dyn:
```TypeScript
incrementBlock(blockIndex: number, value: number, callback: AsyncCallback<void>): void
```

ArkTS-Sta:
```TypeScript
incrementBlock(blockIndex: int, value: int, callback: AsyncCallback<void>): void
```

Increments the contents of a block, and stores the result in the internal transfer buffer.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.NFC_TAG

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-MifareClassicTag-incrementBlock(blockIndex: int, value: int, callback: AsyncCallback<void>): void--><!--Device-MifareClassicTag-incrementBlock(blockIndex: int, value: int, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Communication.NFC.Tag

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| blockIndex | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 是 | The index of block to increment. |
| value | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 是 | The value to increment, non-negative. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 | The callback. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |
| 3100204 | The Tag I/O operation failed. |
| 3100201 | The tag running state is abnormal in the service. |
| 201 | Permission denied. |

## isEmulatedTag

```TypeScript
isEmulatedTag(): boolean
```

Checks if the tag is emulated or not.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-MifareClassicTag-isEmulatedTag(): boolean--><!--Device-MifareClassicTag-isEmulatedTag(): boolean-End-->

**系统能力：** SystemCapability.Communication.NFC.Tag

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | Returns true if tag is emulated, otherwise false. |

## readSingleBlock

ArkTS-Dyn:
```TypeScript
readSingleBlock(blockIndex: number): Promise<number[]>
```

ArkTS-Sta:
```TypeScript
readSingleBlock(blockIndex: int): Promise<int[]>
```

Reads a block, one block size is 16 bytes.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.NFC_TAG

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-MifareClassicTag-readSingleBlock(blockIndex: int): Promise<int[]>--><!--Device-MifareClassicTag-readSingleBlock(blockIndex: int): Promise<int[]>-End-->

**系统能力：** SystemCapability.Communication.NFC.Tag

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| blockIndex | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 是 | The index of block to read. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ArkTS-Dyn: Promise&lt;number[]&gt;  <br>ArkTS-Sta：Promise&lt;int[]&gt; | Returns the block data. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |
| 3100204 | The tag I/O operation failed. |
| 3100201 | The tag running state is abnormal in the service. |
| 201 | Permission denied. |

## readSingleBlock

ArkTS-Dyn:
```TypeScript
readSingleBlock(blockIndex: number, callback: AsyncCallback<number[]>): void
```

ArkTS-Sta:
```TypeScript
readSingleBlock(blockIndex: int, callback: AsyncCallback<int[]>): void
```

Reads a block, one block size is 16 bytes.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.NFC_TAG

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-MifareClassicTag-readSingleBlock(blockIndex: int, callback: AsyncCallback<int[]>): void--><!--Device-MifareClassicTag-readSingleBlock(blockIndex: int, callback: AsyncCallback<int[]>): void-End-->

**系统能力：** SystemCapability.Communication.NFC.Tag

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| blockIndex | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 是 | The index of block to read. |
| callback | ArkTS-Dyn: [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number[]&gt;  <br>ArkTS-Sta：[AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;int[]&gt; | 是 | The callback. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |
| 3100204 | The Tag I/O operation failed. |
| 3100201 | The tag running state is abnormal in the service. |
| 201 | Permission denied. |

## restoreFromBlock

ArkTS-Dyn:
```TypeScript
restoreFromBlock(blockIndex: number): Promise<void>
```

ArkTS-Sta:
```TypeScript
restoreFromBlock(blockIndex: int): Promise<void>
```

Moves the contents of a block into the internal transfer buffer.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.NFC_TAG

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-MifareClassicTag-restoreFromBlock(blockIndex: int): Promise<void>--><!--Device-MifareClassicTag-restoreFromBlock(blockIndex: int): Promise<void>-End-->

**系统能力：** SystemCapability.Communication.NFC.Tag

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| blockIndex | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 是 | The index of value block to be moved from. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | The void |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |
| 3100204 | The tag I/O operation failed. |
| 3100201 | The tag running state is abnormal in the service. |
| 201 | Permission denied. |

## restoreFromBlock

ArkTS-Dyn:
```TypeScript
restoreFromBlock(blockIndex: number, callback: AsyncCallback<void>): void
```

ArkTS-Sta:
```TypeScript
restoreFromBlock(blockIndex: int, callback: AsyncCallback<void>): void
```

Moves the contents of a block into the internal transfer buffer.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.NFC_TAG

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-MifareClassicTag-restoreFromBlock(blockIndex: int, callback: AsyncCallback<void>): void--><!--Device-MifareClassicTag-restoreFromBlock(blockIndex: int, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Communication.NFC.Tag

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| blockIndex | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 是 | The index of value block to be moved from. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 | The callback. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |
| 3100204 | The Tag I/O operation failed. |
| 3100201 | The tag running state is abnormal in the service. |
| 201 | Permission denied. |

## transferToBlock

ArkTS-Dyn:
```TypeScript
transferToBlock(blockIndex: number): Promise<void>
```

ArkTS-Sta:
```TypeScript
transferToBlock(blockIndex: int): Promise<void>
```

Writes the contents of the internal transfer buffer to a value block.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.NFC_TAG

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-MifareClassicTag-transferToBlock(blockIndex: int): Promise<void>--><!--Device-MifareClassicTag-transferToBlock(blockIndex: int): Promise<void>-End-->

**系统能力：** SystemCapability.Communication.NFC.Tag

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| blockIndex | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 是 | The index of value block to be written. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | The void |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |
| 3100204 | The tag I/O operation failed. |
| 3100201 | The tag running state is abnormal in the service. |
| 201 | Permission denied. |

## transferToBlock

ArkTS-Dyn:
```TypeScript
transferToBlock(blockIndex: number, callback: AsyncCallback<void>): void
```

ArkTS-Sta:
```TypeScript
transferToBlock(blockIndex: int, callback: AsyncCallback<void>): void
```

Writes the contents of the internal transfer buffer to a value block.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.NFC_TAG

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-MifareClassicTag-transferToBlock(blockIndex: int, callback: AsyncCallback<void>): void--><!--Device-MifareClassicTag-transferToBlock(blockIndex: int, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Communication.NFC.Tag

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| blockIndex | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 是 | The index of value block to be written. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 | The callback. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |
| 3100204 | The Tag I/O operation failed. |
| 3100201 | The tag running state is abnormal in the service. |
| 201 | Permission denied. |

## writeSingleBlock

ArkTS-Dyn:
```TypeScript
writeSingleBlock(blockIndex: number, data: number[]): Promise<void>
```

ArkTS-Sta:
```TypeScript
writeSingleBlock(blockIndex: int, data: int[]): Promise<void>
```

Writes a block, one block size is 16 bytes.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.NFC_TAG

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-MifareClassicTag-writeSingleBlock(blockIndex: int, data: int[]): Promise<void>--><!--Device-MifareClassicTag-writeSingleBlock(blockIndex: int, data: int[]): Promise<void>-End-->

**系统能力：** SystemCapability.Communication.NFC.Tag

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| blockIndex | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 是 | The index of block to write. |
| data | ArkTS-Dyn: number[]  <br>ArkTS-Sta：int[] | 是 | The block data to write. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | The void |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |
| 3100204 | The tag I/O operation failed. |
| 3100201 | The tag running state is abnormal in the service. |
| 201 | Permission denied. |

## writeSingleBlock

ArkTS-Dyn:
```TypeScript
writeSingleBlock(blockIndex: number, data: number[], callback: AsyncCallback<void>): void
```

ArkTS-Sta:
```TypeScript
writeSingleBlock(blockIndex: int, data: int[], callback: AsyncCallback<void>): void
```

Writes a block, one block size is 16 bytes.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.NFC_TAG

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-MifareClassicTag-writeSingleBlock(blockIndex: int, data: int[], callback: AsyncCallback<void>): void--><!--Device-MifareClassicTag-writeSingleBlock(blockIndex: int, data: int[], callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Communication.NFC.Tag

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| blockIndex | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 是 | The index of block to write. |
| data | ArkTS-Dyn: number[]  <br>ArkTS-Sta：int[] | 是 | The block data to write. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 | The callback. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |
| 3100204 | The Tag I/O operation failed. |
| 3100201 | The tag running state is abnormal in the service. |
| 201 | Permission denied. |

