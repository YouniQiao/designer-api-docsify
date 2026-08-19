# VideoSession

VideoSession inherits from [Session](arkts-camera-camera-session-i.md), [Flash](arkts-camera-camera-flash-i.md), [AutoExposure](arkts-camera-camera-autoexposure-i.md), [WhiteBalance](arkts-camera-camera-whitebalance-i.md), [Focus](arkts-camera-camera-focus-i.md), [Zoom](arkts-camera-camera-zoom-i.md), [Stabilization](arkts-camera-camera-stabilization-i.md), [ColorManagement](arkts-camera-camera-colormanagement-i.md), [AutoDeviceSwitch](arkts-camera-camera-autodeviceswitch-i.md), [Macro](arkts-camera-camera-macro-i-sys.md), [ControlCenter](arkts-camera-camera-controlcenter-i.md), [ManualExposure](../../../reference/apis-camera-kit/arkts-apis-camera-ManualExposure.md), [ManualFocus](../../../reference/apis-camera-kit/arkts-apis-camera-ManualFocus.md), [ManualIso](../../../reference/apis-camera-kit/arkts-apis-camera-ManualIso.md), [OIS](../../../reference/apis-camera-kit/arkts-apis-camera-OIS.md), and [Aperture](../../../reference/apis-camera-kit/arkts-apis-camera-Aperture.md). It implements a video session, which provides operations on the flash, exposure, white balance, focus, zoom, video stabilization, color space, macro mode and controller, manual exposure, manual focus, manual ISO, optical image stabilization, and aperture. **VideoSession** is provided for the default video recording mode. It applies to common scenarios. It supports recording at various resolutions (such as 720p and 1080p) and frame rates (such as 30 fps and 60 fps).

**Inheritance/Implementation:** VideoSession extends [Session](arkts-camera-camera-session-i.md), [Flash](arkts-camera-camera-flash-i.md), [AutoExposure](arkts-camera-camera-autoexposure-i.md), [WhiteBalance](arkts-camera-camera-whitebalance-i.md), [Focus](arkts-camera-camera-focus-i.md), [Zoom](arkts-camera-camera-zoom-i.md), [Stabilization](arkts-camera-camera-stabilization-i.md), [ColorManagement](arkts-camera-camera-colormanagement-i.md), [ControlCenter](arkts-camera-camera-controlcenter-i.md), [AutoDeviceSwitch](arkts-camera-camera-autodeviceswitch-i.md), [Macro](arkts-camera-camera-macro-i-sys.md), [ManualExposure](arkts-camera-camera-manualexposure-i.md), [ManualFocus](arkts-camera-camera-manualfocus-i-sys.md), [ManualIso](arkts-camera-camera-manualiso-i-sys.md), [OIS](arkts-camera-camera-ois-i.md), [Aperture](arkts-camera-camera-aperture-i-sys.md)

**Since:** 23

<!--Device-camera-interface VideoSession--><!--Device-camera-interface VideoSession-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## Modules to Import

```TypeScript
import { camera } from '@kit.CameraKit';
import { cameraPicker } from '@kit.CameraKit';
```

## getSessionConflictFunctions

```TypeScript
getSessionConflictFunctions(): Array<VideoConflictFunctions>
```

Gets session conflict functions.

**Since:** 23

<!--Device-VideoSession-getSessionConflictFunctions(): Array<VideoConflictFunctions>--><!--Device-VideoSession-getSessionConflictFunctions(): Array<VideoConflictFunctions>-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;[VideoConflictFunctions](arkts-camera-camera-videoconflictfunctions-i.md)&gt; | List of session conflict functions. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System Application. |

## getSessionFunctions

```TypeScript
getSessionFunctions(outputCapability: CameraOutputCapability): Array<VideoFunctions>
```

Gets session functions.

**Since:** 23

<!--Device-VideoSession-getSessionFunctions(outputCapability: CameraOutputCapability): Array<VideoFunctions>--><!--Device-VideoSession-getSessionFunctions(outputCapability: CameraOutputCapability): Array<VideoFunctions>-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| outputCapability | [CameraOutputCapability](arkts-camera-camera-cameraoutputcapability-i.md) | Yes | CameraOutputCapability to set. |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;[VideoFunctions](arkts-camera-camera-videofunctions-i.md)&gt; | List of session functions. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System Application. |

