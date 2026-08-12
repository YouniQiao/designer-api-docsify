# getNdefFormatable

## Modules to Import

```TypeScript
import { tag } from '@kit.ConnectivityKit';
```

## getNdefFormatable

```TypeScript
function getNdefFormatable(tagInfo: TagInfo): NdefFormatableTag
```

Obtains an [NdefFormatableTag](arkts-connectivity-tag-ndefformatabletag-t.md#NdefFormatableTag) object based on the tag information.During tag reading, if the tag supports the NDEF Formatable technology,an [NdefFormatableTag](arkts-connectivity-tag-ndefformatabletag-t.md#NdefFormatableTag) object will be created based on the tag information.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-tag-function getNdefFormatable(tagInfo: TagInfo): NdefFormatableTag--><!--Device-tag-function getNdefFormatable(tagInfo: TagInfo): NdefFormatableTag-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| tagInfo | [TagInfo](arkts-connectivity-tag-taginfo-i.md) | Yes | Indicates the dispatched tag information. |

**Return value:**

| Type | Description |
| --- | --- |
| NdefFormatableTag | The { |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | The parameter check failed. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |
| [801](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. |
| [3100201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-connectivity-kit/errorcode-nfc.md#3100201-tag-readwrite-error) | The tag running state is abnormal in the service. |

