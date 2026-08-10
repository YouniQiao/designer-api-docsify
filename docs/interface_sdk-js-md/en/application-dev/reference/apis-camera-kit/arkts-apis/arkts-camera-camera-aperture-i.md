# Aperture

Provides the APIs for aperture settings. It inherits from [ApertureQuery](arkts-camera-camera-aperturequery-i.md).

**Inheritance/Implementation:** Aperture extends [ApertureQuery](arkts-camera-camera-aperturequery-i.md)

**Since:** 24

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-camera-interface Aperture extends ApertureQuery--><!--Device-camera-interface Aperture extends ApertureQuery-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## Modules to Import

```TypeScript
import { camera } from 'kits/@kit.CameraKit';
```

## getPhysicalAperture

ArkTS-Dyn:
```TypeScript
getPhysicalAperture(): number
```

ArkTS-Sta:
```TypeScript
getPhysicalAperture(): double
```

Gets current physical aperture value.

**Since:** 24

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-Aperture-getPhysicalAperture(): double--><!--Device-Aperture-getPhysicalAperture(): double-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：double | The current physical aperture value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 7400102 | Operation not allowed, the inputDevice or the session is abnormal.<br>**Applicable version:** 24 and later |
| 7400103 | Session not config. |
| 202 | Not System Application.<br>**Applicable version:** 11 - 23 |

## getVirtualAperture

ArkTS-Dyn:
```TypeScript
getVirtualAperture(): number
```

ArkTS-Sta:
```TypeScript
getVirtualAperture(): double
```

Obtains the virtual aperture in use.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-Aperture-getVirtualAperture(): double--><!--Device-Aperture-getVirtualAperture(): double-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：double | Virtual aperture. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 7400103 | Session not config. |
| 202 | Not System Application. |

## Examples

```TypeScript
function getVirtualAperture(session: camera.PortraitPhotoSession): number {
  let virtualAperture: number = session.getVirtualAperture();
  return virtualAperture;
}
```

## setPhysicalAperture

ArkTS-Dyn:
```TypeScript
setPhysicalAperture(aperture: number): void
```

ArkTS-Sta:
```TypeScript
setPhysicalAperture(aperture: double): void
```

Sets physical aperture value.

**Since:** 24

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-Aperture-setPhysicalAperture(aperture: double): void--><!--Device-Aperture-setPhysicalAperture(aperture: double): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| aperture | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | physical aperture value. The supported physical aperture range can be obtained by calling [getSupportedPhysicalApertures](arkts-camera-camera-aperturequery-i.md#getsupportedphysicalapertures) |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 7400102 | Operation not allowed, the inputDevice or the session is abnormal.<br>**Applicable version:** 24 and later |
| 7400103 | Session not config. |
| 202 | Not System Application.<br>**Applicable version:** 11 - 23 |

## setVirtualAperture

ArkTS-Dyn:
```TypeScript
setVirtualAperture(aperture: number): void
```

ArkTS-Sta:
```TypeScript
setVirtualAperture(aperture: double): void
```

Sets a virtual aperture. Before the setting, call  
[getSupportedVirtualApertures](arkts-camera-camera-aperturequery-i.md#getsupportedvirtualapertures) to obtain the supported virtual apertures.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-Aperture-setVirtualAperture(aperture: double): void--><!--Device-Aperture-setVirtualAperture(aperture: double): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| aperture | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | virtual aperture value |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 7400103 | Session not config. |
| 202 | Not System Application. |

## Examples

```TypeScript
function setVirtualAperture(session: camera.PortraitPhotoSession, virtualAperture: number): void {
  session.setVirtualAperture(virtualAperture);
}
```

