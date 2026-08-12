# getMifareUltralight

## Modules to Import

```TypeScript
import { tag } from '@kit.ConnectivityKit';
```

## getMifareUltralight

```TypeScript
function getMifareUltralight(tagInfo: TagInfo): MifareUltralightTag
```

Obtains an [MifareUltralightTag](arkts-connectivity-tag-mifareultralighttag-t.md#MifareUltralightTag) object based on the tag information.During tag reading, if the tag supports the MIFARE Ultralight technology,an [MifareUltralightTag](arkts-connectivity-tag-mifareultralighttag-t.md#MifareUltralightTag) object will be created based on the tag information.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-tag-function getMifareUltralight(tagInfo: TagInfo): MifareUltralightTag--><!--Device-tag-function getMifareUltralight(tagInfo: TagInfo): MifareUltralightTag-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| tagInfo | [TagInfo](arkts-connectivity-tag-taginfo-i.md) | Yes | Indicates the dispatched tag information. |

**Return value:**

| Type | Description |
| --- | --- |
| MifareUltralightTag | The { |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | The parameter check failed. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |
| [801](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. |
| [3100201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-connectivity-kit/errorcode-nfc.md#3100201-tag-readwrite-error) | The tag running state is abnormal in the service. |

