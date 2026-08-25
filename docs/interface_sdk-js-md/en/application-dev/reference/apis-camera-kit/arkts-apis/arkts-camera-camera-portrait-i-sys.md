# Portrait (System API)

Portrait: inherits from [PortraitQuery](arkts-camera-camera-portraitquery-i-sys.md). Provides the APIs for portrait photo settings.

**Inheritance/Implementation:** Portrait extends [PortraitQuery](arkts-camera-camera-portraitquery-i-sys.md)

**Since:** 11

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { camera } from 'kits/@kit.CameraKit';
```

## getPortraitEffect

```TypeScript
getPortraitEffect(): PortraitEffect
```

Obtains the portrait effect in use.

**Since:** 10

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [PortraitEffect](arkts-camera-camera-portraiteffect-e-sys.md) |

**Error codes:**

| Error Code ID |
| --- |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## setPortraitEffect

```TypeScript
setPortraitEffect(effect: PortraitEffect): void
```

Sets a portrait effect. Before the setting, use [getSupportedPortraitEffects](arkts-camera-camera-portraitquery-i-sys.md#getsupportedportraiteffects) to obtain the supported portrait effects and check whether the target portrait effect is supported.

**Since:** 10

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| effect | [PortraitEffect](arkts-camera-camera-portraiteffect-e-sys.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
