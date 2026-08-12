# BarcodeTag

Provides methods for accessing Barcode tag.

**Inheritance/Implementation:** BarcodeTag extends [TagSession](TagSession)

**Since:** 18

<!--Device-unnamed-export interface BarcodeTag extends TagSession--><!--Device-unnamed-export interface BarcodeTag extends TagSession-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

## getBarcode

```TypeScript
getBarcode(): Promise<ArrayBuffer>
```

Returns the barcode of a Barcode tag.

**Since:** 18

**Required permissions:** ohos.permission.NFC_TAG

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-BarcodeTag-getBarcode(): Promise<ArrayBuffer>--><!--Device-BarcodeTag-getBarcode(): Promise<ArrayBuffer>-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;ArrayBuffer & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [3100204](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-connectivity-kit/errorcode-nfc.md#3100204-nfc-chip-io-exception) |
| [3100201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-connectivity-kit/errorcode-nfc.md#3100201-tag-readwrite-error) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
