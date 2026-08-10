# createMediaKeySystem

## Modules to Import

```TypeScript
import { drm } from 'kits/@kit.DrmKit';
```

## createMediaKeySystem

```TypeScript
function createMediaKeySystem(name: string): MediaKeySystem
```

Creates a MediaKeySystem instance.

**Since:** 14

**ArkTS mode:** ArkTS-Dyn only, since version 14.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-drm-function createMediaKeySystem(name: string): MediaKeySystem--><!--Device-drm-function createMediaKeySystem(name: string): MediaKeySystem-End-->

**System capability:** SystemCapability.Multimedia.Drm.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | Used to point a Digital Right Management solution. |

**Return value:**

| Type | Description |
| --- | --- |
| [MediaKeySystem](arkts-drm-drm-mediakeysystem-i.md) | The MediaKeySystem instance. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | The parameter check failed. Possibly because: 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| 24700201 | Fatal service error, for example, service died. |
| 24700101 | All unknown errors. |
| 24700103 | Meet max MediaKeySystem num limit. |

## Examples

```TypeScript
import { drm } from '@kit.DrmKit';
// name indicates the DRM solution name. You can obtain the DRM solution name supported by the device through the drm.getMediaKeySystems API, for example, **com.clearplay.drm**.
let name = 'com.clearplay.drm';
let mediaKeySystem: drm.MediaKeySystem = drm.createMediaKeySystem(name);
console.info(`createMediaKeySystem success, name: ${name}`);
```


## createMediaKeySystem

```TypeScript
function createMediaKeySystem(name: string): MediaKeySystem | undefined
```

Creates a MediaKeySystem instance.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-drm-function createMediaKeySystem(name: string): MediaKeySystem | undefined--><!--Device-drm-function createMediaKeySystem(name: string): MediaKeySystem | undefined-End-->

**System capability:** SystemCapability.Multimedia.Drm.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | Used to point a Digital Right Management solution. |

**Return value:**

| Type | Description |
| --- | --- |
| [MediaKeySystem](arkts-drm-drm-mediakeysystem-i.md) | The MediaKeySystem instance or undefined. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | The parameter check failed. Possibly because: 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| 24700201 | Fatal service error, for example, service died. |
| 24700101 | All unknown errors. |
| 24700103 | Meet max MediaKeySystem num limit. |

