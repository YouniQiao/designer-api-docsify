# ColorReservation (System API)

ColorReservation extends [ColorReservationQuery](arkts-camera-camera-colorreservationquery-i-sys.md) Provides API for obtaining and setting a color reservation type.

**Inheritance/Implementation:** ColorReservation extends [ColorReservationQuery](arkts-camera-camera-colorreservationquery-i-sys.md)

**Since:** 15

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { camera } from 'kits/@kit.CameraKit';
```

## getColorReservation

```TypeScript
getColorReservation(): ColorReservationType
```

Obtains the color reservation type in use.

**Since:** 15

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ColorReservationType](arkts-camera-camera-colorreservationtype-e-sys.md) |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) |

## setColorReservation

```TypeScript
setColorReservation(type: ColorReservationType): void
```

Sets a color reservation type. Before the setting, call [getSupportedColorReservationTypes](arkts-camera-camera-colorreservationquery-i-sys.md#getsupportedcolorreservationtypes) to obtain the supported color reservation types.

**Since:** 15

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | [ColorReservationType](arkts-camera-camera-colorreservationtype-e-sys.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [7400102](../errorcode-camera.md#7400102-invalid-operation) |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) |
| [7400201](../errorcode-camera.md#7400201-camera-service-error) |
