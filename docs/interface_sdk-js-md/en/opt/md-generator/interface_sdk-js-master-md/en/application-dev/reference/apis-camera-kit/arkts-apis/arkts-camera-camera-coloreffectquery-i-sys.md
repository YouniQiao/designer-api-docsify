# ColorEffectQuery (System API)

Provides the API to obtain the color effects supported.

**Since:** 23

**Deprecated since:** -1

<!--Device-camera-interface ColorEffectQuery--><!--Device-camera-interface ColorEffectQuery-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { camera } from '@kit.CameraKit';
```

## getSupportedColorEffects

```TypeScript
getSupportedColorEffects(): Array<ColorEffectType>
```

Obtains the supported color effects.

**Since:** 23

**Deprecated since:** -1

<!--Device-ColorEffectQuery-getSupportedColorEffects(): Array<ColorEffectType>--><!--Device-ColorEffectQuery-getSupportedColorEffects(): Array<ColorEffectType>-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array&lt;[ColorEffectType](arkts-camera-camera-coloreffecttype-e-sys.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
function getSupportedColorEffects(session: camera.PhotoSessionForSys): Array<camera.ColorEffectType> {
  let colorEffects: Array<camera.ColorEffectType> = session.getSupportedColorEffects();
  return colorEffects;
}
```
