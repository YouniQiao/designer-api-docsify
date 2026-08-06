# StabilizationQuery

StabilizationQuery provides APIs to check the support for video stabilization.
    **NOTE**  
    
    - This interface was first introduced in API version 12. In this version, a compatibility change was made that  
    preserved the initial version information of inner elements. As a result, you might see outer element's @since  
    version number being higher than that of the inner elements. However, this discrepancy does not affect the  
    functionality of the interface.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-camera-interface StabilizationQuery--><!--Device-camera-interface StabilizationQuery-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## isVideoStabilizationModeSupported

```TypeScript
isVideoStabilizationModeSupported(vsMode: VideoStabilizationMode): boolean
```

Checks whether a video stabilization mode is supported.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-StabilizationQuery-isVideoStabilizationModeSupported(vsMode: VideoStabilizationMode): boolean--><!--Device-StabilizationQuery-isVideoStabilizationModeSupported(vsMode: VideoStabilizationMode): boolean-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| vsMode | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Video stabilization mode. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Check result for the support of the video stabilization mode. **true** if supported, **false** otherwise. If the operation fails, undefined is returned and an error code defined in [CameraErrorCode]{ |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) | Session not config, only throw in session usage. |

