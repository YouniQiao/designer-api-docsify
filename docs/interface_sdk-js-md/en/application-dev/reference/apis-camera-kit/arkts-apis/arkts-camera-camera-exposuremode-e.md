# ExposureMode

枚举，曝光模式。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-camera-enum ExposureMode--><!--Device-camera-enum ExposureMode-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## EXPOSURE_MODE_UNSPECIFIED

```TypeScript
EXPOSURE_MODE_UNSPECIFIED = -1
```

曝光模式未指定。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-ExposureMode-EXPOSURE_MODE_UNSPECIFIED = -1--><!--Device-ExposureMode-EXPOSURE_MODE_UNSPECIFIED = -1-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## EXPOSURE_MODE_LOCKED

```TypeScript
EXPOSURE_MODE_LOCKED = 0
```

锁定曝光模式。不支持曝光区域中心点设置。

设置该模式后，每次拍照时曝光都会默认锁定。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-ExposureMode-EXPOSURE_MODE_LOCKED = 0--><!--Device-ExposureMode-EXPOSURE_MODE_LOCKED = 0-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## EXPOSURE_MODE_AUTO

```TypeScript
EXPOSURE_MODE_AUTO = 1
```

自动曝光模式。支持曝光区域中心点设置，可以使用[AutoExposure.setMeteringPoint](arkts-camera-camera-autoexposure-i.md#setmeteringpoint)接口设置曝光区域中心点。

设置该模式后，仅设置后的首次拍照生效。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-ExposureMode-EXPOSURE_MODE_AUTO = 1--><!--Device-ExposureMode-EXPOSURE_MODE_AUTO = 1-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## EXPOSURE_MODE_CONTINUOUS_AUTO

```TypeScript
EXPOSURE_MODE_CONTINUOUS_AUTO = 2
```

连续自动曝光。不支持曝光区域中心点设置。

设置该模式后，拍照系统会根据每次的环境变化自动调整曝光。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-ExposureMode-EXPOSURE_MODE_CONTINUOUS_AUTO = 2--><!--Device-ExposureMode-EXPOSURE_MODE_CONTINUOUS_AUTO = 2-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## EXPOSURE_MODE_MANUAL

```TypeScript
EXPOSURE_MODE_MANUAL = 3
```

手动曝光。支持设置曝光时长。

设置该模式后，用户可通过  
[ManualExposure.setExposureDuration](../../../reference/apis-camera-kit/arkts-apis-camera-ManualExposure.md#setexposureduration24)设置曝光时长。

**Since:** 24

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-ExposureMode-EXPOSURE_MODE_MANUAL = 3--><!--Device-ExposureMode-EXPOSURE_MODE_MANUAL = 3-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

