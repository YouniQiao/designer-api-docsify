# OIS

OIS (Optical Image Stabilization) interface.

**Inheritance/Implementation:** OIS extends [OISQuery](arkts-camera-camera-oisquery-i.md#oisquery)

**Since:** 24

<!--Device-camera-interface OIS--><!--Device-camera-interface OIS-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## Modules to Import

```TypeScript
```

## setOISMode

```TypeScript
setOISMode(mode: OISMode): void
```

Sets the OIS mode.

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-OIS-setOISMode(mode: OISMode): void--><!--Device-OIS-setOISMode(mode: OISMode): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mode | [OISMode](arkts-camera-camera-oismode-e.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [7400102](../errorcode-camera.md#7400102-invalid-operation) |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) |

## setOISModeCustom

```TypeScript
setOISModeCustom(pitch: number, yaw: number): void
```

Sets custom OIS bias values for each axis.

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-OIS-setOISModeCustom(pitch: double, yaw: double): void--><!--Device-OIS-setOISModeCustom(pitch: double, yaw: double): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| pitch | number | Yes |
| yaw | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [7400102](../errorcode-camera.md#7400102-invalid-operation) |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) |
