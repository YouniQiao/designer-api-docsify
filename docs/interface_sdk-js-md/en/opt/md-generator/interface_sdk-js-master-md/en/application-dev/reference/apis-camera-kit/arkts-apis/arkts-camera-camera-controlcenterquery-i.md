# ControlCenterQuery

ControlCenterQuery is used to check whether the camera controller is supported.

**Since:** 23

**Deprecated since:** -1

<!--Device-camera-interface ControlCenterQuery--><!--Device-camera-interface ControlCenterQuery-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## Modules to Import

```TypeScript
import { camera } from '@kit.CameraKit';
```

## getSupportedEffectTypes

```TypeScript
getSupportedEffectTypes(): Array<ControlCenterEffectType>
```

Obtains the effect types supported by the camera controller.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-ControlCenterQuery-getSupportedEffectTypes(): Array<ControlCenterEffectType>--><!--Device-ControlCenterQuery-getSupportedEffectTypes(): Array<ControlCenterEffectType>-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array&lt;[ControlCenterEffectType](arkts-camera-camera-controlcentereffecttype-e.md)&gt; |

## isControlCenterSupported

```TypeScript
isControlCenterSupported(): boolean
```

Checks whether the camera controller is supported.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-ControlCenterQuery-isControlCenterSupported(): boolean--><!--Device-ControlCenterQuery-isControlCenterSupported(): boolean-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |
