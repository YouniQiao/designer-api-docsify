# getMediaKeySystemUuid

## Modules to Import

```TypeScript
import { drm } from 'kits/@kit.DrmKit';
```

## getMediaKeySystemUuid

```TypeScript
function getMediaKeySystemUuid(name: string): string
```

Get a MediaKeySystem's UUID.

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-drm-function getMediaKeySystemUuid(name: string): string--><!--Device-drm-function getMediaKeySystemUuid(name: string): string-End-->

**System capability:** SystemCapability.Multimedia.Drm.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | The Digital Right Management solution name. |

**Return value:**

| Type | Description |
| --- | --- |
| string | The MediaKeySystem uuid. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | The parameter check failed.Possibly because: &lt;br&gt;1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| 24700201 | Fatal service error, for example, service died. |
| 24700101 | All unknown errors. |

## Examples

```TypeScript
import { drm } from '@kit.DrmKit';

let uuid: string = drm.getMediaKeySystemUuid('com.clearplay.drm');
console.info("getMediaKeySystemUuid: ", uuid);
```

