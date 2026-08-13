# VideoSession

VideoSession继承自[Session](arkts-camera-camera-session-i.md#Session)、[Flash](arkts-camera-camera-flash-i.md#Flash)、 [AutoExposure](arkts-camera-camera-autoexposure-i.md#AutoExposure)、[WhiteBalance](arkts-camera-camera-whitebalance-i.md#WhiteBalance（系统接口）)、[Focus](arkts-camera-camera-focus-i.md#Focus)、 [Zoom](arkts-camera-camera-zoom-i.md#Zoom)、[Stabilization](arkts-camera-camera-stabilization-i.md#Stabilization)、 [ColorManagement](arkts-camera-camera-colormanagement-i.md#ColorManagement)、[AutoDeviceSwitch](arkts-camera-camera-autodeviceswitch-i.md#AutoDeviceSwitch)、 [Macro](arkts-camera-camera-macro-i-sys.md#Macro（系统接口）)、[ControlCenter](arkts-camera-camera-controlcenter-i.md#ControlCenter)、 [ManualExposure](../../../reference/apis-camera-kit/arkts-apis-camera-ManualExposure.md)、 [ManualFocus](../../../reference/apis-camera-kit/arkts-apis-camera-ManualFocus.md)、 [ManualIso](../../../reference/apis-camera-kit/arkts-apis-camera-ManualIso.md)、 [OIS](../../../reference/apis-camera-kit/arkts-apis-camera-OIS.md)、 [Aperture](../../../reference/apis-camera-kit/arkts-apis-camera-Aperture.md)。 普通录像模式会话类，提供了对闪光灯、曝光、白平衡、对焦、变焦、视频防抖、色彩空间、微距及控制器、手动曝光、手动对焦、手动ISO、光学防抖及光圈的操作。 默认的视频录制模式，适用于一般场景。支持720P、1080p等多种分辨率的录制，可选择不同帧率（如30fps、60fps）。

**继承/实现关系：** VideoSession extends [Session](arkts-camera-camera-session-i.md#Session), [Flash](arkts-camera-camera-flash-i.md#Flash), [AutoExposure](arkts-camera-camera-autoexposure-i.md#AutoExposure), [WhiteBalance](arkts-camera-camera-whitebalance-i.md#WhiteBalance（系统接口）), [Focus](arkts-camera-camera-focus-i.md#Focus), [Zoom](arkts-camera-camera-zoom-i.md#Zoom), [Stabilization](arkts-camera-camera-stabilization-i.md#Stabilization), [ColorManagement](arkts-camera-camera-colormanagement-i.md#ColorManagement), [ControlCenter](arkts-camera-camera-controlcenter-i.md#ControlCenter), [AutoDeviceSwitch](arkts-camera-camera-autodeviceswitch-i.md#AutoDeviceSwitch), [Macro](arkts-camera-camera-macro-i-sys.md#Macro（系统接口）), [ManualExposure](arkts-camera-camera-manualexposure-i.md#ManualExposure（系统接口）), [ManualFocus](arkts-camera-camera-manualfocus-i-sys.md#ManualFocus（系统接口）), [ManualIso](arkts-camera-camera-manualiso-i-sys.md#ManualIso（系统接口）), [OIS](arkts-camera-camera-ois-i.md#OIS), [Aperture](arkts-camera-camera-aperture-i-sys.md#Aperture（系统接口）)

**起始版本：** 23

**废弃版本：** -1

<!--Device-camera-interface VideoSession--><!--Device-camera-interface VideoSession-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

## canPreconfig

```TypeScript
canPreconfig(preconfigType: PreconfigType, preconfigRatio?: PreconfigRatio): boolean
```

查询当前Session是否支持指定的预配置类型。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-VideoSession-canPreconfig(preconfigType: PreconfigType, preconfigRatio?: PreconfigRatio): boolean--><!--Device-VideoSession-canPreconfig(preconfigType: PreconfigType, preconfigRatio?: PreconfigRatio): boolean-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| preconfigType | [PreconfigType](arkts-camera-camera-preconfigtype-e.md) | 是 |
| preconfigRatio | [PreconfigRatio](arkts-camera-camera-preconfigratio-e.md) | 否 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [7400201](../errorcode-camera.md#7400201-相机服务异常) |

## offAutoDeviceSwitchStatusChange

```TypeScript
offAutoDeviceSwitchStatusChange(callback?: AsyncCallback<AutoDeviceSwitchStatus>): void
```

Unsubscribes to auto device switch status event callback.

**起始版本：** 23

**废弃版本：** -1

<!--Device-VideoSession-offAutoDeviceSwitchStatusChange(callback?: AsyncCallback<AutoDeviceSwitchStatus>): void--><!--Device-VideoSession-offAutoDeviceSwitchStatusChange(callback?: AsyncCallback<AutoDeviceSwitchStatus>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[AutoDeviceSwitchStatus](arkts-camera-camera-autodeviceswitchstatus-i.md)&gt; | 否 |

## offControlCenterEffectStatusChange

```TypeScript
offControlCenterEffectStatusChange(callback?: AsyncCallback<ControlCenterStatusInfo>): void
```

Unsubscribes to control center effect status change callback.

**起始版本：** 23

**废弃版本：** -1

<!--Device-VideoSession-offControlCenterEffectStatusChange(callback?: AsyncCallback<ControlCenterStatusInfo>): void--><!--Device-VideoSession-offControlCenterEffectStatusChange(callback?: AsyncCallback<ControlCenterStatusInfo>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[ControlCenterStatusInfo](arkts-camera-camera-controlcenterstatusinfo-i.md)&gt; | 否 |

## offError

```TypeScript
offError(callback?: ErrorCallback): void
```

Unsubscribes from error events.

**起始版本：** 23

**废弃版本：** -1

<!--Device-VideoSession-offError(callback?: ErrorCallback): void--><!--Device-VideoSession-offError(callback?: ErrorCallback): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | 否 |

## offExposureInfoChange

```TypeScript
offExposureInfoChange(callback?: Callback<ExposureInfo>): void
```

取消订阅曝光信息变化事件回调。如果订阅了曝光信息，请在释放相机前取消订阅。使用callback异步回调。

**起始版本：** 26.0.0

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-VideoSession-offExposureInfoChange(callback?: Callback<ExposureInfo>): void--><!--Device-VideoSession-offExposureInfoChange(callback?: Callback<ExposureInfo>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[ExposureInfo](arkts-camera-camera-exposureinfo-i-sys.md)&gt; | 否 |

## offFocusStateChange

```TypeScript
offFocusStateChange(callback?: AsyncCallback<FocusState>): void
```

Unsubscribes from focus state change event callback.

**起始版本：** 23

**废弃版本：** -1

<!--Device-VideoSession-offFocusStateChange(callback?: AsyncCallback<FocusState>): void--><!--Device-VideoSession-offFocusStateChange(callback?: AsyncCallback<FocusState>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[FocusState](arkts-camera-camera-focusstate-e.md)&gt; | 否 |

## offIsoInfoChange

```TypeScript
offIsoInfoChange(callback?: Callback<IsoInfo>): void
```

取消监听相机感光度（ISO）状态的变化。

**起始版本：** 23

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-VideoSession-offIsoInfoChange(callback?: Callback<IsoInfo>): void--><!--Device-VideoSession-offIsoInfoChange(callback?: Callback<IsoInfo>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[IsoInfo](arkts-camera-camera-isoinfo-i-sys.md)&gt; | 否 |

## offMacroStatusChanged

```TypeScript
offMacroStatusChanged(callback?: AsyncCallback<boolean>): void
```

Unsubscribes camera macro status event callback.

**起始版本：** 23

**废弃版本：** -1

<!--Device-VideoSession-offMacroStatusChanged(callback?: AsyncCallback<boolean>): void--><!--Device-VideoSession-offMacroStatusChanged(callback?: AsyncCallback<boolean>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 否 |

## offSmoothZoomInfoAvailable

```TypeScript
offSmoothZoomInfoAvailable(callback?: AsyncCallback<SmoothZoomInfo>): void
```

Unsubscribes from zoom info event callback.

**起始版本：** 23

**废弃版本：** -1

<!--Device-VideoSession-offSmoothZoomInfoAvailable(callback?: AsyncCallback<SmoothZoomInfo>): void--><!--Device-VideoSession-offSmoothZoomInfoAvailable(callback?: AsyncCallback<SmoothZoomInfo>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[SmoothZoomInfo](arkts-camera-camera-smoothzoominfo-i.md)&gt; | 否 |

## offSystemPressureLevelChange

```TypeScript
offSystemPressureLevelChange(callback?: AsyncCallback<SystemPressureLevel>): void
```

Unsubscribes to system pressure level event callback.

**起始版本：** 23

**废弃版本：** -1

<!--Device-VideoSession-offSystemPressureLevelChange(callback?: AsyncCallback<SystemPressureLevel>): void--><!--Device-VideoSession-offSystemPressureLevelChange(callback?: AsyncCallback<SystemPressureLevel>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[SystemPressureLevel](arkts-camera-camera-systempressurelevel-e.md)&gt; | 否 |

## off_autoDeviceSwitchStatusChange

```TypeScript
off(type: 'autoDeviceSwitchStatusChange', callback?: AsyncCallback<AutoDeviceSwitchStatus>): void
```

注销监听相机自动切换镜头状态变化。

**起始版本：** 13

**废弃版本：** -1

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-VideoSession-off(type: 'autoDeviceSwitchStatusChange', callback?: AsyncCallback<AutoDeviceSwitchStatus>): void--><!--Device-VideoSession-off(type: 'autoDeviceSwitchStatusChange', callback?: AsyncCallback<AutoDeviceSwitchStatus>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'autoDeviceSwitchStatusChange' | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[AutoDeviceSwitchStatus](arkts-camera-camera-autodeviceswitchstatus-i.md)&gt; | 否 |

## off_controlCenterEffectStatusChange

```TypeScript
off(type: 'controlCenterEffectStatusChange', callback?: AsyncCallback<ControlCenterStatusInfo>): void
```

注销监听相机控制器激活状态变化。

**起始版本：** 20

**废弃版本：** -1

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-VideoSession-off(type: 'controlCenterEffectStatusChange', callback?: AsyncCallback<ControlCenterStatusInfo>): void--><!--Device-VideoSession-off(type: 'controlCenterEffectStatusChange', callback?: AsyncCallback<ControlCenterStatusInfo>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'controlCenterEffectStatusChange' | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[ControlCenterStatusInfo](arkts-camera-camera-controlcenterstatusinfo-i.md)&gt; | 否 |

## off_error

```TypeScript
off(type: 'error', callback?: ErrorCallback): void
```

注销监听普通录像会话的错误事件，通过注册回调函数获取结果。

**起始版本：** 11

**废弃版本：** -1

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-VideoSession-off(type: 'error', callback?: ErrorCallback): void--><!--Device-VideoSession-off(type: 'error', callback?: ErrorCallback): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'error' | 是 |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | 否 |

## off_focusStateChange

```TypeScript
off(type: 'focusStateChange', callback?: AsyncCallback<FocusState>): void
```

注销监听相机聚焦的状态变化。

**起始版本：** 11

**废弃版本：** -1

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-VideoSession-off(type: 'focusStateChange', callback?: AsyncCallback<FocusState>): void--><!--Device-VideoSession-off(type: 'focusStateChange', callback?: AsyncCallback<FocusState>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'focusStateChange' | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[FocusState](arkts-camera-camera-focusstate-e.md)&gt; | 否 |

## off_smoothZoomInfoAvailable

```TypeScript
off(type: 'smoothZoomInfoAvailable', callback?: AsyncCallback<SmoothZoomInfo>): void
```

注销监听相机平滑变焦的状态变化。

**起始版本：** 11

**废弃版本：** -1

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-VideoSession-off(type: 'smoothZoomInfoAvailable', callback?: AsyncCallback<SmoothZoomInfo>): void--><!--Device-VideoSession-off(type: 'smoothZoomInfoAvailable', callback?: AsyncCallback<SmoothZoomInfo>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'smoothZoomInfoAvailable' | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[SmoothZoomInfo](arkts-camera-camera-smoothzoominfo-i.md)&gt; | 否 |

## off_systemPressureLevelChange

```TypeScript
off(type: 'systemPressureLevelChange', callback?: AsyncCallback<SystemPressureLevel>): void
```

注销监听系统压力状态变化。

**起始版本：** 20

**废弃版本：** -1

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-VideoSession-off(type: 'systemPressureLevelChange', callback?: AsyncCallback<SystemPressureLevel>): void--><!--Device-VideoSession-off(type: 'systemPressureLevelChange', callback?: AsyncCallback<SystemPressureLevel>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'systemPressureLevelChange' | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[SystemPressureLevel](arkts-camera-camera-systempressurelevel-e.md)&gt; | 否 |

## onAutoDeviceSwitchStatusChange

```TypeScript
onAutoDeviceSwitchStatusChange(callback: AsyncCallback<AutoDeviceSwitchStatus>): void
```

Subscribes to auto device switch status event callback.

**起始版本：** 23

**废弃版本：** -1

<!--Device-VideoSession-onAutoDeviceSwitchStatusChange(callback: AsyncCallback<AutoDeviceSwitchStatus>): void--><!--Device-VideoSession-onAutoDeviceSwitchStatusChange(callback: AsyncCallback<AutoDeviceSwitchStatus>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[AutoDeviceSwitchStatus](arkts-camera-camera-autodeviceswitchstatus-i.md)&gt; | 是 |

## onControlCenterEffectStatusChange

```TypeScript
onControlCenterEffectStatusChange(callback: AsyncCallback<ControlCenterStatusInfo>): void
```

Subscribes to control center effect status change callback.

**起始版本：** 23

**废弃版本：** -1

<!--Device-VideoSession-onControlCenterEffectStatusChange(callback: AsyncCallback<ControlCenterStatusInfo>): void--><!--Device-VideoSession-onControlCenterEffectStatusChange(callback: AsyncCallback<ControlCenterStatusInfo>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[ControlCenterStatusInfo](arkts-camera-camera-controlcenterstatusinfo-i.md)&gt; | 是 |

## onError

```TypeScript
onError(callback: ErrorCallback): void
```

Subscribes to error events.

**起始版本：** 23

**废弃版本：** -1

<!--Device-VideoSession-onError(callback: ErrorCallback): void--><!--Device-VideoSession-onError(callback: ErrorCallback): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | 是 |

## onExposureInfoChange

```TypeScript
onExposureInfoChange(callback: Callback<ExposureInfo>): void
```

订阅曝光信息变化事件回调。曝光参数更改后，系统将返回更新后的曝光信息。使用callback异步回调。

**起始版本：** 26.0.0

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-VideoSession-onExposureInfoChange(callback: Callback<ExposureInfo>): void--><!--Device-VideoSession-onExposureInfoChange(callback: Callback<ExposureInfo>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[ExposureInfo](arkts-camera-camera-exposureinfo-i-sys.md)&gt; | 是 |

## onFocusStateChange

```TypeScript
onFocusStateChange(callback: AsyncCallback<FocusState>): void
```

Subscribes focus state change event callback.

**起始版本：** 23

**废弃版本：** -1

<!--Device-VideoSession-onFocusStateChange(callback: AsyncCallback<FocusState>): void--><!--Device-VideoSession-onFocusStateChange(callback: AsyncCallback<FocusState>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[FocusState](arkts-camera-camera-focusstate-e.md)&gt; | 是 |

## onIsoInfoChange

```TypeScript
onIsoInfoChange(callback: Callback<IsoInfo>): void
```

监听相机感光度（ISO）状态变化，通过注册回调函数获取最新ISO值。

**起始版本：** 23

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-VideoSession-onIsoInfoChange(callback: Callback<IsoInfo>): void--><!--Device-VideoSession-onIsoInfoChange(callback: Callback<IsoInfo>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[IsoInfo](arkts-camera-camera-isoinfo-i-sys.md)&gt; | 是 |

## onMacroStatusChanged

```TypeScript
onMacroStatusChanged(callback: AsyncCallback<boolean>): void
```

Subscribes camera macro status event callback.

**起始版本：** 23

**废弃版本：** -1

<!--Device-VideoSession-onMacroStatusChanged(callback: AsyncCallback<boolean>): void--><!--Device-VideoSession-onMacroStatusChanged(callback: AsyncCallback<boolean>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |

## onSmoothZoomInfoAvailable

```TypeScript
onSmoothZoomInfoAvailable(callback: AsyncCallback<SmoothZoomInfo>): void
```

Subscribes zoom info event callback.

**起始版本：** 23

**废弃版本：** -1

<!--Device-VideoSession-onSmoothZoomInfoAvailable(callback: AsyncCallback<SmoothZoomInfo>): void--><!--Device-VideoSession-onSmoothZoomInfoAvailable(callback: AsyncCallback<SmoothZoomInfo>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[SmoothZoomInfo](arkts-camera-camera-smoothzoominfo-i.md)&gt; | 是 |

## onSystemPressureLevelChange

```TypeScript
onSystemPressureLevelChange(callback: AsyncCallback<SystemPressureLevel>): void
```

Subscribes to system pressure level event callback.

**起始版本：** 23

**废弃版本：** -1

<!--Device-VideoSession-onSystemPressureLevelChange(callback: AsyncCallback<SystemPressureLevel>): void--><!--Device-VideoSession-onSystemPressureLevelChange(callback: AsyncCallback<SystemPressureLevel>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[SystemPressureLevel](arkts-camera-camera-systempressurelevel-e.md)&gt; | 是 |

## on_autoDeviceSwitchStatusChange

```TypeScript
on(type: 'autoDeviceSwitchStatusChange', callback: AsyncCallback<AutoDeviceSwitchStatus>): void
```

监听相机自动切换镜头状态变化，通过注册回调函数获取结果。使用callback异步回调。 > **说明：** > > 当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。

**起始版本：** 13

**废弃版本：** -1

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-VideoSession-on(type: 'autoDeviceSwitchStatusChange', callback: AsyncCallback<AutoDeviceSwitchStatus>): void--><!--Device-VideoSession-on(type: 'autoDeviceSwitchStatusChange', callback: AsyncCallback<AutoDeviceSwitchStatus>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'autoDeviceSwitchStatusChange' | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[AutoDeviceSwitchStatus](arkts-camera-camera-autodeviceswitchstatus-i.md)&gt; | 是 |

## on_controlCenterEffectStatusChange

```TypeScript
on(type: 'controlCenterEffectStatusChange', callback: AsyncCallback<ControlCenterStatusInfo>): void
```

监听相机控制器效果激活状态变化，通过注册回调函数获取结果。使用callback异步回调。 > **说明：** > > 当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。

**起始版本：** 20

**废弃版本：** -1

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-VideoSession-on(type: 'controlCenterEffectStatusChange', callback: AsyncCallback<ControlCenterStatusInfo>): void--><!--Device-VideoSession-on(type: 'controlCenterEffectStatusChange', callback: AsyncCallback<ControlCenterStatusInfo>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'controlCenterEffectStatusChange' | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[ControlCenterStatusInfo](arkts-camera-camera-controlcenterstatusinfo-i.md)&gt; | 是 |

## on_error

```TypeScript
on(type: 'error', callback: ErrorCallback): void
```

监听普通录像会话的错误事件，通过注册回调函数获取结果。使用callback异步回调。 > **说明：** > > 当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。

**起始版本：** 11

**废弃版本：** -1

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-VideoSession-on(type: 'error', callback: ErrorCallback): void--><!--Device-VideoSession-on(type: 'error', callback: ErrorCallback): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'error' | 是 |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | 是 |

## on_focusStateChange

```TypeScript
on(type: 'focusStateChange', callback: AsyncCallback<FocusState>): void
```

监听相机聚焦的状态变化，通过注册回调函数获取结果。使用callback异步回调。 > **说明：** > > 当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。

**起始版本：** 11

**废弃版本：** -1

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-VideoSession-on(type: 'focusStateChange', callback: AsyncCallback<FocusState>): void--><!--Device-VideoSession-on(type: 'focusStateChange', callback: AsyncCallback<FocusState>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'focusStateChange' | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[FocusState](arkts-camera-camera-focusstate-e.md)&gt; | 是 |

## on_smoothZoomInfoAvailable

```TypeScript
on(type: 'smoothZoomInfoAvailable', callback: AsyncCallback<SmoothZoomInfo>): void
```

监听相机平滑变焦的状态变化，通过注册回调函数获取结果。使用callback异步回调。 > **说明：** > > 当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。

**起始版本：** 11

**废弃版本：** -1

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-VideoSession-on(type: 'smoothZoomInfoAvailable', callback: AsyncCallback<SmoothZoomInfo>): void--><!--Device-VideoSession-on(type: 'smoothZoomInfoAvailable', callback: AsyncCallback<SmoothZoomInfo>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'smoothZoomInfoAvailable' | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[SmoothZoomInfo](arkts-camera-camera-smoothzoominfo-i.md)&gt; | 是 |

## on_systemPressureLevelChange

```TypeScript
on(type: 'systemPressureLevelChange', callback: AsyncCallback<SystemPressureLevel>): void
```

监听系统压力状态变化，通过注册回调函数获取结果。使用callback异步回调。 > **说明：** > > 当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。

**起始版本：** 20

**废弃版本：** -1

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-VideoSession-on(type: 'systemPressureLevelChange', callback: AsyncCallback<SystemPressureLevel>): void--><!--Device-VideoSession-on(type: 'systemPressureLevelChange', callback: AsyncCallback<SystemPressureLevel>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'systemPressureLevelChange' | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[SystemPressureLevel](arkts-camera-camera-systempressurelevel-e.md)&gt; | 是 |

## preconfig

```TypeScript
preconfig(preconfigType: PreconfigType, preconfigRatio?: PreconfigRatio): void
```

对当前Session进行预配置。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-VideoSession-preconfig(preconfigType: PreconfigType, preconfigRatio?: PreconfigRatio): void--><!--Device-VideoSession-preconfig(preconfigType: PreconfigType, preconfigRatio?: PreconfigRatio): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| preconfigType | [PreconfigType](arkts-camera-camera-preconfigtype-e.md) | 是 |
| preconfigRatio | [PreconfigRatio](arkts-camera-camera-preconfigratio-e.md) | 否 |

**错误码：**

| 错误码ID |
| --- |
| [7400201](../errorcode-camera.md#7400201-相机服务异常) |

## setQualityPrioritization

```TypeScript
setQualityPrioritization(quality: QualityPrioritization): void
```

设置录像质量优先级。 > **说明：** > > - 默认为高录像质量，设置为功耗平衡将降低录像质量以减少功耗。实际功耗收益因平台而异。 > > - 建议该接口在[commitConfig](arkts-camera-camera-session-i.md#commitConfig)和 > [start](arkts-camera-camera-session-i.md#start)之间调用。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-VideoSession-setQualityPrioritization(quality: QualityPrioritization): void--><!--Device-VideoSession-setQualityPrioritization(quality: QualityPrioritization): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| quality | [QualityPrioritization](arkts-camera-camera-qualityprioritization-e.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [7400103](../errorcode-camera.md#7400103-会话未配置) |
