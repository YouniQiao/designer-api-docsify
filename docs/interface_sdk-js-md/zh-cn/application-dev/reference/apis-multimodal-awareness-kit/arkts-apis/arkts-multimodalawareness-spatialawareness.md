# @ohos.multimodalAwareness.spatialAwareness

This module provides the capability to subscribe to report the distance measurement result.

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-declare namespace spatialAwareness--><!--Device-unnamed-declare namespace spatialAwareness-End-->

**系统能力：** SystemCapability.MultimodalAwareness.DistanceMeasurement

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { spatialAwareness } from 'kits/@kit.MultimodalAwarenessKit';
```

## 汇总

<!--Del-->
### 函数（系统接口）

| 名称 | 说明 |
| --- | --- |
| [offDistanceMeasure](arkts-multimodalawareness-spatialawareness-offdistancemeasure-f-sys.md#offdistancemeasure) | Unsubscribe from distance measurement result data. |
| [offIndoorOrOutdoorIdentify](arkts-multimodalawareness-spatialawareness-offindoororoutdooridentify-f-sys.md#offindoororoutdooridentify) | Unsubscribe from the results of indoor and outdoor recognition. |
| [onDistanceMeasure](arkts-multimodalawareness-spatialawareness-ondistancemeasure-f-sys.md#ondistancemeasure) | Subscribe to distance measurement result data. |
| [onIndoorOrOutdoorIdentify](arkts-multimodalawareness-spatialawareness-onindoororoutdooridentify-f-sys.md#onindoororoutdooridentify) | Subscribe to the results of indoorand outdoor identification. |
<!--DelEnd-->

<!--Del-->
### 接口（系统接口）

| 名称 | 说明 |
| --- | --- |
| [DistanceMeasurementConfigParams](arkts-multimodalawareness-spatialawareness-distancemeasurementconfigparams-i-sys.md) | Configuration parameters for the distance measurement interface |
| [DistanceMeasurementResponse](arkts-multimodalawareness-spatialawareness-distancemeasurementresponse-i-sys.md) | Interface for distance measurement result |
| [DoorPositionResponse](arkts-multimodalawareness-spatialawareness-doorpositionresponse-i-sys.md) | Interface for indoor or outdoor identify result |
<!--DelEnd-->

<!--Del-->
### 枚举（系统接口）

| 名称 | 说明 |
| --- | --- |
| [DistanceRank](arkts-multimodalawareness-spatialawareness-distancerank-e-sys.md) | Enum for distance rank. |
| [PositionRelativeToDoor](arkts-multimodalawareness-spatialawareness-positionrelativetodoor-e-sys.md) | Enum for identification result inside and outside the door |
| [ReportingMode](arkts-multimodalawareness-spatialawareness-reportingmode-e-sys.md) | Enum for distance measurement result reporting modes. |
| [TechnologyType](arkts-multimodalawareness-spatialawareness-technologytype-e-sys.md) | Enum for distance measurement technology types. |
<!--DelEnd-->

