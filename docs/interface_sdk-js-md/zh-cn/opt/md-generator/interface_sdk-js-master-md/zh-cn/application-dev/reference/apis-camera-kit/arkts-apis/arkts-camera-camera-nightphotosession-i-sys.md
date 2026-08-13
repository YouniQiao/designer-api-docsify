# NightPhotoSession（系统接口）

NightPhotoSession extends Session, Flash, AutoExposure, Focus, Zoom, ColorEffect, ColorManagement, ManualExposure Implements a night photo session, which sets the parameters of the night photo mode and saves all [CameraInput](arkts-camera-camera-camerainput-i.md#CameraInput), [CameraOutput](arkts-camera-camera-cameraoutput-i.md#CameraOutput), and [PhotoOutput](arkts-camera-camera-photooutput-i.md#PhotoOutput) instances required to run the camera. It inherits from [Session](arkts-camera-camera-session-i.md#Session). For night photo capture scenarios, you must listen for the [onCaptureEnd](arkts-camera-camera-photooutput-i.md#on_photoAvailable) event to mark the end of the photo capture session.

**继承/实现关系：** NightPhotoSession extends [Session](arkts-camera-camera-session-i.md#Session), [Flash](arkts-camera-camera-flash-i.md#Flash), [AutoExposure](arkts-camera-camera-autoexposure-i.md#AutoExposure), [Focus](arkts-camera-camera-focus-i.md#Focus), [Zoom](arkts-camera-camera-zoom-i.md#Zoom), [ColorEffect](arkts-camera-camera-coloreffect-i-sys.md#ColorEffect（系统接口）), [Beauty](arkts-camera-camera-beauty-i-sys.md#Beauty（系统接口）), [ColorManagement](arkts-camera-camera-colormanagement-i.md#ColorManagement), [ManualExposure](arkts-camera-camera-manualexposure-i.md#ManualExposure（系统接口）)

**起始版本：** 23

**废弃版本：** -1

<!--Device-camera-interface NightPhotoSession--><!--Device-camera-interface NightPhotoSession-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

## offError

```TypeScript
offError(callback?: ErrorCallback): void
```

Unsubscribes from error events.

**起始版本：** 23

**废弃版本：** -1

<!--Device-NightPhotoSession-offError(callback?: ErrorCallback): void--><!--Device-NightPhotoSession-offError(callback?: ErrorCallback): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | 否 |

## offFocusStateChange

```TypeScript
offFocusStateChange(callback?: AsyncCallback<FocusState>): void
```

Unsubscribes from focus state change event callback.

**起始版本：** 23

**废弃版本：** -1

<!--Device-NightPhotoSession-offFocusStateChange(callback?: AsyncCallback<FocusState>): void--><!--Device-NightPhotoSession-offFocusStateChange(callback?: AsyncCallback<FocusState>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[FocusState](arkts-camera-camera-focusstate-e.md)&gt; | 否 |

## offLcdFlashStatus

```TypeScript
offLcdFlashStatus(callback?: AsyncCallback<LcdFlashStatus>): void
```

Unsubscribes from lcd flash status.

**起始版本：** 23

**废弃版本：** -1

<!--Device-NightPhotoSession-offLcdFlashStatus(callback?: AsyncCallback<LcdFlashStatus>): void--><!--Device-NightPhotoSession-offLcdFlashStatus(callback?: AsyncCallback<LcdFlashStatus>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[LcdFlashStatus](arkts-camera-camera-lcdflashstatus-i-sys.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## offSmoothZoomInfoAvailable

```TypeScript
offSmoothZoomInfoAvailable(callback?: AsyncCallback<SmoothZoomInfo>): void
```

Unsubscribes from zoom info event callback.

**起始版本：** 23

**废弃版本：** -1

<!--Device-NightPhotoSession-offSmoothZoomInfoAvailable(callback?: AsyncCallback<SmoothZoomInfo>): void--><!--Device-NightPhotoSession-offSmoothZoomInfoAvailable(callback?: AsyncCallback<SmoothZoomInfo>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[SmoothZoomInfo](arkts-camera-camera-smoothzoominfo-i.md)&gt; | 否 |

## off_error

```TypeScript
off(type: 'error', callback?: ErrorCallback): void
```

Unsubscribes from PortraitSession error events.

**起始版本：** 11

**废弃版本：** -1

<!--Device-NightPhotoSession-off(type: 'error', callback?: ErrorCallback): void--><!--Device-NightPhotoSession-off(type: 'error', callback?: ErrorCallback): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'error' | 是 |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | 否 |

## 示例

```TypeScript
function unregisterSessionError(nightPhotoSession: camera.NightPhotoSession): void {
  nightPhotoSession.off('error');
}
```

## off_focusStateChange

```TypeScript
off(type: 'focusStateChange', callback?: AsyncCallback<FocusState>): void
```

Unsubscribes from focus state change events.

**起始版本：** 11

**废弃版本：** -1

<!--Device-NightPhotoSession-off(type: 'focusStateChange', callback?: AsyncCallback<FocusState>): void--><!--Device-NightPhotoSession-off(type: 'focusStateChange', callback?: AsyncCallback<FocusState>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'focusStateChange' | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[FocusState](arkts-camera-camera-focusstate-e.md)&gt; | 否 |

## 示例

```TypeScript
function unregisterFocusStateChange(nightPhotoSession: camera.NightPhotoSession): void {
  nightPhotoSession.off('focusStateChange');
}
```

## off_lcdFlashStatus

```TypeScript
off(type: 'lcdFlashStatus', callback?: AsyncCallback<LcdFlashStatus>): void
```

Unsubscribes from LCD flash status change events.

**起始版本：** 12

**废弃版本：** -1

<!--Device-NightPhotoSession-off(type: 'lcdFlashStatus', callback?: AsyncCallback<LcdFlashStatus>): void--><!--Device-NightPhotoSession-off(type: 'lcdFlashStatus', callback?: AsyncCallback<LcdFlashStatus>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'lcdFlashStatus' | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[LcdFlashStatus](arkts-camera-camera-lcdflashstatus-i-sys.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## off_smoothZoomInfoAvailable

```TypeScript
off(type: 'smoothZoomInfoAvailable', callback?: AsyncCallback<SmoothZoomInfo>): void
```

Unsubscribes from smooth zoom state change events.

**起始版本：** 11

**废弃版本：** -1

<!--Device-NightPhotoSession-off(type: 'smoothZoomInfoAvailable', callback?: AsyncCallback<SmoothZoomInfo>): void--><!--Device-NightPhotoSession-off(type: 'smoothZoomInfoAvailable', callback?: AsyncCallback<SmoothZoomInfo>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'smoothZoomInfoAvailable' | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[SmoothZoomInfo](arkts-camera-camera-smoothzoominfo-i.md)&gt; | 否 |

## 示例

```TypeScript
function unregisterSmoothZoomInfo(nightPhotoSession: camera.NightPhotoSession): void {
  nightPhotoSession.off('smoothZoomInfoAvailable');
}
```

## onError

```TypeScript
onError(callback: ErrorCallback): void
```

Subscribes to error events.

**起始版本：** 23

**废弃版本：** -1

<!--Device-NightPhotoSession-onError(callback: ErrorCallback): void--><!--Device-NightPhotoSession-onError(callback: ErrorCallback): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | 是 |

## onFocusStateChange

```TypeScript
onFocusStateChange(callback: AsyncCallback<FocusState>): void
```

Subscribes focus state change event callback.

**起始版本：** 23

**废弃版本：** -1

<!--Device-NightPhotoSession-onFocusStateChange(callback: AsyncCallback<FocusState>): void--><!--Device-NightPhotoSession-onFocusStateChange(callback: AsyncCallback<FocusState>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[FocusState](arkts-camera-camera-focusstate-e.md)&gt; | 是 |

## onLcdFlashStatus

```TypeScript
onLcdFlashStatus(callback: AsyncCallback<LcdFlashStatus>): void
```

Subscribes to lcd flash status.

**起始版本：** 23

**废弃版本：** -1

<!--Device-NightPhotoSession-onLcdFlashStatus(callback: AsyncCallback<LcdFlashStatus>): void--><!--Device-NightPhotoSession-onLcdFlashStatus(callback: AsyncCallback<LcdFlashStatus>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[LcdFlashStatus](arkts-camera-camera-lcdflashstatus-i-sys.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## onSmoothZoomInfoAvailable

```TypeScript
onSmoothZoomInfoAvailable(callback: AsyncCallback<SmoothZoomInfo>): void
```

Subscribes zoom info event callback.

**起始版本：** 23

**废弃版本：** -1

<!--Device-NightPhotoSession-onSmoothZoomInfoAvailable(callback: AsyncCallback<SmoothZoomInfo>): void--><!--Device-NightPhotoSession-onSmoothZoomInfoAvailable(callback: AsyncCallback<SmoothZoomInfo>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[SmoothZoomInfo](arkts-camera-camera-smoothzoominfo-i.md)&gt; | 是 |

## on_error

```TypeScript
on(type: 'error', callback: ErrorCallback): void
```

Subscribes to PortraitSession error events. This API uses an asynchronous callback to return the result.

**起始版本：** 11

**废弃版本：** -1

<!--Device-NightPhotoSession-on(type: 'error', callback: ErrorCallback): void--><!--Device-NightPhotoSession-on(type: 'error', callback: ErrorCallback): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'error' | 是 |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | 是 |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function callback(err: BusinessError): void {
  console.error(`Night photo session error code: ${err.code}`);
}

function registerSessionError(nightPhotoSession: camera.NightPhotoSession): void {
  nightPhotoSession.on('error', callback);
}
```

## on_focusStateChange

```TypeScript
on(type: 'focusStateChange', callback: AsyncCallback<FocusState>): void
```

Subscribes to focus state change events. This API uses an asynchronous callback to return the result.

**起始版本：** 11

**废弃版本：** -1

<!--Device-NightPhotoSession-on(type: 'focusStateChange', callback: AsyncCallback<FocusState>): void--><!--Device-NightPhotoSession-on(type: 'focusStateChange', callback: AsyncCallback<FocusState>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'focusStateChange' | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[FocusState](arkts-camera-camera-focusstate-e.md)&gt; | 是 |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function callback(err: BusinessError, focusState: camera.FocusState): void {
  if (err !== undefined && err.code !== 0) {
    console.error(`Callback Error, errorCode: ${err.code}`);
    return;
  }
  console.info(`Focus state: ${focusState}`);
}

function registerFocusStateChange(nightPhotoSession: camera.NightPhotoSession): void {
  nightPhotoSession.on('focusStateChange', callback);
}
```

## on_lcdFlashStatus

```TypeScript
on(type: 'lcdFlashStatus', callback: AsyncCallback<LcdFlashStatus>): void
```

Subscribes to LCD flash status change events. This API uses an asynchronous callback to return the result.

**起始版本：** 12

**废弃版本：** -1

<!--Device-NightPhotoSession-on(type: 'lcdFlashStatus', callback: AsyncCallback<LcdFlashStatus>): void--><!--Device-NightPhotoSession-on(type: 'lcdFlashStatus', callback: AsyncCallback<LcdFlashStatus>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'lcdFlashStatus' | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[LcdFlashStatus](arkts-camera-camera-lcdflashstatus-i-sys.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## on_smoothZoomInfoAvailable

```TypeScript
on(type: 'smoothZoomInfoAvailable', callback: AsyncCallback<SmoothZoomInfo>): void
```

Subscribes to smooth zoom state change events. This API uses an asynchronous callback to return the result.

**起始版本：** 11

**废弃版本：** -1

<!--Device-NightPhotoSession-on(type: 'smoothZoomInfoAvailable', callback: AsyncCallback<SmoothZoomInfo>): void--><!--Device-NightPhotoSession-on(type: 'smoothZoomInfoAvailable', callback: AsyncCallback<SmoothZoomInfo>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'smoothZoomInfoAvailable' | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[SmoothZoomInfo](arkts-camera-camera-smoothzoominfo-i.md)&gt; | 是 |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function callback(err: BusinessError, smoothZoomInfo: camera.SmoothZoomInfo): void {
  if (err !== undefined && err.code !== 0) {
    console.error(`Callback Error, errorCode: ${err.code}`);
    return;
  }
  console.info(`The duration of smooth zoom: ${smoothZoomInfo.duration}`);
}

function registerSmoothZoomInfo(nightPhotoSession: camera.NightPhotoSession): void {
  nightPhotoSession.on('smoothZoomInfoAvailable', callback);
}
```
