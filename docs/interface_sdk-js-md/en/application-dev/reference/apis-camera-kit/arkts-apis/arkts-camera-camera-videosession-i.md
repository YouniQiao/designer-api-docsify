# VideoSession

VideoSession inherits from [Session](arkts-camera-camera-session-i.md), [Flash](arkts-camera-camera-flash-i.md),   
[AutoExposure](arkts-camera-camera-autoexposure-i.md), [WhiteBalance](arkts-camera-camera-whitebalance-i.md), [Focus](arkts-camera-camera-focus-i.md),   
[Zoom](arkts-camera-camera-zoom-i.md), [Stabilization](arkts-camera-camera-stabilization-i.md),   
[ColorManagement](arkts-camera-camera-colormanagement-i.md), [AutoDeviceSwitch](arkts-camera-camera-autodeviceswitch-i.md),   
[Macro](arkts-camera-camera-macro-i.md), [ControlCenter](arkts-camera-camera-controlcenter-i.md),   
[ManualExposure](../../../reference/apis-camera-kit/arkts-apis-camera-ManualExposure.md),   
[ManualFocus](../../../reference/apis-camera-kit/arkts-apis-camera-ManualFocus.md),   
[ManualIso](../../../reference/apis-camera-kit/arkts-apis-camera-ManualIso.md),   
[OIS](../../../reference/apis-camera-kit/arkts-apis-camera-OIS.md), and   
[Aperture](../../../reference/apis-camera-kit/arkts-apis-camera-Aperture.md).

It implements a video session, which provides operations on the flash, exposure, white balance, focus, zoom, video stabilization, color space, macro mode and controller, manual exposure, manual focus, manual ISO, optical image stabilization, and aperture.

**VideoSession** is provided for the default video recording mode. It applies to common scenarios. It supports recording at various resolutions (such as 720p and 1080p) and frame rates (such as 30 fps and 60 fps).

**Inheritance/Implementation:** VideoSession extends [Session](arkts-camera-camera-session-i.md), [Flash](arkts-camera-camera-flash-i.md), [AutoExposure](arkts-camera-camera-autoexposure-i.md), [WhiteBalance](arkts-camera-camera-whitebalance-i.md), [Focus](arkts-camera-camera-focus-i.md), [Zoom](arkts-camera-camera-zoom-i.md), [Stabilization](arkts-camera-camera-stabilization-i.md), [ColorManagement](arkts-camera-camera-colormanagement-i.md), [ControlCenter](arkts-camera-camera-controlcenter-i.md), [AutoDeviceSwitch](arkts-camera-camera-autodeviceswitch-i.md), [Macro](arkts-camera-camera-macro-i.md), [ManualExposure](arkts-camera-camera-manualexposure-i.md), [ManualFocus](arkts-camera-camera-manualfocus-i.md), [ManualIso](arkts-camera-camera-manualiso-i.md), [OIS](arkts-camera-camera-ois-i.md), [Aperture](arkts-camera-camera-aperture-i.md)

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-camera-interface VideoSession extends Session, Flash, AutoExposure, WhiteBalance, Focus, Zoom, Stabilization,    ColorManagement, ControlCenter, AutoDeviceSwitch, Macro, ManualExposure, ManualFocus, ManualIso, OIS,    Aperture--><!--Device-camera-interface VideoSession extends Session, Flash, AutoExposure, WhiteBalance, Focus, Zoom, Stabilization,    ColorManagement, ControlCenter, AutoDeviceSwitch, Macro, ManualExposure, ManualFocus, ManualIso, OIS,    Aperture-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## Modules to Import

```TypeScript
import { camera } from 'kits/@kit.CameraKit';
```

## canPreconfig

```TypeScript
canPreconfig(preconfigType: PreconfigType, preconfigRatio?: PreconfigRatio): boolean
```

