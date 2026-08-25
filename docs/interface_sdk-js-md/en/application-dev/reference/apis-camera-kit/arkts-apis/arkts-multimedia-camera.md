# @ohos.multimedia.camera(AutoDeviceSwitch)

The module provides a set of camera service APIs for you to easily develop a camera application. The application can access and operate the camera hardware to implement basic operations, such as preview, taking photos, and recording videos. It can also perform more operations, for example, controlling the flash and exposure time, and focusing or adjusting the focus.

> **NOTE：**&gt;
> - This topic describes only system APIs provided by the module. For details about its public APIs, see
> [@ohos.multimedia.camera (Camera Management)](#ohosmultimediacameraautodeviceswitch).

**Since:** 10

**System capability:** SystemCapability.Multimedia.Camera.Core

## Modules to Import

```TypeScript
import { camera } from 'kits/@kit.CameraKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [getCameraManager(AutoDeviceSwitch)](arkts-camera-camera-getcameramanager-f.md) |

<!--Del-->
### Classes(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [EffectSuggestionStatus(AutoDeviceSwitch)](arkts-camera-camera-effectsuggestionstatus-c-sys.md) |
<!--DelEnd-->

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [Aperture(AutoDeviceSwitch)](arkts-camera-camera-aperture-i.md) |
| [ApertureQuery(AutoDeviceSwitch)](arkts-camera-camera-aperturequery-i.md) |
| [AutoDeviceSwitch(AutoDeviceSwitch)](arkts-camera-camera-autodeviceswitch-i.md) |
| [AutoDeviceSwitchQuery(AutoDeviceSwitch)](arkts-camera-camera-autodeviceswitchquery-i.md) |
| [AutoDeviceSwitchStatus(AutoDeviceSwitch)](arkts-camera-camera-autodeviceswitchstatus-i.md) |
| [AutoExposure(AutoDeviceSwitch)](arkts-camera-camera-autoexposure-i.md) |
| [AutoExposureQuery(AutoDeviceSwitch)](arkts-camera-camera-autoexposurequery-i.md) |
| [CameraConcurrentInfo(AutoDeviceSwitch)](arkts-camera-camera-cameraconcurrentinfo-i.md) |
| [CameraDevice(AutoDeviceSwitch)](arkts-camera-camera-cameradevice-i.md) |
| [CameraInput(AutoDeviceSwitch)](arkts-camera-camera-camerainput-i.md) |
| [CameraManager(AutoDeviceSwitch)](arkts-camera-camera-cameramanager-i.md) |
| [CameraOcclusionDetectionResult(AutoDeviceSwitch)](arkts-camera-camera-cameraocclusiondetectionresult-i.md) |
| [CameraOutput(AutoDeviceSwitch)](arkts-camera-camera-cameraoutput-i.md) |
| [CameraOutputCapability(AutoDeviceSwitch)](arkts-camera-camera-cameraoutputcapability-i.md) |
| [CameraStatusInfo(AutoDeviceSwitch)](arkts-camera-camera-camerastatusinfo-i.md) |
| [CaptureEndInfo(AutoDeviceSwitch)](arkts-camera-camera-captureendinfo-i.md) |
| [CapturePhoto(AutoDeviceSwitch)](arkts-camera-camera-capturephoto-i.md) |
| [CaptureSession(AutoDeviceSwitch)](arkts-camera-camera-capturesession-i.md) |
| [CaptureStartInfo(AutoDeviceSwitch)](arkts-camera-camera-capturestartinfo-i.md) |
| [ColorManagement(AutoDeviceSwitch)](arkts-camera-camera-colormanagement-i.md) |
| [ColorManagementQuery(AutoDeviceSwitch)](arkts-camera-camera-colormanagementquery-i.md) |
| [ControlCenter(AutoDeviceSwitch)](arkts-camera-camera-controlcenter-i.md) |
| [ControlCenterQuery(AutoDeviceSwitch)](arkts-camera-camera-controlcenterquery-i.md) |
| [ControlCenterStatusInfo(AutoDeviceSwitch)](arkts-camera-camera-controlcenterstatusinfo-i.md) |
| [ExposureInfo(AutoDeviceSwitch)](arkts-camera-camera-exposureinfo-i.md) |
| [Flash(AutoDeviceSwitch)](arkts-camera-camera-flash-i.md) |
| [FlashQuery(AutoDeviceSwitch)](arkts-camera-camera-flashquery-i.md) |
| [Focus(AutoDeviceSwitch)](arkts-camera-camera-focus-i.md) |
| [FocusQuery(AutoDeviceSwitch)](arkts-camera-camera-focusquery-i.md) |
| [FoldStatusInfo(AutoDeviceSwitch)](arkts-camera-camera-foldstatusinfo-i.md) |
| [FrameRateRange(AutoDeviceSwitch)](arkts-camera-camera-frameraterange-i.md) |
| [FrameShutterEndInfo(AutoDeviceSwitch)](arkts-camera-camera-frameshutterendinfo-i.md) |
| [FrameShutterInfo(AutoDeviceSwitch)](arkts-camera-camera-frameshutterinfo-i.md) |
| [IsoInfo(AutoDeviceSwitch)](arkts-camera-camera-isoinfo-i.md) |
| [Location(AutoDeviceSwitch)](arkts-camera-camera-location-i.md) |
| [Macro(AutoDeviceSwitch)](arkts-camera-camera-macro-i.md) |
| [MacroQuery(AutoDeviceSwitch)](arkts-camera-camera-macroquery-i.md) |
| [ManualExposure(AutoDeviceSwitch)](arkts-camera-camera-manualexposure-i.md) |
| [ManualExposureQuery(AutoDeviceSwitch)](arkts-camera-camera-manualexposurequery-i.md) |
| [ManualFocus(AutoDeviceSwitch)](arkts-camera-camera-manualfocus-i.md) |
| [ManualFocusQuery(AutoDeviceSwitch)](arkts-camera-camera-manualfocusquery-i.md) |
| [ManualIso(AutoDeviceSwitch)](arkts-camera-camera-manualiso-i.md) |
| [ManualIsoQuery(AutoDeviceSwitch)](arkts-camera-camera-manualisoquery-i.md) |
| [MetadataBarcodeObject(AutoDeviceSwitch)](arkts-camera-camera-metadatabarcodeobject-i.md) |
| [MetadataBasicFaceObject(AutoDeviceSwitch)](arkts-camera-camera-metadatabasicfaceobject-i.md) |
| [MetadataCatBodyObject(AutoDeviceSwitch)](arkts-camera-camera-metadatacatbodyobject-i.md) |
| [MetadataCatFaceObject(AutoDeviceSwitch)](arkts-camera-camera-metadatacatfaceobject-i.md) |
| [MetadataDogBodyObject(AutoDeviceSwitch)](arkts-camera-camera-metadatadogbodyobject-i.md) |
| [MetadataDogFaceObject(AutoDeviceSwitch)](arkts-camera-camera-metadatadogfaceobject-i.md) |
| [MetadataFaceObject(AutoDeviceSwitch)](arkts-camera-camera-metadatafaceobject-i.md) |
| [MetadataHumanBodyObject(AutoDeviceSwitch)](arkts-camera-camera-metadatahumanbodyobject-i.md) |
| [MetadataObject(AutoDeviceSwitch)](arkts-camera-camera-metadataobject-i.md) |
| [MetadataOutput(AutoDeviceSwitch)](arkts-camera-camera-metadataoutput-i.md) |
| [MetadataSalientDetectionObject(AutoDeviceSwitch)](arkts-camera-camera-metadatasalientdetectionobject-i.md) |
| [OIS(AutoDeviceSwitch)](arkts-camera-camera-ois-i.md) |
| [OISQuery(AutoDeviceSwitch)](arkts-camera-camera-oisquery-i.md) |
| [Photo(AutoDeviceSwitch)](arkts-camera-camera-photo-i.md) |
| [PhotoCaptureSetting(AutoDeviceSwitch)](arkts-camera-camera-photocapturesetting-i.md) |
| [PhotoConflictFunctions(AutoDeviceSwitch)](arkts-camera-camera-photoconflictfunctions-i.md) |
| [PhotoFunctions(AutoDeviceSwitch)](arkts-camera-camera-photofunctions-i.md) |
| [PhotoOutput(AutoDeviceSwitch)](arkts-camera-camera-photooutput-i.md) |
| [PhotoSession(AutoDeviceSwitch)](arkts-camera-camera-photosession-i.md) |
| [PhotoSessionForSys(AutoDeviceSwitch)](arkts-camera-camera-photosessionforsys-i.md) |
| [PhysicalAperture(AutoDeviceSwitch)](arkts-camera-camera-physicalaperture-i.md) |
| [Point(AutoDeviceSwitch)](arkts-camera-camera-point-i.md) |
| [PortraitPhotoConflictFunctions(AutoDeviceSwitch)](arkts-camera-camera-portraitphotoconflictfunctions-i.md) |
| [PortraitPhotoFunctions(AutoDeviceSwitch)](arkts-camera-camera-portraitphotofunctions-i.md) |
| [PreviewOutput(AutoDeviceSwitch)](arkts-camera-camera-previewoutput-i.md) |
| [Profile(AutoDeviceSwitch)](arkts-camera-camera-profile-i.md) |
| [Rect(AutoDeviceSwitch)](arkts-camera-camera-rect-i.md) |
| [SecureSession(AutoDeviceSwitch)](arkts-camera-camera-securesession-i.md) |
| [Session(AutoDeviceSwitch)](arkts-camera-camera-session-i.md) |
| [Size(AutoDeviceSwitch)](arkts-camera-camera-size-i.md) |
| [SmoothZoomInfo(AutoDeviceSwitch)](arkts-camera-camera-smoothzoominfo-i.md) |
| [Stabilization(AutoDeviceSwitch)](arkts-camera-camera-stabilization-i.md) |
| [StabilizationQuery(AutoDeviceSwitch)](arkts-camera-camera-stabilizationquery-i.md) |
| [TorchStatusInfo(AutoDeviceSwitch)](arkts-camera-camera-torchstatusinfo-i.md) |
| [VideoConflictFunctions(AutoDeviceSwitch)](arkts-camera-camera-videoconflictfunctions-i.md) |
| [VideoFunctions(AutoDeviceSwitch)](arkts-camera-camera-videofunctions-i.md) |
| [VideoOutput(AutoDeviceSwitch)](arkts-camera-camera-videooutput-i.md) |
| [VideoProfile(AutoDeviceSwitch)](arkts-camera-camera-videoprofile-i.md) |
| [VideoSession(AutoDeviceSwitch)](arkts-camera-camera-videosession-i.md) |
| [VideoSessionForSys(AutoDeviceSwitch)](arkts-camera-camera-videosessionforsys-i.md) |
| [WhiteBalance(AutoDeviceSwitch)](arkts-camera-camera-whitebalance-i.md) |
| [WhiteBalanceQuery(AutoDeviceSwitch)](arkts-camera-camera-whitebalancequery-i.md) |
| [Zoom(AutoDeviceSwitch)](arkts-camera-camera-zoom-i.md) |
| [ZoomPointInfo(AutoDeviceSwitch)](arkts-camera-camera-zoompointinfo-i.md) |
| [ZoomQuery(AutoDeviceSwitch)](arkts-camera-camera-zoomquery-i.md) |
| [ZoomRange(AutoDeviceSwitch)](arkts-camera-camera-zoomrange-i.md) |

<!--Del-->
### Interfaces(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [Aperture(AutoDeviceSwitch)](arkts-camera-camera-aperture-i-sys.md) |
| [ApertureInfo(AutoDeviceSwitch)](arkts-camera-camera-apertureinfo-i-sys.md) |
| [ApertureQuery(AutoDeviceSwitch)](arkts-camera-camera-aperturequery-i-sys.md) |
| [ApertureVideoSession(AutoDeviceSwitch)](arkts-camera-camera-aperturevideosession-i-sys.md) |
| [Beauty(AutoDeviceSwitch)](arkts-camera-camera-beauty-i-sys.md) |
| [BeautyQuery(AutoDeviceSwitch)](arkts-camera-camera-beautyquery-i-sys.md) |
| [CameraDevice(AutoDeviceSwitch)](arkts-camera-camera-cameradevice-i-sys.md) |
| [CameraInput(AutoDeviceSwitch)](arkts-camera-camera-camerainput-i-sys.md) |
| [CameraManager(AutoDeviceSwitch)](arkts-camera-camera-cameramanager-i-sys.md) |
| [CameraOutputCapability(AutoDeviceSwitch)](arkts-camera-camera-cameraoutputcapability-i-sys.md) |
| [CameraSharedStatusInfo(AutoDeviceSwitch)](arkts-camera-camera-camerasharedstatusinfo-i-sys.md) |
| [CaptureSession(AutoDeviceSwitch)](arkts-camera-camera-capturesession-i-sys.md) |
| [ColorEffect(AutoDeviceSwitch)](arkts-camera-camera-coloreffect-i-sys.md) |
| [ColorEffectQuery(AutoDeviceSwitch)](arkts-camera-camera-coloreffectquery-i-sys.md) |
| [ColorReservation(AutoDeviceSwitch)](arkts-camera-camera-colorreservation-i-sys.md) |
| [ColorReservationQuery(AutoDeviceSwitch)](arkts-camera-camera-colorreservationquery-i-sys.md) |
| [ControlCenterSession(AutoDeviceSwitch)](arkts-camera-camera-controlcentersession-i-sys.md) |
| [DeferredPhotoProxy(AutoDeviceSwitch)](arkts-camera-camera-deferredphotoproxy-i-sys.md) |
| [DeferredVideoEnhancementInfo(AutoDeviceSwitch)](arkts-camera-camera-deferredvideoenhancementinfo-i-sys.md) |
| [DepthData(AutoDeviceSwitch)](arkts-camera-camera-depthdata-i-sys.md) |
| [DepthDataOutput(AutoDeviceSwitch)](arkts-camera-camera-depthdataoutput-i-sys.md) |
| [DepthFusion(AutoDeviceSwitch)](arkts-camera-camera-depthfusion-i-sys.md) |
| [DepthFusionQuery(AutoDeviceSwitch)](arkts-camera-camera-depthfusionquery-i-sys.md) |
| [DepthProfile(AutoDeviceSwitch)](arkts-camera-camera-depthprofile-i-sys.md) |
| [EffectSuggestion(AutoDeviceSwitch)](arkts-camera-camera-effectsuggestion-i-sys.md) |
| [Flash(AutoDeviceSwitch)](arkts-camera-camera-flash-i-sys.md) |
| [FlashQuery(AutoDeviceSwitch)](arkts-camera-camera-flashquery-i-sys.md) |
| [FluorescencePhotoSession(AutoDeviceSwitch)](arkts-camera-camera-fluorescencephotosession-i-sys.md) |
| [Focus(AutoDeviceSwitch)](arkts-camera-camera-focus-i-sys.md) |
| [FocusQuery(AutoDeviceSwitch)](arkts-camera-camera-focusquery-i-sys.md) |
| [FocusTrackingInfo(AutoDeviceSwitch)](arkts-camera-camera-focustrackinginfo-i-sys.md) |
| [HighResolutionPhotoSession(AutoDeviceSwitch)](arkts-camera-camera-highresolutionphotosession-i-sys.md) |
| [ImagingMode(AutoDeviceSwitch)](arkts-camera-camera-imagingmode-i-sys.md) |
| [ImagingModeQuery(AutoDeviceSwitch)](arkts-camera-camera-imagingmodequery-i-sys.md) |
| [LcdFlashStatus(AutoDeviceSwitch)](arkts-camera-camera-lcdflashstatus-i-sys.md) |
| [LightPaintingPhotoSession(AutoDeviceSwitch)](arkts-camera-camera-lightpaintingphotosession-i-sys.md) |
| [LuminationInfo(AutoDeviceSwitch)](arkts-camera-camera-luminationinfo-i-sys.md) |
| [MacroPhotoSession(AutoDeviceSwitch)](arkts-camera-camera-macrophotosession-i-sys.md) |
| [MacroVideoSession(AutoDeviceSwitch)](arkts-camera-camera-macrovideosession-i-sys.md) |
| [ManualExposure(AutoDeviceSwitch)](arkts-camera-camera-manualexposure-i-sys.md) |
| [ManualExposureQuery(AutoDeviceSwitch)](arkts-camera-camera-manualexposurequery-i-sys.md) |
| [ManualIsoQuery(AutoDeviceSwitch)](arkts-camera-camera-manualisoquery-i-sys.md) |
| [MetadataObject(AutoDeviceSwitch)](arkts-camera-camera-metadataobject-i-sys.md) |
| [NightPhotoSession(AutoDeviceSwitch)](arkts-camera-camera-nightphotosession-i-sys.md) |
| [PanoramaPhotoSession(AutoDeviceSwitch)](arkts-camera-camera-panoramaphotosession-i-sys.md) |
| [Photo(AutoDeviceSwitch)](arkts-camera-camera-photo-i-sys.md) |
| [PhotoOutput(AutoDeviceSwitch)](arkts-camera-camera-photooutput-i-sys.md) |
| [PhotoSession(AutoDeviceSwitch)](arkts-camera-camera-photosession-i-sys.md) |
| [Portrait(AutoDeviceSwitch)](arkts-camera-camera-portrait-i-sys.md) |
| [PortraitPhotoSession(AutoDeviceSwitch)](arkts-camera-camera-portraitphotosession-i-sys.md) |
| [PortraitQuery(AutoDeviceSwitch)](arkts-camera-camera-portraitquery-i-sys.md) |
| [PrelaunchConfig(AutoDeviceSwitch)](arkts-camera-camera-prelaunchconfig-i-sys.md) |
| [PreviewOutput(AutoDeviceSwitch)](arkts-camera-camera-previewoutput-i-sys.md) |
| [ProfessionalPhotoSession(AutoDeviceSwitch)](arkts-camera-camera-professionalphotosession-i-sys.md) |
| [ProfessionalVideoSession(AutoDeviceSwitch)](arkts-camera-camera-professionalvideosession-i-sys.md) |
| [QuickShotPhotoSession(AutoDeviceSwitch)](arkts-camera-camera-quickshotphotosession-i-sys.md) |
| [QuickThumbnail(AutoDeviceSwitch)](arkts-camera-camera-quickthumbnail-i-sys.md) |
| [SceneDetection(AutoDeviceSwitch)](arkts-camera-camera-scenedetection-i-sys.md) |
| [SceneDetectionQuery(AutoDeviceSwitch)](arkts-camera-camera-scenedetectionquery-i-sys.md) |
| [SceneFeatureDetectionResult(AutoDeviceSwitch)](arkts-camera-camera-scenefeaturedetectionresult-i-sys.md) |
| [Session(AutoDeviceSwitch)](arkts-camera-camera-session-i-sys.md) |
| [SettingParam(AutoDeviceSwitch)](arkts-camera-camera-settingparam-i-sys.md) |
| [SketchStatusData(AutoDeviceSwitch)](arkts-camera-camera-sketchstatusdata-i-sys.md) |
| [SlowMotionVideoSession(AutoDeviceSwitch)](arkts-camera-camera-slowmotionvideosession-i-sys.md) |
| [TimeLapsePhotoSession(AutoDeviceSwitch)](arkts-camera-camera-timelapsephotosession-i-sys.md) |
| [TripodDetectionResult(AutoDeviceSwitch)](arkts-camera-camera-tripoddetectionresult-i-sys.md) |
| [TryAEInfo(AutoDeviceSwitch)](arkts-camera-camera-tryaeinfo-i-sys.md) |
| [VideoOutput(AutoDeviceSwitch)](arkts-camera-camera-videooutput-i-sys.md) |
| [VideoSession(AutoDeviceSwitch)](arkts-camera-camera-videosession-i-sys.md) |
| [WhiteBalance(AutoDeviceSwitch)](arkts-camera-camera-whitebalance-i-sys.md) |
| [WhiteBalanceGains(AutoDeviceSwitch)](arkts-camera-camera-whitebalancegains-i-sys.md) |
| [WhiteBalanceQuery(AutoDeviceSwitch)](arkts-camera-camera-whitebalancequery-i-sys.md) |
| [Zoom(AutoDeviceSwitch)](arkts-camera-camera-zoom-i-sys.md) |
| [ZoomQuery(AutoDeviceSwitch)](arkts-camera-camera-zoomquery-i-sys.md) |
<!--DelEnd-->

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [AutomotiveCameraPosition(AutoDeviceSwitch)](arkts-camera-camera-automotivecameraposition-e.md) |
| [CameraConcurrentType(AutoDeviceSwitch)](arkts-camera-camera-cameraconcurrenttype-e.md) |
| [CameraErrorCode(AutoDeviceSwitch)](arkts-camera-camera-cameraerrorcode-e.md) |
| [CameraFormat(AutoDeviceSwitch)](arkts-camera-camera-cameraformat-e.md) |
| [CameraPosition(AutoDeviceSwitch)](arkts-camera-camera-cameraposition-e.md) |
| [CameraStatus(AutoDeviceSwitch)](arkts-camera-camera-camerastatus-e.md) |
| [CameraType(AutoDeviceSwitch)](arkts-camera-camera-cameratype-e.md) |
| [ConnectionType(AutoDeviceSwitch)](arkts-camera-camera-connectiontype-e.md) |
| [ControlCenterEffectType(AutoDeviceSwitch)](arkts-camera-camera-controlcentereffecttype-e.md) |
| [Emotion(AutoDeviceSwitch)](arkts-camera-camera-emotion-e.md) |
| [ExposureMeteringMode(AutoDeviceSwitch)](arkts-camera-camera-exposuremeteringmode-e.md) |
| [ExposureMode(AutoDeviceSwitch)](arkts-camera-camera-exposuremode-e.md) |
| [ExposureState(AutoDeviceSwitch)](arkts-camera-camera-exposurestate-e.md) |
| [FlashMode(AutoDeviceSwitch)](arkts-camera-camera-flashmode-e.md) |
| [FlashState(AutoDeviceSwitch)](arkts-camera-camera-flashstate-e.md) |
| [FocusMode(AutoDeviceSwitch)](arkts-camera-camera-focusmode-e.md) |
| [FocusState(AutoDeviceSwitch)](arkts-camera-camera-focusstate-e.md) |
| [FoldStatus(AutoDeviceSwitch)](arkts-camera-camera-foldstatus-e.md) |
| [HostDeviceType(AutoDeviceSwitch)](arkts-camera-camera-hostdevicetype-e.md) |
| [ImageRotation(AutoDeviceSwitch)](arkts-camera-camera-imagerotation-e.md) |
| [MetadataObjectType(AutoDeviceSwitch)](arkts-camera-camera-metadataobjecttype-e.md) |
| [OISAxes(AutoDeviceSwitch)](arkts-camera-camera-oisaxes-e.md) |
| [OISMode(AutoDeviceSwitch)](arkts-camera-camera-oismode-e.md) |
| [PhotoQualityPrioritization(AutoDeviceSwitch)](arkts-camera-camera-photoqualityprioritization-e.md) |
| [PreconfigRatio(AutoDeviceSwitch)](arkts-camera-camera-preconfigratio-e.md) |
| [PreconfigType(AutoDeviceSwitch)](arkts-camera-camera-preconfigtype-e.md) |
| [QualityLevel(AutoDeviceSwitch)](arkts-camera-camera-qualitylevel-e.md) |
| [QualityPrioritization(AutoDeviceSwitch)](arkts-camera-camera-qualityprioritization-e.md) |
| [SceneMode(AutoDeviceSwitch)](arkts-camera-camera-scenemode-e.md) |
| [SensorColorFilterArrangement(AutoDeviceSwitch)](arkts-camera-camera-sensorcolorfilterarrangement-e.md) |
| [SmoothZoomMode(AutoDeviceSwitch)](arkts-camera-camera-smoothzoommode-e.md) |
| [SystemPressureLevel(AutoDeviceSwitch)](arkts-camera-camera-systempressurelevel-e.md) |
| [TorchMode(AutoDeviceSwitch)](arkts-camera-camera-torchmode-e.md) |
| [VideoCodecType(AutoDeviceSwitch)](arkts-camera-camera-videocodectype-e.md) |
| [VideoStabilizationMode(AutoDeviceSwitch)](arkts-camera-camera-videostabilizationmode-e.md) |
| [WhiteBalanceMode(AutoDeviceSwitch)](arkts-camera-camera-whitebalancemode-e.md) |

<!--Del-->
### Enums(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [AuxiliaryStatus(AutoDeviceSwitch)](arkts-camera-camera-auxiliarystatus-e-sys.md) |
| [AuxiliaryType(AutoDeviceSwitch)](arkts-camera-camera-auxiliarytype-e-sys.md) |
| [BeautyType(AutoDeviceSwitch)](arkts-camera-camera-beautytype-e-sys.md) |
| [CameraErrorCode(AutoDeviceSwitch)](arkts-camera-camera-cameraerrorcode-e-sys.md) |
| [CameraFormat(AutoDeviceSwitch)](arkts-camera-camera-cameraformat-e-sys.md) |
| [CameraImagingMode(AutoDeviceSwitch)](arkts-camera-camera-cameraimagingmode-e-sys.md) |
| [CameraSharedStatus(AutoDeviceSwitch)](arkts-camera-camera-camerasharedstatus-e-sys.md) |
| [ColorEffectType(AutoDeviceSwitch)](arkts-camera-camera-coloreffecttype-e-sys.md) |
| [ColorReservationType(AutoDeviceSwitch)](arkts-camera-camera-colorreservationtype-e-sys.md) |
| [DeferredDeliveryImageType(AutoDeviceSwitch)](arkts-camera-camera-deferreddeliveryimagetype-e-sys.md) |
| [DepthDataAccuracy(AutoDeviceSwitch)](arkts-camera-camera-depthdataaccuracy-e-sys.md) |
| [DepthDataQualityLevel(AutoDeviceSwitch)](arkts-camera-camera-depthdataqualitylevel-e-sys.md) |
| [EffectSuggestionType(AutoDeviceSwitch)](arkts-camera-camera-effectsuggestiontype-e-sys.md) |
| [ExposureMeteringMode(AutoDeviceSwitch)](arkts-camera-camera-exposuremeteringmode-e-sys.md) |
| [FocusDrivenType(AutoDeviceSwitch)](arkts-camera-camera-focusdriventype-e-sys.md) |
| [FocusRangeType(AutoDeviceSwitch)](arkts-camera-camera-focusrangetype-e-sys.md) |
| [FocusTrackingMode(AutoDeviceSwitch)](arkts-camera-camera-focustrackingmode-e-sys.md) |
| [LightPaintingType(AutoDeviceSwitch)](arkts-camera-camera-lightpaintingtype-e-sys.md) |
| [LightStatus(AutoDeviceSwitch)](arkts-camera-camera-lightstatus-e-sys.md) |
| [MetadataObjectType(AutoDeviceSwitch)](arkts-camera-camera-metadataobjecttype-e-sys.md) |
| [PolicyType(AutoDeviceSwitch)](arkts-camera-camera-policytype-e-sys.md) |
| [PortraitEffect(AutoDeviceSwitch)](arkts-camera-camera-portraiteffect-e-sys.md) |
| [PortraitThemeType(AutoDeviceSwitch)](arkts-camera-camera-portraitthemetype-e-sys.md) |
| [RestoreParamType(AutoDeviceSwitch)](arkts-camera-camera-restoreparamtype-e-sys.md) |
| [SceneFeatureType(AutoDeviceSwitch)](arkts-camera-camera-scenefeaturetype-e-sys.md) |
| [SceneMode(AutoDeviceSwitch)](arkts-camera-camera-scenemode-e-sys.md) |
| [SlowMotionStatus(AutoDeviceSwitch)](arkts-camera-camera-slowmotionstatus-e-sys.md) |
| [TimeLapsePreviewType(AutoDeviceSwitch)](arkts-camera-camera-timelapsepreviewtype-e-sys.md) |
| [TimeLapseRecordState(AutoDeviceSwitch)](arkts-camera-camera-timelapserecordstate-e-sys.md) |
| [TripodStatus(AutoDeviceSwitch)](arkts-camera-camera-tripodstatus-e-sys.md) |
| [UsageType(AutoDeviceSwitch)](arkts-camera-camera-usagetype-e-sys.md) |
| [VideoMetaType(AutoDeviceSwitch)](arkts-camera-camera-videometatype-e-sys.md) |
<!--DelEnd-->

### Types

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [ImageType(AutoDeviceSwitch)](arkts-camera-camera-imagetype-t.md) |
