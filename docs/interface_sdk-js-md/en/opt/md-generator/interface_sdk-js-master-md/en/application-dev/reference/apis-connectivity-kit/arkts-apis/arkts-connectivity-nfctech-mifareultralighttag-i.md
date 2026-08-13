# MifareUltralightTag

Provides methods for accessing MifareUltralight tag.

**Inheritance/Implementation:** MifareUltralightTag extends TagSession

**Since:** 23

**Deprecated since:** -1

<!--Device-unnamed-export interface MifareUltralightTag--><!--Device-unnamed-export interface MifareUltralightTag-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

## getType

```TypeScript
getType(): tag.MifareUltralightType
```

Gets the type of the MifareUltralight tag.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-MifareUltralightTag-getType(): tag.MifareUltralightType--><!--Device-MifareUltralightTag-getType(): tag.MifareUltralightType-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| tag.MifareUltralightType |

## readMultiplePages

```TypeScript
readMultiplePages(pageIndex: number): Promise<number[]>
```

Reads 4 pages, total is 16 bytes. Page size is 4 bytes.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.NFC_TAG

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-MifareUltralightTag-readMultiplePages(pageIndex: int): Promise<int[]>--><!--Device-MifareUltralightTag-readMultiplePages(pageIndex: int): Promise<int[]>-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| pageIndex | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number[] & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [3100204](../errorcode-nfc.md#3100204-nfc-chip-io-exception) |
| [3100201](../errorcode-nfc.md#3100201-tag-readwrite-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |

## Examples

```TypeScript
import { tag } from '@kit.ConnectivityKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Obtain the correct MIFARE Ultralight tag by using the tag.TagInfo API in @ohos.nfc.tag.

function nfcTechDemo() {
    // Connect the tag if it has not been connected.
    if (!mifareUltralight.isTagConnected()) {
        if (!mifareUltralight.connectTag()) {
            console.error("mifareUltralight connectTag failed.");
            return;
        }
    }

    try {
        let pageIndex = 1; // Set a correct index.
        mifareUltralight.readMultiplePages(pageIndex).then((data : number[]) => {
            console.info("mifareUltralight readMultiplePages Promise data = " + data);
        }).catch((err : BusinessError)=> {
            console.error(`mifareUltralight readMultiplePages Promise Code: ${err.code}, message: ${err.message}`);
        });
    } catch (businessError) {
        console.error(`mifareUltralight readMultiplePages Promise catch businessError Code: ${(businessError as BusinessError).code}, message: ${(businessError as BusinessError).message}`);
    }
}
```

## readMultiplePages

```TypeScript
readMultiplePages(pageIndex: number, callback: AsyncCallback<number[]>): void
```

Reads 4 pages, total is 16 bytes. Page size is 4 bytes.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.NFC_TAG

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-MifareUltralightTag-readMultiplePages(pageIndex: int, callback: AsyncCallback<int[]>): void--><!--Device-MifareUltralightTag-readMultiplePages(pageIndex: int, callback: AsyncCallback<int[]>): void-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| pageIndex | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number[]&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [3100204](../errorcode-nfc.md#3100204-nfc-chip-io-exception) |
| [3100201](../errorcode-nfc.md#3100201-tag-readwrite-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |

## Examples

```TypeScript
import { tag } from '@kit.ConnectivityKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Obtain the correct MIFARE Ultralight tag by using the tag.TagInfo API in @ohos.nfc.tag.

function nfcTechDemo() {
    // Connect the tag if it has not been connected.
    if (!mifareUltralight.isTagConnected()) {
        if (!mifareUltralight.connectTag()) {
            console.error("mifareUltralight connectTag failed.");
            return;
        }
    }

    try {
        let pageIndex = 1; // Set a correct index.
        mifareUltralight.readMultiplePages(pageIndex, (err : BusinessError, data : number[])=> {
            if (err) {
                console.error(`mifareUltralight readMultiplePages AsyncCallback Code: ${err.code}, message: ${err.message}`);
            } else {
                console.info("mifareUltralight readMultiplePages AsyncCallback data: " + data);
            }
        });
    } catch (businessError) {
        console.error(`mifareUltralight readMultiplePages AsyncCallback catch Code: ${(businessError as BusinessError).code}, message: ${(businessError as BusinessError).message}`);
    }
}
```

## writeSinglePage

```TypeScript
writeSinglePage(pageIndex: number, data: number[]): Promise<void>
```

Writes a page, total 4 bytes.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.NFC_TAG

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-MifareUltralightTag-writeSinglePage(pageIndex: int, data: int[]): Promise<void>--><!--Device-MifareUltralightTag-writeSinglePage(pageIndex: int, data: int[]): Promise<void>-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| pageIndex | number | Yes |
| data | number[] | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [3100204](../errorcode-nfc.md#3100204-nfc-chip-io-exception) |
| [3100201](../errorcode-nfc.md#3100201-tag-readwrite-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |

## Examples

```TypeScript
import { tag } from '@kit.ConnectivityKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Obtain the correct MIFARE Ultralight tag by using the tag.TagInfo API in @ohos.nfc.tag.

function nfcTechDemo() {
    // Connect the tag if it has not been connected.
    if (!mifareUltralight.isTagConnected()) {
        if (!mifareUltralight.connectTag()) {
            console.error("mifareUltralight connectTag failed.");
            return;
        }
    }

    try {
        let pageIndex = 1; // Set a correct index.
        let rawData = [0x01, 0x02, 0x03, 0x04]; // Set the correct data. The value must contain 4 bytes.
        mifareUltralight.writeSinglePage(pageIndex, rawData).then(() => {
            console.info("mifareUltralight writeSinglePage Promise success.");
        }).catch((err : BusinessError)=> {
            console.error(`mifareUltralight writeSinglePage Promise err Code: ${err.code}, message: ${err.message}`);
        });
    } catch (businessError) {
        console.error(`mifareUltralight writeSinglePage Promise catch Code: ${(businessError as BusinessError).code}, message: ${(businessError as BusinessError).message}`);
    }
}
```

## writeSinglePage

```TypeScript
writeSinglePage(pageIndex: number, data: number[], callback: AsyncCallback<void>): void
```

Writes a page, total 4 bytes.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.NFC_TAG

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-MifareUltralightTag-writeSinglePage(pageIndex: int, data: int[], callback: AsyncCallback<void>): void--><!--Device-MifareUltralightTag-writeSinglePage(pageIndex: int, data: int[], callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| pageIndex | number | Yes |
| data | number[] | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [3100204](../errorcode-nfc.md#3100204-nfc-chip-io-exception) |
| [3100201](../errorcode-nfc.md#3100201-tag-readwrite-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |

## Examples

```TypeScript
import { tag } from '@kit.ConnectivityKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Obtain the correct MIFARE Ultralight tag by using the tag.TagInfo API in @ohos.nfc.tag.

function nfcTechDemo() {
    // Connect the tag if it has not been connected.
    if (!mifareUltralight.isTagConnected()) {
        if (!mifareUltralight.connectTag()) {
            console.error("mifareUltralight connectTag failed.");
            return;
        }
    }

    try {
        let pageIndex = 1; // Set a correct index.
        let rawData = [0x01, 0x02, 0x03, 0x04];  // Set the correct data. The value must contain 4 bytes.
        mifareUltralight.writeSinglePage(pageIndex, rawData, (err : BusinessError)=> {
        if (err) {
                console.error(`mifareUltralight writeSinglePage AsyncCallback Code: ${err.code}, message: ${err.message}`);
            } else {
                console.info("mifareUltralight writeSinglePage AsyncCallback success.");
            }
        });
    } catch (businessError) {
        console.error(`mifareUltralight writeSinglePage AsyncCallback catch Code: ${(businessError as BusinessError).code}, message: ${(businessError as BusinessError).message}`);
    }
}
```
