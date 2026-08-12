# ColorEffect (System API)

ColorEffect extends [ColorEffectQuery](arkts-camera-camera-coloreffectquery-i-sys.md#ColorEffectQuery)Provides the APIs to obtain and set the lens color effect.

**Inheritance/Implementation:** ColorEffect extends [ColorEffectQuery](arkts-camera-camera-coloreffectquery-i-sys.md#ColorEffectQuery)

**Since:** 11

<!--Device-camera-interface ColorEffect extends ColorEffectQuery--><!--Device-camera-interface ColorEffect extends ColorEffectQuery-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { camera } from '@kit.CameraKit';
```

## getColorEffect

```TypeScript
getColorEffect(): ColorEffectType
```

Obtains the color effect in use.

**Since:** 11

<!--Device-ColorEffect-getColorEffect(): ColorEffectType--><!--Device-ColorEffect-getColorEffect(): ColorEffectType-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ColorEffectType](arkts-camera-camera-coloreffecttype-e-sys.md) |

**Error codes:**

| Error Code ID |
| --- |
| [7400103](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-camera-kit/errorcode-camera.md#7400103-session-not-configured) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
function getColorEffect(session: camera.PhotoSessionForSys): camera.ColorEffectType {
  let colorEffect: camera.ColorEffectType = session.getColorEffect();
  return colorEffect;
}
```

## setColorEffect

```TypeScript
setColorEffect(type: ColorEffectType): void
```

Sets a color effect. Before the setting, call  
[getSupportedColorEffects](arkts-camera-camera-coloreffectquery-i-sys.md#getSupportedColorEffects) to obtain the supported color effects.

**Since:** 11

<!--Device-ColorEffect-setColorEffect(type: ColorEffectType): void--><!--Device-ColorEffect-setColorEffect(type: ColorEffectType): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | [ColorEffectType](arkts-camera-camera-coloreffecttype-e-sys.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [7400103](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-camera-kit/errorcode-camera.md#7400103-session-not-configured) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
function setColorEffect(session: camera.PhotoSessionForSys, colorEffect: camera.ColorEffectType): void {
  session.setColorEffect(colorEffect);
}
```
