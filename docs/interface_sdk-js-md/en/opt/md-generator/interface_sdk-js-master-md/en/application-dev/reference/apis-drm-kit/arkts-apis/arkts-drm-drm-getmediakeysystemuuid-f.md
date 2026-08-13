# getMediaKeySystemUuid

## Modules to Import

```TypeScript
import { drm } from '@kit.DrmKit';
```

## getMediaKeySystemUuid

```TypeScript
function getMediaKeySystemUuid(name: string): string
```

Obtains the UUID of the DRM content protection system supported by the specified DRM solution.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-drm-function getMediaKeySystemUuid(name: string): string--><!--Device-drm-function getMediaKeySystemUuid(name: string): string-End-->

**System capability:** SystemCapability.Multimedia.Drm.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [24700201](../errorcode-drm.md#24700201-service-exception) |
| [24700101](../errorcode-drm.md#24700101-unknown-error) |

## Examples

```TypeScript
import { drm } from '@kit.DrmKit';

let uuid: string = drm.getMediaKeySystemUuid('com.clearplay.drm');
console.info("getMediaKeySystemUuid: ", uuid);
```
