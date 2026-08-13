# BarcodeTag

Provides methods for accessing Barcode tag.

**Inheritance/Implementation:** BarcodeTag extends TagSession

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-export interface BarcodeTag--><!--Device-unnamed-export interface BarcodeTag-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

## getBarcode

```TypeScript
getBarcode(): Promise<ArrayBuffer>
```

Returns the barcode of a Barcode tag.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Required permissions:** ohos.permission.NFC_TAG

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-BarcodeTag-getBarcode(): Promise<ArrayBuffer>--><!--Device-BarcodeTag-getBarcode(): Promise<ArrayBuffer>-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;ArrayBuffer&gt; | The barcode of tag. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [3100204](../errorcode-nfc.md#3100204-nfc-chip-io-exception) | The tag I/O operation failed. |
| [3100201](../errorcode-nfc.md#3100201-tag-readwrite-error) | The tag running state is abnormal in the service. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |

