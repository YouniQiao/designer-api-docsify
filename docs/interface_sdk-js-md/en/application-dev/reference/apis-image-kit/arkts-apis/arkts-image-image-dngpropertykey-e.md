# DngPropertyKey

表示DNG图片信息的枚举。

> **说明：**
> 
> - 关于字段的更详细描述请参考DNG协议文档DNG Specification 1.4.0.0。
> 
> - 返回字段类型具体参考[DngMetadata](arkts-image-image-dngmetadata-c.md)。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

<!--Device-image-enum DngPropertyKey--><!--Device-image-enum DngPropertyKey-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## DNG_VERSION

```TypeScript
DNG_VERSION = 'DNGVersion'
```

DNG图片的版本号。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DngPropertyKey-DNG_VERSION = 'DNGVersion'--><!--Device-DngPropertyKey-DNG_VERSION = 'DNGVersion'-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## DNG_BACKWARD_VERSION

```TypeScript
DNG_BACKWARD_VERSION = 'DNGBackwardVersion'
```

DNG文件向后兼容的最低版本号。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DngPropertyKey-DNG_BACKWARD_VERSION = 'DNGBackwardVersion'--><!--Device-DngPropertyKey-DNG_BACKWARD_VERSION = 'DNGBackwardVersion'-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## UNIQUE_CAMERA_MODEL

```TypeScript
UNIQUE_CAMERA_MODEL = 'UniqueCameraModel'
```

相机的唯一型号标识，用于区分不同设备。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DngPropertyKey-UNIQUE_CAMERA_MODEL = 'UniqueCameraModel'--><!--Device-DngPropertyKey-UNIQUE_CAMERA_MODEL = 'UniqueCameraModel'-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## LOCALIZED_CAMERA_MODEL

```TypeScript
LOCALIZED_CAMERA_MODEL = 'LocalizedCameraModel'
```

本地化后的相机型号名称。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DngPropertyKey-LOCALIZED_CAMERA_MODEL = 'LocalizedCameraModel'--><!--Device-DngPropertyKey-LOCALIZED_CAMERA_MODEL = 'LocalizedCameraModel'-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## CFA_PLANE_COLOR

```TypeScript
CFA_PLANE_COLOR = 'CFAPlaneColor'
```

CFA各平面的颜色通道定义。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DngPropertyKey-CFA_PLANE_COLOR = 'CFAPlaneColor'--><!--Device-DngPropertyKey-CFA_PLANE_COLOR = 'CFAPlaneColor'-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## CFA_LAYOUT

```TypeScript
CFA_LAYOUT = 'CFALayout'
```

CFA布局类型，如RGGB、BGGR等。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DngPropertyKey-CFA_LAYOUT = 'CFALayout'--><!--Device-DngPropertyKey-CFA_LAYOUT = 'CFALayout'-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## LINEARIZATION_TABLE

```TypeScript
LINEARIZATION_TABLE = 'LinearizationTable'
```

线性化查找表，用于将原始传感器值映射为线性光强度。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DngPropertyKey-LINEARIZATION_TABLE = 'LinearizationTable'--><!--Device-DngPropertyKey-LINEARIZATION_TABLE = 'LinearizationTable'-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## BLACK_LEVEL_REPEAT_DIM

```TypeScript
BLACK_LEVEL_REPEAT_DIM = 'BlackLevelRepeatDim'
```

黑电平重复维度。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DngPropertyKey-BLACK_LEVEL_REPEAT_DIM = 'BlackLevelRepeatDim'--><!--Device-DngPropertyKey-BLACK_LEVEL_REPEAT_DIM = 'BlackLevelRepeatDim'-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## BLACK_LEVEL

```TypeScript
BLACK_LEVEL = 'BlackLevel'
```

零光照下的编码电平，按CFA平面顺序排列。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DngPropertyKey-BLACK_LEVEL = 'BlackLevel'--><!--Device-DngPropertyKey-BLACK_LEVEL = 'BlackLevel'-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## BLACK_LEVEL_DELTA_H

```TypeScript
BLACK_LEVEL_DELTA_H = 'BlackLevelDeltaH'
```

水平方向黑电平校正增量。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DngPropertyKey-BLACK_LEVEL_DELTA_H = 'BlackLevelDeltaH'--><!--Device-DngPropertyKey-BLACK_LEVEL_DELTA_H = 'BlackLevelDeltaH'-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## BLACK_LEVEL_DELTA_V

```TypeScript
BLACK_LEVEL_DELTA_V = 'BlackLevelDeltaV'
```

垂直方向黑电平校正增量。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DngPropertyKey-BLACK_LEVEL_DELTA_V = 'BlackLevelDeltaV'--><!--Device-DngPropertyKey-BLACK_LEVEL_DELTA_V = 'BlackLevelDeltaV'-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## WHITE_LEVEL

```TypeScript
WHITE_LEVEL = 'WhiteLevel'
```

白电平，表示传感器最大有效输出。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DngPropertyKey-WHITE_LEVEL = 'WhiteLevel'--><!--Device-DngPropertyKey-WHITE_LEVEL = 'WhiteLevel'-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## DEFAULT_SCALE

```TypeScript
DEFAULT_SCALE = 'DefaultScale'
```

默认缩放比例。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DngPropertyKey-DEFAULT_SCALE = 'DefaultScale'--><!--Device-DngPropertyKey-DEFAULT_SCALE = 'DefaultScale'-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## DEFAULT_CROP_ORIGIN

```TypeScript
DEFAULT_CROP_ORIGIN = 'DefaultCropOrigin'
```

默认裁剪区域的左上角坐标（x, y）。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DngPropertyKey-DEFAULT_CROP_ORIGIN = 'DefaultCropOrigin'--><!--Device-DngPropertyKey-DEFAULT_CROP_ORIGIN = 'DefaultCropOrigin'-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## DEFAULT_CROP_SIZE

```TypeScript
DEFAULT_CROP_SIZE = 'DefaultCropSize'
```

默认裁剪区域的宽度和高度。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DngPropertyKey-DEFAULT_CROP_SIZE = 'DefaultCropSize'--><!--Device-DngPropertyKey-DEFAULT_CROP_SIZE = 'DefaultCropSize'-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## COLOR_MATRIX1

```TypeScript
COLOR_MATRIX1 = 'ColorMatrix1'
```

第一校准光源下的色彩变换矩阵。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DngPropertyKey-COLOR_MATRIX1 = 'ColorMatrix1'--><!--Device-DngPropertyKey-COLOR_MATRIX1 = 'ColorMatrix1'-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## COLOR_MATRIX2

```TypeScript
COLOR_MATRIX2 = 'ColorMatrix2'
```

第二校准光源下的色彩变换矩阵。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DngPropertyKey-COLOR_MATRIX2 = 'ColorMatrix2'--><!--Device-DngPropertyKey-COLOR_MATRIX2 = 'ColorMatrix2'-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## CAMERA_CALIBRATION1

```TypeScript
CAMERA_CALIBRATION1 = 'CameraCalibration1'
```

第一校准光源下的相机校准矩阵。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DngPropertyKey-CAMERA_CALIBRATION1 = 'CameraCalibration1'--><!--Device-DngPropertyKey-CAMERA_CALIBRATION1 = 'CameraCalibration1'-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## CAMERA_CALIBRATION2

```TypeScript
CAMERA_CALIBRATION2 = 'CameraCalibration2'
```

第二校准光源下的相机校准矩阵。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DngPropertyKey-CAMERA_CALIBRATION2 = 'CameraCalibration2'--><!--Device-DngPropertyKey-CAMERA_CALIBRATION2 = 'CameraCalibration2'-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## REDUCTION_MATRIX1

```TypeScript
REDUCTION_MATRIX1 = 'ReductionMatrix1'
```

第一校准光源下的降维矩阵。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DngPropertyKey-REDUCTION_MATRIX1 = 'ReductionMatrix1'--><!--Device-DngPropertyKey-REDUCTION_MATRIX1 = 'ReductionMatrix1'-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## REDUCTION_MATRIX2

```TypeScript
REDUCTION_MATRIX2 = 'ReductionMatrix2'
```

第二校准光源下的降维矩阵。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DngPropertyKey-REDUCTION_MATRIX2 = 'ReductionMatrix2'--><!--Device-DngPropertyKey-REDUCTION_MATRIX2 = 'ReductionMatrix2'-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## ANALOG_BALANCE

```TypeScript
ANALOG_BALANCE = 'AnalogBalance'
```

模拟增益平衡系数。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DngPropertyKey-ANALOG_BALANCE = 'AnalogBalance'--><!--Device-DngPropertyKey-ANALOG_BALANCE = 'AnalogBalance'-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## AS_SHOT_NEUTRAL

```TypeScript
AS_SHOT_NEUTRAL = 'AsShotNeutral'
```

拍摄时的中性白点。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DngPropertyKey-AS_SHOT_NEUTRAL = 'AsShotNeutral'--><!--Device-DngPropertyKey-AS_SHOT_NEUTRAL = 'AsShotNeutral'-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## AS_SHOT_WHITEXY

```TypeScript
AS_SHOT_WHITEXY = 'AsShotWhiteXY'
```

拍摄时白点的CIE x-y色度坐标。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DngPropertyKey-AS_SHOT_WHITEXY = 'AsShotWhiteXY'--><!--Device-DngPropertyKey-AS_SHOT_WHITEXY = 'AsShotWhiteXY'-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## BASELINE_EXPOSURE

```TypeScript
BASELINE_EXPOSURE = 'BaselineExposure'
```

基准曝光补偿值，单位：EV。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DngPropertyKey-BASELINE_EXPOSURE = 'BaselineExposure'--><!--Device-DngPropertyKey-BASELINE_EXPOSURE = 'BaselineExposure'-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## BASELINE_NOISE

```TypeScript
BASELINE_NOISE = 'BaselineNoise'
```

基准噪声水平。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DngPropertyKey-BASELINE_NOISE = 'BaselineNoise'--><!--Device-DngPropertyKey-BASELINE_NOISE = 'BaselineNoise'-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## BASELINE_SHARPNESS

```TypeScript
BASELINE_SHARPNESS = 'BaselineSharpness'
```

基准锐度增益。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DngPropertyKey-BASELINE_SHARPNESS = 'BaselineSharpness'--><!--Device-DngPropertyKey-BASELINE_SHARPNESS = 'BaselineSharpness'-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## BAYER_GREEN_SPLIT

```TypeScript
BAYER_GREEN_SPLIT = 'BayerGreenSplit'
```

Bayer图像中两个绿色通道的分离程度。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DngPropertyKey-BAYER_GREEN_SPLIT = 'BayerGreenSplit'--><!--Device-DngPropertyKey-BAYER_GREEN_SPLIT = 'BayerGreenSplit'-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## LINEAR_RESPONSE_LIMIT

```TypeScript
LINEAR_RESPONSE_LIMIT = 'LinearResponseLimit'
```

线性响应上限，有效值范围为[0.0, 1.0]。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DngPropertyKey-LINEAR_RESPONSE_LIMIT = 'LinearResponseLimit'--><!--Device-DngPropertyKey-LINEAR_RESPONSE_LIMIT = 'LinearResponseLimit'-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## CAMERA_SERIAL_NUMBER

```TypeScript
CAMERA_SERIAL_NUMBER = 'CameraSerialNumber'
```

相机序列号。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DngPropertyKey-CAMERA_SERIAL_NUMBER = 'CameraSerialNumber'--><!--Device-DngPropertyKey-CAMERA_SERIAL_NUMBER = 'CameraSerialNumber'-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## LENS_INFO

```TypeScript
LENS_INFO = 'LensInfo'
```

镜头信息。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DngPropertyKey-LENS_INFO = 'LensInfo'--><!--Device-DngPropertyKey-LENS_INFO = 'LensInfo'-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## CHROMA_BLUR_RADIUS

```TypeScript
CHROMA_BLUR_RADIUS = 'ChromaBlurRadius'
```

色度模糊半径。单位：像素（px）。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DngPropertyKey-CHROMA_BLUR_RADIUS = 'ChromaBlurRadius'--><!--Device-DngPropertyKey-CHROMA_BLUR_RADIUS = 'ChromaBlurRadius'-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## ANTI_ALIAS_STRENGTH

```TypeScript
ANTI_ALIAS_STRENGTH = 'AntiAliasStrength'
```

抗锯齿滤波器强度。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DngPropertyKey-ANTI_ALIAS_STRENGTH = 'AntiAliasStrength'--><!--Device-DngPropertyKey-ANTI_ALIAS_STRENGTH = 'AntiAliasStrength'-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## SHADOW_SCALE

```TypeScript
SHADOW_SCALE = 'ShadowScale'
```

阴影区域缩放因子。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DngPropertyKey-SHADOW_SCALE = 'ShadowScale'--><!--Device-DngPropertyKey-SHADOW_SCALE = 'ShadowScale'-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## DNG_PRIVATE_DATA

```TypeScript
DNG_PRIVATE_DATA = 'DNGPrivateData'
```

厂商私有数据块。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DngPropertyKey-DNG_PRIVATE_DATA = 'DNGPrivateData'--><!--Device-DngPropertyKey-DNG_PRIVATE_DATA = 'DNGPrivateData'-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## MAKER_NOTE_SAFETY

```TypeScript
MAKER_NOTE_SAFETY = 'MakerNoteSafety'
```

EXIF MakerNote 是否安全可保留。0：不安全，1：安全

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DngPropertyKey-MAKER_NOTE_SAFETY = 'MakerNoteSafety'--><!--Device-DngPropertyKey-MAKER_NOTE_SAFETY = 'MakerNoteSafety'-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## CALIBRATION_ILLUMINANT1

```TypeScript
CALIBRATION_ILLUMINANT1 = 'CalibrationIlluminant1'
```

第一校准光源类型。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DngPropertyKey-CALIBRATION_ILLUMINANT1 = 'CalibrationIlluminant1'--><!--Device-DngPropertyKey-CALIBRATION_ILLUMINANT1 = 'CalibrationIlluminant1'-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## CALIBRATION_ILLUMINANT2

```TypeScript
CALIBRATION_ILLUMINANT2 = 'CalibrationIlluminant2'
```

第二校准光源类型。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DngPropertyKey-CALIBRATION_ILLUMINANT2 = 'CalibrationIlluminant2'--><!--Device-DngPropertyKey-CALIBRATION_ILLUMINANT2 = 'CalibrationIlluminant2'-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## BEST_QUALITY_SCALE

```TypeScript
BEST_QUALITY_SCALE = 'BestQualityScale'
```

最佳画质缩放比例。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DngPropertyKey-BEST_QUALITY_SCALE = 'BestQualityScale'--><!--Device-DngPropertyKey-BEST_QUALITY_SCALE = 'BestQualityScale'-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## RAW_DATA_UNIQUE_ID

```TypeScript
RAW_DATA_UNIQUE_ID = 'RawDataUniqueID'
```

原始图像数据的唯一标识符。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DngPropertyKey-RAW_DATA_UNIQUE_ID = 'RawDataUniqueID'--><!--Device-DngPropertyKey-RAW_DATA_UNIQUE_ID = 'RawDataUniqueID'-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## ORIGINAL_RAW_FILE_NAME

```TypeScript
ORIGINAL_RAW_FILE_NAME = 'OriginalRawFileName'
```

原始RAW文件名。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DngPropertyKey-ORIGINAL_RAW_FILE_NAME = 'OriginalRawFileName'--><!--Device-DngPropertyKey-ORIGINAL_RAW_FILE_NAME = 'OriginalRawFileName'-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## ORIGINAL_RAW_FILE_DATA

```TypeScript
ORIGINAL_RAW_FILE_DATA = 'OriginalRawFileData'
```

原始RAW文件的完整数据。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DngPropertyKey-ORIGINAL_RAW_FILE_DATA = 'OriginalRawFileData'--><!--Device-DngPropertyKey-ORIGINAL_RAW_FILE_DATA = 'OriginalRawFileData'-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## ACTIVE_AREA

```TypeScript
ACTIVE_AREA = 'ActiveArea'
```

有效图像区域。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DngPropertyKey-ACTIVE_AREA = 'ActiveArea'--><!--Device-DngPropertyKey-ACTIVE_AREA = 'ActiveArea'-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## MASKED_AREAS

```TypeScript
MASKED_AREAS = 'MaskedAreas'
```

被遮蔽区域列表。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DngPropertyKey-MASKED_AREAS = 'MaskedAreas'--><!--Device-DngPropertyKey-MASKED_AREAS = 'MaskedAreas'-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## AS_SHOT_ICC_PROFILE

```TypeScript
AS_SHOT_ICC_PROFILE = 'AsShotICCProfile'
```

拍摄时使用的ICC色彩配置文件。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DngPropertyKey-AS_SHOT_ICC_PROFILE = 'AsShotICCProfile'--><!--Device-DngPropertyKey-AS_SHOT_ICC_PROFILE = 'AsShotICCProfile'-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## AS_SHOT_PRE_PROFILE_MATRIX

```TypeScript
AS_SHOT_PRE_PROFILE_MATRIX = 'AsShotPreProfileMatrix'
```

应用ICC配置文件前的预变换矩阵。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DngPropertyKey-AS_SHOT_PRE_PROFILE_MATRIX = 'AsShotPreProfileMatrix'--><!--Device-DngPropertyKey-AS_SHOT_PRE_PROFILE_MATRIX = 'AsShotPreProfileMatrix'-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## CURRENT_ICC_PROFILE

```TypeScript
CURRENT_ICC_PROFILE = 'CurrentICCProfile'
```

当前使用的ICC色彩配置文件。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DngPropertyKey-CURRENT_ICC_PROFILE = 'CurrentICCProfile'--><!--Device-DngPropertyKey-CURRENT_ICC_PROFILE = 'CurrentICCProfile'-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## CURRENT_PRE_PROFILE_MATRIX

```TypeScript
CURRENT_PRE_PROFILE_MATRIX = 'CurrentPreProfileMatrix'
```

当前ICC配置文件前的预变换矩阵。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DngPropertyKey-CURRENT_PRE_PROFILE_MATRIX = 'CurrentPreProfileMatrix'--><!--Device-DngPropertyKey-CURRENT_PRE_PROFILE_MATRIX = 'CurrentPreProfileMatrix'-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## COLORIMETRIC_REFERENCE

```TypeScript
COLORIMETRIC_REFERENCE = 'ColorimetricReference'
```

色度参考标准。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DngPropertyKey-COLORIMETRIC_REFERENCE = 'ColorimetricReference'--><!--Device-DngPropertyKey-COLORIMETRIC_REFERENCE = 'ColorimetricReference'-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## CAMERA_CALIBRATION_SIGNATURE

```TypeScript
CAMERA_CALIBRATION_SIGNATURE = 'CameraCalibrationSignature'
```

相机校准签名。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DngPropertyKey-CAMERA_CALIBRATION_SIGNATURE = 'CameraCalibrationSignature'--><!--Device-DngPropertyKey-CAMERA_CALIBRATION_SIGNATURE = 'CameraCalibrationSignature'-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## PROFILE_CALIBRATION_SIGNATURE

```TypeScript
PROFILE_CALIBRATION_SIGNATURE = 'ProfileCalibrationSignature'
```

配置文件校准签名。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DngPropertyKey-PROFILE_CALIBRATION_SIGNATURE = 'ProfileCalibrationSignature'--><!--Device-DngPropertyKey-PROFILE_CALIBRATION_SIGNATURE = 'ProfileCalibrationSignature'-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## EXTRA_CAMERA_PROFILES

```TypeScript
EXTRA_CAMERA_PROFILES = 'ExtraCameraProfiles'
```

额外相机配置文件索引列表。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DngPropertyKey-EXTRA_CAMERA_PROFILES = 'ExtraCameraProfiles'--><!--Device-DngPropertyKey-EXTRA_CAMERA_PROFILES = 'ExtraCameraProfiles'-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## AS_SHOT_PROFILE_NAME

```TypeScript
AS_SHOT_PROFILE_NAME = 'AsShotProfileName'
```

拍摄时使用的配置文件名称。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DngPropertyKey-AS_SHOT_PROFILE_NAME = 'AsShotProfileName'--><!--Device-DngPropertyKey-AS_SHOT_PROFILE_NAME = 'AsShotProfileName'-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## NOISE_REDUCTION_APPLIED

```TypeScript
NOISE_REDUCTION_APPLIED = 'NoiseReductionApplied'
```

已应用的降噪强度级别。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DngPropertyKey-NOISE_REDUCTION_APPLIED = 'NoiseReductionApplied'--><!--Device-DngPropertyKey-NOISE_REDUCTION_APPLIED = 'NoiseReductionApplied'-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## PROFILE_NAME

```TypeScript
PROFILE_NAME = 'ProfileName'
```

色彩配置文件名称。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DngPropertyKey-PROFILE_NAME = 'ProfileName'--><!--Device-DngPropertyKey-PROFILE_NAME = 'ProfileName'-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## PROFILE_HUE_SAT_MAP_DIMS

```TypeScript
PROFILE_HUE_SAT_MAP_DIMS = 'ProfileHueSatMapDims'
```

色调/饱和度映射表维度。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DngPropertyKey-PROFILE_HUE_SAT_MAP_DIMS = 'ProfileHueSatMapDims'--><!--Device-DngPropertyKey-PROFILE_HUE_SAT_MAP_DIMS = 'ProfileHueSatMapDims'-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## PROFILE_HUE_SAT_MAP_DATA1

```TypeScript
PROFILE_HUE_SAT_MAP_DATA1 = 'ProfileHueSatMapData1'
```

第一组色调/饱和度映射表数据。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DngPropertyKey-PROFILE_HUE_SAT_MAP_DATA1 = 'ProfileHueSatMapData1'--><!--Device-DngPropertyKey-PROFILE_HUE_SAT_MAP_DATA1 = 'ProfileHueSatMapData1'-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## PROFILE_HUE_SAT_MAP_DATA2

```TypeScript
PROFILE_HUE_SAT_MAP_DATA2 = 'ProfileHueSatMapData2'
```

第二组色调/饱和度映射表数据。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DngPropertyKey-PROFILE_HUE_SAT_MAP_DATA2 = 'ProfileHueSatMapData2'--><!--Device-DngPropertyKey-PROFILE_HUE_SAT_MAP_DATA2 = 'ProfileHueSatMapData2'-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## PROFILE_TONE_CURVE

```TypeScript
PROFILE_TONE_CURVE = 'ProfileToneCurve'
```

配置文件色调曲线。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DngPropertyKey-PROFILE_TONE_CURVE = 'ProfileToneCurve'--><!--Device-DngPropertyKey-PROFILE_TONE_CURVE = 'ProfileToneCurve'-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## PROFILE_EMBED_POLICY

```TypeScript
PROFILE_EMBED_POLICY = 'ProfileEmbedPolicy'
```

配置文件嵌入策略。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DngPropertyKey-PROFILE_EMBED_POLICY = 'ProfileEmbedPolicy'--><!--Device-DngPropertyKey-PROFILE_EMBED_POLICY = 'ProfileEmbedPolicy'-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## PROFILE_COPYRIGHT

```TypeScript
PROFILE_COPYRIGHT = 'ProfileCopyright'
```

配置文件版权信息。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DngPropertyKey-PROFILE_COPYRIGHT = 'ProfileCopyright'--><!--Device-DngPropertyKey-PROFILE_COPYRIGHT = 'ProfileCopyright'-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## FORWARD_MATRIX1

```TypeScript
FORWARD_MATRIX1 = 'ForwardMatrix1'
```

第一前向变换矩阵。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DngPropertyKey-FORWARD_MATRIX1 = 'ForwardMatrix1'--><!--Device-DngPropertyKey-FORWARD_MATRIX1 = 'ForwardMatrix1'-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## FORWARD_MATRIX2

```TypeScript
FORWARD_MATRIX2 = 'ForwardMatrix2'
```

第二前向变换矩阵。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DngPropertyKey-FORWARD_MATRIX2 = 'ForwardMatrix2'--><!--Device-DngPropertyKey-FORWARD_MATRIX2 = 'ForwardMatrix2'-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## PREVIEW_APPLICATION_NAME

```TypeScript
PREVIEW_APPLICATION_NAME = 'PreviewApplicationName'
```

预览图生成应用程序名称。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DngPropertyKey-PREVIEW_APPLICATION_NAME = 'PreviewApplicationName'--><!--Device-DngPropertyKey-PREVIEW_APPLICATION_NAME = 'PreviewApplicationName'-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## PREVIEW_APPLICATION_VERSION

```TypeScript
PREVIEW_APPLICATION_VERSION = 'PreviewApplicationVersion'
```

预览图生成应用程序版本。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DngPropertyKey-PREVIEW_APPLICATION_VERSION = 'PreviewApplicationVersion'--><!--Device-DngPropertyKey-PREVIEW_APPLICATION_VERSION = 'PreviewApplicationVersion'-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## PREVIEW_SETTINGS_NAME

```TypeScript
PREVIEW_SETTINGS_NAME = 'PreviewSettingsName'
```

预览图处理设置名称。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DngPropertyKey-PREVIEW_SETTINGS_NAME = 'PreviewSettingsName'--><!--Device-DngPropertyKey-PREVIEW_SETTINGS_NAME = 'PreviewSettingsName'-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## PREVIEW_SETTINGS_DIGEST

```TypeScript
PREVIEW_SETTINGS_DIGEST = 'PreviewSettingsDigest'
```

预览图设置的MD5摘要。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DngPropertyKey-PREVIEW_SETTINGS_DIGEST = 'PreviewSettingsDigest'--><!--Device-DngPropertyKey-PREVIEW_SETTINGS_DIGEST = 'PreviewSettingsDigest'-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## PREVIEW_COLOR_SPACE

```TypeScript
PREVIEW_COLOR_SPACE = 'PreviewColorSpace'
```

