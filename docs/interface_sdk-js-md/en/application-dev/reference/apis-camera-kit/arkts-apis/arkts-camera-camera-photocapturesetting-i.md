# PhotoCaptureSetting

Describes the settings for taking an image.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-camera-interface PhotoCaptureSetting--><!--Device-camera-interface PhotoCaptureSetting-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## Modules to Import

```TypeScript
import { camera } from '@kit.CameraKit';
```

## compressionQuality

```TypeScript
compressionQuality?: int
```

Photo image compression quality.

**Type:** int

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-PhotoCaptureSetting-compressionQuality?: int--><!--Device-PhotoCaptureSetting-compressionQuality?: int-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## location

```TypeScript
location?: Location
```

Geolocation information of the image (depending on the device hardware information by default).

**Type:** Location

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-PhotoCaptureSetting-location?: Location--><!--Device-PhotoCaptureSetting-location?: Location-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## mirror

```TypeScript
mirror?: boolean
```

Whether mirror photography is enabled (disabled by default). Before using this enumerated value, call [isMirrorSupported](arkts-camera-camera-photooutput-i.md#isMirrorSupported) to check whether mirror photography is supported. **true** if enabled, **false** otherwise.

**Type:** boolean

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-PhotoCaptureSetting-mirror?: boolean--><!--Device-PhotoCaptureSetting-mirror?: boolean-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## quality

```TypeScript
quality?: QualityLevel
```

Image quality (high by default).

**Type:** QualityLevel

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-PhotoCaptureSetting-quality?: QualityLevel--><!--Device-PhotoCaptureSetting-quality?: QualityLevel-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## rotation

```TypeScript
rotation?: ImageRotation
```

Rotation angle of the image. The default value is **0**, indicating clockwise rotation.

**Type:** [ImageRotation](arkts-camera-camera-imagerotation-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-PhotoCaptureSetting-rotation?: ImageRotation--><!--Device-PhotoCaptureSetting-rotation?: ImageRotation-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