Checks whether this session supports a preconfigured resolution.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-VideoSession-canPreconfig(preconfigType: PreconfigType, preconfigRatio?: PreconfigRatio): boolean--><!--Device-VideoSession-canPreconfig(preconfigType: PreconfigType, preconfigRatio?: PreconfigRatio): boolean-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| preconfigType | [PreconfigType](arkts-camera-camera-preconfigtype-e.md) | Yes | Resolution type. |
| preconfigRatio | [PreconfigRatio](arkts-camera-camera-preconfigratio-e.md) | No | Aspect ratio. The default value is 16:9. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true**: The preconfigured resolution is supported. &lt;br&gt;**false**: The preconfigured resolution is not supported. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7400201](../errorcode-camera.md#7400201-camera-service-error) | Camera service fatal error. |

## off('error')

```TypeScript
off(type: 'error', callback?: ErrorCallback): void
```

Unsubscribes from **VideoSession** error events. This API uses a callback to return the result.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-VideoSession-off(type: 'error', callback?: ErrorCallback): void--><!--Device-VideoSession-off(type: 'error', callback?: ErrorCallback): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'error' | Yes | Event type. The value is fixed at **'error'**. The event can be listened for when a session is created. |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | No | Callback used to return the result. If this parameter is specified, the subscription to the specified event with the specified callback is canceled. (The callback object cannot be an anonymous function.) Otherwise, the subscriptions to the specified event with all the callbacks are canceled. |

## off('focusStateChange')

```TypeScript
off(type: 'focusStateChange', callback?: AsyncCallback<FocusState>): void
```

Unsubscribes from focus state change events.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-VideoSession-off(type: 'focusStateChange', callback?: AsyncCallback<FocusState>): void--><!--Device-VideoSession-off(type: 'focusStateChange', callback?: AsyncCallback<FocusState>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'focusStateChange' | Yes | Event type. The value is fixed at **'focusStateChange'**. The event can be listened for when a session is created. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;FocusState&gt; | No | Callback used to return the result. If this parameter is specified, the subscription to the specified event with the specified callback is canceled. (The callback object cannot be an anonymous function.) Otherwise, the subscriptions to the specified event with all the callbacks are canceled. |

## off('smoothZoomInfoAvailable')

```TypeScript
off(type: 'smoothZoomInfoAvailable', callback?: AsyncCallback<SmoothZoomInfo>): void
```

Unsubscribes from smooth zoom state change events.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-VideoSession-off(type: 'smoothZoomInfoAvailable', callback?: AsyncCallback<SmoothZoomInfo>): void--><!--Device-VideoSession-off(type: 'smoothZoomInfoAvailable', callback?: AsyncCallback<SmoothZoomInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'smoothZoomInfoAvailable' | Yes | Event type. The value is fixed at **'smoothZoomInfoAvailable'**. The event can be listened for when a session is created. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;SmoothZoomInfo&gt; | No | Callback used to return the result. If this parameter is specified, the subscription to the specified event with the specified callback is canceled. (The callback object cannot be an anonymous function.) Otherwise, the subscriptions to the specified event with all the callbacks are canceled. |

## off('controlCenterEffectStatusChange')

```TypeScript
off(type: 'controlCenterEffectStatusChange', callback?: AsyncCallback<ControlCenterStatusInfo>): void
```

Unsubscribes from events indicating that the camera controller effect status changes.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-VideoSession-off(type: 'controlCenterEffectStatusChange', callback?: AsyncCallback<ControlCenterStatusInfo>): void--><!--Device-VideoSession-off(type: 'controlCenterEffectStatusChange', callback?: AsyncCallback<ControlCenterStatusInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'controlCenterEffectStatusChange' | Yes | Event type. The value is fixed at **'controlCenterEffectStatusChange'**. The event can be listened for when a session is created. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;ControlCenterStatusInfo&gt; | No | Callback used to return the result. If this parameter is specified, the subscription to the specified event with the specified callback is canceled. ( The callback object cannot be an anonymous function.) Otherwise, the subscriptions to the specified event with all the callbacks are canceled. |

## off('macroStatusChanged')

```TypeScript
off(type: 'macroStatusChanged', callback?: AsyncCallback<boolean>): void
```

Unsubscribes from macro state change events.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-VideoSession-off(type: 'macroStatusChanged', callback?: AsyncCallback<boolean>): void--><!--Device-VideoSession-off(type: 'macroStatusChanged', callback?: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'macroStatusChanged' | Yes | Event type. The value is fixed at **'macroStatusChanged'**. The event can be listened for when a session is created. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | No | Callback used to return the result. If this parameter is specified, the subscription to the specified event with the specified callback is canceled. (The callback object cannot be an anonymous function.) Otherwise, the subscriptions to the specified event with all the callbacks are canceled. If **true** is returned, the unsubscription is successful. If **false** is returned, the unsubscription fails. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System Application.<br>**Applicable version:** 11 - 19 |

## off('autoDeviceSwitchStatusChange')

```TypeScript
off(type: 'autoDeviceSwitchStatusChange', callback?: AsyncCallback<AutoDeviceSwitchStatus>): void
```

Unsubscribes from automatic camera switch status change events.

**Since:** 13

**ArkTS mode:** ArkTS-Dyn only, since version 13.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-VideoSession-off(type: 'autoDeviceSwitchStatusChange', callback?: AsyncCallback<AutoDeviceSwitchStatus>): void--><!--Device-VideoSession-off(type: 'autoDeviceSwitchStatusChange', callback?: AsyncCallback<AutoDeviceSwitchStatus>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'autoDeviceSwitchStatusChange' | Yes | Event type. The value is fixed at **'autoDeviceSwitchStatusChange'**. The event can be listened for when a session is created. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;AutoDeviceSwitchStatus&gt; | No | Callback used to return the result. If this parameter is specified, the subscription to the specified event with the specified callback is canceled. (The callback object cannot be an anonymous function.) Otherwise, the subscriptions to the specified event with all the callbacks are canceled. |

## off('systemPressureLevelChange')

```TypeScript
off(type: 'systemPressureLevelChange', callback?: AsyncCallback<SystemPressureLevel>): void
```

Unsubscribes from system pressure level change events.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-VideoSession-off(type: 'systemPressureLevelChange', callback?: AsyncCallback<SystemPressureLevel>): void--><!--Device-VideoSession-off(type: 'systemPressureLevelChange', callback?: AsyncCallback<SystemPressureLevel>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'systemPressureLevelChange' | Yes | Event type. The value is fixed at **'systemPressureLevelChange'**. The event can be listened for when a session is created. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;SystemPressureLevel&gt; | No | Callback used to return the result. If this parameter is specified, the subscription to the specified event with the specified callback is canceled. (The callback object cannot be an anonymous function.) Otherwise, the subscriptions to the specified event with all the callbacks are canceled. |

## offAutoDeviceSwitchStatusChange

```TypeScript
offAutoDeviceSwitchStatusChange(callback?: AsyncCallback<AutoDeviceSwitchStatus>): void
```

Unsubscribes to auto device switch status event callback.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-VideoSession-offAutoDeviceSwitchStatusChange(callback?: AsyncCallback<AutoDeviceSwitchStatus>): void--><!--Device-VideoSession-offAutoDeviceSwitchStatusChange(callback?: AsyncCallback<AutoDeviceSwitchStatus>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;AutoDeviceSwitchStatus&gt; | No | Callback used to return the result. |

## offControlCenterEffectStatusChange

```TypeScript
offControlCenterEffectStatusChange(callback?: AsyncCallback<ControlCenterStatusInfo>): void
```

Unsubscribes to control center effect status change callback.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-VideoSession-offControlCenterEffectStatusChange(callback?: AsyncCallback<ControlCenterStatusInfo>): void--><!--Device-VideoSession-offControlCenterEffectStatusChange(callback?: AsyncCallback<ControlCenterStatusInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;ControlCenterStatusInfo&gt; | No | Callback used to get control center effect status. |

## offError

```TypeScript
offError(callback?: ErrorCallback): void
```

Unsubscribes from error events.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-VideoSession-offError(callback?: ErrorCallback): void--><!--Device-VideoSession-offError(callback?: ErrorCallback): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | No | Callback used to get the capture session errors. |

## offExposureInfoChange

```TypeScript
offExposureInfoChange(callback?: Callback<ExposureInfo>): void
```

Unsubscribes from exposure information change events. If you have subscribed to exposure information, cancel the subscription before releasing the camera. This API uses an asynchronous callback to return the result.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-VideoSession-offExposureInfoChange(callback?: Callback<ExposureInfo>): void--><!--Device-VideoSession-offExposureInfoChange(callback?: Callback<ExposureInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;ExposureInfo&gt; | No | Callback used to return the result. If this parameter is specified, the subscription to the specified event with the specified callback is canceled. (The callback object cannot be an anonymous function.) Otherwise, the subscriptions to the specified event with all the callbacks are canceled. |

## offFocusStateChange

```TypeScript
offFocusStateChange(callback?: AsyncCallback<FocusState>): void
```

Unsubscribes from focus state change event callback.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-VideoSession-offFocusStateChange(callback?: AsyncCallback<FocusState>): void--><!--Device-VideoSession-offFocusStateChange(callback?: AsyncCallback<FocusState>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;FocusState&gt; | No | Callback used to get the focus state change. |

## offIsoInfoChange

```TypeScript
offIsoInfoChange(callback?: Callback<IsoInfo>): void
```

Unsubscribes from ISO state change events.

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-VideoSession-offIsoInfoChange(callback?: Callback<IsoInfo>): void--><!--Device-VideoSession-offIsoInfoChange(callback?: Callback<IsoInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;IsoInfo&gt; | No | Callback used for unsubscription. &lt;br&gt;If this parameter is specified, the subscription to the specified event with the specified callback is canceled. (The callback object cannot be an anonymous function.) &lt;br&gt;Otherwise, the subscriptions to the specified event with all the callbacks are canceled. |

## offMacroStatusChanged

```TypeScript
offMacroStatusChanged(callback?: AsyncCallback<boolean>): void
```

Unsubscribes camera macro status event callback.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-VideoSession-offMacroStatusChanged(callback?: AsyncCallback<boolean>): void--><!--Device-VideoSession-offMacroStatusChanged(callback?: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | No | Callback used to return macro detection result, true indicating macro scene is detected and can be enabled, false indicating no macro scene is detected, and macro should be disabled. |

## offSmoothZoomInfoAvailable

```TypeScript
offSmoothZoomInfoAvailable(callback?: AsyncCallback<SmoothZoomInfo>): void
```

Unsubscribes from zoom info event callback.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-VideoSession-offSmoothZoomInfoAvailable(callback?: AsyncCallback<SmoothZoomInfo>): void--><!--Device-VideoSession-offSmoothZoomInfoAvailable(callback?: AsyncCallback<SmoothZoomInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;SmoothZoomInfo&gt; | No | Callback used to get the zoom info. |

## offSystemPressureLevelChange

```TypeScript
offSystemPressureLevelChange(callback?: AsyncCallback<SystemPressureLevel>): void
```

Unsubscribes to system pressure level event callback.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-VideoSession-offSystemPressureLevelChange(callback?: AsyncCallback<SystemPressureLevel>): void--><!--Device-VideoSession-offSystemPressureLevelChange(callback?: AsyncCallback<SystemPressureLevel>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;SystemPressureLevel&gt; | No | Callback used to return the result. |

## on('error')

```TypeScript
on(type: 'error', callback: ErrorCallback): void
```

Subscribes to **VideoSession** error events. This API uses an asynchronous callback to return the result.

> **NOTE：**
> 
> Currently, you cannot use **off()** to unregister the callback in the callback method of **on()**.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-VideoSession-on(type: 'error', callback: ErrorCallback): void--><!--Device-VideoSession-on(type: 'error', callback: ErrorCallback): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'error' | Yes | Event type. The value is fixed at **'error'**. The event can be listened for when a session is created. This event is triggered and the error message is returned when an error occurs during the calling of a session-related API such as [beginConfig](arkts-camera-camera-session-i.md#beginconfig), [commitConfig](arkts-camera-camera-session-i.md#commitconfig), and [addInput](arkts-camera-camera-session-i.md#addinput). |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | Yes | Callback used to return an error code defined in [CameraErrorCode](arkts-camera-camera-cameraerrorcode-e.md). |

## on('focusStateChange')

```TypeScript
on(type: 'focusStateChange', callback: AsyncCallback<FocusState>): void
```

Subscribes to focus state change events. This API uses an asynchronous callback to return the result.

> **NOTE：**
> 
> Currently, you cannot use **off()** to unregister the callback in the callback method of **on()**.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-VideoSession-on(type: 'focusStateChange', callback: AsyncCallback<FocusState>): void--><!--Device-VideoSession-on(type: 'focusStateChange', callback: AsyncCallback<FocusState>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'focusStateChange' | Yes | Event type. The value is fixed at **'focusStateChange'**. The event can be listened for when a session is created. This event is triggered only when the camera focus state changes in auto focus mode. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;FocusState&gt; | Yes | Callback used to return the focus state change. |

## on('smoothZoomInfoAvailable')

```TypeScript
on(type: 'smoothZoomInfoAvailable', callback: AsyncCallback<SmoothZoomInfo>): void
```

Subscribes to smooth zoom state change events. This API uses an asynchronous callback to return the result.

> **NOTE：**
> 
> Currently, you cannot use **off()** to unregister the callback in the callback method of **on()**.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-VideoSession-on(type: 'smoothZoomInfoAvailable', callback: AsyncCallback<SmoothZoomInfo>): void--><!--Device-VideoSession-on(type: 'smoothZoomInfoAvailable', callback: AsyncCallback<SmoothZoomInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'smoothZoomInfoAvailable' | Yes | Event type. The value is fixed at **'smoothZoomInfoAvailable'**. The event can be listened for when a session is created. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;SmoothZoomInfo&gt; | Yes | Callback used to return the smooth zoom state change. |

## on('controlCenterEffectStatusChange')

```TypeScript
on(type: 'controlCenterEffectStatusChange', callback: AsyncCallback<ControlCenterStatusInfo>): void
```

Subscribes to events indicating that the camera controller effect status changes. This API uses an asynchronous callback to return the result.

> **NOTE：**
> 
> Currently, you cannot use **off()** to unregister the callback in the callback method of **on()**.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-VideoSession-on(type: 'controlCenterEffectStatusChange', callback: AsyncCallback<ControlCenterStatusInfo>): void--><!--Device-VideoSession-on(type: 'controlCenterEffectStatusChange', callback: AsyncCallback<ControlCenterStatusInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'controlCenterEffectStatusChange' | Yes | Event type. The value is fixed at **'controlCenterEffectStatusChange'**. The event can be listened for when a session is created. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;ControlCenterStatusInfo&gt; | Yes | Callback used to return the effect status of the current controller. |

## on('macroStatusChanged')

```TypeScript
on(type: 'macroStatusChanged', callback: AsyncCallback<boolean>): void
```

Subscribes to macro state change events. This API uses an asynchronous callback to return the result.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-VideoSession-on(type: 'macroStatusChanged', callback: AsyncCallback<boolean>): void--><!--Device-VideoSession-on(type: 'macroStatusChanged', callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'macroStatusChanged' | Yes | Event type. The value is fixed at **'macroStatusChanged'**. The event can be listened for when a session is created. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes | Callback used to return the macro state. **true** if enabled, **false** otherwise. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System Application.<br>**Applicable version:** 11 - 19 |

## on('autoDeviceSwitchStatusChange')

```TypeScript
on(type: 'autoDeviceSwitchStatusChange', callback: AsyncCallback<AutoDeviceSwitchStatus>): void
```

Subscribes to automatic camera switch status change events. This API uses an asynchronous callback to return the result.

> **NOTE：**
> 
> Currently, you cannot use **off()** to unregister the callback in the callback method of **on()**.

**Since:** 13

**ArkTS mode:** ArkTS-Dyn only, since version 13.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-VideoSession-on(type: 'autoDeviceSwitchStatusChange', callback: AsyncCallback<AutoDeviceSwitchStatus>): void--><!--Device-VideoSession-on(type: 'autoDeviceSwitchStatusChange', callback: AsyncCallback<AutoDeviceSwitchStatus>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'autoDeviceSwitchStatusChange' | Yes | Event type. The value is fixed at **'autoDeviceSwitchStatusChange'**. The event can be listened for when a session is created. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;AutoDeviceSwitchStatus&gt; | Yes | Callback used to obtain the status of automatic camera switch. |

## on('systemPressureLevelChange')

```TypeScript
on(type: 'systemPressureLevelChange', callback: AsyncCallback<SystemPressureLevel>): void
```

Subscribes to system pressure level change events. This API uses an asynchronous callback to return the result.

> **NOTE：**
> 
> Currently, you cannot use **off()** to unregister the callback in the callback method of **on()**.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-VideoSession-on(type: 'systemPressureLevelChange', callback: AsyncCallback<SystemPressureLevel>): void--><!--Device-VideoSession-on(type: 'systemPressureLevelChange', callback: AsyncCallback<SystemPressureLevel>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'systemPressureLevelChange' | Yes | Event type. The value is fixed at **'systemPressureLevelChange'**. The event can be listened for when a session is created. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;SystemPressureLevel&gt; | Yes | Callback used to return the current system pressure level. |

## onAutoDeviceSwitchStatusChange

```TypeScript
onAutoDeviceSwitchStatusChange(callback: AsyncCallback<AutoDeviceSwitchStatus>): void
```

Subscribes to auto device switch status event callback.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-VideoSession-onAutoDeviceSwitchStatusChange(callback: AsyncCallback<AutoDeviceSwitchStatus>): void--><!--Device-VideoSession-onAutoDeviceSwitchStatusChange(callback: AsyncCallback<AutoDeviceSwitchStatus>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;AutoDeviceSwitchStatus&gt; | Yes | Callback used to return the result. |

## onControlCenterEffectStatusChange

```TypeScript
onControlCenterEffectStatusChange(callback: AsyncCallback<ControlCenterStatusInfo>): void
```

Subscribes to control center effect status change callback.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-VideoSession-onControlCenterEffectStatusChange(callback: AsyncCallback<ControlCenterStatusInfo>): void--><!--Device-VideoSession-onControlCenterEffectStatusChange(callback: AsyncCallback<ControlCenterStatusInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;ControlCenterStatusInfo&gt; | Yes | Callback used to get control center effect status. |

## onError

```TypeScript
onError(callback: ErrorCallback): void
```

Subscribes to error events.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-VideoSession-onError(callback: ErrorCallback): void--><!--Device-VideoSession-onError(callback: ErrorCallback): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | Yes | Callback used to get the capture session errors. |

## onExposureInfoChange

```TypeScript
onExposureInfoChange(callback: Callback<ExposureInfo>): void
```

Subscribes to exposure information change events. After the exposure parameters are changed, the system returns the updated exposure information. This API uses an asynchronous callback to return the result.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-VideoSession-onExposureInfoChange(callback: Callback<ExposureInfo>): void--><!--Device-VideoSession-onExposureInfoChange(callback: Callback<ExposureInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;ExposureInfo&gt; | Yes | Callback used to obtain the exposure information. |

## onFocusStateChange

```TypeScript
onFocusStateChange(callback: AsyncCallback<FocusState>): void
```

Subscribes focus state change event callback.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-VideoSession-onFocusStateChange(callback: AsyncCallback<FocusState>): void--><!--Device-VideoSession-onFocusStateChange(callback: AsyncCallback<FocusState>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;FocusState&gt; | Yes | Callback used to get the focus state change. |

## onIsoInfoChange

```TypeScript
onIsoInfoChange(callback: Callback<IsoInfo>): void
```

Subscribes to sensitivity (ISO) state change events and obtains the latest ISO value through a callback.

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-VideoSession-onIsoInfoChange(callback: Callback<IsoInfo>): void--><!--Device-VideoSession-onIsoInfoChange(callback: Callback<IsoInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;IsoInfo&gt; | Yes | Callback used to obtain the current ISO value of the camera. |

## onMacroStatusChanged

```TypeScript
onMacroStatusChanged(callback: AsyncCallback<boolean>): void
```

Subscribes camera macro status event callback.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-VideoSession-onMacroStatusChanged(callback: AsyncCallback<boolean>): void--><!--Device-VideoSession-onMacroStatusChanged(callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes | Callback used to return macro detection result, true indicating macro scene is detected and can be enabled, false indicating no macro scene is detected, and macro should be disabled. |

## onSmoothZoomInfoAvailable

```TypeScript
onSmoothZoomInfoAvailable(callback: AsyncCallback<SmoothZoomInfo>): void
```

Subscribes zoom info event callback.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-VideoSession-onSmoothZoomInfoAvailable(callback: AsyncCallback<SmoothZoomInfo>): void--><!--Device-VideoSession-onSmoothZoomInfoAvailable(callback: AsyncCallback<SmoothZoomInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;SmoothZoomInfo&gt; | Yes | Callback used to get the zoom info. |

## onSystemPressureLevelChange

```TypeScript
onSystemPressureLevelChange(callback: AsyncCallback<SystemPressureLevel>): void
```

Subscribes to system pressure level event callback.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-VideoSession-onSystemPressureLevelChange(callback: AsyncCallback<SystemPressureLevel>): void--><!--Device-VideoSession-onSystemPressureLevelChange(callback: AsyncCallback<SystemPressureLevel>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;SystemPressureLevel&gt; | Yes | Callback used to return the result. |

## preconfig

```TypeScript
preconfig(preconfigType: PreconfigType, preconfigRatio?: PreconfigRatio): void
```

Preconfigures this session.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-VideoSession-preconfig(preconfigType: PreconfigType, preconfigRatio?: PreconfigRatio): void--><!--Device-VideoSession-preconfig(preconfigType: PreconfigType, preconfigRatio?: PreconfigRatio): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| preconfigType | [PreconfigType](arkts-camera-camera-preconfigtype-e.md) | Yes | Resolution type. |
| preconfigRatio | [PreconfigRatio](arkts-camera-camera-preconfigratio-e.md) | No | Aspect ratio. The default value is 16:9. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7400201](../errorcode-camera.md#7400201-camera-service-error) | Camera service fatal error. |

## setQualityPrioritization

```TypeScript
setQualityPrioritization(quality: QualityPrioritization): void
```

Sets the priority level for video recording quality.

> **NOTE：**
> 
> - The default value is **HIGH_QUALITY**. Switching to **POWER_BALANCE** will compromise video recording quality
> to achieve lower power usage. The extent of power conservation achieved varies depending on the platform.
> 
> - It is recommended that this API be called between
> [commitConfig](arkts-camera-camera-session-i.md#commitconfig) and
> [start](arkts-camera-camera-session-i.md#start).

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-VideoSession-setQualityPrioritization(quality: QualityPrioritization): void--><!--Device-VideoSession-setQualityPrioritization(quality: QualityPrioritization): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| quality | [QualityPrioritization](arkts-camera-camera-qualityprioritization-e.md) | Yes | Priority level to set. The default value is **HIGH_QUALITY**. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) | Session not config. The session has not been committed or configured. |

