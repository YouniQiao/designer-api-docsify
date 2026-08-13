# PhotoSession

PhotoSession继承自[Session](arkts-camera-camera-session-i.md#Session)、[Flash](arkts-camera-camera-flash-i.md#Flash)、 [AutoExposure](arkts-camera-camera-autoexposure-i.md#AutoExposure)、[WhiteBalance](arkts-camera-camera-whitebalance-i.md#WhiteBalance（系统接口）)、[Focus](arkts-camera-camera-focus-i.md#Focus)、 [Zoom](arkts-camera-camera-zoom-i.md#Zoom)、[ColorManagement](arkts-camera-camera-colormanagement-i.md#ColorManagement)、 [AutoDeviceSwitch](arkts-camera-camera-autodeviceswitch-i.md#AutoDeviceSwitch)、[Macro](arkts-camera-camera-macro-i-sys.md#Macro（系统接口）)、 [ManualExposure](../../../reference/apis-camera-kit/arkts-apis-camera-ManualExposure.md)、 [ManualFocus](../../../reference/apis-camera-kit/arkts-apis-camera-ManualFocus.md)、 [ManualIso](../../../reference/apis-camera-kit/arkts-apis-camera-ManualIso.md)、 [OIS](../../../reference/apis-camera-kit/arkts-apis-camera-OIS.md)、 [Aperture](../../../reference/apis-camera-kit/arkts-apis-camera-Aperture.md)。 普通拍照模式会话类，提供了对闪光灯、曝光、白平衡、对焦、变焦、色彩空间、微距、手动曝光、手动对焦、手动ISO、光学防抖及光圈的操作。 默认的拍照模式，用于拍摄标准照片。支持多种照片格式和分辨率，适合大多数日常拍摄场景。

**继承/实现关系：** PhotoSession extends [Session](arkts-camera-camera-session-i.md#Session), [Flash](arkts-camera-camera-flash-i.md#Flash), [AutoExposure](arkts-camera-camera-autoexposure-i.md#AutoExposure), [WhiteBalance](arkts-camera-camera-whitebalance-i.md#WhiteBalance（系统接口）), [Focus](arkts-camera-camera-focus-i.md#Focus), [Zoom](arkts-camera-camera-zoom-i.md#Zoom), [ColorManagement](arkts-camera-camera-colormanagement-i.md#ColorManagement), [AutoDeviceSwitch](arkts-camera-camera-autodeviceswitch-i.md#AutoDeviceSwitch), [Macro](arkts-camera-camera-macro-i-sys.md#Macro（系统接口）), [ManualExposure](arkts-camera-camera-manualexposure-i.md#ManualExposure（系统接口）), [ManualFocus](arkts-camera-camera-manualfocus-i-sys.md#ManualFocus（系统接口）), [ManualIso](arkts-camera-camera-manualiso-i-sys.md#ManualIso（系统接口）), [OIS](arkts-camera-camera-ois-i.md#OIS), [Aperture](arkts-camera-camera-aperture-i-sys.md#Aperture（系统接口）)

**起始版本：** 23

**废弃版本：** -1

<!--Device-camera-interface PhotoSession--><!--Device-camera-interface PhotoSession-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

## getSessionConflictFunctions

```TypeScript
getSessionConflictFunctions(): Array<PhotoConflictFunctions>
```

Gets session conflict functions.

**起始版本：** 23

**废弃版本：** -1

<!--Device-PhotoSession-getSessionConflictFunctions(): Array<PhotoConflictFunctions>--><!--Device-PhotoSession-getSessionConflictFunctions(): Array<PhotoConflictFunctions>-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Array&lt;[PhotoConflictFunctions](arkts-camera-camera-photoconflictfunctions-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## getSessionFunctions

```TypeScript
getSessionFunctions(outputCapability: CameraOutputCapability): Array<PhotoFunctions>
```

Gets session functions.

**起始版本：** 23

**废弃版本：** -1

<!--Device-PhotoSession-getSessionFunctions(outputCapability: CameraOutputCapability): Array<PhotoFunctions>--><!--Device-PhotoSession-getSessionFunctions(outputCapability: CameraOutputCapability): Array<PhotoFunctions>-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| outputCapability | [CameraOutputCapability](arkts-camera-camera-cameraoutputcapability-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Array&lt;[PhotoFunctions](arkts-camera-camera-photofunctions-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## offEffectSuggestionChange

```TypeScript
offEffectSuggestionChange(callback?: AsyncCallback<EffectSuggestionType>): void
```

Unsubscribes from effect suggestion event callback.

**起始版本：** 23

**废弃版本：** -1

<!--Device-PhotoSession-offEffectSuggestionChange(callback?: AsyncCallback<EffectSuggestionType>): void--><!--Device-PhotoSession-offEffectSuggestionChange(callback?: AsyncCallback<EffectSuggestionType>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[EffectSuggestionType](arkts-camera-camera-effectsuggestiontype-e-sys.md)&gt; | 否 |

## offFeatureDetection

```TypeScript
offFeatureDetection(featureType: SceneFeatureType, callback?: AsyncCallback<SceneFeatureDetectionResult>): void
```

Unsubscribes from feature detection result.

**起始版本：** 23

**废弃版本：** -1

<!--Device-PhotoSession-offFeatureDetection(featureType: SceneFeatureType, callback?: AsyncCallback<SceneFeatureDetectionResult>): void--><!--Device-PhotoSession-offFeatureDetection(featureType: SceneFeatureType, callback?: AsyncCallback<SceneFeatureDetectionResult>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [featureType](arkts-camera-camera-scenefeaturedetectionresult-i-sys.md) | [SceneFeatureType](arkts-camera-camera-scenefeaturetype-e-sys.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[SceneFeatureDetectionResult](arkts-camera-camera-scenefeaturedetectionresult-i-sys.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## offLcdFlashStatus

```TypeScript
offLcdFlashStatus(callback?: AsyncCallback<LcdFlashStatus>): void
```

Unsubscribes from lcd flash status.

**起始版本：** 23

**废弃版本：** -1

<!--Device-PhotoSession-offLcdFlashStatus(callback?: AsyncCallback<LcdFlashStatus>): void--><!--Device-PhotoSession-offLcdFlashStatus(callback?: AsyncCallback<LcdFlashStatus>): void-End-->

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

## off_effectSuggestionChange

```TypeScript
off(type: 'effectSuggestionChange', callback?: AsyncCallback<EffectSuggestionType>): void
```

Unsubscribes from effect suggestion event callback.

**起始版本：** 12

**废弃版本：** -1

<!--Device-PhotoSession-off(type: 'effectSuggestionChange', callback?: AsyncCallback<EffectSuggestionType>): void--><!--Device-PhotoSession-off(type: 'effectSuggestionChange', callback?: AsyncCallback<EffectSuggestionType>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'effectSuggestionChange' | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[EffectSuggestionType](arkts-camera-camera-effectsuggestiontype-e-sys.md)&gt; | 否 |

## off_featureDetection

```TypeScript
off(type: 'featureDetection', featureType: SceneFeatureType, callback?: AsyncCallback<SceneFeatureDetectionResult>): void
```

Unsubscribe from camera feature detection status change events.

**起始版本：** 12

**废弃版本：** -1

<!--Device-PhotoSession-off(type: 'featureDetection', featureType: SceneFeatureType, callback?: AsyncCallback<SceneFeatureDetectionResult>): void--><!--Device-PhotoSession-off(type: 'featureDetection', featureType: SceneFeatureType, callback?: AsyncCallback<SceneFeatureDetectionResult>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'featureDetection' | 是 |
| [featureType](arkts-camera-camera-scenefeaturedetectionresult-i-sys.md) | [SceneFeatureType](arkts-camera-camera-scenefeaturetype-e-sys.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[SceneFeatureDetectionResult](arkts-camera-camera-scenefeaturedetectionresult-i-sys.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
function unregisterFeatureDetectionStatus(photoSession: camera.PhotoSession, featureType: camera.SceneFeatureType): void {
  photoSession.off('featureDetection', featureType);
}
```

## off_lcdFlashStatus

```TypeScript
off(type: 'lcdFlashStatus', callback?: AsyncCallback<LcdFlashStatus>): void
```

Unsubscribes from LCD flash status change events.

**起始版本：** 13

**废弃版本：** -1

<!--Device-PhotoSession-off(type: 'lcdFlashStatus', callback?: AsyncCallback<LcdFlashStatus>): void--><!--Device-PhotoSession-off(type: 'lcdFlashStatus', callback?: AsyncCallback<LcdFlashStatus>): void-End-->

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

## 示例

```TypeScript
function unregisterLcdFlashStatus(photoSession: camera.PhotoSession): void {
  photoSession.off('lcdFlashStatus');
}
```

## off_macroStatusChanged

```TypeScript
off(type: 'macroStatusChanged', callback?: AsyncCallback<boolean>): void
```

注销相机微距状态变化的监听。

**起始版本：** 11

**废弃版本：** -1

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-PhotoSession-off(type: 'macroStatusChanged', callback?: AsyncCallback<boolean>): void--><!--Device-PhotoSession-off(type: 'macroStatusChanged', callback?: AsyncCallback<boolean>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'macroStatusChanged' | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## onEffectSuggestionChange

```TypeScript
onEffectSuggestionChange(callback: AsyncCallback<EffectSuggestionType>): void
```

Subscribes to effect suggestion event callback.

**起始版本：** 23

**废弃版本：** -1

<!--Device-PhotoSession-onEffectSuggestionChange(callback: AsyncCallback<EffectSuggestionType>): void--><!--Device-PhotoSession-onEffectSuggestionChange(callback: AsyncCallback<EffectSuggestionType>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[EffectSuggestionType](arkts-camera-camera-effectsuggestiontype-e-sys.md)&gt; | 是 |

## onFeatureDetection

```TypeScript
onFeatureDetection(featureType: SceneFeatureType, callback: AsyncCallback<SceneFeatureDetectionResult>): void
```

Subscribes to feature detection results.

**起始版本：** 23

**废弃版本：** -1

<!--Device-PhotoSession-onFeatureDetection(featureType: SceneFeatureType, callback: AsyncCallback<SceneFeatureDetectionResult>): void--><!--Device-PhotoSession-onFeatureDetection(featureType: SceneFeatureType, callback: AsyncCallback<SceneFeatureDetectionResult>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [featureType](arkts-camera-camera-scenefeaturedetectionresult-i-sys.md) | [SceneFeatureType](arkts-camera-camera-scenefeaturetype-e-sys.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[SceneFeatureDetectionResult](arkts-camera-camera-scenefeaturedetectionresult-i-sys.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## onLcdFlashStatus

```TypeScript
onLcdFlashStatus(callback: AsyncCallback<LcdFlashStatus>): void
```

Subscribes to lcd flash status.

**起始版本：** 23

**废弃版本：** -1

<!--Device-PhotoSession-onLcdFlashStatus(callback: AsyncCallback<LcdFlashStatus>): void--><!--Device-PhotoSession-onLcdFlashStatus(callback: AsyncCallback<LcdFlashStatus>): void-End-->

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

## on_effectSuggestionChange

```TypeScript
on(type: 'effectSuggestionChange', callback: AsyncCallback<EffectSuggestionType>): void
```

Subscribes to effect suggestion event callback.

**起始版本：** 12

**废弃版本：** -1

<!--Device-PhotoSession-on(type: 'effectSuggestionChange', callback: AsyncCallback<EffectSuggestionType>): void--><!--Device-PhotoSession-on(type: 'effectSuggestionChange', callback: AsyncCallback<EffectSuggestionType>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'effectSuggestionChange' | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[EffectSuggestionType](arkts-camera-camera-effectsuggestiontype-e-sys.md)&gt; | 是 |

## on_featureDetection

```TypeScript
on(type: 'featureDetection', featureType: SceneFeatureType, callback: AsyncCallback<SceneFeatureDetectionResult>): void
```

Subscribe to scene feature detection status change events. This API uses an asynchronous callback to return the result.

**起始版本：** 12

**废弃版本：** -1

<!--Device-PhotoSession-on(type: 'featureDetection', featureType: SceneFeatureType, callback: AsyncCallback<SceneFeatureDetectionResult>): void--><!--Device-PhotoSession-on(type: 'featureDetection', featureType: SceneFeatureType, callback: AsyncCallback<SceneFeatureDetectionResult>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'featureDetection' | 是 |
| [featureType](arkts-camera-camera-scenefeaturedetectionresult-i-sys.md) | [SceneFeatureType](arkts-camera-camera-scenefeaturetype-e-sys.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[SceneFeatureDetectionResult](arkts-camera-camera-scenefeaturedetectionresult-i-sys.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function callback(err: BusinessError, result: camera.SceneFeatureDetectionResult): void {
  if (err !== undefined && err.code !== 0) {
    console.error(`Callback Error, errorCode: ${err.code}`);
    return;
  }
  console.info(`feature type: ${result.featureType}`);
  console.info(`feature status: ${result.detected}`);
}

function registerFeatureDetectionStatus(photoSession: camera.PhotoSession, featureType: camera.SceneFeatureType): void {
  photoSession.on('featureDetection', featureType, callback);
}
```

## on_lcdFlashStatus

```TypeScript
on(type: 'lcdFlashStatus', callback: AsyncCallback<LcdFlashStatus>): void
```

Subscribes to LCD flash status change events. This API uses an asynchronous callback to return the result.

**起始版本：** 13

**废弃版本：** -1

<!--Device-PhotoSession-on(type: 'lcdFlashStatus', callback: AsyncCallback<LcdFlashStatus>): void--><!--Device-PhotoSession-on(type: 'lcdFlashStatus', callback: AsyncCallback<LcdFlashStatus>): void-End-->

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

function registerLcdFlashStatus(photoSession: camera.PhotoSession): void {
  photoSession.on('lcdFlashStatus', callback);
}
```

## on_macroStatusChanged

```TypeScript
on(type: 'macroStatusChanged', callback: AsyncCallback<boolean>): void
```

监听相机微距状态变化，通过注册回调函数获取结果。使用callback异步回调。

**起始版本：** 11

**废弃版本：** -1

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-PhotoSession-on(type: 'macroStatusChanged', callback: AsyncCallback<boolean>): void--><!--Device-PhotoSession-on(type: 'macroStatusChanged', callback: AsyncCallback<boolean>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'macroStatusChanged' | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
