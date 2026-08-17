# NdefTag

Provides methods for accessing NDEF tag.

**Inheritance/Implementation:** NdefTag extends TagSession

**Since:** 23

<!--Device-unnamed-export interface NdefTag--><!--Device-unnamed-export interface NdefTag-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

## canSetReadOnly

```TypeScript
canSetReadOnly(): boolean
```

Checks NDEF tag can be set read-only.

**Since:** 23

**Required permissions:** ohos.permission.NFC_TAG

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-NdefTag-canSetReadOnly(): boolean--><!--Device-NdefTag-canSetReadOnly(): boolean-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns true if the tag can be set readonly, otherwise returns false. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [3100201](../errorcode-nfc.md#3100201-tag-readwrite-error) | The tag running state is abnormal in the service. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |

**Examples**

```TypeScript
import { tag } from '@kit.ConnectivityKit';

// Obtain the correct ndefTag tag by using the tag.TagInfo API in @ohos.nfc.tag.
let canSetReadOnly : boolean = ndefTag.canSetReadOnly();
console.info("ndef canSetReadOnly: " + canSetReadOnly);
```

## getNdefMessage

```TypeScript
getNdefMessage(): NdefMessage
```

Gets the NDEF message that was read from NDEF tag when tag discovery.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-NdefTag-getNdefMessage(): NdefMessage--><!--Device-NdefTag-getNdefMessage(): NdefMessage-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Return value:**

| Type | Description |
| --- | --- |
| [NdefMessage](arkts-connectivity-nfctech-ndefmessage-i.md) | The instance of NdefMessage. |

## getNdefTagType

```TypeScript
getNdefTagType(): tag.NfcForumType
```

Gets the type of NDEF tag.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-NdefTag-getNdefTagType(): tag.NfcForumType--><!--Device-NdefTag-getNdefTagType(): tag.NfcForumType-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Return value:**

| Type | Description |
| --- | --- |
| tag.NfcForumType | The type of NDEF tag. |

## getNdefTagTypeString

```TypeScript
getNdefTagTypeString(type: tag.NfcForumType): string
```

Converts the NFC forum type into string defined in NFC forum.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-NdefTag-getNdefTagTypeString(type: tag.NfcForumType): string--><!--Device-NdefTag-getNdefTagTypeString(type: tag.NfcForumType): string-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | tag.NfcForumType | Yes | NFC forum type of NDEF tag. |

**Return value:**

| Type | Description |
| --- | --- |
| string | The NFC forum string type. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | The parameter check failed. Possible causes: <br> 1. Mandatory parameters are left unspecified. <br> 2. Incorrect parameters types. <br> 3. Parameter verification failed. |

## isNdefWritable

```TypeScript
isNdefWritable(): boolean
```

Checks if NDEF tag is writable.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-NdefTag-isNdefWritable(): boolean--><!--Device-NdefTag-isNdefWritable(): boolean-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns true if the tag is writable, otherwise returns false. |

**Examples**

```TypeScript
import { tag } from '@kit.ConnectivityKit';

// Obtain the correct ndefTag tag by using the tag.TagInfo API in @ohos.nfc.tag.
let isWritable : boolean = ndefTag.isNdefWritable();
console.info("ndef isNdefWritable: " + isWritable);
```

## readNdef

```TypeScript
readNdef(): Promise<NdefMessage>
```

Reads NDEF message on this tag.

**Since:** 23

**Required permissions:** ohos.permission.NFC_TAG

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-NdefTag-readNdef(): Promise<NdefMessage>--><!--Device-NdefTag-readNdef(): Promise<NdefMessage>-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[NdefMessage](arkts-connectivity-nfctech-ndefmessage-i.md)&gt; | The NDEF message in tag. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | The parameter check failed. Possible causes: <br> 1. Mandatory parameters are left unspecified. <br> 2. Incorrect parameters types. <br> 3. Parameter verification failed. |
| [3100204](../errorcode-nfc.md#3100204-nfc-chip-io-exception) | The tag I/O operation failed. |
| [3100201](../errorcode-nfc.md#3100201-tag-readwrite-error) | The tag running state is abnormal in the service. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |

## readNdef

```TypeScript
readNdef(callback: AsyncCallback<NdefMessage>): void
```

Reads NDEF message on this tag.

**Since:** 23

**Required permissions:** ohos.permission.NFC_TAG

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-NdefTag-readNdef(callback: AsyncCallback<NdefMessage>): void--><!--Device-NdefTag-readNdef(callback: AsyncCallback<NdefMessage>): void-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[NdefMessage](arkts-connectivity-nfctech-ndefmessage-i.md)&gt; | Yes | The callback. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | The parameter check failed. Possible causes: <br> 1. Mandatory parameters are left unspecified. <br> 2. Incorrect parameters types. <br> 3. Parameter verification failed. |
| [3100204](../errorcode-nfc.md#3100204-nfc-chip-io-exception) | The Tag I/O operation failed. |
| [3100201](../errorcode-nfc.md#3100201-tag-readwrite-error) | The tag running state is abnormal in the service. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |

## setReadOnly

```TypeScript
setReadOnly(): Promise<void>
```

Sets the NDEF tag read-only.

**Since:** 23

**Required permissions:** ohos.permission.NFC_TAG

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-NdefTag-setReadOnly(): Promise<void>--><!--Device-NdefTag-setReadOnly(): Promise<void>-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | The void |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | The parameter check failed. Possible causes: <br> 1. Mandatory parameters are left unspecified. <br> 2. Incorrect parameters types. <br> 3. Parameter verification failed. |
| [3100204](../errorcode-nfc.md#3100204-nfc-chip-io-exception) | The tag I/O operation failed. |
| [3100201](../errorcode-nfc.md#3100201-tag-readwrite-error) | The tag running state is abnormal in the service. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |

**Examples**

```TypeScript
import { tag } from '@kit.ConnectivityKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Obtain the correct ndefTag tag by using the tag.TagInfo API in @ohos.nfc.tag.

function nfcTechDemo() {
    // Connect the tag if it has not been connected.
    if (!ndefTag.isTagConnected()) {
        if (!ndefTag.connectTag()) {
            console.error("ndefTag connectTag failed.");
            return;
        }
    }

    try {
        ndefTag.setReadOnly().then(() => {
            console.info("ndef setReadOnly Promise success.");
        }).catch((err : BusinessError)=> {
            console.error("ndef setReadOnly Promise err Code: ${err.code}, message: ${err.message}");
        });
    } catch (businessError) {
        console.error(`ndef setReadOnly Promise catch businessError Code: ${(businessError as BusinessError).code}, message: ${(businessError as BusinessError).message}`);
    }
}
```

## setReadOnly

```TypeScript
setReadOnly(callback: AsyncCallback<void>): void
```

Sets the NDEF tag read-only.

**Since:** 23

**Required permissions:** ohos.permission.NFC_TAG

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-NdefTag-setReadOnly(callback: AsyncCallback<void>): void--><!--Device-NdefTag-setReadOnly(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | The callback. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | The parameter check failed. Possible causes: <br> 1. Mandatory parameters are left unspecified. <br> 2. Incorrect parameters types. <br> 3. Parameter verification failed. |
| [3100204](../errorcode-nfc.md#3100204-nfc-chip-io-exception) | The Tag I/O operation failed. |
| [3100201](../errorcode-nfc.md#3100201-tag-readwrite-error) | The tag running state is abnormal in the service. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |

**Examples**

```TypeScript
import { tag } from '@kit.ConnectivityKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Obtain the correct ndefTag tag by using the tag.TagInfo API in @ohos.nfc.tag.

function nfcTechDemo() {
    // Connect the tag if it has not been connected.
    if (!ndefTag.isTagConnected()) {
        if (!ndefTag.connectTag()) {
            console.error("ndefTag connectTag failed.");
            return;
        }
    }

    try {
        ndefTag.setReadOnly((err : BusinessError)=> {
            if (err) {
                console.error(`ndef setReadOnly AsyncCallback err Code: ${err.code}, message: ${err.message}`);
            } else {
                console.info("ndef setReadOnly AsyncCallback success.");
            }
        });
    } catch (businessError) {
        console.error(`ndef setReadOnly AsyncCallback catch businessError Code: ${(businessError as BusinessError).code}, message: ${(businessError as BusinessError).message}`);
    }
}
```

## writeNdef

```TypeScript
writeNdef(msg: NdefMessage): Promise<void>
```

Writes NDEF message into this tag.

**Since:** 23

**Required permissions:** ohos.permission.NFC_TAG

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-NdefTag-writeNdef(msg: NdefMessage): Promise<void>--><!--Device-NdefTag-writeNdef(msg: NdefMessage): Promise<void>-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| msg | [NdefMessage](arkts-connectivity-nfctech-ndefmessage-i.md) | Yes | The NDEF message to be written. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | The void |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | The parameter check failed. Possible causes: <br> 1. Mandatory parameters are left unspecified. <br> 2. Incorrect parameters types. <br> 3. Parameter verification failed. |
| [3100204](../errorcode-nfc.md#3100204-nfc-chip-io-exception) | The tag I/O operation failed. |
| [3100201](../errorcode-nfc.md#3100201-tag-readwrite-error) | The tag running state is abnormal in the service. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |

## writeNdef

```TypeScript
writeNdef(msg: NdefMessage, callback: AsyncCallback<void>): void
```

Writes NDEF message into this tag.

**Since:** 23

**Required permissions:** ohos.permission.NFC_TAG

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-NdefTag-writeNdef(msg: NdefMessage, callback: AsyncCallback<void>): void--><!--Device-NdefTag-writeNdef(msg: NdefMessage, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| msg | [NdefMessage](arkts-connectivity-nfctech-ndefmessage-i.md) | Yes | The NDEF message to be written. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | The callback. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | The parameter check failed. Possible causes: <br> 1. Mandatory parameters are left unspecified. <br> 2. Incorrect parameters types. <br> 3. Parameter verification failed. |
| [3100204](../errorcode-nfc.md#3100204-nfc-chip-io-exception) | The Tag I/O operation failed. |
| [3100201](../errorcode-nfc.md#3100201-tag-readwrite-error) | The tag running state is abnormal in the service. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |

