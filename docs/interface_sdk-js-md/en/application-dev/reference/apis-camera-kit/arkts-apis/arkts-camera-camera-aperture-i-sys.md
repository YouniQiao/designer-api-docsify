# Aperture

Provides the APIs for aperture settings. It inherits from [ApertureQuery](arkts-camera-camera-aperturequery-i.md).

**Inheritance/Implementation:** Aperture extends [ApertureQuery](arkts-camera-camera-aperturequery-i.md)

**Since:** 24

**System capability:** SystemCapability.Multimedia.Camera.Core

## Modules to Import

```TypeScript
import { camera } from 'kits/@kit.CameraKit';
```

## getVirtualAperture

```TypeScript
getVirtualAperture(): number
```

Obtains the virtual aperture in use.

**Since:** 11

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) |

## setVirtualAperture

```TypeScript
setVirtualAperture(aperture: number): void
```

Sets a virtual aperture. Before the setting, call [getSupportedVirtualApertures](arkts-camera-camera-aperturequery-i-sys.md#getsupportedvirtualapertures) to obtain the supported virtual apertures.

**Since:** 11

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [aperture](arkts-camera-camera-apertureinfo-i-sys.md) | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) |