## offApertureInfoChange

```TypeScript
offApertureInfoChange(callback?: Callback<ApertureInfo>): void
```

Unsubscribes from aperture info event callback.

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-VideoSession-offApertureInfoChange(callback?: Callback<ApertureInfo>): void--><!--Device-VideoSession-offApertureInfoChange(callback?: Callback<ApertureInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[ApertureInfo](arkts-camera-camera-apertureinfo-i-sys.md)&gt; | No | Callback used to get the aperture info. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System Application. |

## offEffectSuggestionChange

```TypeScript
offEffectSuggestionChange(callback?: AsyncCallback<EffectSuggestionType>): void
```

Unsubscribes from effect suggestion change events.

**Since:** 23

<!--Device-VideoSession-offEffectSuggestionChange(callback?: AsyncCallback<EffectSuggestionType>): void--><!--Device-VideoSession-offEffectSuggestionChange(callback?: AsyncCallback<EffectSuggestionType>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;[EffectSuggestionType](arkts-camera-camera-effectsuggestiontype-e-sys.md)&gt; | No | Callback used to return the result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System Application. |

## offFocusTrackingInfoAvailable

```TypeScript
offFocusTrackingInfoAvailable(callback?: Callback<FocusTrackingInfo>): void
```

Unsubscribes from focus tracking info event callback.

**Since:** 23

<!--Device-VideoSession-offFocusTrackingInfoAvailable(callback?: Callback<FocusTrackingInfo>): void--><!--Device-VideoSession-offFocusTrackingInfoAvailable(callback?: Callback<FocusTrackingInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[FocusTrackingInfo](arkts-camera-camera-focustrackinginfo-i-sys.md)&gt; | No | Callback used to get the focus tracking info. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System Application. |

## offLcdFlashStatus

```TypeScript
offLcdFlashStatus(callback?: AsyncCallback<LcdFlashStatus>): void
```

Unsubscribes from lcd flash status.

**Since:** 23

<!--Device-VideoSession-offLcdFlashStatus(callback?: AsyncCallback<LcdFlashStatus>): void--><!--Device-VideoSession-offLcdFlashStatus(callback?: AsyncCallback<LcdFlashStatus>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;[LcdFlashStatus](arkts-camera-camera-lcdflashstatus-i-sys.md)&gt; | No | Callback used to get the lcd flash status. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System Application. |

## offLightStatusChange

```TypeScript
offLightStatusChange(callback?: AsyncCallback<LightStatus>): void
```

Unsubscribes camera light status event callback.

**Since:** 23

<!--Device-VideoSession-offLightStatusChange(callback?: AsyncCallback<LightStatus>): void--><!--Device-VideoSession-offLightStatusChange(callback?: AsyncCallback<LightStatus>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;[LightStatus](arkts-camera-camera-lightstatus-e-sys.md)&gt; | No | Callback used to return the result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System Application. |

## off('effectSuggestionChange')

```TypeScript
off(type: 'effectSuggestionChange', callback?: AsyncCallback<EffectSuggestionType>): void
```

Unsubscribes from effect suggestion change events.

**Since:** 18

<!--Device-VideoSession-off(type: 'effectSuggestionChange', callback?: AsyncCallback<EffectSuggestionType>): void--><!--Device-VideoSession-off(type: 'effectSuggestionChange', callback?: AsyncCallback<EffectSuggestionType>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'effectSuggestionChange' | Yes | Event type. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;[EffectSuggestionType](arkts-camera-camera-effectsuggestiontype-e-sys.md)&gt; | No | Callback used to return the result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System Application. |

## off('focusTrackingInfoAvailable')

```TypeScript
off(type: 'focusTrackingInfoAvailable', callback?: Callback<FocusTrackingInfo>): void
```

Unsubscribes from focus tracking information events.

**Since:** 15

<!--Device-VideoSession-off(type: 'focusTrackingInfoAvailable', callback?: Callback<FocusTrackingInfo>): void--><!--Device-VideoSession-off(type: 'focusTrackingInfoAvailable', callback?: Callback<FocusTrackingInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'focusTrackingInfoAvailable' | Yes | Event type. The value is fixed at **'focusTrackingInfoAvailable'**. The event can be listened for when a VideoSessionForSys object is created. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[FocusTrackingInfo](arkts-camera-camera-focustrackinginfo-i-sys.md)&gt; | No | Callback used to return the result. This parameter is optional. If this parameter is specified, the subscription to the specified event **on('focusTrackingInfoAvailable')** with the specified callback is canceled. (The callback object cannot be an anonymous function.) |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System Application. |

**Examples**

```TypeScript
function unregisterFocusTrackingInfoChanged(session: camera.VideoSessionForSys): void {
  session.off('focusTrackingInfoAvailable');
}
```

## off('lcdFlashStatus')

```TypeScript
off(type: 'lcdFlashStatus', callback?: AsyncCallback<LcdFlashStatus>): void
```

Unsubscribes from LCD flash status change events.

**Since:** 13

<!--Device-VideoSession-off(type: 'lcdFlashStatus', callback?: AsyncCallback<LcdFlashStatus>): void--><!--Device-VideoSession-off(type: 'lcdFlashStatus', callback?: AsyncCallback<LcdFlashStatus>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'lcdFlashStatus' | Yes | Event type. The value is fixed at **'lcdFlashStatus'**. The event can be listened for when a session is created. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;[LcdFlashStatus](arkts-camera-camera-lcdflashstatus-i-sys.md)&gt; | No | Callback used to return the result. This parameter is optional. If this parameter is specified, the subscription to the specified event **on('lcdFlashStatus')** with the specified callback is canceled. (The callback object cannot be an anonymous function.) |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System Application. |

**Examples**

```TypeScript
function unregisterLcdFlashStatus(videoSession: camera.VideoSession): void {
  videoSession.off('lcdFlashStatus');
}
```

## off('lightStatusChange')

```TypeScript
off(type: 'lightStatusChange', callback?: AsyncCallback<LightStatus>): void
```

Unsubscribes from camera light status changes.

**Since:** 18

<!--Device-VideoSession-off(type: 'lightStatusChange', callback?: AsyncCallback<LightStatus>): void--><!--Device-VideoSession-off(type: 'lightStatusChange', callback?: AsyncCallback<LightStatus>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'lightStatusChange' | Yes | Event type. The value is fixed at **'lightStatusChange'**. <br>The event can be listened for when a VideoSessionForSys object is created. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;[LightStatus](arkts-camera-camera-lightstatus-e-sys.md)&gt; | No | Callback used to return the result. This parameter is optional. If this parameter is specified, the subscription to the specified event **on('lightStatusChange')** with the specified callback is canceled. (The callback object cannot be an anonymous function.) |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System Application. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function LightStatusCallback(err: BusinessError, lightStatus: camera.LightStatus) : void {
  if (err !== undefined && err.code !== 0) {
    console.error(`Callback Error, errorCode: ${err.code}`);
    return;
  }
  console.info(`lightStatus: ${lightStatus}`);
}

function handleLightStatusOff(mSession: camera.VideoSessionForSys): void {
  console.info('handleLightStatusOff');
  try {
    mSession.on('lightStatusChange', LightStatusCallback);
  } catch (error) {
    let err = error as BusinessError;
    console.error(`handleLightStatusOff err:${err}`);
  }
}
```

## off('macroStatusChanged')

```TypeScript
off(type: 'macroStatusChanged', callback?: AsyncCallback<boolean>): void
```

Unsubscribes from macro state change events.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-VideoSession-off(type: 'macroStatusChanged', callback?: AsyncCallback<boolean>): void--><!--Device-VideoSession-off(type: 'macroStatusChanged', callback?: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'macroStatusChanged' | Yes | Event type. The value is fixed at **'macroStatusChanged'**. The event can be listened for when a session is created. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;boolean&gt; | No | Callback used to return the result. If this parameter is specified, the subscription to the specified event with the specified callback is canceled. (The callback object cannot be an anonymous function.) Otherwise, the subscriptions to the specified event with all the callbacks are canceled. If **true** is returned, the unsubscription is successful. If **false** is returned, the unsubscription fails. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System Application.<br>**Applicable version:** 11 - 19 |

## onApertureInfoChange

```TypeScript
onApertureInfoChange(callback: Callback<ApertureInfo>): void
```

Subscribes aperture info event callback.

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-VideoSession-onApertureInfoChange(callback: Callback<ApertureInfo>): void--><!--Device-VideoSession-onApertureInfoChange(callback: Callback<ApertureInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[ApertureInfo](arkts-camera-camera-apertureinfo-i-sys.md)&gt; | Yes | Callback used to get the aperture info. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System Application. |

## onEffectSuggestionChange

```TypeScript
onEffectSuggestionChange(callback: AsyncCallback<EffectSuggestionType>): void
```

Subscribes to effect suggestion change events.

**Since:** 23

<!--Device-VideoSession-onEffectSuggestionChange(callback: AsyncCallback<EffectSuggestionType>): void--><!--Device-VideoSession-onEffectSuggestionChange(callback: AsyncCallback<EffectSuggestionType>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;[EffectSuggestionType](arkts-camera-camera-effectsuggestiontype-e-sys.md)&gt; | Yes | Callback used to return the result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System Application. |

## onFocusTrackingInfoAvailable

```TypeScript
onFocusTrackingInfoAvailable(callback: Callback<FocusTrackingInfo>): void
```

Subscribes to focus tracking info event callback.

**Since:** 23

<!--Device-VideoSession-onFocusTrackingInfoAvailable(callback: Callback<FocusTrackingInfo>): void--><!--Device-VideoSession-onFocusTrackingInfoAvailable(callback: Callback<FocusTrackingInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[FocusTrackingInfo](arkts-camera-camera-focustrackinginfo-i-sys.md)&gt; | Yes | Callback used to get the focus tracking info. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System Application. |

## onLcdFlashStatus

```TypeScript
onLcdFlashStatus(callback: AsyncCallback<LcdFlashStatus>): void
```

Subscribes to lcd flash status.

**Since:** 23

<!--Device-VideoSession-onLcdFlashStatus(callback: AsyncCallback<LcdFlashStatus>): void--><!--Device-VideoSession-onLcdFlashStatus(callback: AsyncCallback<LcdFlashStatus>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;[LcdFlashStatus](arkts-camera-camera-lcdflashstatus-i-sys.md)&gt; | Yes | Callback used to get the lcd flash status. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System Application. |

## onLightStatusChange

```TypeScript
onLightStatusChange(callback: AsyncCallback<LightStatus>): void
```

Subscribes camera light status event callback.

**Since:** 23

<!--Device-VideoSession-onLightStatusChange(callback: AsyncCallback<LightStatus>): void--><!--Device-VideoSession-onLightStatusChange(callback: AsyncCallback<LightStatus>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;[LightStatus](arkts-camera-camera-lightstatus-e-sys.md)&gt; | Yes | Callback used to return the result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System Application. |

## on('effectSuggestionChange')

```TypeScript
on(type: 'effectSuggestionChange', callback: AsyncCallback<EffectSuggestionType>): void
```

Subscribes to effect suggestion change events.

**Since:** 18

<!--Device-VideoSession-on(type: 'effectSuggestionChange', callback: AsyncCallback<EffectSuggestionType>): void--><!--Device-VideoSession-on(type: 'effectSuggestionChange', callback: AsyncCallback<EffectSuggestionType>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'effectSuggestionChange' | Yes | Event type. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;[EffectSuggestionType](arkts-camera-camera-effectsuggestiontype-e-sys.md)&gt; | Yes | Callback used to return the result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System Application. |

## on('focusTrackingInfoAvailable')

```TypeScript
on(type: 'focusTrackingInfoAvailable', callback: Callback<FocusTrackingInfo>): void
```

Subscribes to focus tracking information events. This API uses an asynchronous callback to return the result.

**Since:** 15

<!--Device-VideoSession-on(type: 'focusTrackingInfoAvailable', callback: Callback<FocusTrackingInfo>): void--><!--Device-VideoSession-on(type: 'focusTrackingInfoAvailable', callback: Callback<FocusTrackingInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'focusTrackingInfoAvailable' | Yes | Event type. The value is fixed at **'focusTrackingInfoAvailable'**. The event can be listened for when a VideoSessionForSys object is created. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[FocusTrackingInfo](arkts-camera-camera-focustrackinginfo-i-sys.md)&gt; | Yes | Callback used to return the focus tracking information. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System Application. |

**Examples**

```TypeScript
function callback(focusTrackingInfo: camera.FocusTrackingInfo): void {
  console.info(`Focus tracking mode: ${focusTrackingInfo.trackingMode}`);
  console.info(`Focus tracking Region: topLeftX ${focusTrackingInfo.trackingRegion.topLeftX}
                                       topLeftY ${focusTrackingInfo.trackingRegion.topLeftY}
                                       width ${focusTrackingInfo.trackingRegion.width}
                                       height ${focusTrackingInfo.trackingRegion.height}`);
}

function registerFocusTrackingInfoChanged(session: camera.VideoSessionForSys): void {
  session.on('focusTrackingInfoAvailable', callback);
}
```

## on('lcdFlashStatus')

```TypeScript
on(type: 'lcdFlashStatus', callback: AsyncCallback<LcdFlashStatus>): void
```

Subscribes to LCD flash status change events. This API uses an asynchronous callback to return the result.

**Since:** 13

<!--Device-VideoSession-on(type: 'lcdFlashStatus', callback: AsyncCallback<LcdFlashStatus>): void--><!--Device-VideoSession-on(type: 'lcdFlashStatus', callback: AsyncCallback<LcdFlashStatus>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'lcdFlashStatus' | Yes | Event type. The value is fixed at **'lcdFlashStatus'**. The event can be listened for when a session is created. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;[LcdFlashStatus](arkts-camera-camera-lcdflashstatus-i-sys.md)&gt; | Yes | Callback used to return the LCD flash status change. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System Application. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function callback(err: BusinessError, lcdFlashStatus: camera.LcdFlashStatus): void {
  if (err !== undefined && err.code !== 0) {
    console.error(`Callback Error, errorCode: ${err.code}`);
    return;
  }
  console.info(`isLcdFlashNeeded: ${lcdFlashStatus.isLcdFlashNeeded}`);
  console.info(`lcdCompensation: ${lcdFlashStatus.lcdCompensation}`);
}

function registerLcdFlashStatus(videoSession: camera.VideoSession): void {
  videoSession.on('lcdFlashStatus', callback);
}
```

## on('lightStatusChange')

```TypeScript
on(type: 'lightStatusChange', callback: AsyncCallback<LightStatus>): void
```

Subscribes to camera light status changes. This API uses an asynchronous callback to return the result.

**Since:** 18

<!--Device-VideoSession-on(type: 'lightStatusChange', callback: AsyncCallback<LightStatus>): void--><!--Device-VideoSession-on(type: 'lightStatusChange', callback: AsyncCallback<LightStatus>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'lightStatusChange' | Yes | Event type. The value is fixed at **'lightStatusChange'**. <br>The event can be listened for when a VideoSessionForSys object is created. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;[LightStatus](arkts-camera-camera-lightstatus-e-sys.md)&gt; | Yes | Callback used to return the light status information. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System Application. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function handleLightStatusCallback(err: BusinessError, lightStatus: camera.LightStatus) : void {
  if (err !== undefined && err.code !== 0) {
    console.error(`Callback Error, errorCode: ${err.code}`);
    return;
  }
  console.info(`lightStatus: ${lightStatus}`);
}

function handleLightStatusOn(mSession: camera.VideoSessionForSys): void {
  console.info('handleLightStatusOn');
  try {
    mSession.on('lightStatusChange', handleLightStatusCallback);
  } catch (error) {
    let err = error as BusinessError;
    console.error(`handleLightStatusOn err:${err}`);
  }
}
```

## on('macroStatusChanged')

```TypeScript
on(type: 'macroStatusChanged', callback: AsyncCallback<boolean>): void
```

Subscribes to macro state change events. This API uses an asynchronous callback to return the result.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-VideoSession-on(type: 'macroStatusChanged', callback: AsyncCallback<boolean>): void--><!--Device-VideoSession-on(type: 'macroStatusChanged', callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'macroStatusChanged' | Yes | Event type. The value is fixed at **'macroStatusChanged'**. The event can be listened for when a session is created. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;boolean&gt; | Yes | Callback used to return the macro state. **true** if enabled, **false** otherwise. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System Application.<br>**Applicable version:** 11 - 19 |

