# Aperture (System API)

Provides the APIs for aperture settings. It inherits from [ApertureQuery](arkts-camera-camera-aperturequery-i-sys.md#ApertureQuery-(System-API)).

**Inheritance/Implementation:** Aperture extends [ApertureQuery](arkts-camera-camera-aperturequery-i-sys.md#ApertureQuery-(System-API))

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-camera-interface Aperture--><!--Device-camera-interface Aperture-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { camera } from 'camera';
```

## getPhysicalAperture

```TypeScript
getPhysicalAperture(): double
```

Gets current physical aperture value.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-Aperture-getPhysicalAperture(): double--><!--Device-Aperture-getPhysicalAperture(): double-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| double | The current physical aperture value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7400102](../errorcode-camera.md#7400102-invalid-operation) | Operation not allowed, the inputDevice or the session is abnormal.<br>**Applicable version:** 24 and later |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) | Session not config. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System Application.<br>**Applicable version:** 11 - 23 |

## Examples

```TypeScript
function getPhysicalAperture(session: camera.PortraitPhotoSession): number {
  let physicalAperture: number = session.getPhysicalAperture();
  return physicalAperture;
}
```

## getVirtualAperture

```TypeScript
getVirtualAperture(): double
```

Obtains the virtual aperture in use.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-Aperture-getVirtualAperture(): double--><!--Device-Aperture-getVirtualAperture(): double-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| double | Virtual aperture. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) | Session not config. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System Application. |

## Examples

```TypeScript
function getVirtualAperture(session: camera.PortraitPhotoSession): number {
  let virtualAperture: number = session.getVirtualAperture();
  return virtualAperture;
}
```

## setPhysicalAperture

```TypeScript
setPhysicalAperture(aperture: double): void
```

Sets physical aperture value.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-Aperture-setPhysicalAperture(aperture: double): void--><!--Device-Aperture-setPhysicalAperture(aperture: double): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| aperture | double | Yes | physical aperture value. The supported physical aperture range can be obtained by calling [getSupportedPhysicalApertures](arkts-camera-camera-aperturequery-i-sys.md#getSupportedPhysicalApertures) |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7400102](../errorcode-camera.md#7400102-invalid-operation) | Operation not allowed, the inputDevice or the session is abnormal.<br>**Applicable version:** 24 and later |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) | Session not config. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System Application.<br>**Applicable version:** 11 - 23 |

## Examples

```TypeScript
function setPhysicalAperture(session: camera.PortraitPhotoSession, physicalAperture: number): void {
  session.setPhysicalAperture(physicalAperture);
}
```

## setVirtualAperture

```TypeScript
setVirtualAperture(aperture: double): void
```

Sets a virtual aperture. Before the setting, call [getSupportedVirtualApertures](arkts-camera-camera-aperturequery-i-sys.md#getSupportedVirtualApertures) to obtain the supported virtual apertures.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-Aperture-setVirtualAperture(aperture: double): void--><!--Device-Aperture-setVirtualAperture(aperture: double): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| aperture | double | Yes | virtual aperture value |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) | Session not config. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System Application. |

## Examples

```TypeScript
function setVirtualAperture(session: camera.PortraitPhotoSession, virtualAperture: number): void {
  session.setVirtualAperture(virtualAperture);
}
```

