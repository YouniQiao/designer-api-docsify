# @ohos.multimedia.camera(AutoDeviceSwitch)

The module provides a set of camera service APIs for you to easily develop a camera application. The application can access and operate the camera hardware to implement basic operations, such as preview, taking photos, and recording videos. It can also perform more operations, for example, controlling the flash and exposure time, and focusing or adjusting the focus.

> **NOTE：**
> 
> - This topic describes only system APIs provided by the module. For details about its public APIs, see
> [@ohos.multimedia.camera (Camera Management)](#camera).

**Since:** 10

<!--Device-unnamed-declare namespace camera--><!--Device-unnamed-declare namespace camera-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## Modules to Import

```TypeScript
import { camera } from '@kit.CameraKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [getCameraManager](arkts-camera-camera-getcameramanager-f.md#getcameramanager) |

<!--Del-->
### Classes（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [EffectSuggestionStatus](arkts-camera-camera-effectsuggestionstatus-c-sys.md) |
<!--DelEnd-->

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [Aperture](arkts-camera-camera-aperture-i.md) |
| [ApertureQuery](arkts-camera-camera-aperturequery-i.md) |
| [AutoDeviceSwitch](arkts-camera-camera-autodeviceswitch-i.md) |
| [AutoDeviceSwitchQuery](arkts-camera-camera-autodeviceswitchquery-i.md) |
| [AutoDeviceSwitchStatus](arkts-camera-camera-autodeviceswitchstatus-i.md) |
| [AutoExposure](arkts-camera-camera-autoexposure-i.md) |
| [AutoExposureQuery](arkts-camera-camera-autoexposurequery-i.md) |
| [CameraConcurrentInfo](arkts-camera-camera-cameraconcurrentinfo-i.md) |
| [CameraDevice](arkts-camera-camera-cameradevice-i.md) |
| [CameraInput](arkts-camera-camera-camerainput-i.md) |
| [CameraManager](arkts-camera-camera-cameramanager-i.md) |
| [CameraOcclusionDetectionResult](arkts-camera-camera-cameraocclusiondetectionresult-i.md) |
| [CameraOutput](arkts-camera-camera-cameraoutput-i.md) |
| [CameraOutputCapability](arkts-camera-camera-cameraoutputcapability-i.md) |
| [CameraStatusInfo](arkts-camera-camera-camerastatusinfo-i.md) |
| [CaptureEndInfo](arkts-camera-camera-captureendinfo-i.md) |
| [CapturePhoto](arkts-camera-camera-capturephoto-i.md) |
| [CaptureSession](arkts-camera-camera-capturesession-i.md) |
| [CaptureStartInfo](arkts-camera-camera-capturestartinfo-i.md) |
| [ColorManagement](arkts-camera-camera-colormanagement-i.md) |
| [ColorManagementQuery](arkts-camera-camera-colormanagementquery-i.md) |
| [ControlCenter](arkts-camera-camera-controlcenter-i.md) |
| [ControlCenterQuery](arkts-camera-camera-controlcenterquery-i.md) |
| [ControlCenterStatusInfo](arkts-camera-camera-controlcenterstatusinfo-i.md) |
| [ExposureInfo](arkts-camera-camera-exposureinfo-i.md) |
| [Flash](arkts-camera-camera-flash-i.md) |
| [FlashQuery](arkts-camera-camera-flashquery-i.md) |
| [Focus](arkts-camera-camera-focus-i.md) |
| [FocusQuery](arkts-camera-camera-focusquery-i.md) |
| [FoldStatusInfo](arkts-camera-camera-foldstatusinfo-i.md) |
| [FrameRateRange](arkts-camera-camera-frameraterange-i.md) |
| [FrameShutterEndInfo](arkts-camera-camera-frameshutterendinfo-i.md) |
| [FrameShutterInfo](arkts-camera-camera-frameshutterinfo-i.md) |
| [IsoInfo](arkts-camera-camera-isoinfo-i.md) |
| [Location](arkts-camera-camera-location-i.md) |
| [Macro](arkts-camera-camera-macro-i.md) |
| [MacroQuery](arkts-camera-camera-macroquery-i.md) |
| [ManualExposure](arkts-camera-camera-manualexposure-i.md) |
| [ManualExposureQuery](arkts-camera-camera-manualexposurequery-i.md) |
| [ManualFocus](arkts-camera-camera-manualfocus-i.md) |
| [ManualFocusQuery](arkts-camera-camera-manualfocusquery-i.md) |
| [ManualIso](arkts-camera-camera-manualiso-i.md) |
| [ManualIsoQuery](arkts-camera-camera-manualisoquery-i.md) |
| [MetadataBarcodeObject](arkts-camera-camera-metadatabarcodeobject-i.md) |
| [MetadataBasicFaceObject](arkts-camera-camera-metadatabasicfaceobject-i.md) |
| [MetadataCatBodyObject](arkts-camera-camera-metadatacatbodyobject-i.md) |
| [MetadataCatFaceObject](arkts-camera-camera-metadatacatfaceobject-i.md) |
| [MetadataDogBodyObject](arkts-camera-camera-metadatadogbodyobject-i.md) |
| [MetadataDogFaceObject](arkts-camera-camera-metadatadogfaceobject-i.md) |
| [MetadataFaceObject](arkts-camera-camera-metadatafaceobject-i.md) |
| [MetadataHumanBodyObject](arkts-camera-camera-metadatahumanbodyobject-i.md) |
| [MetadataObject](arkts-camera-camera-metadataobject-i.md) |
| [MetadataOutput](arkts-camera-camera-metadataoutput-i.md) |
| [MetadataSalientDetectionObject](arkts-camera-camera-metadatasalientdetectionobject-i.md) |
| [OIS](arkts-camera-camera-ois-i.md) |
| [OISQuery](arkts-camera-camera-oisquery-i.md) |
| [Photo](arkts-camera-camera-photo-i.md) |
| [PhotoCaptureSetting](arkts-camera-camera-photocapturesetting-i.md) |
| [PhotoConflictFunctions](arkts-camera-camera-photoconflictfunctions-i.md) |
| [PhotoFunctions](arkts-camera-camera-photofunctions-i.md) |
| [PhotoOutput](arkts-camera-camera-photooutput-i.md) |
| [PhotoSession](arkts-camera-camera-photosession-i.md) |
| [PhotoSessionForSys](arkts-camera-camera-photosessionforsys-i.md) |
| [PhysicalAperture](arkts-camera-camera-physicalaperture-i.md) |
| [Point](arkts-camera-camera-point-i.md) |
| [PortraitPhotoConflictFunctions](arkts-camera-camera-portraitphotoconflictfunctions-i.md) |
| [PortraitPhotoFunctions](arkts-camera-camera-portraitphotofunctions-i.md) |
| [PreviewOutput](arkts-camera-camera-previewoutput-i.md) |
| [Profile](arkts-camera-camera-profile-i.md) |
| [Rect](arkts-camera-camera-rect-i.md) |
| [SecureSession](arkts-camera-camera-securesession-i.md) |
| [Session](arkts-camera-camera-session-i.md) |
| [Size](arkts-camera-camera-size-i.md) |
| [SmoothZoomInfo](arkts-camera-camera-smoothzoominfo-i.md) |
| [Stabilization](arkts-camera-camera-stabilization-i.md) |
| [StabilizationQuery](arkts-camera-camera-stabilizationquery-i.md) |
| [TorchStatusInfo](arkts-camera-camera-torchstatusinfo-i.md) |
| [VideoConflictFunctions](arkts-camera-camera-videoconflictfunctions-i.md) |
| [VideoFunctions](arkts-camera-camera-videofunctions-i.md) |
| [VideoOutput](arkts-camera-camera-videooutput-i.md) |
| [VideoProfile](arkts-camera-camera-videoprofile-i.md) |
| [VideoSession](arkts-camera-camera-videosession-i.md) |
| [VideoSessionForSys](arkts-camera-camera-videosessionforsys-i.md) |
| [WhiteBalance](arkts-camera-camera-whitebalance-i.md) |
| [WhiteBalanceQuery](arkts-camera-camera-whitebalancequery-i.md) |
| [Zoom](arkts-camera-camera-zoom-i.md) |
| [ZoomPointInfo](arkts-camera-camera-zoompointinfo-i.md) |
| [ZoomQuery](arkts-camera-camera-zoomquery-i.md) |
| [ZoomRange](arkts-camera-camera-zoomrange-i.md) |

<!--Del-->
### Interfaces（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [ApertureInfo](arkts-camera-camera-apertureinfo-i-sys.md) |
| [ApertureVideoSession](arkts-camera-camera-aperturevideosession-i-sys.md) |
| [Beauty](arkts-camera-camera-beauty-i-sys.md) |
| [BeautyQuery](arkts-camera-camera-beautyquery-i-sys.md) |
| [CameraDevice](arkts-camera-camera-cameradevice-i-sys.md) |
| [CameraInput](arkts-camera-camera-camerainput-i-sys.md) |
| [CameraManager](arkts-camera-camera-cameramanager-i-sys.md) |
| [CameraOutputCapability](arkts-camera-camera-cameraoutputcapability-i-sys.md) |
| [CaptureSession](arkts-camera-camera-capturesession-i-sys.md) |
| [ColorEffect](arkts-camera-camera-coloreffect-i-sys.md) |
| [ColorEffectQuery](arkts-camera-camera-coloreffectquery-i-sys.md) |
| [ColorReservation](arkts-camera-camera-colorreservation-i-sys.md) |
| [ColorReservationQuery](arkts-camera-camera-colorreservationquery-i-sys.md) |
| [ControlCenterSession](arkts-camera-camera-controlcentersession-i-sys.md) |
| [DeferredPhotoProxy](arkts-camera-camera-deferredphotoproxy-i-sys.md) |
| [DeferredVideoEnhancementInfo](arkts-camera-camera-deferredvideoenhancementinfo-i-sys.md) |
| [DepthData](arkts-camera-camera-depthdata-i-sys.md) |
| [DepthDataOutput](arkts-camera-camera-depthdataoutput-i-sys.md) |
| [DepthFusion](arkts-camera-camera-depthfusion-i-sys.md) |
| [DepthFusionQuery](arkts-camera-camera-depthfusionquery-i-sys.md) |
| [DepthProfile](arkts-camera-camera-depthprofile-i-sys.md) |
| [EffectSuggestion](arkts-camera-camera-effectsuggestion-i-sys.md) |
| [Flash](arkts-camera-camera-flash-i-sys.md) |
| [FlashQuery](arkts-camera-camera-flashquery-i-sys.md) |
| [FluorescencePhotoSession](arkts-camera-camera-fluorescencephotosession-i-sys.md) |
| [Focus](arkts-camera-camera-focus-i-sys.md) |
| [FocusQuery](arkts-camera-camera-focusquery-i-sys.md) |
| [FocusTrackingInfo](arkts-camera-camera-focustrackinginfo-i-sys.md) |
| [HighResolutionPhotoSession](arkts-camera-camera-highresolutionphotosession-i-sys.md) |
| [ImagingMode](arkts-camera-camera-imagingmode-i-sys.md) |
| [ImagingModeQuery](arkts-camera-camera-imagingmodequery-i-sys.md) |
| [LcdFlashStatus](arkts-camera-camera-lcdflashstatus-i-sys.md) |
| [LightPaintingPhotoSession](arkts-camera-camera-lightpaintingphotosession-i-sys.md) |
| [LuminationInfo](arkts-camera-camera-luminationinfo-i-sys.md) |
| [MacroPhotoSession](arkts-camera-camera-macrophotosession-i-sys.md) |
| [MacroVideoSession](arkts-camera-camera-macrovideosession-i-sys.md) |
| [MetadataObject](arkts-camera-camera-metadataobject-i-sys.md) |
| [NightPhotoSession](arkts-camera-camera-nightphotosession-i-sys.md) |
| [PanoramaPhotoSession](arkts-camera-camera-panoramaphotosession-i-sys.md) |
| [Photo](arkts-camera-camera-photo-i-sys.md) |
| [PhotoOutput](arkts-camera-camera-photooutput-i-sys.md) |
| [PhotoSession](arkts-camera-camera-photosession-i-sys.md) |
| [Portrait](arkts-camera-camera-portrait-i-sys.md) |
| [PortraitPhotoSession](arkts-camera-camera-portraitphotosession-i-sys.md) |
| [PortraitQuery](arkts-camera-camera-portraitquery-i-sys.md) |
| [PrelaunchConfig](arkts-camera-camera-prelaunchconfig-i-sys.md) |
| [PreviewOutput](arkts-camera-camera-previewoutput-i-sys.md) |
| [ProfessionalPhotoSession](arkts-camera-camera-professionalphotosession-i-sys.md) |
| [ProfessionalVideoSession](arkts-camera-camera-professionalvideosession-i-sys.md) |
| [QuickShotPhotoSession](arkts-camera-camera-quickshotphotosession-i-sys.md) |
| [QuickThumbnail](arkts-camera-camera-quickthumbnail-i-sys.md) |
| [SceneDetection](arkts-camera-camera-scenedetection-i-sys.md) |
| [SceneDetectionQuery](arkts-camera-camera-scenedetectionquery-i-sys.md) |
| [SceneFeatureDetectionResult](arkts-camera-camera-scenefeaturedetectionresult-i-sys.md) |
| [Session](arkts-camera-camera-session-i-sys.md) |
| [SettingParam](arkts-camera-camera-settingparam-i-sys.md) |
| [SketchStatusData](arkts-camera-camera-sketchstatusdata-i-sys.md) |
| [SlowMotionVideoSession](arkts-camera-camera-slowmotionvideosession-i-sys.md) |
| [TimeLapsePhotoSession](arkts-camera-camera-timelapsephotosession-i-sys.md) |
| [TripodDetectionResult](arkts-camera-camera-tripoddetectionresult-i-sys.md) |
| [TryAEInfo](arkts-camera-camera-tryaeinfo-i-sys.md) |
| [VideoOutput](arkts-camera-camera-videooutput-i-sys.md) |
| [VideoSession](arkts-camera-camera-videosession-i-sys.md) |
| [WhiteBalanceGains](arkts-camera-camera-whitebalancegains-i-sys.md) |
| [Zoom](arkts-camera-camera-zoom-i-sys.md) |
| [ZoomQuery](arkts-camera-camera-zoomquery-i-sys.md) |
<!--DelEnd-->

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [AutomotiveCameraPosition](arkts-camera-camera-automotivecameraposition-e.md) |
| [CameraConcurrentType](arkts-camera-camera-cameraconcurrenttype-e.md) |
| [CameraErrorCode](arkts-camera-camera-cameraerrorcode-e.md) |
| [CameraFormat](arkts-camera-camera-cameraformat-e.md) |
| [CameraPosition](arkts-camera-camera-cameraposition-e.md) |
| [CameraStatus](arkts-camera-camera-camerastatus-e.md) |
| [CameraType](arkts-camera-camera-cameratype-e.md) |
| [ConnectionType](arkts-camera-camera-connectiontype-e.md) |
| [ControlCenterEffectType](arkts-camera-camera-controlcentereffecttype-e.md) |
| [Emotion](arkts-camera-camera-emotion-e.md) |
| [ExposureMeteringMode](arkts-camera-camera-exposuremeteringmode-e.md) |
| [ExposureMode](arkts-camera-camera-exposuremode-e.md) |
| [ExposureState](arkts-camera-camera-exposurestate-e.md) |
| [FlashMode](arkts-camera-camera-flashmode-e.md) |
| [FlashState](arkts-camera-camera-flashstate-e.md) |
| [FocusMode](arkts-camera-camera-focusmode-e.md) |
| [FocusState](arkts-camera-camera-focusstate-e.md) |
| [FoldStatus](arkts-camera-camera-foldstatus-e.md) |
| [HostDeviceType](arkts-camera-camera-hostdevicetype-e.md) |
| [ImageRotation](arkts-camera-camera-imagerotation-e.md) |
| [MetadataObjectType](arkts-camera-camera-metadataobjecttype-e.md) |
| [OISAxes](arkts-camera-camera-oisaxes-e.md) |
| [OISMode](arkts-camera-camera-oismode-e.md) |
| [PhotoQualityPrioritization](arkts-camera-camera-photoqualityprioritization-e.md) |
| [PreconfigRatio](arkts-camera-camera-preconfigratio-e.md) |
| [PreconfigType](arkts-camera-camera-preconfigtype-e.md) |
| [QualityLevel](arkts-camera-camera-qualitylevel-e.md) |
| [QualityPrioritization](arkts-camera-camera-qualityprioritization-e.md) |
| [SceneMode](arkts-camera-camera-scenemode-e.md) |
| [SensorColorFilterArrangement](arkts-camera-camera-sensorcolorfilterarrangement-e.md) |
| [SmoothZoomMode](arkts-camera-camera-smoothzoommode-e.md) |
| [SystemPressureLevel](arkts-camera-camera-systempressurelevel-e.md) |
| [TorchMode](arkts-camera-camera-torchmode-e.md) |
| [VideoCodecType](arkts-camera-camera-videocodectype-e.md) |
| [VideoStabilizationMode](arkts-camera-camera-videostabilizationmode-e.md) |
| [WhiteBalanceMode](arkts-camera-camera-whitebalancemode-e.md) |

<!--Del-->
### Enums（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [AuxiliaryStatus](arkts-camera-camera-auxiliarystatus-e-sys.md) |
| [AuxiliaryType](arkts-camera-camera-auxiliarytype-e-sys.md) |
| [BeautyType](arkts-camera-camera-beautytype-e-sys.md) |
| [CameraErrorCode](arkts-camera-camera-cameraerrorcode-e-sys.md) |
| [CameraFormat](arkts-camera-camera-cameraformat-e-sys.md) |
| [CameraImagingMode](arkts-camera-camera-cameraimagingmode-e-sys.md) |
| [ColorEffectType](arkts-camera-camera-coloreffecttype-e-sys.md) |
| [ColorReservationType](arkts-camera-camera-colorreservationtype-e-sys.md) |
| [DeferredDeliveryImageType](arkts-camera-camera-deferreddeliveryimagetype-e-sys.md) |
| [DepthDataAccuracy](arkts-camera-camera-depthdataaccuracy-e-sys.md) |
| [DepthDataQualityLevel](arkts-camera-camera-depthdataqualitylevel-e-sys.md) |
| [EffectSuggestionType](arkts-camera-camera-effectsuggestiontype-e-sys.md) |
| [FocusDrivenType](arkts-camera-camera-focusdriventype-e-sys.md) |
| [FocusRangeType](arkts-camera-camera-focusrangetype-e-sys.md) |
| [FocusTrackingMode](arkts-camera-camera-focustrackingmode-e-sys.md) |
| [LightPaintingType](arkts-camera-camera-lightpaintingtype-e-sys.md) |
| [LightStatus](arkts-camera-camera-lightstatus-e-sys.md) |
| [MetadataObjectType](arkts-camera-camera-metadataobjecttype-e-sys.md) |
| [PolicyType](arkts-camera-camera-policytype-e-sys.md) |
| [PortraitEffect](arkts-camera-camera-portraiteffect-e-sys.md) |
| [PortraitThemeType](arkts-camera-camera-portraitthemetype-e-sys.md) |
| [RestoreParamType](arkts-camera-camera-restoreparamtype-e-sys.md) |
| [SceneFeatureType](arkts-camera-camera-scenefeaturetype-e-sys.md) |
| [SceneMode](arkts-camera-camera-scenemode-e-sys.md) |
| [SlowMotionStatus](arkts-camera-camera-slowmotionstatus-e-sys.md) |
| [TimeLapsePreviewType](arkts-camera-camera-timelapsepreviewtype-e-sys.md) |
| [TimeLapseRecordState](arkts-camera-camera-timelapserecordstate-e-sys.md) |
| [TripodStatus](arkts-camera-camera-tripodstatus-e-sys.md) |
| [UsageType](arkts-camera-camera-usagetype-e-sys.md) |
| [VideoMetaType](arkts-camera-camera-videometatype-e-sys.md) |
<!--DelEnd-->

### Types

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [ImageType](arkts-camera-camera-imagetype-t.md) |
