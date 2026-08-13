# createMediaKeySystem

## Modules to Import

```TypeScript
import { drm } from '@kit.DrmKit';
```

## createMediaKeySystem

```TypeScript
function createMediaKeySystem(name: string): MediaKeySystem
```

Creates a MediaKeySystem instance.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-drm-function createMediaKeySystem(name: string): MediaKeySystem--><!--Device-drm-function createMediaKeySystem(name: string): MediaKeySystem-End-->

**System capability:** SystemCapability.Multimedia.Drm.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | DRM solution name, for example, **"com.clearplay.drm"**. |

**Return value:**

| Type | Description |
| --- | --- |
| [MediaKeySystem](arkts-drm-drm-mediakeysystem-i.md) | MediaKeySystem instance. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | The parameter check failed. Possibly because: 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| [24700201](../errorcode-drm.md#24700201-service-exception) | Fatal service error, for example, service died. |
| [24700101](../errorcode-drm.md#24700101-unknown-error) | All unknown errors. |
| [24700103](../errorcode-drm.md#24700103-too-many-mediakeysystem-instances) | Meet max MediaKeySystem num limit. |

## Examples

```TypeScript
import { drm } from '@kit.DrmKit';
import { BusinessError } from '@kit.BasicServicesKit';
try {
  let mediaKeySystem: drm.MediaKeySystem = drm.createMediaKeySystem("com.clearplay.drm");
} catch (err) {
  let error = err as BusinessError;
  console.error(`createMediaKeySystem ERROR: ${error}`);  
}
```


## createMediaKeySystem

```TypeScript
function createMediaKeySystem(name: string): MediaKeySystem | undefined
```

Creates a MediaKeySystem instance.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

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
| [401](../../errorcode-universal.md#401-parameter-check-failed) | The parameter check failed. Possibly because: 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| [24700201](../errorcode-drm.md#24700201-service-exception) | Fatal service error, for example, service died. |
| [24700101](../errorcode-drm.md#24700101-unknown-error) | All unknown errors. |
| [24700103](../errorcode-drm.md#24700103-too-many-mediakeysystem-instances) | Meet max MediaKeySystem num limit. |

