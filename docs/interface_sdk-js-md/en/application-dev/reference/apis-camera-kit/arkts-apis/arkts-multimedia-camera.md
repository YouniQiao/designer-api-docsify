# @ohos.multimedia.camera(AutoDeviceSwitch)

The module provides a set of camera service APIs for you to easily develop a camera application. The application can access and operate the camera hardware to implement basic operations, such as preview, taking photos, and recording videos. It can also perform more operations, for example, controlling the flash and exposure time, and focusing or adjusting the focus.

> **NOTE：**
> 
> - This topic describes only system APIs provided by the module. For details about its public APIs, see
> [@ohos.multimedia.camera (Camera Management)](arkts-multimedia-camera.md).

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-unnamed-declare namespace camera--><!--Device-unnamed-declare namespace camera-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## Modules to Import

```TypeScript
import { camera } from 'kits/@kit.CameraKit';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [getCameraManager](arkts-camera-camera-getcameramanager-f.md#getcameramanager) | Obtains a CameraManager instance. This API returns the result synchronously. |

<!--Del-->
### Classes（系统接口）

| Name | Description |
| --- | --- |
| [EffectSuggestionStatus](arkts-camera-camera-effectsuggestionstatus-c-sys.md) | Effect suggestion status |
<!--DelEnd-->

### Interfaces

| Name | Description |
| --- | --- |
| [Aperture](arkts-camera-camera-aperture-i.md) | Provides the APIs for aperture settings. It inherits from [ApertureQuery](arkts-camera-camera-aperturequery-i.md). |
| [ApertureQuery](arkts-camera-camera-aperturequery-i.md) | Provides the aperture query capability. |
| [AutoDeviceSwitch](arkts-camera-camera-autodeviceswitch-i.md) | **AutoDeviceSwitch** inherits from [AutoDeviceSwitchQuery](arkts-camera-camera-autodeviceswitchquery-i.md) and is used to enable or disable automatic camera switch. This capability can be used only on foldable devices. For details about the development, see  [Practices for Automatic Camera Switching (ArkTS)](../../../media/camera/camera-auto-switch.md).  It is recommended that the system automatically handle input device switching, session configuration, and parameter continuity during automatic camera switch. If the system detects that the zoom ranges of the two cameras are different during camera switching, it will notify the application through the **isDeviceCapabilityChanged** field in [AutoDeviceSwitchStatus](arkts-camera-camera-autodeviceswitchstatus-i.md). However, the application still needs to handle the UX change. For example, for the zoom range adjustment, the application needs to call  [getZoomRatioRange](arkts-camera-camera-zoomquery-i.md#getzoomratiorange) to obtain data and update the UX. Therefore,  **AutoDeviceSwitch** is more applicable to simplified UX interactions. |
| [AutoDeviceSwitchQuery](arkts-camera-camera-autodeviceswitchquery-i.md) | **AutoDeviceSwitchQuery** is used to check whether a device supports automatic camera switch.  [Automatic Camera Switching](arkts-camera-camera-autodeviceswitch-i.md#enableautodeviceswitch) is supported only on foldable devices. For details about how to enable this capability, see  [enableAutoDeviceSwitch](arkts-camera-camera-autodeviceswitch-i.md#enableautodeviceswitch). |
| [AutoDeviceSwitchStatus](arkts-camera-camera-autodeviceswitchstatus-i.md) | Describes the information about the automatic camera switch status. |
| [AutoExposure](arkts-camera-camera-autoexposure-i.md) | **AutoExposure** inherits from [AutoExposureQuery](arkts-camera-camera-autoexposurequery-i.md).  It provides APIs related to auto exposure. |
| [AutoExposureQuery](arkts-camera-camera-autoexposurequery-i.md) | AutoExposureQuery provides APIs to query the automatic exposure feature of a camera device.  >  > - In this version, a compatibility change was made that preserved the initial version information of inner > elements. As a result, you might see outer element's @since version number being higher than that of the inner > elements. However, this discrepancy does not affect the functionality of the interface. |
| [CameraConcurrentInfo](arkts-camera-camera-cameraconcurrentinfo-i.md) | Describes the camera's concurrency information. |
| [CameraDevice](arkts-camera-camera-cameradevice-i.md) | Describes the camera device information. |
| [CameraInput](arkts-camera-camera-camerainput-i.md) | **CameraInput** defines the camera input object.  It provides camera device information used in [Session](arkts-camera-camera-session-i.md). |
| [CameraManager](arkts-camera-camera-cameramanager-i.md) | **CameraManager** implements camera management. Before calling any API in **CameraManager**, you must use  [getCameraManager](arkts-camera-camera-getcameramanager-f.md#getcameramanager) to obtain a **CameraManager** instance. |
| [CameraOcclusionDetectionResult](arkts-camera-camera-cameraocclusiondetectionresult-i.md) | Describes the instance returned by the occlusion status callback, which indicates whether the camera lens is blocked or dirty. |
| [CameraOutput](arkts-camera-camera-cameraoutput-i.md) | CameraOutput implements output information used in [Session](arkts-camera-camera-session-i.md). It is the base class of  **output**. |
| [CameraOutputCapability](arkts-camera-camera-cameraoutputcapability-i.md) | Describes the camera output capability. |
| [CameraStatusInfo](arkts-camera-camera-camerastatusinfo-i.md) | Describes the camera status information. |
| [CaptureEndInfo](arkts-camera-camera-captureendinfo-i.md) | Describes the capture end information. |
| [CapturePhoto](arkts-camera-camera-capturephoto-i.md) | **CapturePhoto** provides APIs for obtaining the objects of the full-quality image and the uncompressed image. |
| [CaptureSession](arkts-camera-camera-capturesession-i.md) | **CaptureSession** implements a capture session, which saves all [CameraInput](arkts-camera-camera-camerainput-i.md) and  [CameraOutput](arkts-camera-camera-cameraoutput-i.md) instances required to run the camera and requests the camera to complete shooting or video recording. |
| [CaptureStartInfo](arkts-camera-camera-capturestartinfo-i.md) | Describes the capture start information. |
| [ColorManagement](arkts-camera-camera-colormanagement-i.md) | **ColorManagement** inherits from [ColorManagementQuery](arkts-camera-camera-colormanagementquery-i.md).  It provides the APIs for color space settings. |
| [ColorManagementQuery](arkts-camera-camera-colormanagementquery-i.md) | ColorManagementQuery provides the APIs for color space query. |
| [ControlCenter](arkts-camera-camera-controlcenter-i.md) | **ControlCenter** inherits from [ControlCenterQuery](arkts-camera-camera-controlcenterquery-i.md).  It is used to enable the camera controller. |
| [ControlCenterQuery](arkts-camera-camera-controlcenterquery-i.md) | ControlCenterQuery is used to check whether the camera controller is supported. |
| [ControlCenterStatusInfo](arkts-camera-camera-controlcenterstatusinfo-i.md) | Describes the effect status information of a camera controller. |
| [ExposureInfo](arkts-camera-camera-exposureinfo-i.md) | Describes the exposure information object. |
| [Flash](arkts-camera-camera-flash-i.md) | **Flash** inherits from [FlashQuery](arkts-camera-camera-flashquery-i.md).  It provides APIs related to the flash. |
| [FlashQuery](arkts-camera-camera-flashquery-i.md) | FlashQuery provides APIs to query the flash status and mode of a camera device.  > **NOTE：** >  > - This interface was first introduced in API version 12. In this version, a compatibility change was made that > preserved the initial version information of inner elements. As a result, you might see outer element's @since > version number being higher than that of the inner elements. However, this discrepancy does not affect the > functionality of the interface. |
| [Focus](arkts-camera-camera-focus-i.md) | **Focus** inherits from [FocusQuery](arkts-camera-camera-focusquery-i.md).  It provides APIs related to focus operations. |
| [FocusQuery](arkts-camera-camera-focusquery-i.md) | FocusQuery provides APIs to check whether a focus mode is supported.  > **NOTE：** >  > - This interface was first introduced in API version 12. In this version, a compatibility change was made that > preserved the initial version information of inner elements. As a result, you might see outer element's @since > version number being higher than that of the inner elements. However, this discrepancy does not affect the > functionality of the interface. |
| [FoldStatusInfo](arkts-camera-camera-foldstatusinfo-i.md) | Describes the fold state information about a foldable device. |
| [FrameRateRange](arkts-camera-camera-frameraterange-i.md) | Describes the frame rate range. |
| [FrameShutterEndInfo](arkts-camera-camera-frameshutterendinfo-i.md) | Describes the frame shutter end information during capture. |
| [FrameShutterInfo](arkts-camera-camera-frameshutterinfo-i.md) | Describes the frame shutter information. |
| [IsoInfo](arkts-camera-camera-isoinfo-i.md) | Describes the information about the sensitivity (ISO) settings. |
| [Location](arkts-camera-camera-location-i.md) | Describes the geolocation information. |
| [Macro](arkts-camera-camera-macro-i.md) | **Macro** inherits from [MacroQuery](arkts-camera-camera-macroquery-i.md).  It provides the API to enable macro photography. |
| [MacroQuery](arkts-camera-camera-macroquery-i.md) | MacroQuery provides the API to check the support for macro photography. |
| [ManualExposure](arkts-camera-camera-manualexposure-i.md) | ManualExposure extends [ManualExposureQuery](arkts-camera-camera-manualexposurequery-i.md)Provides APIs to obtain and set the exposure duration. |
| [ManualExposureQuery](arkts-camera-camera-manualexposurequery-i.md) | Provides APIs to obtain the manual exposure range supported. |
| [ManualFocus](arkts-camera-camera-manualfocus-i.md) | ManualFocus object. |
| [ManualFocusQuery](arkts-camera-camera-manualfocusquery-i.md) | Manual Focus Query object. |
| [ManualIso](arkts-camera-camera-manualiso-i.md) | ManualIso object. |
| [ManualIsoQuery](arkts-camera-camera-manualisoquery-i.md) | Provides APIs to check whether a camera device supports manual ISO setting and obtain the ISO range supported by the device. |
| [MetadataBarcodeObject](arkts-camera-camera-metadatabarcodeobject-i.md) | Barcode metadata detected by the camera, which is extended from [MetadataObject](arkts-camera-camera-metadataobject-i.md). It serves as the data source of the camera information in [CameraInput](arkts-camera-camera-camerainput-i.md). It is obtained by calling metadataOutput.  [on('metadataObjectsAvailable')](camera.MetadataOutput.on(type: 'metadataObjectsAvailable', callback: AsyncCallback&lt;Array<MetadataObject>&gt;&lt;MetadataObject&gt;>)). |
| [MetadataBasicFaceObject](arkts-camera-camera-metadatabasicfaceobject-i.md) | Basic face metadata detected by the camera, which is extended from [MetadataObject](arkts-camera-camera-metadataobject-i.md). It serves as the data source of the camera information in [CameraInput](arkts-camera-camera-camerainput-i.md). It is obtained by calling metadataOutput.  [on('metadataObjectsAvailable')](camera.MetadataOutput.on(type: 'metadataObjectsAvailable', callback: AsyncCallback&lt;Array<MetadataObject>&gt;&lt;MetadataObject&gt;>)). |
| [MetadataCatBodyObject](arkts-camera-camera-metadatacatbodyobject-i.md) | Cat body metadata detected by the camera, which is extended from [MetadataObject](arkts-camera-camera-metadataobject-i.md). It serves as the data source of the camera information in [CameraInput](arkts-camera-camera-camerainput-i.md). It is obtained by calling metadataOutput.  [on('metadataObjectsAvailable')](camera.MetadataOutput.on(type: 'metadataObjectsAvailable', callback: AsyncCallback&lt;Array<MetadataObject>&gt;&lt;MetadataObject&gt;>)). |
| [MetadataCatFaceObject](arkts-camera-camera-metadatacatfaceobject-i.md) | Cat face metadata detected by the camera, which is extended from [MetadataObject](arkts-camera-camera-metadataobject-i.md). It serves as the data source of the camera information in [CameraInput](arkts-camera-camera-camerainput-i.md). It is obtained by calling metadataOutput.  [on('metadataObjectsAvailable')](camera.MetadataOutput.on(type: 'metadataObjectsAvailable', callback: AsyncCallback&lt;Array<MetadataObject>&gt;&lt;MetadataObject&gt;>)). |
| [MetadataDogBodyObject](arkts-camera-camera-metadatadogbodyobject-i.md) | Dog body metadata detected by the camera, which is extended from [MetadataObject](arkts-camera-camera-metadataobject-i.md). It serves as the data source of the camera information in [CameraInput](arkts-camera-camera-camerainput-i.md). It is obtained by calling metadataOutput.  [on('metadataObjectsAvailable')](camera.MetadataOutput.on(type: 'metadataObjectsAvailable', callback: AsyncCallback&lt;Array<MetadataObject>&gt;&lt;MetadataObject&gt;>)). |
| [MetadataDogFaceObject](arkts-camera-camera-metadatadogfaceobject-i.md) | Dog face metadata detected by the camera, which is extended from [MetadataObject](arkts-camera-camera-metadataobject-i.md). It serves as the data source of the camera information in [CameraInput](arkts-camera-camera-camerainput-i.md). It is obtained by calling metadataOutput.  [on('metadataObjectsAvailable')](camera.MetadataOutput.on(type: 'metadataObjectsAvailable', callback: AsyncCallback&lt;Array<MetadataObject>&gt;&lt;MetadataObject&gt;>)). |
| [MetadataFaceObject](arkts-camera-camera-metadatafaceobject-i.md) | Face metadata detected by the camera, which is extended from [MetadataObject](arkts-camera-camera-metadataobject-i.md). It serves as the data source of the camera information in [CameraInput](arkts-camera-camera-camerainput-i.md). It is obtained by calling metadataOutput.  [on('metadataObjectsAvailable')](camera.MetadataOutput.on(type: 'metadataObjectsAvailable', callback: AsyncCallback&lt;Array<MetadataObject>&gt;&lt;MetadataObject&gt;>)). |
| [MetadataHumanBodyObject](arkts-camera-camera-metadatahumanbodyobject-i.md) | Human body metadata detected by the camera, which is extended from [MetadataObject](arkts-camera-camera-metadataobject-i.md). It serves as the data source of the camera information in [CameraInput](arkts-camera-camera-camerainput-i.md). It is obtained by calling metadataOutput.  [on('metadataObjectsAvailable')](camera.MetadataOutput.on(type: 'metadataObjectsAvailable', callback: AsyncCallback&lt;Array<MetadataObject>&gt;&lt;MetadataObject&gt;>)). |
| [MetadataObject](arkts-camera-camera-metadataobject-i.md) | Describes the camera metadata, which is the data source of [CameraInput](arkts-camera-camera-camerainput-i.md). The metadata is obtained through **metadataOutput.on('metadataObjectsAvailable')**. |
| [MetadataOutput](arkts-camera-camera-metadataoutput-i.md) | MetadataOutput implements metadata streams. It inherits from [CameraOutput](arkts-camera-camera-cameraoutput-i.md). |
| [MetadataSalientDetectionObject](arkts-camera-camera-metadatasalientdetectionobject-i.md) | Salient subject metadata detected by the camera, which is extended from  [MetadataObject](arkts-camera-camera-metadataobject-i.md). It serves as the data source of the camera information in  [CameraInput](arkts-camera-camera-camerainput-i.md). It is obtained by calling metadataOutput.  [on('metadataObjectsAvailable')](camera.MetadataOutput.on(type: 'metadataObjectsAvailable', callback: AsyncCallback&lt;Array<MetadataObject>&gt;&lt;MetadataObject&gt;>)). |
| [OIS](arkts-camera-camera-ois-i.md) | OIS (Optical Image Stabilization) interface. |
| [OISQuery](arkts-camera-camera-oisquery-i.md) | OIS (Optical Image Stabilization) query interface. |
| [Photo](arkts-camera-camera-photo-i.md) | Photo defines a full-quality image object. |
| [PhotoCaptureSetting](arkts-camera-camera-photocapturesetting-i.md) | Describes the settings for taking an image. |
| [PhotoConflictFunctions](arkts-camera-camera-photoconflictfunctions-i.md) | Photo Conflict Functions object. |
| [PhotoFunctions](arkts-camera-camera-photofunctions-i.md) | Photo Functions object. |
| [PhotoOutput](arkts-camera-camera-photooutput-i.md) | PhotoOutput implements output information used in a photo session. It inherits from  [CameraOutput](arkts-camera-camera-cameraoutput-i.md). |
| [PhotoSession](arkts-camera-camera-photosession-i.md) | **PhotoSession** inherits from [Session](arkts-camera-camera-session-i.md), [Flash](arkts-camera-camera-flash-i.md),  [AutoExposure](arkts-camera-camera-autoexposure-i.md), [WhiteBalance](arkts-camera-camera-whitebalance-i.md), [Focus](arkts-camera-camera-focus-i.md),  [Zoom](arkts-camera-camera-zoom-i.md), [ColorManagement](arkts-camera-camera-colormanagement-i.md),  [AutoDeviceSwitch](arkts-camera-camera-autodeviceswitch-i.md), [Macro](arkts-camera-camera-macro-i.md),  [ManualExposure](../../../reference/apis-camera-kit/arkts-apis-camera-ManualExposure.md),  [ManualFocus](../../../reference/apis-camera-kit/arkts-apis-camera-ManualFocus.md),  [ManualIso](../../../reference/apis-camera-kit/arkts-apis-camera-ManualIso.md),  [OIS](../../../reference/apis-camera-kit/arkts-apis-camera-OIS.md), and  [Aperture](../../../reference/apis-camera-kit/arkts-apis-camera-Aperture.md).  It implements a photo session, which provides operations on the flash, exposure, white balance, focus, zoom, color space, macro mode, manual exposure, manual focus, manual ISO setting, optical image stabilization (OIS), and aperture.  **PhotoSession** is provided for the default photo mode. It is used to take standard photos. It supports multiple photo formats and resolutions, which are suitable for most daily photo capture scenarios. |
| [PhotoSessionForSys](arkts-camera-camera-photosessionforsys-i.md) | Implements a photo session for system applications, which sets the parameters of the normal photo mode and saves all [CameraInput](arkts-camera-camera-camerainput-i.md) and [CameraOutput](arkts-camera-camera-cameraoutput-i.md)instances required to run the camera. It inherits from [Session](arkts-camera-camera-session-i.md). |
| [PhysicalAperture](arkts-camera-camera-physicalaperture-i.md) | Describes the physical aperture object. |
| [Point](arkts-camera-camera-point-i.md) | Describes the point coordinates, which are used for focus and exposure configuration. |
| [PortraitPhotoConflictFunctions](arkts-camera-camera-portraitphotoconflictfunctions-i.md) | Portrait Photo Conflict Functions object. |
| [PortraitPhotoFunctions](arkts-camera-camera-portraitphotofunctions-i.md) | Portrait Photo Functions object. |
| [PreviewOutput](arkts-camera-camera-previewoutput-i.md) | PreviewOutput implements preview output. It inherits from [CameraOutput](arkts-camera-camera-cameraoutput-i.md). |
| [Profile](arkts-camera-camera-profile-i.md) | Describes the camera profile. |
| [Rect](arkts-camera-camera-rect-i.md) | Describes a rectangle. The coordinate system for the returned detection points is based on the landscape device orientation, with the charging port on the right. In this coordinate system, the top-left corner is (0, 0), and the bottom-right corner is (1, 1). Here, **topLeftX** and **topLeftY** represent the coordinates of the top-left corner of the rectangle, whereas **width** and **height** represent the width and height of the rectangle, respectively. When cropping or selecting a face region based on specific requirements, the x and y coordinates of the rectangle must be multiplied by the width and height of the actual camera preview output stream to obtain the cropped face region.  The width and height of the actual preview stream refer to the resolution of the camera output stream. For details,see **size** in [profile](arkts-camera-camera-profile-i.md).  For details about how to obtain the preview stream data, see  [Dual-Channel Preview (ArkTS)](../../../media/camera/camera-dual-channel-preview.md). |
| [SecureSession](arkts-camera-camera-securesession-i.md) | **SecureSession** inherits from [Session](arkts-camera-camera-session-i.md), [Flash](arkts-camera-camera-flash-i.md),  [AutoExposure](arkts-camera-camera-autoexposure-i.md), [WhiteBalance](arkts-camera-camera-whitebalance-i.md), [Focus](arkts-camera-camera-focus-i.md), and [Zoom](arkts-camera-camera-zoom-i.md).  It implements a secure session, which provides operations on the flash, exposure, white balance, focus, and zoom.  You can call [createSession](arkts-camera-camera-cameramanager-i.md#createsession) with [SceneMode](arkts-camera-camera-scenemode-e.md) set to **SECURE_PHOTO** to create a session in secure mode. The secure mode is designed for applications with high security requirements, such as facial recognition systems and banking services. It must be used together with the &lt;!--RP1--&gt;security TA&lt;!--RP1End--&gt; to support service scenarios where both standard preview streams and security streams are output.&lt;!--RP2--&gt;  The security TA can verify the signature of data delivered by the server, sign images, parse and assemble TLV logic, and read, create, and operate keys. It applies to image processing.&lt;!--RP2End--&gt; |
| [Session](arkts-camera-camera-session-i.md) | **Session** implements a session, which saves all [CameraInput](arkts-camera-camera-camerainput-i.md) and  [CameraOutput](arkts-camera-camera-cameraoutput-i.md) instances required to run the camera and requests the camera to take a photo or record a video. |
| [Size](arkts-camera-camera-size-i.md) | Describes the image dimensions. |
| [SmoothZoomInfo](arkts-camera-camera-smoothzoominfo-i.md) | Describes the smooth zoom information. |
| [Stabilization](arkts-camera-camera-stabilization-i.md) | **Stabilization** inherits from [StabilizationQuery](arkts-camera-camera-stabilizationquery-i.md).  It provides APIs to set video stabilization.  You can set video stabilization only when a [VideoOutput](arkts-camera-camera-videooutput-i.md) stream exists in the session. |
| [StabilizationQuery](arkts-camera-camera-stabilizationquery-i.md) | StabilizationQuery provides APIs to check the support for video stabilization.  > **NOTE：** >  > - This interface was first introduced in API version 12. In this version, a compatibility change was made that > preserved the initial version information of inner elements. As a result, you might see outer element's @since > version number being higher than that of the inner elements. However, this discrepancy does not affect the > functionality of the interface. |
| [TorchStatusInfo](arkts-camera-camera-torchstatusinfo-i.md) | Describes the flashlight status information. |
| [VideoConflictFunctions](arkts-camera-camera-videoconflictfunctions-i.md) | Video Conflict Functions object. |
| [VideoFunctions](arkts-camera-camera-videofunctions-i.md) | Video Functions object. |
| [VideoOutput](arkts-camera-camera-videooutput-i.md) | VideoOutput implements output information used in a video session. It inherits from  [CameraOutput](arkts-camera-camera-cameraoutput-i.md). |
| [VideoProfile](arkts-camera-camera-videoprofile-i.md) | Describes the video configuration information. It inherits from [Profile](arkts-camera-camera-profile-i.md). |
| [VideoSession](arkts-camera-camera-videosession-i.md) | VideoSession inherits from [Session](arkts-camera-camera-session-i.md), [Flash](arkts-camera-camera-flash-i.md),  [AutoExposure](arkts-camera-camera-autoexposure-i.md), [WhiteBalance](arkts-camera-camera-whitebalance-i.md), [Focus](arkts-camera-camera-focus-i.md),  [Zoom](arkts-camera-camera-zoom-i.md), [Stabilization](arkts-camera-camera-stabilization-i.md),  [ColorManagement](arkts-camera-camera-colormanagement-i.md), [AutoDeviceSwitch](arkts-camera-camera-autodeviceswitch-i.md),  [Macro](arkts-camera-camera-macro-i.md), [ControlCenter](arkts-camera-camera-controlcenter-i.md),  [ManualExposure](../../../reference/apis-camera-kit/arkts-apis-camera-ManualExposure.md),  [ManualFocus](../../../reference/apis-camera-kit/arkts-apis-camera-ManualFocus.md),  [ManualIso](../../../reference/apis-camera-kit/arkts-apis-camera-ManualIso.md),  [OIS](../../../reference/apis-camera-kit/arkts-apis-camera-OIS.md), and  [Aperture](../../../reference/apis-camera-kit/arkts-apis-camera-Aperture.md).  It implements a video session, which provides operations on the flash, exposure, white balance, focus, zoom, video stabilization, color space, macro mode and controller, manual exposure, manual focus, manual ISO, optical image stabilization, and aperture.  **VideoSession** is provided for the default video recording mode. It applies to common scenarios. It supports recording at various resolutions (such as 720p and 1080p) and frame rates (such as 30 fps and 60 fps). |
| [VideoSessionForSys](arkts-camera-camera-videosessionforsys-i.md) | Implements a video session for system applications, which sets the parameters of the normal video mode and saves all [CameraInput](arkts-camera-camera-camerainput-i.md) and [CameraOutput](arkts-camera-camera-cameraoutput-i.md)instances required to run the camera. It inherits from [Session](arkts-camera-camera-session-i.md). |
| [WhiteBalance](arkts-camera-camera-whitebalance-i.md) | **WhiteBalance** inherits from [WhiteBalanceQuery](arkts-camera-camera-whitebalancequery-i.md).  It provides APIs to process white balance, including obtaining and setting the white balance mode and white balance value. |
| [WhiteBalanceQuery](arkts-camera-camera-whitebalancequery-i.md) | WhiteBalanceQuery provides APIs to check whether a white balance mode is supported and obtain the white balance mode range supported. |
| [Zoom](arkts-camera-camera-zoom-i.md) | **Zoom** inherits from [ZoomQuery](arkts-camera-camera-zoomquery-i.md).  It provides APIs related to zoom operations. |
| [ZoomPointInfo](arkts-camera-camera-zoompointinfo-i.md) | Describes the equivalent focal length information. |
| [ZoomQuery](arkts-camera-camera-zoomquery-i.md) | ZoomQuery provides APIs to query the zoom feature of a device camera, including the API to obtain the supported zoom ratio range.  > **NOTE：** >  > - This interface was first introduced in API version 12. In this version, a compatibility change was made that > preserved the initial version information of inner elements. As a result, you might see outer element's @since > version number being higher than that of the inner elements. However, this discrepancy does not affect the > functionality of the interface. |
| [ZoomRange](arkts-camera-camera-zoomrange-i.md) | Describes the zoom range. |

<!--Del-->
### Interfaces（系统接口）

| Name | Description |
| --- | --- |
| [ApertureInfo](arkts-camera-camera-apertureinfo-i-sys.md) | Describes the aperture information. |
| [ApertureVideoSession](arkts-camera-camera-aperturevideosession-i-sys.md) | Aperture video session object. |
| [Beauty](arkts-camera-camera-beauty-i-sys.md) | Beauty extends [BeautyQuery](arkts-camera-camera-beautyquery-i-sys.md)Provides APIs to obtain and set the beauty effect. |
| [BeautyQuery](arkts-camera-camera-beautyquery-i-sys.md) | Provides APIs to obtain and set the beauty effect. |
| [CameraDevice](arkts-camera-camera-cameradevice-i-sys.md) | Describes the camera device information. |
| [CameraInput](arkts-camera-camera-camerainput-i-sys.md) | **CameraInput** defines the camera input object.  It provides camera device information used in [Session](arkts-camera-camera-session-i.md). |
| [CameraManager](arkts-camera-camera-cameramanager-i-sys.md) | **CameraManager** implements camera management. Before calling any API in **CameraManager**, you must use  [getCameraManager](arkts-camera-camera-getcameramanager-f.md#getcameramanager) to obtain a **CameraManager** instance. |
| [CameraOutputCapability](arkts-camera-camera-cameraoutputcapability-i-sys.md) | Describes the camera output capability. |
| [CaptureSession](arkts-camera-camera-capturesession-i-sys.md) | **CaptureSession** implements a capture session, which saves all [CameraInput](arkts-camera-camera-camerainput-i.md) and  [CameraOutput](arkts-camera-camera-cameraoutput-i.md) instances required to run the camera and requests the camera to complete shooting or video recording. |
| [ColorEffect](arkts-camera-camera-coloreffect-i-sys.md) | ColorEffect extends [ColorEffectQuery](arkts-camera-camera-coloreffectquery-i-sys.md)Provides the APIs to obtain and set the lens color effect. |
| [ColorEffectQuery](arkts-camera-camera-coloreffectquery-i-sys.md) | Provides the API to obtain the color effects supported. |
| [ColorReservation](arkts-camera-camera-colorreservation-i-sys.md) | ColorReservation extends [ColorReservationQuery](arkts-camera-camera-colorreservationquery-i-sys.md)Provides API for obtaining and setting a color reservation type. |
| [ColorReservationQuery](arkts-camera-camera-colorreservationquery-i-sys.md) | Provides APIs for querying the color retention type supported by the device. |
| [ControlCenterSession](arkts-camera-camera-controlcentersession-i-sys.md) | Control center session object. |
| [DeferredPhotoProxy](arkts-camera-camera-deferredphotoproxy-i-sys.md) | A class object that functions as a thumbnail proxy. |
| [DeferredVideoEnhancementInfo](arkts-camera-camera-deferredvideoenhancementinfo-i-sys.md) | Deferred video enhancement info. |
| [DepthData](arkts-camera-camera-depthdata-i-sys.md) | Describes a depth data object. |
| [DepthDataOutput](arkts-camera-camera-depthdataoutput-i-sys.md) | Implements depth data output. It inherits from [CameraOutput](arkts-camera-camera-cameraoutput-i.md). |
| [DepthFusion](arkts-camera-camera-depthfusion-i-sys.md) | Depth fusion class. It inherits from [DepthFusionQuery](arkts-camera-camera-depthfusionquery-i-sys.md). |
| [DepthFusionQuery](arkts-camera-camera-depthfusionquery-i-sys.md) | A class for querying depth fusion capabilities. |
| [DepthProfile](arkts-camera-camera-depthprofile-i-sys.md) | Describes the profile of depth data. It inherits from [Profile](arkts-camera-camera-profile-i.md). |
| [EffectSuggestion](arkts-camera-camera-effectsuggestion-i-sys.md) | EffectSuggestion object. |
| [Flash](arkts-camera-camera-flash-i-sys.md) | **Flash** inherits from [FlashQuery](arkts-camera-camera-flashquery-i.md).  It provides APIs related to the flash. |
| [FlashQuery](arkts-camera-camera-flashquery-i-sys.md) | FlashQuery provides APIs to query the flash status and mode of a camera device.  > **NOTE：** >  > - This interface was first introduced in API version 12. In this version, a compatibility change was made that > preserved the initial version information of inner elements. As a result, you might see outer element's @since > version number being higher than that of the inner elements. However, this discrepancy does not affect the > functionality of the interface. |
| [FluorescencePhotoSession](arkts-camera-camera-fluorescencephotosession-i-sys.md) | Fluorescence photo session object. |
| [Focus](arkts-camera-camera-focus-i-sys.md) | **Focus** inherits from [FocusQuery](arkts-camera-camera-focusquery-i.md).  It provides APIs related to focus operations. |
| [FocusQuery](arkts-camera-camera-focusquery-i-sys.md) | FocusQuery provides APIs to check whether a focus mode is supported.  > **NOTE：** >  > - This interface was first introduced in API version 12. In this version, a compatibility change was made that > preserved the initial version information of inner elements. As a result, you might see outer element's @since > version number being higher than that of the inner elements. However, this discrepancy does not affect the > functionality of the interface. |
| [FocusTrackingInfo](arkts-camera-camera-focustrackinginfo-i-sys.md) | Describes the focus tracking information, which is obtained by calling VideoSessionForSys.  [on('focusTrackingInfoAvailable')](camera.VideoSession.on(type: 'focusTrackingInfoAvailable', callback: Callback&lt;FocusTrackingInfo&gt;)). |
| [HighResolutionPhotoSession](arkts-camera-camera-highresolutionphotosession-i-sys.md) | HighResolutionPhotoSession extends Session, AutoExposure, Focus Implements a high-resolution photo session, which sets the parameters of the high-resolution photo mode and saves all [CameraInput](arkts-camera-camera-camerainput-i.md) and [CameraOutput](arkts-camera-camera-cameraoutput-i.md)instances required to run the camera. It inherits from [Session](arkts-camera-camera-session-i.md).  > **NOTE：** >  > In high-resolution photo capture scenarios, the physical camera lens must be used instead of the logical lens. |
| [ImagingMode](arkts-camera-camera-imagingmode-i-sys.md) | Implements imaging mode. |
| [ImagingModeQuery](arkts-camera-camera-imagingmodequery-i-sys.md) | Imaging mode query object. |
| [LcdFlashStatus](arkts-camera-camera-lcdflashstatus-i-sys.md) | Describes the LCD flash information. |
| [LightPaintingPhotoSession](arkts-camera-camera-lightpaintingphotosession-i-sys.md) | LightPaintingPhotoSession extends Session, Flash, Focus, Zoom, ColorEffect Implements a light painting photo session, which sets the parameters of the light painting photo mode and saves all  [CameraInput](arkts-camera-camera-camerainput-i.md) and [CameraOutput](arkts-camera-camera-cameraoutput-i.md)instances required to run the camera. It inherits from [Session](arkts-camera-camera-session-i.md). |
| [LuminationInfo](arkts-camera-camera-luminationinfo-i-sys.md) | Describes the illumination information. |
| [MacroPhotoSession](arkts-camera-camera-macrophotosession-i-sys.md) | Implements a macro photo session, which sets the parameters of the macro photo mode and saves all  [CameraInput](arkts-camera-camera-camerainput-i.md) and [CameraOutput](arkts-camera-camera-cameraoutput-i.md)instances required to run the camera. It inherits from [Session](arkts-camera-camera-session-i.md). |
| [MacroVideoSession](arkts-camera-camera-macrovideosession-i-sys.md) | Implements a macro video session, which sets the parameters of the macro video mode and saves all  [CameraInput](arkts-camera-camera-camerainput-i.md) and [CameraOutput](arkts-camera-camera-cameraoutput-i.md)instances required to run the camera. It inherits from [Session](arkts-camera-camera-session-i.md). |
| [MetadataObject](arkts-camera-camera-metadataobject-i-sys.md) | Describes the camera metadata, which is the data source of [CameraInput](arkts-camera-camera-camerainput-i.md). The metadata is obtained through **metadataOutput.on('metadataObjectsAvailable')**. |
| [NightPhotoSession](arkts-camera-camera-nightphotosession-i-sys.md) | NightPhotoSession extends Session, Flash, AutoExposure, Focus, Zoom, ColorEffect, ColorManagement, ManualExposure Implements a night photo session, which sets the parameters of the night photo mode and saves all  [CameraInput](arkts-camera-camera-camerainput-i.md), [CameraOutput](arkts-camera-camera-cameraoutput-i.md), and  [PhotoOutput](arkts-camera-camera-photooutput-i.md) instances required to run the camera. It inherits from  [Session](arkts-camera-camera-session-i.md).For night photo capture scenarios, you must listen for the  [onCaptureEnd](camera.PhotoOutput.on(type: 'captureEnd', callback: AsyncCallback&lt;CaptureEndInfo&gt;))event to mark the end of the photo capture session. |
| [PanoramaPhotoSession](arkts-camera-camera-panoramaphotosession-i-sys.md) | PanoramaPhotoSession extends Session, Focus, AutoExposure, WhiteBalance, ColorEffect Implements a panoramic photo session, which sets the parameters of the panoramic photo mode and saves all  [CameraInput](arkts-camera-camera-camerainput-i.md) and [CameraOutput](arkts-camera-camera-cameraoutput-i.md)instances required to run the camera. It inherits from [Session](arkts-camera-camera-session-i.md). |
| [Photo](arkts-camera-camera-photo-i-sys.md) | Photo defines a full-quality image object. |
| [PhotoOutput](arkts-camera-camera-photooutput-i-sys.md) | PhotoOutput implements output information used in a photo session. It inherits from  [CameraOutput](arkts-camera-camera-cameraoutput-i.md). |
| [PhotoSession](arkts-camera-camera-photosession-i-sys.md) | **PhotoSession** inherits from [Session](arkts-camera-camera-session-i.md), [Flash](arkts-camera-camera-flash-i.md),  [AutoExposure](arkts-camera-camera-autoexposure-i.md), [WhiteBalance](arkts-camera-camera-whitebalance-i.md), [Focus](arkts-camera-camera-focus-i.md),  [Zoom](arkts-camera-camera-zoom-i.md), [ColorManagement](arkts-camera-camera-colormanagement-i.md),  [AutoDeviceSwitch](arkts-camera-camera-autodeviceswitch-i.md), [Macro](arkts-camera-camera-macro-i.md),  [ManualExposure](../../../reference/apis-camera-kit/arkts-apis-camera-ManualExposure.md),  [ManualFocus](../../../reference/apis-camera-kit/arkts-apis-camera-ManualFocus.md),  [ManualIso](../../../reference/apis-camera-kit/arkts-apis-camera-ManualIso.md),  [OIS](../../../reference/apis-camera-kit/arkts-apis-camera-OIS.md), and  [Aperture](../../../reference/apis-camera-kit/arkts-apis-camera-Aperture.md).  It implements a photo session, which provides operations on the flash, exposure, white balance, focus, zoom, color space, macro mode, manual exposure, manual focus, manual ISO setting, optical image stabilization (OIS), and aperture.  **PhotoSession** is provided for the default photo mode. It is used to take standard photos. It supports multiple photo formats and resolutions, which are suitable for most daily photo capture scenarios. |
| [Portrait](arkts-camera-camera-portrait-i-sys.md) | Portrait: inherits from [PortraitQuery](arkts-camera-camera-portraitquery-i-sys.md).Provides the APIs for portrait photo settings. |
| [PortraitPhotoSession](arkts-camera-camera-portraitphotosession-i-sys.md) | PortraitPhotoSession extends Session, Flash, AutoExposure, Focus, Zoom, Beauty, ColorEffect, ColorManagement,Portrait, Aperture Implements a portrait photo session, which sets the parameters of the portrait photo mode and saves all  [CameraInput](arkts-camera-camera-camerainput-i.md) and [CameraOutput](arkts-camera-camera-cameraoutput-i.md)instances required to run the camera. It inherits from [Session](arkts-camera-camera-session-i.md). |
| [PortraitQuery](arkts-camera-camera-portraitquery-i-sys.md) | Queries portrait parameters. |
| [PrelaunchConfig](arkts-camera-camera-prelaunchconfig-i-sys.md) | Defines the camera prelaunch configuration.Currently, the configuration is used for sensor-level prelaunch. It will be used for stream-level prelaunch in a later version. |
| [PreviewOutput](arkts-camera-camera-previewoutput-i-sys.md) | PreviewOutput implements preview output. It inherits from [CameraOutput](arkts-camera-camera-cameraoutput-i.md). |
| [ProfessionalPhotoSession](arkts-camera-camera-professionalphotosession-i-sys.md) | ProfessionalPhotoSession extends Session, AutoExposure, ManualExposure, Focus, ManualFocus, WhiteBalance, ManualIso, Flash, Zoom, ColorEffect, Aperture Implements a professional photo session, which sets the parameters of the professional photo mode and saves all  [CameraInput](arkts-camera-camera-camerainput-i.md) and [CameraOutput](arkts-camera-camera-cameraoutput-i.md)instances required to run the camera. It inherits from [Session](arkts-camera-camera-session-i.md). |
| [ProfessionalVideoSession](arkts-camera-camera-professionalvideosession-i-sys.md) | ProfessionalVideoSession extends Session, AutoExposure, ManualExposure, Focus, ManualFocus, WhiteBalance, ManualIso, Flash, Zoom, ColorEffect, Aperture Implements a professional video session, which sets the parameters of the professional video mode and saves all  [CameraInput](arkts-camera-camera-camerainput-i.md) and [CameraOutput](arkts-camera-camera-cameraoutput-i.md)instances required to run the camera. It inherits from [Session](arkts-camera-camera-session-i.md). |
| [QuickShotPhotoSession](arkts-camera-camera-quickshotphotosession-i-sys.md) | Quick shot photo session object. |
| [QuickThumbnail](arkts-camera-camera-quickthumbnail-i-sys.md) | Quick thumbnail object |
| [SceneDetection](arkts-camera-camera-scenedetection-i-sys.md) | Provides the scene detection capability. It inherits from [SceneDetectionQuery](arkts-camera-camera-scenedetectionquery-i-sys.md). |
| [SceneDetectionQuery](arkts-camera-camera-scenedetectionquery-i-sys.md) | Provides the scene detection and query capabilities. |
| [SceneFeatureDetectionResult](arkts-camera-camera-scenefeaturedetectionresult-i-sys.md) | Describes the scene feature detection result. |
| [Session](arkts-camera-camera-session-i-sys.md) | **Session** implements a session, which saves all [CameraInput](arkts-camera-camera-camerainput-i.md) and  [CameraOutput](arkts-camera-camera-cameraoutput-i.md) instances required to run the camera and requests the camera to take a photo or record a video. |
| [SettingParam](arkts-camera-camera-settingparam-i-sys.md) | Defines the effect parameters used to preheat an image. |
| [SketchStatusData](arkts-camera-camera-sketchstatusdata-i-sys.md) | Defines the PiP status data. |
| [SlowMotionVideoSession](arkts-camera-camera-slowmotionvideosession-i-sys.md) | SlowMotionVideoSession extends Session, Flash, AutoExposure, Focus, Zoom, ColorEffect Implements a slow-motion video session, which sets the parameters of the slow-motion video mode and saves all  [CameraInput](arkts-camera-camera-camerainput-i.md) and [CameraOutput](arkts-camera-camera-cameraoutput-i.md)instances required to run the camera. It inherits from [Session](arkts-camera-camera-session-i.md). |
| [TimeLapsePhotoSession](arkts-camera-camera-timelapsephotosession-i-sys.md) | TimeLapsePhotoSession extends Session, Focus, ManualFocus, AutoExposure, ManualExposure, ManualIso, WhiteBalance,Zoom, ColorEffect Implements a time-lapse photo session, which sets the parameters of the time-lapse photo mode and saves all  [CameraInput](arkts-camera-camera-camerainput-i.md) and [CameraOutput](arkts-camera-camera-cameraoutput-i.md)instances required to run the camera. It inherits from [Session](arkts-camera-camera-session-i.md). |
| [TripodDetectionResult](arkts-camera-camera-tripoddetectionresult-i-sys.md) | TripodDetectionResult extends [SceneFeatureDetectionResult](arkts-camera-camera-scenefeaturedetectionresult-i-sys.md)Describes the tripod detection result. |
| [TryAEInfo](arkts-camera-camera-tryaeinfo-i-sys.md) | Describes the Try AE parameters. Try AE indicates that the hardware reports the status based on the ambient illumination change during time-lapse photographing. |
| [VideoOutput](arkts-camera-camera-videooutput-i-sys.md) | VideoOutput implements output information used in a video session. It inherits from  [CameraOutput](arkts-camera-camera-cameraoutput-i.md). |
| [VideoSession](arkts-camera-camera-videosession-i-sys.md) | VideoSession inherits from [Session](arkts-camera-camera-session-i.md), [Flash](arkts-camera-camera-flash-i.md),  [AutoExposure](arkts-camera-camera-autoexposure-i.md), [WhiteBalance](arkts-camera-camera-whitebalance-i.md), [Focus](arkts-camera-camera-focus-i.md),  [Zoom](arkts-camera-camera-zoom-i.md), [Stabilization](arkts-camera-camera-stabilization-i.md),  [ColorManagement](arkts-camera-camera-colormanagement-i.md), [AutoDeviceSwitch](arkts-camera-camera-autodeviceswitch-i.md),  [Macro](arkts-camera-camera-macro-i.md), [ControlCenter](arkts-camera-camera-controlcenter-i.md),  [ManualExposure](../../../reference/apis-camera-kit/arkts-apis-camera-ManualExposure.md),  [ManualFocus](../../../reference/apis-camera-kit/arkts-apis-camera-ManualFocus.md),  [ManualIso](../../../reference/apis-camera-kit/arkts-apis-camera-ManualIso.md),  [OIS](../../../reference/apis-camera-kit/arkts-apis-camera-OIS.md), and  [Aperture](../../../reference/apis-camera-kit/arkts-apis-camera-Aperture.md).  It implements a video session, which provides operations on the flash, exposure, white balance, focus, zoom, video stabilization, color space, macro mode and controller, manual exposure, manual focus, manual ISO, optical image stabilization, and aperture.  **VideoSession** is provided for the default video recording mode. It applies to common scenarios. It supports recording at various resolutions (such as 720p and 1080p) and frame rates (such as 30 fps and 60 fps). |
| [WhiteBalanceGains](arkts-camera-camera-whitebalancegains-i-sys.md) | RGB white balance gain values. |
| [Zoom](arkts-camera-camera-zoom-i-sys.md) | **Zoom** inherits from [ZoomQuery](arkts-camera-camera-zoomquery-i.md).  It provides APIs related to zoom operations. |
| [ZoomQuery](arkts-camera-camera-zoomquery-i-sys.md) | ZoomQuery provides APIs to query the zoom feature of a device camera, including the API to obtain the supported zoom ratio range.  > **NOTE：** >  > - This interface was first introduced in API version 12. In this version, a compatibility change was made that > preserved the initial version information of inner elements. As a result, you might see outer element's @since > version number being higher than that of the inner elements. However, this discrepancy does not affect the > functionality of the interface. |
<!--DelEnd-->

### Enums

| Name | Description |
| --- | --- |
| [AutomotiveCameraPosition](arkts-camera-camera-automotivecameraposition-e.md) | Enum for automotive camera position. |
| [CameraConcurrentType](arkts-camera-camera-cameraconcurrenttype-e.md) | Enumerates the camera concurrency types. |
| [CameraErrorCode](arkts-camera-camera-cameraerrorcode-e.md) | Enumerates the camera error codes,  which are returned when an API call is incorrect or the **on()** API is used to listen for the error status. |
| [CameraFormat](arkts-camera-camera-cameraformat-e.md) | Enumerates the camera output formats. |
| [CameraPosition](arkts-camera-camera-cameraposition-e.md) | Enumerates the camera positions. |
| [CameraStatus](arkts-camera-camera-camerastatus-e.md) | Enumerates the camera statuses. |
| [CameraType](arkts-camera-camera-cameratype-e.md) | Enumerates the camera types. |
| [ConnectionType](arkts-camera-camera-connectiontype-e.md) | Enumerates the camera connection types. |
| [ControlCenterEffectType](arkts-camera-camera-controlcentereffecttype-e.md) | Enumerates the effect types supported by the camera controller. |
| [Emotion](arkts-camera-camera-emotion-e.md) | Enumerates the types of emotions in the detected human face information. |
| [ExposureMeteringMode](arkts-camera-camera-exposuremeteringmode-e.md) | Enumerates the exposure metering modes. |
| [ExposureMode](arkts-camera-camera-exposuremode-e.md) | Enumerates the exposure modes. |
| [ExposureState](arkts-camera-camera-exposurestate-e.md) | Enumerates the exposure states. |
| [FlashMode](arkts-camera-camera-flashmode-e.md) | Enumerates the flash modes. |
| [FlashState](arkts-camera-camera-flashstate-e.md) | Enumerates the flash states. |
| [FocusMode](arkts-camera-camera-focusmode-e.md) | Enumerates the focus modes. |
| [FocusState](arkts-camera-camera-focusstate-e.md) | Enumerates the focus states. |
| [FoldStatus](arkts-camera-camera-foldstatus-e.md) | Enumerates the fold states available for a fordable device. |
| [HostDeviceType](arkts-camera-camera-hostdevicetype-e.md) | Enumerates the remote camera types. |
| [ImageRotation](arkts-camera-camera-imagerotation-e.md) | Enumerates the image rotation angles. |
| [MetadataObjectType](arkts-camera-camera-metadataobjecttype-e.md) | Enumerates the types of metadata objects used for camera detection. |
| [OISAxes](arkts-camera-camera-oisaxes-e.md) | Enumerates the OIS axes. |
| [OISMode](arkts-camera-camera-oismode-e.md) | Enumerates the optical image stabilization (OIS) mode. |
| [PhotoQualityPrioritization](arkts-camera-camera-photoqualityprioritization-e.md) | Enumerates the photo quality prioritization strategies. |
| [PreconfigRatio](arkts-camera-camera-preconfigratio-e.md) | Enumerates the preconfigured aspect ratios. |
| [PreconfigType](arkts-camera-camera-preconfigtype-e.md) | Enumerates the preconfigured resolution types. |
| [QualityLevel](arkts-camera-camera-qualitylevel-e.md) | Enumerates the image quality levels. |
| [QualityPrioritization](arkts-camera-camera-qualityprioritization-e.md) | Enumerates the priority levels for video recording quality. |
| [SceneMode](arkts-camera-camera-scenemode-e.md) | Enumerates the camera scene modes. |
| [SensorColorFilterArrangement](arkts-camera-camera-sensorcolorfilterarrangement-e.md) | Enumerates the arrangement modes of the sensor color filter. |
| [SmoothZoomMode](arkts-camera-camera-smoothzoommode-e.md) | Enumerates the smooth zoom modes. |
| [SystemPressureLevel](arkts-camera-camera-systempressurelevel-e.md) | Enumerates the system pressure levels. |
| [TorchMode](arkts-camera-camera-torchmode-e.md) | Enumerates the flashlight modes. |
| [VideoCodecType](arkts-camera-camera-videocodectype-e.md) | Enumerates the video codec types. |
| [VideoStabilizationMode](arkts-camera-camera-videostabilizationmode-e.md) | Enumerates the video stabilization modes. |
| [WhiteBalanceMode](arkts-camera-camera-whitebalancemode-e.md) | Enumerates the white balance modes. |

<!--Del-->
### Enums（系统接口）

| Name | Description |
| --- | --- |
| [AuxiliaryStatus](arkts-camera-camera-auxiliarystatus-e-sys.md) | Enum for auxiliary status. |
| [AuxiliaryType](arkts-camera-camera-auxiliarytype-e-sys.md) | Enum for auxiliary type. |
| [BeautyType](arkts-camera-camera-beautytype-e-sys.md) | Enumerates the beauty types. |
| [CameraErrorCode](arkts-camera-camera-cameraerrorcode-e-sys.md) | Enumerates the camera error codes,  which are returned when an API call is incorrect or the **on()** API is used to listen for the error status. |
| [CameraFormat](arkts-camera-camera-cameraformat-e-sys.md) | Enumerates the camera output formats. |
| [CameraImagingMode](arkts-camera-camera-cameraimagingmode-e-sys.md) | Enumerates the camera imaging modes. |
| [ColorEffectType](arkts-camera-camera-coloreffecttype-e-sys.md) | Enumerates the color effect types. |
| [ColorReservationType](arkts-camera-camera-colorreservationtype-e-sys.md) | Enumerates the color reservation types. |
| [DeferredDeliveryImageType](arkts-camera-camera-deferreddeliveryimagetype-e-sys.md) | Enumerates the deferred delivery image types. In deferred delivery, photo and video capture are divided into two phases. In the first phase, an image or video is output to users at a relatively fast speed. In the second phase, a higher-resolution image or video is output again after optimization processing. |
| [DepthDataAccuracy](arkts-camera-camera-depthdataaccuracy-e-sys.md) | Describes the accuracy of depth data. |
| [DepthDataQualityLevel](arkts-camera-camera-depthdataqualitylevel-e-sys.md) | Enumerates the quality levels of depth data. |
| [EffectSuggestionType](arkts-camera-camera-effectsuggestiontype-e-sys.md) | Enum for effect suggestion. |
| [FocusDrivenType](arkts-camera-camera-focusdriventype-e-sys.md) | Enumerates the focus drive types. |
| [FocusRangeType](arkts-camera-camera-focusrangetype-e-sys.md) | Enumerates the focus range types. |
| [FocusTrackingMode](arkts-camera-camera-focustrackingmode-e-sys.md) | Enumerates the focus tracking modes. |
| [LightPaintingType](arkts-camera-camera-lightpaintingtype-e-sys.md) | Enumerates the types of light painting shutter modes. |
| [LightStatus](arkts-camera-camera-lightstatus-e-sys.md) | Enumerates the camera light statuses, which are obtained by calling VideoSessionForSys.  [on('lightStatusChange')](camera.VideoSession.on(type: 'lightStatusChange', callback: AsyncCallback&lt;LightStatus&gt;)). |
| [MetadataObjectType](arkts-camera-camera-metadataobjecttype-e-sys.md) | Enumerates the types of metadata objects used for camera detection. |
| [PolicyType](arkts-camera-camera-policytype-e-sys.md) | Enumerates the policy types. |
| [PortraitEffect](arkts-camera-camera-portraiteffect-e-sys.md) | Enumerates the portrait effects. |
| [PortraitThemeType](arkts-camera-camera-portraitthemetype-e-sys.md) | Enumerates the camera portrait theme types. |
| [RestoreParamType](arkts-camera-camera-restoreparamtype-e-sys.md) | Enumerates the types of the parameters used for prelaunch. |
| [SceneFeatureType](arkts-camera-camera-scenefeaturetype-e-sys.md) | Enumerates the scene features. |
| [SceneMode](arkts-camera-camera-scenemode-e-sys.md) | Enumerates the camera scene modes. |
| [SlowMotionStatus](arkts-camera-camera-slowmotionstatus-e-sys.md) | Enumerates the slow-motion states. |
| [TimeLapsePreviewType](arkts-camera-camera-timelapsepreviewtype-e-sys.md) | Enumerates the time-lapse preview types, which affect the shooting algorithm. |
| [TimeLapseRecordState](arkts-camera-camera-timelapserecordstate-e-sys.md) | Enumerates the time-lapse recording states. |
| [TripodStatus](arkts-camera-camera-tripodstatus-e-sys.md) | Enumerates the tripod statuses. |
| [UsageType](arkts-camera-camera-usagetype-e-sys.md) | Enum for usage type used in capture session. |
| [VideoMetaType](arkts-camera-camera-videometatype-e-sys.md) | Video meta type. |
<!--DelEnd-->

### Types

| Name | Description |
| --- | --- |
| [ImageType](arkts-camera-camera-imagetype-t.md) | Defines the image container type, which is used to obtain full-quality images or uncompressed images (YUV). |

