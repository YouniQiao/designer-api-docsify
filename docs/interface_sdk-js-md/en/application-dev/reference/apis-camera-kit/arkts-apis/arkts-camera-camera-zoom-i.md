# Zoom

Zoom继承自[ZoomQuery](arkts-camera-camera-zoomquery-i.md)。

变焦类，对设备变焦操作。

**Inheritance/Implementation:** Zoom extends [ZoomQuery](arkts-camera-camera-zoomquery-i.md)

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-camera-interface Zoom extends ZoomQuery--><!--Device-camera-interface Zoom extends ZoomQuery-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## Modules to Import

```TypeScript
import { camera } from 'kits/@kit.CameraKit';
```

## getZoomRatio

ArkTS-Dyn:
```TypeScript
getZoomRatio(): number
```

ArkTS-Sta:
```TypeScript
getZoomRatio(): double
```

获取当前的变焦比。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-Zoom-getZoomRatio(): double--><!--Device-Zoom-getZoomRatio(): double-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：double | 获取当前的变焦比结果。接口调用失败会返回相应错误码，错误码类型[CameraErrorCode]{ |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 7400103 | Session not config. |
| 7400201 | Camera service fatal error.<br>**Applicable version:** 12 and later |

## setSmoothZoom

ArkTS-Dyn:
```TypeScript
setSmoothZoom(targetRatio: number, mode?: SmoothZoomMode): void
```

ArkTS-Sta:
```TypeScript
setSmoothZoom(targetRatio: double, mode?: SmoothZoomMode): void
```

触发平滑变焦。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-Zoom-setSmoothZoom(targetRatio: double, mode?: SmoothZoomMode): void--><!--Device-Zoom-setSmoothZoom(targetRatio: double, mode?: SmoothZoomMode): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| targetRatio | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | 目标值。通过[getZoomRatioRange](arkts-camera-camera-zoomquery-i.md#getzoomratiorange)获取支持的变焦范围，如果设置 超过支持范围的值，则只保留精度范围内数值。 |
| mode | [SmoothZoomMode](arkts-camera-camera-smoothzoommode-e.md) | No | 平滑变焦模式。默认为0。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 7400103 | Session not config.<br>**Applicable version:** 11 - 17 |

## setZoomRatio

ArkTS-Dyn:
```TypeScript
setZoomRatio(zoomRatio: number): void
```

ArkTS-Sta:
```TypeScript
setZoomRatio(zoomRatio: double): void
```

设置变焦比，变焦精度最高为小数点后两位，如果设置超过支持的精度范围，则只保留精度范围内数值。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-Zoom-setZoomRatio(zoomRatio: double): void--><!--Device-Zoom-setZoomRatio(zoomRatio: double): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| zoomRatio | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | 可变焦距比，通过[getZoomRatioRange](arkts-camera-camera-zoomquery-i.md#getzoomratiorange)获取支持的变焦范围，如果设置 超过支持范围的值，则只保留精度范围内数值。 &lt;br&gt;设置可变焦距比到底层生效需要一定时间，获取正确设置的可变焦距比需要等待1~2帧的时间。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 7400103 | Session not config. |

