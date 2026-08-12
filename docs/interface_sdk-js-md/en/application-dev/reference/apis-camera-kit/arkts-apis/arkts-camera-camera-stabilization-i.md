# Stabilization

**Stabilization** inherits from [StabilizationQuery](arkts-camera-camera-stabilizationquery-i.md#StabilizationQuery).

It provides APIs to set video stabilization.

You can set video stabilization only when a [VideoOutput](arkts-camera-camera-videooutput-i.md#VideoOutput) stream exists in the session.

**Inheritance/Implementation:** Stabilization extends [StabilizationQuery](arkts-camera-camera-stabilizationquery-i.md#StabilizationQuery)

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-camera-interface Stabilization extends StabilizationQuery--><!--Device-camera-interface Stabilization extends StabilizationQuery-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## Modules to Import

```TypeScript
import { camera } from '@kit.CameraKit';
```

## getActiveVideoStabilizationMode

```TypeScript
getActiveVideoStabilizationMode(): VideoStabilizationMode
```

Obtains the video stabilization mode in use.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-Stabilization-getActiveVideoStabilizationMode(): VideoStabilizationMode--><!--Device-Stabilization-getActiveVideoStabilizationMode(): VideoStabilizationMode-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Return value:**

| Type | Description |
| --- | --- |
| [VideoStabilizationMode](arkts-camera-camera-videostabilizationmode-e.md) | Video stabilization mode obtained. If the API call fails, undefined is returned. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7400103](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-camera-kit/errorcode-camera.md#7400103-session-not-configured) | Session not config. |

## setVideoStabilizationMode

```TypeScript
setVideoStabilizationMode(mode: VideoStabilizationMode): void
```

Sets a video stabilization mode. Before the setting, call   
[isVideoStabilizationModeSupported](arkts-camera-camera-stabilizationquery-i.md#isVideoStabilizationModeSupported) to check whether the target video stabilization mode is supported. It is recommended that you set the video stabilization mode between [commitConfig](arkts-camera-camera-session-i.md#commitConfig) and [Start](arkts-camera-camera-session-i.md#start).

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-Stabilization-setVideoStabilizationMode(mode: VideoStabilizationMode): void--><!--Device-Stabilization-setVideoStabilizationMode(mode: VideoStabilizationMode): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mode | [VideoStabilizationMode](arkts-camera-camera-videostabilizationmode-e.md) | Yes | Video stabilization mode. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7400103](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-camera-kit/errorcode-camera.md#7400103-session-not-configured) | Session not config. |

