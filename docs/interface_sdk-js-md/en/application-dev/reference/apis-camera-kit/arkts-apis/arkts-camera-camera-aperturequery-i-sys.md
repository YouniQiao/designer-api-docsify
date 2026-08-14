# ApertureQuery (System API)

Provides the aperture query capability.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-camera-interface ApertureQuery--><!--Device-camera-interface ApertureQuery-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { camera } from 'camera';
```

## getSupportedPhysicalApertures

```TypeScript
getSupportedPhysicalApertures(): Array<PhysicalAperture>
```

Gets the supported physical apertures. Move to ApertureQuery interface from Aperture since 12.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-ApertureQuery-getSupportedPhysicalApertures(): Array<PhysicalAperture>--><!--Device-ApertureQuery-getSupportedPhysicalApertures(): Array<PhysicalAperture>-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;[PhysicalAperture](arkts-camera-camera-physicalaperture-i-sys.md)&gt; | The array of supported physical apertures. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7400102](../errorcode-camera.md#7400102-invalid-operation) | Operation not allowed, the inputDevice or the session is abnormal.<br>**Applicable version:** 24 and later |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) | Session not config. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System Application.<br>**Applicable version:** 11 - 23 |

## getSupportedVirtualApertures

```TypeScript
getSupportedVirtualApertures(): Array<double>
```

Obtains the supported virtual apertures.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-ApertureQuery-getSupportedVirtualApertures(): Array<double>--><!--Device-ApertureQuery-getSupportedVirtualApertures(): Array<double>-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;double&gt; | Array of virtual apertures supported. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) | Session not config, only throw in session usage. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System Application. |

