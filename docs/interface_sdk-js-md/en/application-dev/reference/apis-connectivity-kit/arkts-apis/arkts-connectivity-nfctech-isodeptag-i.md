# IsoDepTag

Provides methods for accessing IsoDep tag.

**Inheritance/Implementation:** IsoDepTag extends TagSession

**Since:** 23

<!--Device-unnamed-export interface IsoDepTag--><!--Device-unnamed-export interface IsoDepTag-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

## getHiLayerResponse

```TypeScript
getHiLayerResponse(): int[]
```

Gets IsoDep HiLayer Response bytes of the tag, which is based on NfcB RF technology. It could be null if not based on NfcB.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-IsoDepTag-getHiLayerResponse(): int[]--><!--Device-IsoDepTag-getHiLayerResponse(): int[]-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Return value:**

| Type | Description |
| --- | --- |
| int[] | Returns HiLayer Response bytes, the length could be 0. |

**Examples**

```TypeScript
import { tag } from '@kit.ConnectivityKit';

// Obtain the correct isoDep tag by using the tag.TagInfo API in @ohos.nfc.tag.
let hiLayerResponse : number[] = isoDep.getHiLayerResponse();
console.info("isoDep hiLayerResponse: " + hiLayerResponse);
```

## getHistoricalBytes

```TypeScript
getHistoricalBytes(): int[]
```

Gets IsoDep Historical bytes of the tag, which is based on NfcA RF technology. It could be null if not based on NfcA.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-IsoDepTag-getHistoricalBytes(): int[]--><!--Device-IsoDepTag-getHistoricalBytes(): int[]-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Return value:**

| Type | Description |
| --- | --- |
| int[] | Returns the Historical bytes, the length could be 0. |

**Examples**

```TypeScript
import { tag } from '@kit.ConnectivityKit';

// Obtain the correct isoDep tag by using the tag.TagInfo API in @ohos.nfc.tag.
let historicalBytes : number[] = isoDep.getHistoricalBytes();
console.info("isoDep historicalBytes: " + historicalBytes);
```

## isExtendedApduSupported

```TypeScript
isExtendedApduSupported(): Promise<boolean>
```

Checks if extended apdu length supported or not.

**Since:** 23

**Required permissions:** ohos.permission.NFC_TAG

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-IsoDepTag-isExtendedApduSupported(): Promise<boolean>--><!--Device-IsoDepTag-isExtendedApduSupported(): Promise<boolean>-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Returns true if extended apdu length supported, otherwise false. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | The parameter check failed. Possible causes: <br> 1. Mandatory parameters are left unspecified. <br> 2. Incorrect parameters types. <br> 3. Parameter verification failed. |
| [3100201](../errorcode-nfc.md#3100201-tag-readwrite-error) | The tag running state is abnormal in the service. |
| [3100204](../errorcode-nfc.md#3100204-nfc-chip-io-exception) | The tag I/O operation failed. |

**Examples**

```TypeScript
import { tag } from '@kit.ConnectivityKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Obtain the correct isoDep tag by using the tag.TagInfo API in @ohos.nfc.tag.
function nfcTechDemo() {
    // Connect the tag if it has not been connected.
    if (!isoDep.isTagConnected()) {
        if (!isoDep.connectTag()) {
            console.error("isoDep connectTag failed.");
            return;
        }
    }

    try {
        isoDep.isExtendedApduSupported().then((response: boolean) => {
            console.info("isoDep isExtendedApduSupported Promise response: " + response);
        }).catch((err: BusinessError) => {
            console.error(`isoDep isExtendedApduSupported Promise Code: ${err.code}, message: ${err.message}`);
        });
    } catch (businessError) {
        console.error(`isoDep isExtendedApduSupported Promise Code: ${(businessError as BusinessError).code}, message: ${(businessError as BusinessError).message}`);
    }
}
```

## isExtendedApduSupported

```TypeScript
isExtendedApduSupported(callback: AsyncCallback<boolean>): void
```

Checks if extended apdu length supported or not.

**Since:** 23

**Required permissions:** ohos.permission.NFC_TAG

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-IsoDepTag-isExtendedApduSupported(callback: AsyncCallback<boolean>): void--><!--Device-IsoDepTag-isExtendedApduSupported(callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;boolean&gt; | Yes | The callback. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | The parameter check failed. Possible causes: <br> 1. Mandatory parameters are left unspecified. <br> 2. Incorrect parameters types. <br> 3. Parameter verification failed. |
| [3100201](../errorcode-nfc.md#3100201-tag-readwrite-error) | The tag running state is abnormal in the service. |
| [3100204](../errorcode-nfc.md#3100204-nfc-chip-io-exception) | The Tag I/O operation failed. |

**Examples**

```TypeScript
import { tag } from '@kit.ConnectivityKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Obtain the correct isoDep tag by using the tag.TagInfo API in @ohos.nfc.tag.
function nfcTechDemo() {
    // Connect the tag if it has not been connected.
    if (!isoDep.isTagConnected()) {
        if (!isoDep.connectTag()) {
            console.error("isoDep connectTag failed.");
            return;
        }
    }

    try {
        isoDep.isExtendedApduSupported((err: BusinessError, response: boolean) => {
            if (err) {
                console.error(`isoDep isExtendedApduSupported AsyncCallback Code: ${err.code}, message: ${err. message}`);
            } else {
                console.info("isoDep isExtendedApduSupported AsyncCallback response: " + response);
            }
        });
    } catch (businessError) {
        console.error(`isoDep isExtendedApduSupported AsyncCallback Code: ${(businessError as Business).code}, message: ${(businessError as Business).message}`);
    }
}
```

