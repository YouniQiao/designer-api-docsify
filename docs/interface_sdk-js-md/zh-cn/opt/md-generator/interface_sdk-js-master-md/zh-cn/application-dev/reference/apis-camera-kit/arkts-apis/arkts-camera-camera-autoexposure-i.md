# AutoExposure

AutoExposure继承自[AutoExposureQuery](arkts-camera-camera-autoexposurequery-i.md)。

自动曝光类，对设备自动曝光（AE）操作。

**继承/实现关系：** AutoExposure extends [AutoExposureQuery](arkts-camera-camera-autoexposurequery-i.md)

**起始版本：** 11

<!--Device-camera-interface AutoExposure extends AutoExposureQuery--><!--Device-camera-interface AutoExposure extends AutoExposureQuery-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

## getExposureMeteringMode

```TypeScript
getExposureMeteringMode(): ExposureMeteringMode
```

获取当前曝光测光模式。

**起始版本：** 24

**原子化服务API：** 从API版本24开始，该接口支持在原子化服务API中使用。

<!--Device-AutoExposure-getExposureMeteringMode(): ExposureMeteringMode--><!--Device-AutoExposure-getExposureMeteringMode(): ExposureMeteringMode-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 |
| --- |
| [ExposureMeteringMode](arkts-camera-camera-exposuremeteringmode-e.md) |

**错误码：**

| 错误码ID |
| --- |
| [7400102](../errorcode-camera.md#7400102-非法操作) |
| [7400103](../errorcode-camera.md#7400103-会话未配置) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## getExposureMode

```TypeScript
getExposureMode(): ExposureMode
```

获取当前曝光模式。

> **说明：**
> 
> 若未通过[setExposureMode](arkts-camera-camera-autoexposure-i.md#setexposuremode)接口进行设置，直接调用该接口查询当前曝光模式，会返回无效值。

**起始版本：** 11

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-AutoExposure-getExposureMode(): ExposureMode--><!--Device-AutoExposure-getExposureMode(): ExposureMode-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 |
| --- |
| [ExposureMode](arkts-camera-camera-exposuremode-e.md) |

**错误码：**

| 错误码ID |
| --- |
| [7400103](../errorcode-camera.md#7400103-会话未配置) |

## getExposureValue

```TypeScript
getExposureValue(): number
```

查询当前曝光值。

**起始版本：** 11

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-AutoExposure-getExposureValue(): double--><!--Device-AutoExposure-getExposureValue(): double-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [7400103](../errorcode-camera.md#7400103-会话未配置) |

## getMeteringPoint

```TypeScript
getMeteringPoint(): Point
```

查询曝光区域中心点。

**起始版本：** 11

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-AutoExposure-getMeteringPoint(): Point--><!--Device-AutoExposure-getMeteringPoint(): Point-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 |
| --- |
| [Point](../../apis-test-kit/arkts-apis/arkts-test-uitest-point-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [7400103](../errorcode-camera.md#7400103-会话未配置) |

## offExposureStateChange

```TypeScript
offExposureStateChange(callback?: Callback<ExposureState>): void
```

注销监听曝光状态事件变更。使用callback异步回调。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-AutoExposure-offExposureStateChange(callback?: Callback<ExposureState>): void--><!--Device-AutoExposure-offExposureStateChange(callback?: Callback<ExposureState>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;ExposureState&gt; | 否 |

## onExposureStateChange

```TypeScript
onExposureStateChange(callback: Callback<ExposureState>): void
```

监听曝光状态事件变更。使用callback异步回调。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-AutoExposure-onExposureStateChange(callback: Callback<ExposureState>): void--><!--Device-AutoExposure-onExposureStateChange(callback: Callback<ExposureState>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;ExposureState&gt; | 是 |

## setExposureBias

```TypeScript
setExposureBias(exposureBias: number): void
```

设置曝光补偿，曝光补偿值（EV）。

进行设置之前，建议先通过方法[getExposureBiasRange](arkts-camera-camera-autoexposurequery-i.md#getexposurebiasrange)查询支持的范围。

**起始版本：** 11

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-AutoExposure-setExposureBias(exposureBias: double): void--><!--Device-AutoExposure-setExposureBias(exposureBias: double): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| exposureBias | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [7400102](../errorcode-camera.md#7400102-非法操作) |
| [7400103](../errorcode-camera.md#7400103-会话未配置) |

## setExposureMeteringMode

```TypeScript
setExposureMeteringMode(aeMeteringMode: ExposureMeteringMode): void
```

设置曝光测光模式。

**起始版本：** 24

**原子化服务API：** 从API版本24开始，该接口支持在原子化服务API中使用。

<!--Device-AutoExposure-setExposureMeteringMode(aeMeteringMode: ExposureMeteringMode): void--><!--Device-AutoExposure-setExposureMeteringMode(aeMeteringMode: ExposureMeteringMode): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| aeMeteringMode | [ExposureMeteringMode](arkts-camera-camera-exposuremeteringmode-e.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [7400101](../errorcode-camera.md#7400101-无效入参) |
| [7400102](../errorcode-camera.md#7400102-非法操作) |
| [7400103](../errorcode-camera.md#7400103-会话未配置) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## setExposureMode

```TypeScript
setExposureMode(aeMode: ExposureMode): void
```

设置曝光模式。进行设置之前，需要先检查设备是否支持指定的曝光模式，可使用方法  
[isExposureModeSupported](arkts-camera-camera-autoexposurequery-i.md#isexposuremodesupported)。

**起始版本：** 11

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-AutoExposure-setExposureMode(aeMode: ExposureMode): void--><!--Device-AutoExposure-setExposureMode(aeMode: ExposureMode): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| aeMode | [ExposureMode](arkts-camera-camera-exposuremode-e.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [7400102](../errorcode-camera.md#7400102-非法操作) |
| [7400103](../errorcode-camera.md#7400103-会话未配置) |

## setMeteringPoint

```TypeScript
setMeteringPoint(point: Point): void
```

设置曝光区域中心点，曝光点应在0-1坐标系内，该坐标系左上角为{0，0}，右下角为{1，1}。

此坐标系是以设备充电口在右侧时的横向设备方向为基准的，例如应用的预览界面布局以设备充电口在下侧时的竖向方向为基准，布局宽高为{w，h}，且触摸点为{x，y}，则转换后的坐标点为{y/h，1-x/w}。

**起始版本：** 11

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-AutoExposure-setMeteringPoint(point: Point): void--><!--Device-AutoExposure-setMeteringPoint(point: Point): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| point | [Point](../../apis-test-kit/arkts-apis/arkts-test-uitest-point-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [7400103](../errorcode-camera.md#7400103-会话未配置) |
