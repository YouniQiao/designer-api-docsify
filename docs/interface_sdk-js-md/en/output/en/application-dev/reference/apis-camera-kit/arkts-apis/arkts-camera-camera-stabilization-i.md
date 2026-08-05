# Stabilization

**Stabilization** inherits from [StabilizationQuery]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_. It provides APIs to set video stabilization. You can set video stabilization only when a [VideoOutput]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ stream exists in the session.

**Inheritance/Implementation:** Stabilization extends [StabilizationQuery](arkts-camera-camera-stabilizationquery-i.md)

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-camera-interface Stabilization extends StabilizationQuery--><!--Device-camera-interface Stabilization extends StabilizationQuery-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

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
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | Video stabilization mode obtained. If the API call fails, undefined is |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) | Session not config. |

## setVideoStabilizationMode

```TypeScript
setVideoStabilizationMode(mode: VideoStabilizationMode): void
```

Sets a video stabilization mode. Before the setting, call [isVideoStabilizationModeSupported]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ to check whether the target video stabilization mode is supported. It is recommended that you set the video stabilization mode between [commitConfig]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ and [Start]\_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-Stabilization-setVideoStabilizationMode(mode: VideoStabilizationMode): void--><!--Device-Stabilization-setVideoStabilizationMode(mode: VideoStabilizationMode): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mode | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Video stabilization mode. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) | Session not config. |

