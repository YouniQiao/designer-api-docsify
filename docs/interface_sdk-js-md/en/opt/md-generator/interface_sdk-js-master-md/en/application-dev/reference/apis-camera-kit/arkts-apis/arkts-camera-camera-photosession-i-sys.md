# PhotoSession

**PhotoSession** inherits from [Session](arkts-camera-camera-session-i.md#Session), [Flash](arkts-camera-camera-flash-i.md#Flash), [AutoExposure](arkts-camera-camera-autoexposure-i.md#AutoExposure), [WhiteBalance](arkts-camera-camera-whitebalance-i.md#WhiteBalance-(System-API)), [Focus](arkts-camera-camera-focus-i.md#Focus), [Zoom](arkts-camera-camera-zoom-i.md#Zoom), [ColorManagement](arkts-camera-camera-colormanagement-i.md#ColorManagement), [AutoDeviceSwitch](arkts-camera-camera-autodeviceswitch-i.md#AutoDeviceSwitch), [Macro](arkts-camera-camera-macro-i-sys.md#Macro-(System-API)), [ManualExposure](../../../reference/apis-camera-kit/arkts-apis-camera-ManualExposure.md), [ManualFocus](../../../reference/apis-camera-kit/arkts-apis-camera-ManualFocus.md), [ManualIso](../../../reference/apis-camera-kit/arkts-apis-camera-ManualIso.md), [OIS](../../../reference/apis-camera-kit/arkts-apis-camera-OIS.md), and [Aperture](../../../reference/apis-camera-kit/arkts-apis-camera-Aperture.md). It implements a photo session, which provides operations on the flash, exposure, white balance, focus, zoom, color space, macro mode, manual exposure, manual focus, manual ISO setting, optical image stabilization (OIS), and aperture. **PhotoSession** is provided for the default photo mode. It is used to take standard photos. It supports multiple photo formats and resolutions, which are suitable for most daily photo capture scenarios.

**Inheritance/Implementation:** PhotoSession extends [Session](arkts-camera-camera-session-i.md#Session), [Flash](arkts-camera-camera-flash-i.md#Flash), [AutoExposure](arkts-camera-camera-autoexposure-i.md#AutoExposure), [WhiteBalance](arkts-camera-camera-whitebalance-i.md#WhiteBalance-(System-API)), [Focus](arkts-camera-camera-focus-i.md#Focus), [Zoom](arkts-camera-camera-zoom-i.md#Zoom), [ColorManagement](arkts-camera-camera-colormanagement-i.md#ColorManagement), [AutoDeviceSwitch](arkts-camera-camera-autodeviceswitch-i.md#AutoDeviceSwitch), [Macro](arkts-camera-camera-macro-i-sys.md#Macro-(System-API)), [ManualExposure](arkts-camera-camera-manualexposure-i.md#ManualExposure-(System-API)), [ManualFocus](arkts-camera-camera-manualfocus-i-sys.md#ManualFocus-(System-API)), [ManualIso](arkts-camera-camera-manualiso-i-sys.md#ManualIso-(System-API)), [OIS](arkts-camera-camera-ois-i.md#OIS), [Aperture](arkts-camera-camera-aperture-i-sys.md#Aperture-(System-API))

**Since:** 23

**Deprecated since:** -1

<!--Device-camera-interface PhotoSession--><!--Device-camera-interface PhotoSession-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## Modules to Import

```TypeScript
import { camera } from '@kit.CameraKit';
```

## getSessionConflictFunctions

```TypeScript
getSessionConflictFunctions(): Array<PhotoConflictFunctions>
```

Gets session conflict functions.

**Since:** 23

**Deprecated since:** -1

<!--Device-PhotoSession-getSessionConflictFunctions(): Array<PhotoConflictFunctions>--><!--Device-PhotoSession-getSessionConflictFunctions(): Array<PhotoConflictFunctions>-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array&lt;[PhotoConflictFunctions](arkts-camera-camera-photoconflictfunctions-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## getSessionFunctions

```TypeScript
getSessionFunctions(outputCapability: CameraOutputCapability): Array<PhotoFunctions>
```

Gets session functions.

**Since:** 23

**Deprecated since:** -1

<!--Device-PhotoSession-getSessionFunctions(outputCapability: CameraOutputCapability): Array<PhotoFunctions>--><!--Device-PhotoSession-getSessionFunctions(outputCapability: CameraOutputCapability): Array<PhotoFunctions>-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| outputCapability | [CameraOutputCapability](arkts-camera-camera-cameraoutputcapability-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array&lt;[PhotoFunctions](arkts-camera-camera-photofunctions-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## offEffectSuggestionChange

```TypeScript
offEffectSuggestionChange(callback?: AsyncCallback<EffectSuggestionType>): void
```

Unsubscribes from effect suggestion event callback.

**Since:** 23

**Deprecated since:** -1

<!--Device-PhotoSession-offEffectSuggestionChange(callback?: AsyncCallback<EffectSuggestionType>): void--><!--Device-PhotoSession-offEffectSuggestionChange(callback?: AsyncCallback<EffectSuggestionType>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[EffectSuggestionType](arkts-camera-camera-effectsuggestiontype-e-sys.md)&gt; | No |

## offFeatureDetection

```TypeScript
offFeatureDetection(featureType: SceneFeatureType, callback?: AsyncCallback<SceneFeatureDetectionResult>): void
```

Unsubscribes from feature detection result.

**Since:** 23

**Deprecated since:** -1

<!--Device-PhotoSession-offFeatureDetection(featureType: SceneFeatureType, callback?: AsyncCallback<SceneFeatureDetectionResult>): void--><!--Device-PhotoSession-offFeatureDetection(featureType: SceneFeatureType, callback?: AsyncCallback<SceneFeatureDetectionResult>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [featureType](arkts-camera-camera-scenefeaturedetectionresult-i-sys.md) | [SceneFeatureType](arkts-camera-camera-scenefeaturetype-e-sys.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[SceneFeatureDetectionResult](arkts-camera-camera-scenefeaturedetectionresult-i-sys.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## offLcdFlashStatus

```TypeScript
offLcdFlashStatus(callback?: AsyncCallback<LcdFlashStatus>): void
```

Unsubscribes from lcd flash status.

**Since:** 23

**Deprecated since:** -1

<!--Device-PhotoSession-offLcdFlashStatus(callback?: AsyncCallback<LcdFlashStatus>): void--><!--Device-PhotoSession-offLcdFlashStatus(callback?: AsyncCallback<LcdFlashStatus>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[LcdFlashStatus](arkts-camera-camera-lcdflashstatus-i-sys.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## off_effectSuggestionChange

```TypeScript
off(type: 'effectSuggestionChange', callback?: AsyncCallback<EffectSuggestionType>): void
```

Unsubscribes from effect suggestion event callback.

**Since:** 12

**Deprecated since:** -1

<!--Device-PhotoSession-off(type: 'effectSuggestionChange', callback?: AsyncCallback<EffectSuggestionType>): void--><!--Device-PhotoSession-off(type: 'effectSuggestionChange', callback?: AsyncCallback<EffectSuggestionType>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'effectSuggestionChange' | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[EffectSuggestionType](arkts-camera-camera-effectsuggestiontype-e-sys.md)&gt; | No |

## off_featureDetection

```TypeScript
off(type: 'featureDetection', featureType: SceneFeatureType, callback?: AsyncCallback<SceneFeatureDetectionResult>): void
```

Unsubscribe from camera feature detection status change events.

**Since:** 12

**Deprecated since:** -1

<!--Device-PhotoSession-off(type: 'featureDetection', featureType: SceneFeatureType, callback?: AsyncCallback<SceneFeatureDetectionResult>): void--><!--Device-PhotoSession-off(type: 'featureDetection', featureType: SceneFeatureType, callback?: AsyncCallback<SceneFeatureDetectionResult>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'featureDetection' | Yes |
| [featureType](arkts-camera-camera-scenefeaturedetectionresult-i-sys.md) | [SceneFeatureType](arkts-camera-camera-scenefeaturetype-e-sys.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[SceneFeatureDetectionResult](arkts-camera-camera-scenefeaturedetectionresult-i-sys.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

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

**Since:** 13

**Deprecated since:** -1

<!--Device-PhotoSession-off(type: 'lcdFlashStatus', callback?: AsyncCallback<LcdFlashStatus>): void--><!--Device-PhotoSession-off(type: 'lcdFlashStatus', callback?: AsyncCallback<LcdFlashStatus>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'lcdFlashStatus' | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[LcdFlashStatus](arkts-camera-camera-lcdflashstatus-i-sys.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
function unregisterLcdFlashStatus(photoSession: camera.PhotoSession): void {
  photoSession.off('lcdFlashStatus');
}
```

## off_macroStatusChanged

```TypeScript
off(type: 'macroStatusChanged', callback?: AsyncCallback<boolean>): void
```

Unsubscribes from macro state change events.

**Since:** 11

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-PhotoSession-off(type: 'macroStatusChanged', callback?: AsyncCallback<boolean>): void--><!--Device-PhotoSession-off(type: 'macroStatusChanged', callback?: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'macroStatusChanged' | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## onEffectSuggestionChange

```TypeScript
onEffectSuggestionChange(callback: AsyncCallback<EffectSuggestionType>): void
```

Subscribes to effect suggestion event callback.

**Since:** 23

**Deprecated since:** -1

<!--Device-PhotoSession-onEffectSuggestionChange(callback: AsyncCallback<EffectSuggestionType>): void--><!--Device-PhotoSession-onEffectSuggestionChange(callback: AsyncCallback<EffectSuggestionType>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[EffectSuggestionType](arkts-camera-camera-effectsuggestiontype-e-sys.md)&gt; | Yes |

## onFeatureDetection

```TypeScript
onFeatureDetection(featureType: SceneFeatureType, callback: AsyncCallback<SceneFeatureDetectionResult>): void
```

Subscribes to feature detection results.

**Since:** 23

**Deprecated since:** -1

<!--Device-PhotoSession-onFeatureDetection(featureType: SceneFeatureType, callback: AsyncCallback<SceneFeatureDetectionResult>): void--><!--Device-PhotoSession-onFeatureDetection(featureType: SceneFeatureType, callback: AsyncCallback<SceneFeatureDetectionResult>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [featureType](arkts-camera-camera-scenefeaturedetectionresult-i-sys.md) | [SceneFeatureType](arkts-camera-camera-scenefeaturetype-e-sys.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[SceneFeatureDetectionResult](arkts-camera-camera-scenefeaturedetectionresult-i-sys.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## onLcdFlashStatus

```TypeScript
onLcdFlashStatus(callback: AsyncCallback<LcdFlashStatus>): void
```

Subscribes to lcd flash status.

**Since:** 23

**Deprecated since:** -1

<!--Device-PhotoSession-onLcdFlashStatus(callback: AsyncCallback<LcdFlashStatus>): void--><!--Device-PhotoSession-onLcdFlashStatus(callback: AsyncCallback<LcdFlashStatus>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[LcdFlashStatus](arkts-camera-camera-lcdflashstatus-i-sys.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## on_effectSuggestionChange

```TypeScript
on(type: 'effectSuggestionChange', callback: AsyncCallback<EffectSuggestionType>): void
```

Subscribes to effect suggestion event callback.

**Since:** 12

**Deprecated since:** -1

<!--Device-PhotoSession-on(type: 'effectSuggestionChange', callback: AsyncCallback<EffectSuggestionType>): void--><!--Device-PhotoSession-on(type: 'effectSuggestionChange', callback: AsyncCallback<EffectSuggestionType>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'effectSuggestionChange' | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[EffectSuggestionType](arkts-camera-camera-effectsuggestiontype-e-sys.md)&gt; | Yes |

## on_featureDetection

```TypeScript
on(type: 'featureDetection', featureType: SceneFeatureType, callback: AsyncCallback<SceneFeatureDetectionResult>): void
```

Subscribe to scene feature detection status change events. This API uses an asynchronous callback to return the result.

**Since:** 12

**Deprecated since:** -1

<!--Device-PhotoSession-on(type: 'featureDetection', featureType: SceneFeatureType, callback: AsyncCallback<SceneFeatureDetectionResult>): void--><!--Device-PhotoSession-on(type: 'featureDetection', featureType: SceneFeatureType, callback: AsyncCallback<SceneFeatureDetectionResult>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'featureDetection' | Yes |
| [featureType](arkts-camera-camera-scenefeaturedetectionresult-i-sys.md) | [SceneFeatureType](arkts-camera-camera-scenefeaturetype-e-sys.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[SceneFeatureDetectionResult](arkts-camera-camera-scenefeaturedetectionresult-i-sys.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

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

**Since:** 13

**Deprecated since:** -1

<!--Device-PhotoSession-on(type: 'lcdFlashStatus', callback: AsyncCallback<LcdFlashStatus>): void--><!--Device-PhotoSession-on(type: 'lcdFlashStatus', callback: AsyncCallback<LcdFlashStatus>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'lcdFlashStatus' | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[LcdFlashStatus](arkts-camera-camera-lcdflashstatus-i-sys.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

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

Subscribes to macro state change events. This API uses an asynchronous callback to return the result.

**Since:** 11

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-PhotoSession-on(type: 'macroStatusChanged', callback: AsyncCallback<boolean>): void--><!--Device-PhotoSession-on(type: 'macroStatusChanged', callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'macroStatusChanged' | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