预览图色彩空间。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DngPropertyKey-PREVIEW_COLOR_SPACE = 'PreviewColorSpace'--><!--Device-DngPropertyKey-PREVIEW_COLOR_SPACE = 'PreviewColorSpace'-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## PREVIEW_DATE_TIME

```TypeScript
PREVIEW_DATE_TIME = 'PreviewDateTime'
```

预览图生成时间。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DngPropertyKey-PREVIEW_DATE_TIME = 'PreviewDateTime'--><!--Device-DngPropertyKey-PREVIEW_DATE_TIME = 'PreviewDateTime'-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## RAW_IMAGE_DIGEST

```TypeScript
RAW_IMAGE_DIGEST = 'RawImageDigest'
```

原始图像数据的MD5摘要。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DngPropertyKey-RAW_IMAGE_DIGEST = 'RawImageDigest'--><!--Device-DngPropertyKey-RAW_IMAGE_DIGEST = 'RawImageDigest'-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## ORIGINAL_RAW_FILE_DIGEST

```TypeScript
ORIGINAL_RAW_FILE_DIGEST = 'OriginalRawFileDigest'
```

原始RAW文件数据的MD5摘要。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DngPropertyKey-ORIGINAL_RAW_FILE_DIGEST = 'OriginalRawFileDigest'--><!--Device-DngPropertyKey-ORIGINAL_RAW_FILE_DIGEST = 'OriginalRawFileDigest'-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## SUB_TILE_BLOCK_SIZE

```TypeScript
SUB_TILE_BLOCK_SIZE = 'SubTileBlockSize'
```

图像分块存储，定义块的长和宽。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DngPropertyKey-SUB_TILE_BLOCK_SIZE = 'SubTileBlockSize'--><!--Device-DngPropertyKey-SUB_TILE_BLOCK_SIZE = 'SubTileBlockSize'-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## ROW_INTERLEAVE_FACTOR

```TypeScript
ROW_INTERLEAVE_FACTOR = 'RowInterleaveFactor'
```

行交织因子。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DngPropertyKey-ROW_INTERLEAVE_FACTOR = 'RowInterleaveFactor'--><!--Device-DngPropertyKey-ROW_INTERLEAVE_FACTOR = 'RowInterleaveFactor'-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## PROFILE_LOOK_TABLE_DIMS

```TypeScript
PROFILE_LOOK_TABLE_DIMS = 'ProfileLookTableDims'
```

ProfileLookTableData的维度。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DngPropertyKey-PROFILE_LOOK_TABLE_DIMS = 'ProfileLookTableDims'--><!--Device-DngPropertyKey-PROFILE_LOOK_TABLE_DIMS = 'ProfileLookTableDims'-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## PROFILE_LOOK_TABLE_DATA

```TypeScript
PROFILE_LOOK_TABLE_DATA = 'ProfileLookTableData'
```

色彩表数据。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DngPropertyKey-PROFILE_LOOK_TABLE_DATA = 'ProfileLookTableData'--><!--Device-DngPropertyKey-PROFILE_LOOK_TABLE_DATA = 'ProfileLookTableData'-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## OPCODE_LIST1

```TypeScript
OPCODE_LIST1 = 'OpcodeList1'
```

第一操作码列表。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DngPropertyKey-OPCODE_LIST1 = 'OpcodeList1'--><!--Device-DngPropertyKey-OPCODE_LIST1 = 'OpcodeList1'-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## OPCODE_LIST2

```TypeScript
OPCODE_LIST2 = 'OpcodeList2'
```

第二操作码列表。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DngPropertyKey-OPCODE_LIST2 = 'OpcodeList2'--><!--Device-DngPropertyKey-OPCODE_LIST2 = 'OpcodeList2'-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## OPCODE_LIST3

```TypeScript
OPCODE_LIST3 = 'OpcodeList3'
```

第三操作码列表。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DngPropertyKey-OPCODE_LIST3 = 'OpcodeList3'--><!--Device-DngPropertyKey-OPCODE_LIST3 = 'OpcodeList3'-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## NOISE_PROFILE

```TypeScript
NOISE_PROFILE = 'NoiseProfile'
```

噪声剖面参数。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DngPropertyKey-NOISE_PROFILE = 'NoiseProfile'--><!--Device-DngPropertyKey-NOISE_PROFILE = 'NoiseProfile'-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## ORIGINAL_DEFAULT_FINAL_SIZE

```TypeScript
ORIGINAL_DEFAULT_FINAL_SIZE = 'OriginalDefaultFinalSize'
```

