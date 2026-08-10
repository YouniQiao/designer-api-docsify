# offReaderModeWithInterval

## Modules to Import

```TypeScript
import { tag } from 'kits/@kit.ConnectivityKit';
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
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;TagInfo&gt; | No | The callback to dispatched the TagInfo object for application. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported. |
| 3100203 | The off() API can be called only when the on() has been called. |
| 3100201 | The tag running state is abnormal in the service. |
| 201 | Permission denied. |

