# isMediaKeySystemSupported

## Modules to Import

```TypeScript
import { drm } from 'kits/@kit.DrmKit';
```

## isMediaKeySystemSupported

```TypeScript
function isMediaKeySystemSupported(name: string, mimeType: string, level: ContentProtectionLevel): boolean
```

Judge whether a system that specifies name, mimetype and content protection level is supported.

**Since:** 14

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-drm-function isMediaKeySystemSupported(name: string, mimeType: string, level: ContentProtectionLevel): boolean--><!--Device-drm-function isMediaKeySystemSupported(name: string, mimeType: string, level: ContentProtectionLevel): boolean-End-->

**System capability:** SystemCapability.Multimedia.Drm.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| mimeType | string | Yes |
| level | [ContentProtectionLevel](arkts-drm-drm-contentprotectionlevel-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [24700201](../errorcode-drm.md#24700201-service-exception) |
| [24700101](../errorcode-drm.md#24700101-unknown-error) |

## Examples

```TypeScript
import { drm } from '@kit.DrmKit';

let supported: boolean = drm.isMediaKeySystemSupported('com.clearplay.drm', 'video/avc', drm.ContentProtectionLevel.CONTENT_PROTECTION_LEVEL_SW_CRYPTO);
console.info("isMediaKeySystemSupported: ", supported);
```


## isMediaKeySystemSupported

```TypeScript
function isMediaKeySystemSupported(name: string, mimeType: string): boolean
```

Judge whether a system that specifies name, mimetype is supported.

**Since:** 14

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-drm-function isMediaKeySystemSupported(name: string, mimeType: string): boolean--><!--Device-drm-function isMediaKeySystemSupported(name: string, mimeType: string): boolean-End-->

**System capability:** SystemCapability.Multimedia.Drm.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| mimeType | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [24700201](../errorcode-drm.md#24700201-service-exception) |
| [24700101](../errorcode-drm.md#24700101-unknown-error) |

## Examples

```TypeScript
import { drm } from '@kit.DrmKit';

let supported: boolean = drm.isMediaKeySystemSupported('com.clearplay.drm', 'video/avc');
console.info("isMediaKeySystemSupported: ", supported);
```


## isMediaKeySystemSupported

```TypeScript
function isMediaKeySystemSupported(name: string): boolean
```

Judge whether a system that specifies name is supported.

**Since:** 14

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-drm-function isMediaKeySystemSupported(name: string): boolean--><!--Device-drm-function isMediaKeySystemSupported(name: string): boolean-End-->

**System capability:** SystemCapability.Multimedia.Drm.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [24700201](../errorcode-drm.md#24700201-service-exception) |
| [24700101](../errorcode-drm.md#24700101-unknown-error) |

## Examples

```TypeScript
import { drm } from '@kit.DrmKit';

let supported: boolean = drm.isMediaKeySystemSupported('com.clearplay.drm');
console.info("isMediaKeySystemSupported: ", supported);
```
