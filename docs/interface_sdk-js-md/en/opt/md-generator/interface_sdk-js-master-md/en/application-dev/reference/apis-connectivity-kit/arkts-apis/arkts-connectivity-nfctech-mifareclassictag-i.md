# MifareClassicTag

Provides methods for accessing MifareClassic tag.

**Inheritance/Implementation:** MifareClassicTag extends [TagSession](arkts-connectivity-tagsession-tagsession-i.md)

**Since:** 12

<!--Device-unnamed-export interface MifareClassicTag extends TagSession--><!--Device-unnamed-export interface MifareClassicTag extends TagSession-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

## authenticateSector

```TypeScript
authenticateSector(sectorIndex: number, key: number[], isKeyA: boolean): Promise<void>
```

Authenticates a sector with the key. Only successful authentication sector can be operated.

**Since:** 12

**Required permissions:** ohos.permission.NFC_TAG

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-MifareClassicTag-authenticateSector(sectorIndex: int, key: int[], isKeyA: boolean): Promise<void>--><!--Device-MifareClassicTag-authenticateSector(sectorIndex: int, key: int[], isKeyA: boolean): Promise<void>-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sectorIndex | number | Yes |
| key | number[] | Yes |
| isKeyA | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [3100204](../errorcode-nfc.md#3100204-nfc-chip-io-exception) |
| [3100201](../errorcode-nfc.md#3100201-tag-readwrite-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |

## authenticateSector

```TypeScript
authenticateSector(sectorIndex: number, key: number[], isKeyA: boolean, callback: AsyncCallback<void>): void
```

Authenticates a sector with the key. Only successful authentication sector can be operated.

**Since:** 12

**Required permissions:** ohos.permission.NFC_TAG

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-MifareClassicTag-authenticateSector(sectorIndex: int, key: int[], isKeyA: boolean, callback: AsyncCallback<void>): void--><!--Device-MifareClassicTag-authenticateSector(sectorIndex: int, key: int[], isKeyA: boolean, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sectorIndex | number | Yes |
| key | number[] | Yes |
| isKeyA | boolean | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [3100204](../errorcode-nfc.md#3100204-nfc-chip-io-exception) |
| [3100201](../errorcode-nfc.md#3100201-tag-readwrite-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |

## decrementBlock

```TypeScript
decrementBlock(blockIndex: number, value: number): Promise<void>
```

Decreases the contents of a block, and stores the result in the internal transfer buffer.

**Since:** 12

**Required permissions:** ohos.permission.NFC_TAG

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-MifareClassicTag-decrementBlock(blockIndex: int, value: int): Promise<void>--><!--Device-MifareClassicTag-decrementBlock(blockIndex: int, value: int): Promise<void>-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| blockIndex | number | Yes |
| value | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [3100204](../errorcode-nfc.md#3100204-nfc-chip-io-exception) |
| [3100201](../errorcode-nfc.md#3100201-tag-readwrite-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |

## decrementBlock

```TypeScript
decrementBlock(blockIndex: number, value: number, callback: AsyncCallback<void>): void
```

Decreases the contents of a block, and stores the result in the internal transfer buffer.

**Since:** 12

**Required permissions:** ohos.permission.NFC_TAG

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-MifareClassicTag-decrementBlock(blockIndex: int, value: int, callback: AsyncCallback<void>): void--><!--Device-MifareClassicTag-decrementBlock(blockIndex: int, value: int, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| blockIndex | number | Yes |
| value | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [3100204](../errorcode-nfc.md#3100204-nfc-chip-io-exception) |
| [3100201](../errorcode-nfc.md#3100201-tag-readwrite-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |

## getBlockCountInSector

```TypeScript
getBlockCountInSector(sectorIndex: number): number
```

Gets the number of blocks in the sector.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-MifareClassicTag-getBlockCountInSector(sectorIndex: int): int--><!--Device-MifareClassicTag-getBlockCountInSector(sectorIndex: int): int-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sectorIndex | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## getBlockIndex

```TypeScript
getBlockIndex(sectorIndex: number): number
```

Gets the first block of the specific sector.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-MifareClassicTag-getBlockIndex(sectorIndex: int): int--><!--Device-MifareClassicTag-getBlockIndex(sectorIndex: int): int-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sectorIndex | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## getSectorCount

```TypeScript
getSectorCount(): number
```

Gets the number of sectors in MifareClassic tag.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-MifareClassicTag-getSectorCount(): int--><!--Device-MifareClassicTag-getSectorCount(): int-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## getSectorIndex

```TypeScript
getSectorIndex(blockIndex: number): number
```

Gets the sector index, that the sector contains the specific block.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-MifareClassicTag-getSectorIndex(blockIndex: int): int--><!--Device-MifareClassicTag-getSectorIndex(blockIndex: int): int-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| blockIndex | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## getTagSize

```TypeScript
getTagSize(): number
```

Gets size of the tag in bytes.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-MifareClassicTag-getTagSize(): int--><!--Device-MifareClassicTag-getTagSize(): int-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## getType

```TypeScript
getType(): tag.MifareClassicType
```

Gets the type of the MifareClassic tag.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-MifareClassicTag-getType(): tag.MifareClassicType--><!--Device-MifareClassicTag-getType(): tag.MifareClassicType-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| tag.MifareClassicType |

## incrementBlock

```TypeScript
incrementBlock(blockIndex: number, value: number): Promise<void>
```

Increments the contents of a block, and stores the result in the internal transfer buffer.

**Since:** 12

**Required permissions:** ohos.permission.NFC_TAG

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-MifareClassicTag-incrementBlock(blockIndex: int, value: int): Promise<void>--><!--Device-MifareClassicTag-incrementBlock(blockIndex: int, value: int): Promise<void>-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| blockIndex | number | Yes |
| value | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [3100204](../errorcode-nfc.md#3100204-nfc-chip-io-exception) |
| [3100201](../errorcode-nfc.md#3100201-tag-readwrite-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |

## incrementBlock

```TypeScript
incrementBlock(blockIndex: number, value: number, callback: AsyncCallback<void>): void
```

Increments the contents of a block, and stores the result in the internal transfer buffer.

**Since:** 12

**Required permissions:** ohos.permission.NFC_TAG

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-MifareClassicTag-incrementBlock(blockIndex: int, value: int, callback: AsyncCallback<void>): void--><!--Device-MifareClassicTag-incrementBlock(blockIndex: int, value: int, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| blockIndex | number | Yes |
| value | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [3100204](../errorcode-nfc.md#3100204-nfc-chip-io-exception) |
| [3100201](../errorcode-nfc.md#3100201-tag-readwrite-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |

## isEmulatedTag

```TypeScript
isEmulatedTag(): boolean
```

Checks if the tag is emulated or not.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-MifareClassicTag-isEmulatedTag(): boolean--><!--Device-MifareClassicTag-isEmulatedTag(): boolean-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## readSingleBlock

```TypeScript
readSingleBlock(blockIndex: number): Promise<number[]>
```

Reads a block, one block size is 16 bytes.

**Since:** 12

**Required permissions:** ohos.permission.NFC_TAG

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-MifareClassicTag-readSingleBlock(blockIndex: int): Promise<int[]>--><!--Device-MifareClassicTag-readSingleBlock(blockIndex: int): Promise<int[]>-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| blockIndex | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;number[]&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [3100204](../errorcode-nfc.md#3100204-nfc-chip-io-exception) |
| [3100201](../errorcode-nfc.md#3100201-tag-readwrite-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |

## readSingleBlock

```TypeScript
readSingleBlock(blockIndex: number, callback: AsyncCallback<number[]>): void
```

Reads a block, one block size is 16 bytes.

**Since:** 12

**Required permissions:** ohos.permission.NFC_TAG

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-MifareClassicTag-readSingleBlock(blockIndex: int, callback: AsyncCallback<int[]>): void--><!--Device-MifareClassicTag-readSingleBlock(blockIndex: int, callback: AsyncCallback<int[]>): void-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| blockIndex | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number[]&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [3100204](../errorcode-nfc.md#3100204-nfc-chip-io-exception) |
| [3100201](../errorcode-nfc.md#3100201-tag-readwrite-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |

## restoreFromBlock

```TypeScript
restoreFromBlock(blockIndex: number): Promise<void>
```

Moves the contents of a block into the internal transfer buffer.

**Since:** 12

**Required permissions:** ohos.permission.NFC_TAG

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-MifareClassicTag-restoreFromBlock(blockIndex: int): Promise<void>--><!--Device-MifareClassicTag-restoreFromBlock(blockIndex: int): Promise<void>-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| blockIndex | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [3100204](../errorcode-nfc.md#3100204-nfc-chip-io-exception) |
| [3100201](../errorcode-nfc.md#3100201-tag-readwrite-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |

## restoreFromBlock

```TypeScript
restoreFromBlock(blockIndex: number, callback: AsyncCallback<void>): void
```

Moves the contents of a block into the internal transfer buffer.

**Since:** 12

**Required permissions:** ohos.permission.NFC_TAG

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-MifareClassicTag-restoreFromBlock(blockIndex: int, callback: AsyncCallback<void>): void--><!--Device-MifareClassicTag-restoreFromBlock(blockIndex: int, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| blockIndex | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [3100204](../errorcode-nfc.md#3100204-nfc-chip-io-exception) |
| [3100201](../errorcode-nfc.md#3100201-tag-readwrite-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |

## transferToBlock

```TypeScript
transferToBlock(blockIndex: number): Promise<void>
```

Writes the contents of the internal transfer buffer to a value block.

**Since:** 12

**Required permissions:** ohos.permission.NFC_TAG

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-MifareClassicTag-transferToBlock(blockIndex: int): Promise<void>--><!--Device-MifareClassicTag-transferToBlock(blockIndex: int): Promise<void>-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| blockIndex | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [3100204](../errorcode-nfc.md#3100204-nfc-chip-io-exception) |
| [3100201](../errorcode-nfc.md#3100201-tag-readwrite-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |

## transferToBlock

```TypeScript
transferToBlock(blockIndex: number, callback: AsyncCallback<void>): void
```

Writes the contents of the internal transfer buffer to a value block.

**Since:** 12

**Required permissions:** ohos.permission.NFC_TAG

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-MifareClassicTag-transferToBlock(blockIndex: int, callback: AsyncCallback<void>): void--><!--Device-MifareClassicTag-transferToBlock(blockIndex: int, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| blockIndex | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [3100204](../errorcode-nfc.md#3100204-nfc-chip-io-exception) |
| [3100201](../errorcode-nfc.md#3100201-tag-readwrite-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |

## writeSingleBlock

```TypeScript
writeSingleBlock(blockIndex: number, data: number[]): Promise<void>
```

Writes a block, one block size is 16 bytes.

**Since:** 12

**Required permissions:** ohos.permission.NFC_TAG

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-MifareClassicTag-writeSingleBlock(blockIndex: int, data: int[]): Promise<void>--><!--Device-MifareClassicTag-writeSingleBlock(blockIndex: int, data: int[]): Promise<void>-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| blockIndex | number | Yes |
| data | number[] | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [3100204](../errorcode-nfc.md#3100204-nfc-chip-io-exception) |
| [3100201](../errorcode-nfc.md#3100201-tag-readwrite-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |

## writeSingleBlock

```TypeScript
writeSingleBlock(blockIndex: number, data: number[], callback: AsyncCallback<void>): void
```

Writes a block, one block size is 16 bytes.

**Since:** 12

**Required permissions:** ohos.permission.NFC_TAG

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-MifareClassicTag-writeSingleBlock(blockIndex: int, data: int[], callback: AsyncCallback<void>): void--><!--Device-MifareClassicTag-writeSingleBlock(blockIndex: int, data: int[], callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| blockIndex | number | Yes |
| data | number[] | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [3100204](../errorcode-nfc.md#3100204-nfc-chip-io-exception) |
| [3100201](../errorcode-nfc.md#3100201-tag-readwrite-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |
