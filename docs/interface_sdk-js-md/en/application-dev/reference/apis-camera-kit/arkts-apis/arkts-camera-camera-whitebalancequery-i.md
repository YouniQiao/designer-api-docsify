# WhiteBalanceQuery (System API)

WhiteBalanceQuery provides APIs to check whether a white balance mode is supported and obtain the white balance mode range supported.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-camera-interface WhiteBalanceQuery--><!--Device-camera-interface WhiteBalanceQuery-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { camera } from '@kit.CameraKit';
```

## getColorTintRange

```TypeScript
getColorTintRange(): Array<int>
```

Obtains the supported white balance hue adjustment range.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-WhiteBalanceQuery-getColorTintRange(): Array<int>--><!--Device-WhiteBalanceQuery-getColorTintRange(): Array<int>-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;int&gt; | Hue adjustment range. If the API call fails, **undefined** is returned. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) | Session not config, only throw in session usage. |

