# ColorEffectQuery (System API)

Provides the API to obtain the color effects supported.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-camera-interface ColorEffectQuery--><!--Device-camera-interface ColorEffectQuery-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { camera } from 'kits/@kit.CameraKit';
```

## getSupportedColorEffects

```TypeScript
getSupportedColorEffects(): Array<ColorEffectType>
```

Obtains the supported color effects.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-ColorEffectQuery-getSupportedColorEffects(): Array<ColorEffectType>--><!--Device-ColorEffectQuery-getSupportedColorEffects(): Array<ColorEffectType>-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;ColorEffectType&gt; | Array of color effects supported. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) | Session not config, only throw in session usage. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System Application. |

## Examples

```TypeScript
function getSupportedColorEffects(session: camera.PhotoSessionForSys): Array<camera.ColorEffectType> {
  let colorEffects: Array<camera.ColorEffectType> = session.getSupportedColorEffects();
  return colorEffects;
}
```

