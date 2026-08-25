# PortraitQuery (System API)

Queries portrait parameters.

**Since:** 12

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { camera } from 'kits/@kit.CameraKit';
```

## getSupportedPortraitEffects

```TypeScript
getSupportedPortraitEffects(): Array<PortraitEffect>
```

Obtains the supported portrait effects.

**Since:** 10

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array&lt;[PortraitEffect](arkts-camera-camera-portraiteffect-e-sys.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
