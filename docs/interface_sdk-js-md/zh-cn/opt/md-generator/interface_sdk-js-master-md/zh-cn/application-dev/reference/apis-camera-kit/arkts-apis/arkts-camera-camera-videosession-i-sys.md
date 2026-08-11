# VideoSession

VideoSession继承自[Session](arkts-camera-camera-session-i.md)、[Flash](arkts-camera-camera-flash-i.md)、  
[AutoExposure](arkts-camera-camera-autoexposure-i.md)、[WhiteBalance](arkts-camera-camera-whitebalance-i.md)、[Focus](arkts-camera-camera-focus-i.md)、  
[Zoom](arkts-camera-camera-zoom-i.md)、[Stabilization](arkts-camera-camera-stabilization-i.md)、  
[ColorManagement](arkts-camera-camera-colormanagement-i.md)、[AutoDeviceSwitch](arkts-camera-camera-autodeviceswitch-i.md)、  
[Macro](arkts-camera-camera-macro-i.md)、[ControlCenter](arkts-camera-camera-controlcenter-i.md)、  
[ManualExposure](../../../reference/apis-camera-kit/arkts-apis-camera-ManualExposure.md)、  
[ManualFocus](../../../reference/apis-camera-kit/arkts-apis-camera-ManualFocus.md)、  
[ManualIso](../../../reference/apis-camera-kit/arkts-apis-camera-ManualIso.md)、  
[OIS](../../../reference/apis-camera-kit/arkts-apis-camera-OIS.md)、  
[Aperture](../../../reference/apis-camera-kit/arkts-apis-camera-Aperture.md)。

普通录像模式会话类，提供了对闪光灯、曝光、白平衡、对焦、变焦、视频防抖、色彩空间、微距及控制器、手动曝光、手动对焦、手动ISO、光学防抖及光圈的操作。

默认的视频录制模式，适用于一般场景。支持720P、1080p等多种分辨率的录制，可选择不同帧率（如30fps、60fps）。

**继承/实现关系：** VideoSession extends [Session](arkts-camera-camera-session-i.md), [Flash](arkts-camera-camera-flash-i.md), [AutoExposure](arkts-camera-camera-autoexposure-i.md), [WhiteBalance](arkts-camera-camera-whitebalance-i.md), [Focus](arkts-camera-camera-focus-i.md), [Zoom](arkts-camera-camera-zoom-i.md), [Stabilization](arkts-camera-camera-stabilization-i.md), [ColorManagement](arkts-camera-camera-colormanagement-i.md), [ControlCenter](arkts-camera-camera-controlcenter-i.md), [AutoDeviceSwitch](arkts-camera-camera-autodeviceswitch-i.md), [Macro](arkts-camera-camera-macro-i.md), [ManualExposure](arkts-camera-camera-manualexposure-i.md), [ManualFocus](arkts-camera-camera-manualfocus-i.md), [ManualIso](arkts-camera-camera-manualiso-i.md), [OIS](arkts-camera-camera-ois-i.md), [Aperture](arkts-camera-camera-aperture-i.md)

**起始版本：** 11

<!--Device-camera-interface VideoSession extends Session, Flash, AutoExposure, WhiteBalance, Focus, Zoom, Stabilization,    ColorManagement, ControlCenter, AutoDeviceSwitch, Macro, ManualExposure, ManualFocus, ManualIso, OIS,    Aperture--><!--Device-camera-interface VideoSession extends Session, Flash, AutoExposure, WhiteBalance, Focus, Zoom, Stabilization,    ColorManagement, ControlCenter, AutoDeviceSwitch, Macro, ManualExposure, ManualFocus, ManualIso, OIS,    Aperture-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

## getSessionConflictFunctions

```TypeScript
getSessionConflictFunctions(): Array<VideoConflictFunctions>
```

Gets session conflict functions.

**起始版本：** 13

<!--Device-VideoSession-getSessionConflictFunctions(): Array<VideoConflictFunctions>--><!--Device-VideoSession-getSessionConflictFunctions(): Array<VideoConflictFunctions>-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Array&lt;VideoConflictFunctions&gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## getSessionFunctions

```TypeScript
getSessionFunctions(outputCapability: CameraOutputCapability): Array<VideoFunctions>
```

Gets session functions.

**起始版本：** 13

