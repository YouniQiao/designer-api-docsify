# Stabilization

**Stabilization** inherits from [StabilizationQuery](arkts-camera-camera-stabilizationquery-i.md).

It provides APIs to set video stabilization.

You can set video stabilization only when a [VideoOutput](arkts-camera-camera-videooutput-i.md) stream exists in the session.

**Inheritance/Implementation:** Stabilization extends [StabilizationQuery](arkts-camera-camera-stabilizationquery-i.md)

**Since:** 11

<!--Device-camera-interface Stabilization extends StabilizationQuery--><!--Device-camera-interface Stabilization extends StabilizationQuery-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## Modules to Import

```TypeScript
import { camera } from 'kits/@kit.CameraKit';
```

## getActiveVideoStabilizationMode

```TypeScript
getActiveVideoStabilizationMode(): VideoStabilizationMode
```

Obtains the video stabilization mode in use.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-Stabilization-getActiveVideoStabilizationMode(): VideoStabilizationMode--><!--Device-Stabilization-getActiveVideoStabilizationMode(): VideoStabilizationMode-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [VideoStabilizationMode](arkts-camera-camera-videostabilizationmode-e.md) |

**Error codes:**

| Error Code ID |
| --- |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) |

## setVideoStabilizationMode

```TypeScript
setVideoStabilizationMode(mode: VideoStabilizationMode): void
```

Sets a video stabilization mode. Before the setting, call   
[isVideoStabilizationModeSupported](arkts-camera-camera-stabilizationquery-i.md#isvideostabilizationmodesupported) to check whether the target video stabilization mode is supported. It is recommended that you set the video stabilization mode between [commitConfig](arkts-camera-camera-session-i.md#commitconfig) and [Start](arkts-camera-camera-session-i.md#start).

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-Stabilization-setVideoStabilizationMode(mode: VideoStabilizationMode): void--><!--Device-Stabilization-setVideoStabilizationMode(mode: VideoStabilizationMode): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mode | [VideoStabilizationMode](arkts-camera-camera-videostabilizationmode-e.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) |
