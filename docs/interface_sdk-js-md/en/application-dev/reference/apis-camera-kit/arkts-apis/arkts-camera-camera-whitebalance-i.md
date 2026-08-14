# WhiteBalance (System API)

**WhiteBalance** inherits from [WhiteBalanceQuery](arkts-camera-camera-whitebalancequery-i.md#WhiteBalanceQuery-(System-API)). It provides APIs to process white balance, including obtaining and setting the white balance mode and white balance value.

**Inheritance/Implementation:** WhiteBalance extends [WhiteBalanceQuery](arkts-camera-camera-whitebalancequery-i.md#WhiteBalanceQuery-(System-API))

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-camera-interface WhiteBalance--><!--Device-camera-interface WhiteBalance-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { camera } from 'camera';
```

## getColorTint

```TypeScript
getColorTint(): int
```

Gets current color tint.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-WhiteBalance-getColorTint(): int--><!--Device-WhiteBalance-getColorTint(): int-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Return value:**

| Type | Description |
| --- | --- |
| int | The current color tint. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) | Session not config. |

## setColorTint

```TypeScript
setColorTint(colorTint: int): void
```

Sets color tint.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-WhiteBalance-setColorTint(colorTint: int): void--><!--Device-WhiteBalance-setColorTint(colorTint: int): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| colorTint | int | Yes | Color tint, the supported range can be obtained by calling [getColorTintRange](arkts-camera-camera-whitebalancequery-i.md#getColorTintRange). |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) | Session not config. |

