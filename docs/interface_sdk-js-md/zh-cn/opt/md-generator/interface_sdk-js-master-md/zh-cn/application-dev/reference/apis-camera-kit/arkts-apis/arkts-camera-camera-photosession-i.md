# PhotoSession

PhotoSession继承自[Session](arkts-camera-camera-session-i.md#Session)、[Flash](arkts-camera-camera-flash-i.md#Flash)、 [AutoExposure](arkts-camera-camera-autoexposure-i.md#AutoExposure)、[WhiteBalance](arkts-camera-camera-whitebalance-i.md#WhiteBalance（系统接口）)、[Focus](arkts-camera-camera-focus-i.md#Focus)、 [Zoom](arkts-camera-camera-zoom-i.md#Zoom)、[ColorManagement](arkts-camera-camera-colormanagement-i.md#ColorManagement)、 [AutoDeviceSwitch](arkts-camera-camera-autodeviceswitch-i.md#AutoDeviceSwitch)、[Macro](arkts-camera-camera-macro-i-sys.md#Macro（系统接口）)、 [ManualExposure](../../../reference/apis-camera-kit/arkts-apis-camera-ManualExposure.md)、 [ManualFocus](../../../reference/apis-camera-kit/arkts-apis-camera-ManualFocus.md)、 [ManualIso](../../../reference/apis-camera-kit/arkts-apis-camera-ManualIso.md)、 [OIS](../../../reference/apis-camera-kit/arkts-apis-camera-OIS.md)、 [Aperture](../../../reference/apis-camera-kit/arkts-apis-camera-Aperture.md)。 普通拍照模式会话类，提供了对闪光灯、曝光、白平衡、对焦、变焦、色彩空间、微距、手动曝光、手动对焦、手动ISO、光学防抖及光圈的操作。 默认的拍照模式，用于拍摄标准照片。支持多种照片格式和分辨率，适合大多数日常拍摄场景。

**继承/实现关系：** PhotoSession extends [Session](arkts-camera-camera-session-i.md#Session), [Flash](arkts-camera-camera-flash-i.md#Flash), [AutoExposure](arkts-camera-camera-autoexposure-i.md#AutoExposure), [WhiteBalance](arkts-camera-camera-whitebalance-i.md#WhiteBalance（系统接口）), [Focus](arkts-camera-camera-focus-i.md#Focus), [Zoom](arkts-camera-camera-zoom-i.md#Zoom), [ColorManagement](arkts-camera-camera-colormanagement-i.md#ColorManagement), [AutoDeviceSwitch](arkts-camera-camera-autodeviceswitch-i.md#AutoDeviceSwitch), [Macro](arkts-camera-camera-macro-i-sys.md#Macro（系统接口）), [ManualExposure](arkts-camera-camera-manualexposure-i.md#ManualExposure（系统接口）), [ManualFocus](arkts-camera-camera-manualfocus-i-sys.md#ManualFocus（系统接口）), [ManualIso](arkts-camera-camera-manualiso-i-sys.md#ManualIso（系统接口）), [OIS](arkts-camera-camera-ois-i.md#OIS), [Aperture](arkts-camera-camera-aperture-i-sys.md#Aperture（系统接口）)

**起始版本：** 23

**废弃版本：** -1

<!--Device-camera-interface PhotoSession--><!--Device-camera-interface PhotoSession-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

## canPreconfig

```TypeScript
canPreconfig(preconfigType: PreconfigType, preconfigRatio?: PreconfigRatio): boolean
```

查询当前Session是否支持指定的预配置类型。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-PhotoSession-canPreconfig(preconfigType: PreconfigType, preconfigRatio?: PreconfigRatio): boolean--><!--Device-PhotoSession-canPreconfig(preconfigType: PreconfigType, preconfigRatio?: PreconfigRatio): boolean-End-->

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

<!--Device-PhotoSession-offAutoDeviceSwitchStatusChange(callback?: AsyncCallback<AutoDeviceSwitchStatus>): void--><!--Device-PhotoSession-offAutoDeviceSwitchStatusChange(callback?: AsyncCallback<AutoDeviceSwitchStatus>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[AutoDeviceSwitchStatus](arkts-camera-camera-autodeviceswitchstatus-i.md)&gt; | 否 |

## offError

```TypeScript
offError(callback?: ErrorCallback): void
```

Unsubscribes from error events.

**起始版本：** 23

**废弃版本：** -1

<!--Device-PhotoSession-offError(callback?: ErrorCallback): void--><!--Device-PhotoSession-offError(callback?: ErrorCallback): void-End-->

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

**起始版本：** 24

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本24开始，该接口支持在原子化服务API中使用。

<!--Device-PhotoSession-offExposureInfoChange(callback?: Callback<ExposureInfo>): void--><!--Device-PhotoSession-offExposureInfoChange(callback?: Callback<ExposureInfo>): void-End-->

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

<!--Device-PhotoSession-offFocusStateChange(callback?: AsyncCallback<FocusState>): void--><!--Device-PhotoSession-offFocusStateChange(callback?: AsyncCallback<FocusState>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[FocusState](arkts-camera-camera-focusstate-e.md)&gt; | 否 |

## offIsoInfoChange

```TypeScript
offIsoInfoChange(callback?: Callback<IsoInfo>): void
```

取消订阅ISO信息变化事件回调。

**起始版本：** 24

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本24开始，该接口支持在原子化服务API中使用。

<!--Device-PhotoSession-offIsoInfoChange(callback?: Callback<IsoInfo>): void--><!--Device-PhotoSession-offIsoInfoChange(callback?: Callback<IsoInfo>): void-End-->

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

<!--Device-PhotoSession-offMacroStatusChanged(callback?: AsyncCallback<boolean>): void--><!--Device-PhotoSession-offMacroStatusChanged(callback?: AsyncCallback<boolean>): void-End-->

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

<!--Device-PhotoSession-offSmoothZoomInfoAvailable(callback?: AsyncCallback<SmoothZoomInfo>): void--><!--Device-PhotoSession-offSmoothZoomInfoAvailable(callback?: AsyncCallback<SmoothZoomInfo>): void-End-->

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

<!--Device-PhotoSession-offSystemPressureLevelChange(callback?: AsyncCallback<SystemPressureLevel>): void--><!--Device-PhotoSession-offSystemPressureLevelChange(callback?: AsyncCallback<SystemPressureLevel>): void-End-->

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

<!--Device-PhotoSession-off(type: 'autoDeviceSwitchStatusChange', callback?: AsyncCallback<AutoDeviceSwitchStatus>): void--><!--Device-PhotoSession-off(type: 'autoDeviceSwitchStatusChange', callback?: AsyncCallback<AutoDeviceSwitchStatus>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'autoDeviceSwitchStatusChange' | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[AutoDeviceSwitchStatus](arkts-camera-camera-autodeviceswitchstatus-i.md)&gt; | 否 |

## off_error

```TypeScript
off(type: 'error', callback?: ErrorCallback): void
```

注销监听普通拍照会话的错误事件，通过注册回调函数获取结果。

**起始版本：** 11

**废弃版本：** -1

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-PhotoSession-off(type: 'error', callback?: ErrorCallback): void--><!--Device-PhotoSession-off(type: 'error', callback?: ErrorCallback): void-End-->

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

<!--Device-PhotoSession-off(type: 'focusStateChange', callback?: AsyncCallback<FocusState>): void--><!--Device-PhotoSession-off(type: 'focusStateChange', callback?: AsyncCallback<FocusState>): void-End-->

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

<!--Device-PhotoSession-off(type: 'smoothZoomInfoAvailable', callback?: AsyncCallback<SmoothZoomInfo>): void--><!--Device-PhotoSession-off(type: 'smoothZoomInfoAvailable', callback?: AsyncCallback<SmoothZoomInfo>): void-End-->

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

<!--Device-PhotoSession-off(type: 'systemPressureLevelChange', callback?: AsyncCallback<SystemPressureLevel>): void--><!--Device-PhotoSession-off(type: 'systemPressureLevelChange', callback?: AsyncCallback<SystemPressureLevel>): void-End-->

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

<!--Device-PhotoSession-onAutoDeviceSwitchStatusChange(callback: AsyncCallback<AutoDeviceSwitchStatus>): void--><!--Device-PhotoSession-onAutoDeviceSwitchStatusChange(callback: AsyncCallback<AutoDeviceSwitchStatus>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[AutoDeviceSwitchStatus](arkts-camera-camera-autodeviceswitchstatus-i.md)&gt; | 是 |

## onError

```TypeScript
onError(callback: ErrorCallback): void
```

Subscribes to error events.

**起始版本：** 23

**废弃版本：** -1

<!--Device-PhotoSession-onError(callback: ErrorCallback): void--><!--Device-PhotoSession-onError(callback: ErrorCallback): void-End-->

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

**起始版本：** 24

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本24开始，该接口支持在原子化服务API中使用。

<!--Device-PhotoSession-onExposureInfoChange(callback: Callback<ExposureInfo>): void--><!--Device-PhotoSession-onExposureInfoChange(callback: Callback<ExposureInfo>): void-End-->

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

<!--Device-PhotoSession-onFocusStateChange(callback: AsyncCallback<FocusState>): void--><!--Device-PhotoSession-onFocusStateChange(callback: AsyncCallback<FocusState>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[FocusState](arkts-camera-camera-focusstate-e.md)&gt; | 是 |

## onIsoInfoChange

```TypeScript
onIsoInfoChange(callback: Callback<IsoInfo>): void
```

订阅ISO信息变化事件回调。

**起始版本：** 24

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本24开始，该接口支持在原子化服务API中使用。

<!--Device-PhotoSession-onIsoInfoChange(callback: Callback<IsoInfo>): void--><!--Device-PhotoSession-onIsoInfoChange(callback: Callback<IsoInfo>): void-End-->

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

<!--Device-PhotoSession-onMacroStatusChanged(callback: AsyncCallback<boolean>): void--><!--Device-PhotoSession-onMacroStatusChanged(callback: AsyncCallback<boolean>): void-End-->

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

<!--Device-PhotoSession-onSmoothZoomInfoAvailable(callback: AsyncCallback<SmoothZoomInfo>): void--><!--Device-PhotoSession-onSmoothZoomInfoAvailable(callback: AsyncCallback<SmoothZoomInfo>): void-End-->

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

<!--Device-PhotoSession-onSystemPressureLevelChange(callback: AsyncCallback<SystemPressureLevel>): void--><!--Device-PhotoSession-onSystemPressureLevelChange(callback: AsyncCallback<SystemPressureLevel>): void-End-->

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

<!--Device-PhotoSession-on(type: 'autoDeviceSwitchStatusChange', callback: AsyncCallback<AutoDeviceSwitchStatus>): void--><!--Device-PhotoSession-on(type: 'autoDeviceSwitchStatusChange', callback: AsyncCallback<AutoDeviceSwitchStatus>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'autoDeviceSwitchStatusChange' | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[AutoDeviceSwitchStatus](arkts-camera-camera-autodeviceswitchstatus-i.md)&gt; | 是 |

## on_error

```TypeScript
on(type: 'error', callback: ErrorCallback): void
```

监听普通拍照会话的错误事件，通过注册回调函数获取结果。使用callback异步回调。 > **说明：** > > 当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。

**起始版本：** 11

**废弃版本：** -1

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-PhotoSession-on(type: 'error', callback: ErrorCallback): void--><!--Device-PhotoSession-on(type: 'error', callback: ErrorCallback): void-End-->

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

<!--Device-PhotoSession-on(type: 'focusStateChange', callback: AsyncCallback<FocusState>): void--><!--Device-PhotoSession-on(type: 'focusStateChange', callback: AsyncCallback<FocusState>): void-End-->

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

<!--Device-PhotoSession-on(type: 'smoothZoomInfoAvailable', callback: AsyncCallback<SmoothZoomInfo>): void--><!--Device-PhotoSession-on(type: 'smoothZoomInfoAvailable', callback: AsyncCallback<SmoothZoomInfo>): void-End-->

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

<!--Device-PhotoSession-on(type: 'systemPressureLevelChange', callback: AsyncCallback<SystemPressureLevel>): void--><!--Device-PhotoSession-on(type: 'systemPressureLevelChange', callback: AsyncCallback<SystemPressureLevel>): void-End-->

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

<!--Device-PhotoSession-preconfig(preconfigType: PreconfigType, preconfigRatio?: PreconfigRatio): void--><!--Device-PhotoSession-preconfig(preconfigType: PreconfigType, preconfigRatio?: PreconfigRatio): void-End-->

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