原始默认最终输出尺寸（宽, 高）。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DngPropertyKey-ORIGINAL_DEFAULT_FINAL_SIZE = 'OriginalDefaultFinalSize'--><!--Device-DngPropertyKey-ORIGINAL_DEFAULT_FINAL_SIZE = 'OriginalDefaultFinalSize'-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## ORIGINAL_BEST_QUALITY_FINAL_SIZE

```TypeScript
ORIGINAL_BEST_QUALITY_FINAL_SIZE = 'OriginalBestQualityFinalSize'
```

原始最佳画质输出尺寸（宽, 高）。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DngPropertyKey-ORIGINAL_BEST_QUALITY_FINAL_SIZE = 'OriginalBestQualityFinalSize'--><!--Device-DngPropertyKey-ORIGINAL_BEST_QUALITY_FINAL_SIZE = 'OriginalBestQualityFinalSize'-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## ORIGINAL_DEFAULT_CROP_SIZE

```TypeScript
ORIGINAL_DEFAULT_CROP_SIZE = 'OriginalDefaultCropSize'
```

原始默认裁剪尺寸（宽, 高）。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DngPropertyKey-ORIGINAL_DEFAULT_CROP_SIZE = 'OriginalDefaultCropSize'--><!--Device-DngPropertyKey-ORIGINAL_DEFAULT_CROP_SIZE = 'OriginalDefaultCropSize'-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## PROFILE_HUE_SAT_MAP_ENCODING

```TypeScript
PROFILE_HUE_SAT_MAP_ENCODING = 'ProfileHueSatMapEncoding'
```

色调/饱和度映射表编码方式。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DngPropertyKey-PROFILE_HUE_SAT_MAP_ENCODING = 'ProfileHueSatMapEncoding'--><!--Device-DngPropertyKey-PROFILE_HUE_SAT_MAP_ENCODING = 'ProfileHueSatMapEncoding'-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## PROFILE_LOOK_TABLE_ENCODING

```TypeScript
PROFILE_LOOK_TABLE_ENCODING = 'ProfileLookTableEncoding'
```

色彩表编码方式。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DngPropertyKey-PROFILE_LOOK_TABLE_ENCODING = 'ProfileLookTableEncoding'--><!--Device-DngPropertyKey-PROFILE_LOOK_TABLE_ENCODING = 'ProfileLookTableEncoding'-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## BASELINE_EXPOSURE_OFFSET

```TypeScript
BASELINE_EXPOSURE_OFFSET = 'BaselineExposureOffset'
```

基准曝光偏移量，单位：EV。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DngPropertyKey-BASELINE_EXPOSURE_OFFSET = 'BaselineExposureOffset'--><!--Device-DngPropertyKey-BASELINE_EXPOSURE_OFFSET = 'BaselineExposureOffset'-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## DEFAULT_BLACK_RENDER

```TypeScript
DEFAULT_BLACK_RENDER = 'DefaultBlackRender'
```

默认黑场渲染方式。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DngPropertyKey-DEFAULT_BLACK_RENDER = 'DefaultBlackRender'--><!--Device-DngPropertyKey-DEFAULT_BLACK_RENDER = 'DefaultBlackRender'-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## NEW_RAW_IMAGE_DIGEST

```TypeScript
NEW_RAW_IMAGE_DIGEST = 'NewRawImageDigest'
```

修改后原始图像数据的新MD5摘要。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DngPropertyKey-NEW_RAW_IMAGE_DIGEST = 'NewRawImageDigest'--><!--Device-DngPropertyKey-NEW_RAW_IMAGE_DIGEST = 'NewRawImageDigest'-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## RAW_TO_PREVIEW_GAIN

```TypeScript
RAW_TO_PREVIEW_GAIN = 'RawToPreviewGain'
```

主RAW图与预览图之间的增益比。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DngPropertyKey-RAW_TO_PREVIEW_GAIN = 'RawToPreviewGain'--><!--Device-DngPropertyKey-RAW_TO_PREVIEW_GAIN = 'RawToPreviewGain'-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## DEFAULT_USER_CROP

```TypeScript
DEFAULT_USER_CROP = 'DefaultUserCrop'
```

默认用户裁剪区域。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DngPropertyKey-DEFAULT_USER_CROP = 'DefaultUserCrop'--><!--Device-DngPropertyKey-DEFAULT_USER_CROP = 'DefaultUserCrop'-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

