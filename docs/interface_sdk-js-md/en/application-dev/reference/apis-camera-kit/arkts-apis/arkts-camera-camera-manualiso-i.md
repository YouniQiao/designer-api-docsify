# ManualIso

ManualIso object.

**Inheritance/Implementation:** ManualIso extends [ManualIsoQuery](arkts-camera-camera-manualisoquery-i.md)

**Since:** 24

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-camera-interface ManualIso extends ManualIsoQuery--><!--Device-camera-interface ManualIso extends ManualIsoQuery-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## Modules to Import

```TypeScript
import { camera } from 'kits/@kit.CameraKit';
```

## getIso

ArkTS-Dyn:
```TypeScript
getIso(): number
```

ArkTS-Sta:
```TypeScript
getIso(): int
```

Gets current ISO.

**Since:** 24

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-ManualIso-getIso(): int--><!--Device-ManualIso-getIso(): int-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：int | The current ISO. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 7400102 | Operation not allowed, the inputDevice or the session is abnormal.<br>**Applicable version:** 24 and later |
| 7400103 | Session not config. |
| 202 | Not System Application.<br>**Applicable version:** 12 - 23 |

## setIso

ArkTS-Dyn:
```TypeScript
setIso(iso: number): void
```

ArkTS-Sta:
```TypeScript
setIso(iso: int): void
```

Sets ISO sensitivity value, within the range of getSupportedIsoRange. This control can not be effective if ExposureMode is set to EXPOSURE_MODE_LOCKED.

**Since:** 24

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-ManualIso-setIso(iso: int): void--><!--Device-ManualIso-setIso(iso: int): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| iso | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | ISO |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 7400101 | Parameter missing or parameter type incorrect.<br>**Applicable version:** 12 - 23 |
| 7400102 | Operation not allowed, the inputDevice or the session is abnormal.<br>**Applicable version:** 24 and later |
| 7400103 | Session not config. |
| 202 | Not System Application.<br>**Applicable version:** 12 - 23 |