<!--Device-VideoSession-getSessionFunctions(outputCapability: CameraOutputCapability): Array<VideoFunctions>--><!--Device-VideoSession-getSessionFunctions(outputCapability: CameraOutputCapability): Array<VideoFunctions>-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| outputCapability | [CameraOutputCapability](arkts-camera-camera-cameraoutputcapability-i-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Array&lt;VideoFunctions&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## off('lcdFlashStatus')

```TypeScript
off(type: 'lcdFlashStatus', callback?: AsyncCallback<LcdFlashStatus>): void
```

Unsubscribes from LCD flash status change events.

**起始版本：** 13

<!--Device-VideoSession-off(type: 'lcdFlashStatus', callback?: AsyncCallback<LcdFlashStatus>): void--><!--Device-VideoSession-off(type: 'lcdFlashStatus', callback?: AsyncCallback<LcdFlashStatus>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'lcdFlashStatus' | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;LcdFlashStatus&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
function unregisterLcdFlashStatus(videoSession: camera.VideoSession): void {
  videoSession.off('lcdFlashStatus');
}
```

## off('focusTrackingInfoAvailable')

```TypeScript
off(type: 'focusTrackingInfoAvailable', callback?: Callback<FocusTrackingInfo>): void
```

Unsubscribes from focus tracking information events.

**起始版本：** 15

<!--Device-VideoSession-off(type: 'focusTrackingInfoAvailable', callback?: Callback<FocusTrackingInfo>): void--><!--Device-VideoSession-off(type: 'focusTrackingInfoAvailable', callback?: Callback<FocusTrackingInfo>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'focusTrackingInfoAvailable' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;FocusTrackingInfo&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
function unregisterFocusTrackingInfoChanged(session: camera.VideoSessionForSys): void {
  session.off('focusTrackingInfoAvailable');
}
```

## off('effectSuggestionChange')

```TypeScript
off(type: 'effectSuggestionChange', callback?: AsyncCallback<EffectSuggestionType>): void
```

Unsubscribes from effect suggestion change events.

**起始版本：** 18

<!--Device-VideoSession-off(type: 'effectSuggestionChange', callback?: AsyncCallback<EffectSuggestionType>): void--><!--Device-VideoSession-off(type: 'effectSuggestionChange', callback?: AsyncCallback<EffectSuggestionType>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'effectSuggestionChange' | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;EffectSuggestionType&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## off('lightStatusChange')

```TypeScript
off(type: 'lightStatusChange', callback?: AsyncCallback<LightStatus>): void
```

Unsubscribes from camera light status changes.

**起始版本：** 18

<!--Device-VideoSession-off(type: 'lightStatusChange', callback?: AsyncCallback<LightStatus>): void--><!--Device-VideoSession-off(type: 'lightStatusChange', callback?: AsyncCallback<LightStatus>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'lightStatusChange' | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;LightStatus&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

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

## offApertureInfoChange

```TypeScript
offApertureInfoChange(callback?: Callback<ApertureInfo>): void
```

Unsubscribes from aperture info event callback.

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-VideoSession-offApertureInfoChange(callback?: Callback<ApertureInfo>): void--><!--Device-VideoSession-offApertureInfoChange(callback?: Callback<ApertureInfo>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;ApertureInfo&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## on('lcdFlashStatus')

```TypeScript
on(type: 'lcdFlashStatus', callback: AsyncCallback<LcdFlashStatus>): void
```

Subscribes to LCD flash status change events. This API uses an asynchronous callback to return the result.

**起始版本：** 13

<!--Device-VideoSession-on(type: 'lcdFlashStatus', callback: AsyncCallback<LcdFlashStatus>): void--><!--Device-VideoSession-on(type: 'lcdFlashStatus', callback: AsyncCallback<LcdFlashStatus>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'lcdFlashStatus' | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;LcdFlashStatus&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

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

## on('focusTrackingInfoAvailable')

```TypeScript
on(type: 'focusTrackingInfoAvailable', callback: Callback<FocusTrackingInfo>): void
```

Subscribes to focus tracking information events. This API uses an asynchronous callback to return the result.

**起始版本：** 15

<!--Device-VideoSession-on(type: 'focusTrackingInfoAvailable', callback: Callback<FocusTrackingInfo>): void--><!--Device-VideoSession-on(type: 'focusTrackingInfoAvailable', callback: Callback<FocusTrackingInfo>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'focusTrackingInfoAvailable' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;FocusTrackingInfo&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

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

## on('effectSuggestionChange')

```TypeScript
on(type: 'effectSuggestionChange', callback: AsyncCallback<EffectSuggestionType>): void
```

Subscribes to effect suggestion change events.

**起始版本：** 18

<!--Device-VideoSession-on(type: 'effectSuggestionChange', callback: AsyncCallback<EffectSuggestionType>): void--><!--Device-VideoSession-on(type: 'effectSuggestionChange', callback: AsyncCallback<EffectSuggestionType>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'effectSuggestionChange' | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;EffectSuggestionType&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## on('lightStatusChange')

```TypeScript
on(type: 'lightStatusChange', callback: AsyncCallback<LightStatus>): void
```

Subscribes to camera light status changes. This API uses an asynchronous callback to return the result.

**起始版本：** 18

<!--Device-VideoSession-on(type: 'lightStatusChange', callback: AsyncCallback<LightStatus>): void--><!--Device-VideoSession-on(type: 'lightStatusChange', callback: AsyncCallback<LightStatus>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'lightStatusChange' | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;LightStatus&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

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

## onApertureInfoChange

```TypeScript
onApertureInfoChange(callback: Callback<ApertureInfo>): void
```

Subscribes aperture info event callback.

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-VideoSession-onApertureInfoChange(callback: Callback<ApertureInfo>): void--><!--Device-VideoSession-onApertureInfoChange(callback: Callback<ApertureInfo>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;ApertureInfo&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
