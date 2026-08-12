# offReaderModeWithInterval

## Modules to Import

```TypeScript
import { tag } from '@kit.ConnectivityKit';
```

## offReaderModeWithInterval

```TypeScript
function offReaderModeWithInterval(elementName: ElementName, callback?: Callback<TagInfo>): void
```

Disable foreground reader mode settings explicitly.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Required permissions:** ohos.permission.NFC_TAG

<!--Device-tag-function offReaderModeWithInterval(elementName: ElementName, callback?: Callback<TagInfo>): void--><!--Device-tag-function offReaderModeWithInterval(elementName: ElementName, callback?: Callback<TagInfo>): void-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| elementName | [ElementName](../../apis-ability-kit/arkts-apis/arkts-ability-elementname-i.md) | Yes | The element name of application, must include the bundleName and abilityName. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[TagInfo](arkts-connectivity-tag-taginfo-i.md)&gt; | No | The callback to dispatched the TagInfo object for application. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. |
| [3100203](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-connectivity-kit/errorcode-nfc.md#3100203-incorrect-api-call-sequence) | The off() API can be called only when the on() has been called. |
| [3100201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-connectivity-kit/errorcode-nfc.md#3100201-tag-readwrite-error) | The tag running state is abnormal in the service. |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | Permission denied. |

