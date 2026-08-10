# PhotoCaptureSetting

拍摄照片的设置。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-camera-interface PhotoCaptureSetting--><!--Device-camera-interface PhotoCaptureSetting-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## Modules to Import

```TypeScript
import { camera } from 'kits/@kit.CameraKit';
```

## compressionQuality

```TypeScript
compressionQuality?: int
```

图片压缩质量值，取值范围为(1, 100)。

当compressionQuality未下发时，默认按quality生效；若quality与compressionQuality同时下发则按compressionQuality下发生效；若quality与compressionQuality均未下发则图片质量默认是高等。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-PhotoCaptureSetting-compressionQuality?: int--><!--Device-PhotoCaptureSetting-compressionQuality?: int-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## location

```TypeScript
location?: Location
```

图片地理位置信息（默认以设备硬件信息为准）。

**Type:** [Location](../../apis-location-kit/arkts-apis/arkts-location-geolocationmanager-location-i.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-PhotoCaptureSetting-location?: Location--><!--Device-PhotoCaptureSetting-location?: Location-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## mirror

```TypeScript
mirror?: boolean
```

镜像使能开关（默认关）。使用之前需要使用[isMirrorSupported](arkts-camera-camera-photooutput-i.md#ismirrorsupported)进行判断是否支持。true表示使能，false表示不使能。

**Type:** boolean

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-PhotoCaptureSetting-mirror?: boolean--><!--Device-PhotoCaptureSetting-mirror?: boolean-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## quality

```TypeScript
quality?: QualityLevel
```

图片质量。

当quality未下发时，默认按compressionQuality下发生效；若quality与compressionQuality同时下发则按compressionQuality下发生效；若quality与compressionQuality均未下发则图片质量默认是高等。

**Type:** [QualityLevel](../../apis-image-kit/arkts-apis/arkts-image-videoprocessingengine-qualitylevel-e.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-PhotoCaptureSetting-quality?: QualityLevel--><!--Device-PhotoCaptureSetting-quality?: QualityLevel-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## rotation

```TypeScript
rotation?: ImageRotation
```

图片旋转角度（默认0度，顺时针旋转）。

**Type:** [ImageRotation](arkts-camera-camera-imagerotation-e.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-PhotoCaptureSetting-rotation?: ImageRotation--><!--Device-PhotoCaptureSetting-rotation?: ImageRotation-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

