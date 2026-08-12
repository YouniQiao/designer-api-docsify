# ToneAttrs

Tone attributes.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-systemSoundManager-interface ToneAttrs--><!--Device-systemSoundManager-interface ToneAttrs-End-->

**System capability:** SystemCapability.Multimedia.SystemSound.Core

## Modules to Import

```TypeScript
import { systemSoundManager } from '@kit.AudioKit';
```

## getCategory

ArkTS-Dyn:
```TypeScript
getCategory(): number
```

ArkTS-Sta:
```TypeScript
getCategory(): int
```

Gets tone category.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-ToneAttrs-getCategory(): int--><!--Device-ToneAttrs-getCategory(): int-End-->

**System capability:** SystemCapability.Multimedia.SystemSound.Core

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：int | Tone category. This value can be one of { |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Caller is not a system application. |

## Examples

```TypeScript
toneAttrs.getCategory();
```

## getCustomizedType

```TypeScript
getCustomizedType(): ToneCustomizedType
```

Gets customized type of tone.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-ToneAttrs-getCustomizedType(): ToneCustomizedType--><!--Device-ToneAttrs-getCustomizedType(): ToneCustomizedType-End-->

**System capability:** SystemCapability.Multimedia.SystemSound.Core

**Return value:**

| Type | Description |
| --- | --- |
| [ToneCustomizedType](arkts-audio-systemsoundmanager-tonecustomizedtype-e.md) | Customized type of tone. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Caller is not a system application. |

## Examples

```TypeScript
toneAttrs.getCustomizedType();
```

## getFileName

```TypeScript
getFileName(): string
```

Gets file name of tone.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-ToneAttrs-getFileName(): string--><!--Device-ToneAttrs-getFileName(): string-End-->

**System capability:** SystemCapability.Multimedia.SystemSound.Core

**Return value:**

| Type | Description |
| --- | --- |
| string | file name. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Caller is not a system application. |

## Examples

```TypeScript
toneAttrs.getFileName();
```

## getMediaType

```TypeScript
getMediaType(): MediaType
```

Gets media type. This function returns [AUDIO](arkts-audio-systemsoundmanager-mediatype-e.md#AUDIO) if the media type has not been changed by [setMediaType](#setMediaType).

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-ToneAttrs-getMediaType(): MediaType--><!--Device-ToneAttrs-getMediaType(): MediaType-End-->

**System capability:** SystemCapability.Multimedia.SystemSound.Core

**Return value:**

| Type | Description |
| --- | --- |
| MediaType | Media type. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Caller is not a system application. |

## Examples

```TypeScript
toneAttrs.getMediaType();
```

## getTitle

```TypeScript
getTitle(): string
```

Gets title of tone.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-ToneAttrs-getTitle(): string--><!--Device-ToneAttrs-getTitle(): string-End-->

**System capability:** SystemCapability.Multimedia.SystemSound.Core

**Return value:**

| Type | Description |
| --- | --- |
| string | title. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Caller is not a system application. |

## Examples

```TypeScript
toneAttrs.getTitle();
```

## getUri

```TypeScript
getUri(): string
```

Gets uri of tone.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-ToneAttrs-getUri(): string--><!--Device-ToneAttrs-getUri(): string-End-->

**System capability:** SystemCapability.Multimedia.SystemSound.Core

**Return value:**

| Type | Description |
| --- | --- |
| string | uri. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Caller is not a system application. |

## Examples

```TypeScript
toneAttrs.getUri();
```

## setCategory

ArkTS-Dyn:
```TypeScript
setCategory(category: number): void
```

ArkTS-Sta:
```TypeScript
setCategory(category: int): void
```

Sets tone category.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-ToneAttrs-setCategory(category: int): void--><!--Device-ToneAttrs-setCategory(category: int): void-End-->

**System capability:** SystemCapability.Multimedia.SystemSound.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| category | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | tone category. This parameter can be one of [TONE_CATEGORY_RINGTONE](arkts-audio-systemsoundmanager-con-sys.md#TONE_CATEGORY_RINGTONE), [TONE_CATEGORY_TEXT_MESSAGE](arkts-audio-systemsoundmanager-con-sys.md#TONE_CATEGORY_TEXT_MESSAGE), [TONE_CATEGORY_NOTIFICATION](arkts-audio-systemsoundmanager-con-sys.md#TONE_CATEGORY_NOTIFICATION), [TONE_CATEGORY_ALARM](arkts-audio-systemsoundmanager-con-sys.md#TONE_CATEGORY_ALARM). In addition, this parameter can be result of OR logical operator of these constants. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Caller is not a system application. |

## Examples

```TypeScript
let toneAttrs = systemSoundManager.createCustomizedToneAttrs();
let categoryValue = systemSoundManager.TONE_CATEGORY_ALARM; // Change the value to the required constant.
toneAttrs.setCategory(categoryValue);
```

## setFileName

```TypeScript
setFileName(name: string): void
```

Sets file name of tone.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-ToneAttrs-setFileName(name: string): void--><!--Device-ToneAttrs-setFileName(name: string): void-End-->

**System capability:** SystemCapability.Multimedia.SystemSound.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | file name. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Caller is not a system application. |

## Examples

```TypeScript
let toneAttrs = systemSoundManager.createCustomizedToneAttrs();
let fileName = 'textFileName';
toneAttrs.setFileName(fileName);
```

## setMediaType

```TypeScript
setMediaType(type: MediaType): void
```

Sets media type.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-ToneAttrs-setMediaType(type: MediaType): void--><!--Device-ToneAttrs-setMediaType(type: MediaType): void-End-->

**System capability:** SystemCapability.Multimedia.SystemSound.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | MediaType | Yes | Target media type. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Caller is not a system application. |

## Examples

```TypeScript
let type: systemSoundManager.MediaType = systemSoundManager.MediaType.VIDEO; // Use the required type.
let toneAttrs = systemSoundManager.createCustomizedToneAttrs();
toneAttrs.setMediaType(type);
```

## setTitle

```TypeScript
setTitle(title: string): void
```

Sets title of tone.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-ToneAttrs-setTitle(title: string): void--><!--Device-ToneAttrs-setTitle(title: string): void-End-->

**System capability:** SystemCapability.Multimedia.SystemSound.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| title | string | Yes | Title of tone. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Caller is not a system application. |

## Examples

```TypeScript
let toneAttrs = systemSoundManager.createCustomizedToneAttrs();
let title = 'text';
toneAttrs.setTitle(title);
```

