# PhotoOutput

PhotoOutput implements output information used in a photo session. It inherits from [CameraOutput](arkts-camera-camera-cameraoutput-i.md#CameraOutput).

**Inheritance/Implementation:** PhotoOutput extends [CameraOutput](arkts-camera-camera-cameraoutput-i.md#CameraOutput)

**Since:** 23

**Deprecated since:** -1

<!--Device-camera-interface PhotoOutput--><!--Device-camera-interface PhotoOutput-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## Modules to Import

```TypeScript
import { camera } from '@kit.CameraKit';
```

## burstCapture

```TypeScript
burstCapture(setting: PhotoCaptureSetting): Promise<void>
```

Starts the burst mode, in which users can capture a series of photos in quick succession. This API is generally used in photo mode. After the burst mode starts, the bottom layer continues displaying photos. You can call [confirmCapture](#confirmCapture) to cancel the burst mode. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

<!--Device-PhotoOutput-burstCapture(setting: PhotoCaptureSetting): Promise<void>--><!--Device-PhotoOutput-burstCapture(setting: PhotoCaptureSetting): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| setting | [PhotoCaptureSetting](arkts-camera-camera-photocapturesetting-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [7400101](../errorcode-camera.md#7400101-invalid-parameter) |
| [7400104](../errorcode-camera.md#7400104-session-not-running) |
| [7400201](../errorcode-camera.md#7400201-camera-service-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function burstCapture(photoOutput: camera.PhotoOutput): void {
  let captureLocation: camera.Location = {
    latitude: 0,
    longitude: 0,
    altitude: 0
  }
  let settings: camera.PhotoCaptureSetting = {
    quality: camera.QualityLevel.QUALITY_LEVEL_LOW,
    rotation: camera.ImageRotation.ROTATION_0,
    location: captureLocation,
    mirror: false
  }
  photoOutput.burstCapture(settings).then(() => {
    console.info('Promise returned to indicate that photo burstCapture request success.');
  }).catch((error: BusinessError) => {
    console.error(`Failed to photo output burstCapture, error code: ${error.code}.`);
  });
}
```

## confirmCapture

```TypeScript
confirmCapture(): void
```

Confirms photo capture. This API is generally used in night photo mode when users need to stop the exposure countdown and take a photo in advance. This API is used to end the burst mode, which is started by calling [burstCapture](#burstCapture).

**Since:** 23

**Deprecated since:** -1

<!--Device-PhotoOutput-confirmCapture(): void--><!--Device-PhotoOutput-confirmCapture(): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Error codes:**

| Error Code ID |
| --- |
| [7400104](../errorcode-camera.md#7400104-session-not-running) |
| [7400201](../errorcode-camera.md#7400201-camera-service-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function confirmCapture(photoOutput: camera.PhotoOutput): void {
  try {
    photoOutput.confirmCapture();
  } catch (error) {
    let err = error as BusinessError;
    console.error(`The confirmCapture call failed. error code: ${err.code}`);
  }
}
```

## deferImageDelivery

```TypeScript
deferImageDelivery(type: DeferredDeliveryImageType): void
```

Enables deferred delivery of a certain type.

**Since:** 23

**Deprecated since:** -1

<!--Device-PhotoOutput-deferImageDelivery(type: DeferredDeliveryImageType): void--><!--Device-PhotoOutput-deferImageDelivery(type: DeferredDeliveryImageType): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | [DeferredDeliveryImageType](arkts-camera-camera-deferreddeliveryimagetype-e-sys.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [7400101](../errorcode-camera.md#7400101-invalid-parameter) |
| [7400104](../errorcode-camera.md#7400104-session-not-running) |
| [7400201](../errorcode-camera.md#7400201-camera-service-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
function deferImageDelivery(photoOutput: camera.PhotoOutput, type: camera.DeferredDeliveryImageType): void {
  photoOutput.deferImageDelivery(type);
}
```

## enableAutoCloudImageEnhancement

```TypeScript
enableAutoCloudImageEnhancement(enabled: boolean): void
```

Enable auto cloud image enhancement

**Since:** 23

**Deprecated since:** -1

<!--Device-PhotoOutput-enableAutoCloudImageEnhancement(enabled: boolean): void--><!--Device-PhotoOutput-enableAutoCloudImageEnhancement(enabled: boolean): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enabled | boolean | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [7400101](../errorcode-camera.md#7400101-invalid-parameter) |
| [7400201](../errorcode-camera.md#7400201-camera-service-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## enableAutoHighQualityPhoto

```TypeScript
enableAutoHighQualityPhoto(enabled: boolean): void
```

Enables automatic high quality for photos. Before using this API, call [isAutoHighQualityPhotoSupported](#isAutoHighQualityPhotoSupported) to check whether automatic high quality is supported.

**Since:** 23

**Deprecated since:** -1

<!--Device-PhotoOutput-enableAutoHighQualityPhoto(enabled: boolean): void--><!--Device-PhotoOutput-enableAutoHighQualityPhoto(enabled: boolean): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enabled | boolean | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [7400101](../errorcode-camera.md#7400101-invalid-parameter) |
| [7400104](../errorcode-camera.md#7400104-session-not-running) |
| [7400201](../errorcode-camera.md#7400201-camera-service-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function enableAutoHighQualityPhoto(photoOutput: camera.PhotoOutput): void {
  return photoOutput.enableAutoHighQualityPhoto(true);
}
```

## enableDepthDataDelivery

```TypeScript
enableDepthDataDelivery(enabled: boolean): void
```

Enable depth data delivery.

**Since:** 23

**Deprecated since:** -1

<!--Device-PhotoOutput-enableDepthDataDelivery(enabled: boolean): void--><!--Device-PhotoOutput-enableDepthDataDelivery(enabled: boolean): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enabled | boolean | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [7400101](../errorcode-camera.md#7400101-invalid-parameter) |
| [7400104](../errorcode-camera.md#7400104-session-not-running) |
| [7400201](../errorcode-camera.md#7400201-camera-service-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## enableOffline

```TypeScript
enableOffline(): void
```

Enable offline processing.

**Since:** 23

**Deprecated since:** -1

<!--Device-PhotoOutput-enableOffline(): void--><!--Device-PhotoOutput-enableOffline(): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Error codes:**

| Error Code ID |
| --- |
| [7400104](../errorcode-camera.md#7400104-session-not-running) |
| [7400201](../errorcode-camera.md#7400201-camera-service-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## enableOriginalImageGeneration

```TypeScript
enableOriginalImageGeneration(enabled: boolean): void
```

Enable original image generation.

**Since:** 24

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-PhotoOutput-enableOriginalImageGeneration(enabled: boolean): void--><!--Device-PhotoOutput-enableOriginalImageGeneration(enabled: boolean): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enabled | boolean | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [7400201](../errorcode-camera.md#7400201-camera-service-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## enableQuickThumbnail

```TypeScript
enableQuickThumbnail(enabled: boolean): void
```

Enables or disables the quick thumbnail feature. This API takes effect after [addOutput](arkts-camera-camera-session-i.md#addOutput) and [addInput](arkts-camera-camera-session-i.md#addInput) and before [commitConfig](arkts-camera-camera-session-i.md#commitConfig).

**Since:** 23

**Deprecated since:** -1

<!--Device-PhotoOutput-enableQuickThumbnail(enabled: boolean): void--><!--Device-PhotoOutput-enableQuickThumbnail(enabled: boolean): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enabled | boolean | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [7400101](../errorcode-camera.md#7400101-invalid-parameter) |
| [7400104](../errorcode-camera.md#7400104-session-not-running) |
| [7400201](../errorcode-camera.md#7400201-camera-service-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { camera } from '@kit.CameraKit';

async function enableQuickThumbnail(context: common.BaseContext, mode: camera.SceneMode, photoProfile: camera.Profile): Promise<void> {
  let cameraManager: camera.CameraManager = camera.getCameraManager(context);
  let cameras: Array<camera.CameraDevice> = cameraManager.getSupportedCameras();
  // Create a CaptureSession instance.
  let session: camera.Session = cameraManager.createSession(mode);
  // Start configuration for the session.
  session.beginConfig();
  // Add a CameraInput instance to the session.
  let cameraInput: camera.CameraInput = cameraManager.createCameraInput(cameras[0]);
  await cameraInput.open();
  session.addInput(cameraInput);
  // Add a PhotoOutput instance to the session.
  let photoOutput: camera.PhotoOutput = cameraManager.createPhotoOutput(photoProfile);
  session.addOutput(photoOutput);
  let isSupported: boolean = photoOutput.isQuickThumbnailSupported();
  if (!isSupported) {
    console.info('Quick Thumbnail is not supported to be turned on.');
    return;
  }
  try {
    photoOutput.enableQuickThumbnail(true);
  } catch (error) {
    let err = error as BusinessError;
    console.error(`The enableQuickThumbnail call failed. error code: ${err.code}`);
  }
}
```

## enableRawDelivery

```TypeScript
enableRawDelivery(enabled: boolean): void
```

Enable raw image image delivery.

**Since:** 23

**Deprecated since:** -1

<!--Device-PhotoOutput-enableRawDelivery(enabled: boolean): void--><!--Device-PhotoOutput-enableRawDelivery(enabled: boolean): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enabled | boolean | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [7400101](../errorcode-camera.md#7400101-invalid-parameter) |
| [7400104](../errorcode-camera.md#7400104-session-not-running) |
| [7400201](../errorcode-camera.md#7400201-camera-service-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## isAutoCloudImageEnhancementSupported

```TypeScript
isAutoCloudImageEnhancementSupported(): boolean
```

Confirm if the auto cloud image enhancement is supported.

**Since:** 23

**Deprecated since:** -1

<!--Device-PhotoOutput-isAutoCloudImageEnhancementSupported(): boolean--><!--Device-PhotoOutput-isAutoCloudImageEnhancementSupported(): boolean-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [7400201](../errorcode-camera.md#7400201-camera-service-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## isAutoHighQualityPhotoSupported

```TypeScript
isAutoHighQualityPhotoSupported(): boolean
```

Checks whether automatic high quality is supported for photos.

**Since:** 23

**Deprecated since:** -1

<!--Device-PhotoOutput-isAutoHighQualityPhotoSupported(): boolean--><!--Device-PhotoOutput-isAutoHighQualityPhotoSupported(): boolean-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [7400104](../errorcode-camera.md#7400104-session-not-running) |
| [7400201](../errorcode-camera.md#7400201-camera-service-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function isAutoHighQualityPhotoSupported(photoOutput: camera.PhotoOutput): boolean {
  return photoOutput.isAutoHighQualityPhotoSupported();
}
```

## isDeferredImageDeliveryEnabled

```TypeScript
isDeferredImageDeliveryEnabled(type: DeferredDeliveryImageType): boolean
```

Checks whether deferred delivery of a certain type is enabled.

**Since:** 23

**Deprecated since:** -1

<!--Device-PhotoOutput-isDeferredImageDeliveryEnabled(type: DeferredDeliveryImageType): boolean--><!--Device-PhotoOutput-isDeferredImageDeliveryEnabled(type: DeferredDeliveryImageType): boolean-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | [DeferredDeliveryImageType](arkts-camera-camera-deferreddeliveryimagetype-e-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [7400101](../errorcode-camera.md#7400101-invalid-parameter) |
| [7400104](../errorcode-camera.md#7400104-session-not-running) |
| [7400201](../errorcode-camera.md#7400201-camera-service-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
function isDeferredImageDeliveryEnabled(photoOutput: camera.PhotoOutput, type: camera.DeferredDeliveryImageType): boolean {
  let res: boolean = false;
  res = photoOutput.isDeferredImageDeliveryEnabled(type);
  return res;
}
```

## isDeferredImageDeliverySupported

```TypeScript
isDeferredImageDeliverySupported(type: DeferredDeliveryImageType): boolean
```

Checks whether deferred delivery of a certain type is supported.

**Since:** 23

**Deprecated since:** -1

<!--Device-PhotoOutput-isDeferredImageDeliverySupported(type: DeferredDeliveryImageType): boolean--><!--Device-PhotoOutput-isDeferredImageDeliverySupported(type: DeferredDeliveryImageType): boolean-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | [DeferredDeliveryImageType](arkts-camera-camera-deferreddeliveryimagetype-e-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [7400101](../errorcode-camera.md#7400101-invalid-parameter) |
| [7400104](../errorcode-camera.md#7400104-session-not-running) |
| [7400201](../errorcode-camera.md#7400201-camera-service-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
function isDeferredImageDeliverySupported(photoOutput: camera.PhotoOutput, type: camera.DeferredDeliveryImageType): boolean {
  let res: boolean = false;
  res = photoOutput.isDeferredImageDeliverySupported(type);
  return res;
}
```

## isDepthDataDeliverySupported

```TypeScript
isDepthDataDeliverySupported(): boolean
```

Check if the depth data delivery is supported.

**Since:** 23

**Deprecated since:** -1

<!--Device-PhotoOutput-isDepthDataDeliverySupported(): boolean--><!--Device-PhotoOutput-isDepthDataDeliverySupported(): boolean-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [7400104](../errorcode-camera.md#7400104-session-not-running) |
| [7400201](../errorcode-camera.md#7400201-camera-service-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## isOfflineSupported

```TypeScript
isOfflineSupported(): boolean
```

Confirm if offline processing is supported.

**Since:** 23

**Deprecated since:** -1

<!--Device-PhotoOutput-isOfflineSupported(): boolean--><!--Device-PhotoOutput-isOfflineSupported(): boolean-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [7400201](../errorcode-camera.md#7400201-camera-service-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## isOriginalImageGenerationSupported

```TypeScript
isOriginalImageGenerationSupported(): boolean
```

Confirm if original image generation supported.

**Since:** 24

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-PhotoOutput-isOriginalImageGenerationSupported(): boolean--><!--Device-PhotoOutput-isOriginalImageGenerationSupported(): boolean-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [7400201](../errorcode-camera.md#7400201-camera-service-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## isQuickThumbnailSupported

```TypeScript
isQuickThumbnailSupported(): boolean
```

Checks whether the quick thumbnail feature is supported. This API takes effect after [addOutput](arkts-camera-camera-session-i.md#addOutput) and [addInput](arkts-camera-camera-session-i.md#addInput) and before [commitConfig](arkts-camera-camera-session-i.md#commitConfig).

**Since:** 23

**Deprecated since:** -1

<!--Device-PhotoOutput-isQuickThumbnailSupported(): boolean--><!--Device-PhotoOutput-isQuickThumbnailSupported(): boolean-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [7400104](../errorcode-camera.md#7400104-session-not-running) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

async function isQuickThumbnailSupported(context: common.BaseContext, mode: camera.SceneMode, photoProfile: camera.Profile): Promise<boolean> {
  let cameraManager: camera.CameraManager = camera.getCameraManager(context);
  let cameras: Array<camera.CameraDevice> = cameraManager.getSupportedCameras();
  // Create a CaptureSession instance.
  let session: camera.Session = cameraManager.createSession(mode);
  // Start configuration for the session.
  session.beginConfig();
  // Add a CameraInput instance to the session.
  if (cameras.length <= 0) {
    console.info('Get supported cameras is null or [].');
    return false;
  }
  let cameraInput: camera.CameraInput = cameraManager.createCameraInput(cameras[0]);
  await cameraInput.open();
  session.addInput(cameraInput);
  // Add a PhotoOutput instance to the session.
  let photoOutput: camera.PhotoOutput = cameraManager.createPhotoOutput(photoProfile);
  try {
    session.addOutput(photoOutput);
  } catch (error) {
    let err = error as BusinessError;
    console.error(`AddOutput called failed. error code: ${err.code}`);
    return false;
  }
  let isSupported: boolean = photoOutput.isQuickThumbnailSupported();
  return isSupported;
}
```

## isRawDeliverySupported

```TypeScript
isRawDeliverySupported(): boolean
```

Confirm if the raw image delivery is supported

**Since:** 23

**Deprecated since:** -1

<!--Device-PhotoOutput-isRawDeliverySupported(): boolean--><!--Device-PhotoOutput-isRawDeliverySupported(): boolean-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [7400104](../errorcode-camera.md#7400104-session-not-running) |
| [7400201](../errorcode-camera.md#7400201-camera-service-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## offDeferredPhotoProxyAvailable

```TypeScript
offDeferredPhotoProxyAvailable(callback?: AsyncCallback<DeferredPhotoProxy>): void
```

Unsubscribes deferred photo proxy available event callback.

**Since:** 23

**Deprecated since:** -1

<!--Device-PhotoOutput-offDeferredPhotoProxyAvailable(callback?: AsyncCallback<DeferredPhotoProxy>): void--><!--Device-PhotoOutput-offDeferredPhotoProxyAvailable(callback?: AsyncCallback<DeferredPhotoProxy>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[DeferredPhotoProxy](arkts-camera-camera-deferredphotoproxy-i-sys.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## offOfflineDeliveryFinished

```TypeScript
offOfflineDeliveryFinished(callback?: AsyncCallback<void>): void
```

Unsubscribes offline Delivery finished events. This method is valid only after enableOffline() is called.

**Since:** 23

**Deprecated since:** -1

<!--Device-PhotoOutput-offOfflineDeliveryFinished(callback?: AsyncCallback<void>): void--><!--Device-PhotoOutput-offOfflineDeliveryFinished(callback?: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## offQuickThumbnail

```TypeScript
offQuickThumbnail(callback?: AsyncCallback<image.PixelMap>): void
```

Unsubscribes from camera thumbnail events. This method is valid only after enableQuickThumbnail(true) is called.

**Since:** 23

**Deprecated since:** -1

<!--Device-PhotoOutput-offQuickThumbnail(callback?: AsyncCallback<image.PixelMap>): void--><!--Device-PhotoOutput-offQuickThumbnail(callback?: AsyncCallback<image.PixelMap>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;image.PixelMap&gt; | No |

## off_deferredPhotoProxyAvailable

```TypeScript
off(type: 'deferredPhotoProxyAvailable', callback?: AsyncCallback<DeferredPhotoProxy>): void
```

Unsubscribes from events indicating available thumbnail proxies.

**Since:** 11

**Deprecated since:** -1

<!--Device-PhotoOutput-off(type: 'deferredPhotoProxyAvailable', callback?: AsyncCallback<DeferredPhotoProxy>): void--><!--Device-PhotoOutput-off(type: 'deferredPhotoProxyAvailable', callback?: AsyncCallback<DeferredPhotoProxy>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'deferredPhotoProxyAvailable' | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[DeferredPhotoProxy](arkts-camera-camera-deferredphotoproxy-i-sys.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { image } from '@kit.ImageKit';

function callback(err: BusinessError, proxyObj: camera.DeferredPhotoProxy): void {
  if (err !== undefined && err.code !== 0) {
    console.error(`Callback Error, errorCode: ${err.code}`);
    return;
  }
  proxyObj.getThumbnail().then((thumbnail: image.PixelMap) => {
    AppStorage.setOrCreate('proxyThumbnail', thumbnail);
  });
}

function unRegisterPhotoOutputDeferredPhotoProxyAvailable(photoOutput: camera.PhotoOutput): void {
  photoOutput.off('deferredPhotoProxyAvailable', callback);
}
```

## off_offlineDeliveryFinished

```TypeScript
off(type: 'offlineDeliveryFinished', callback?: AsyncCallback<void>): void
```

Unsubscribes offline Delivery finished events. This method is valid only after enableOffline() is called.

**Since:** 18

**Deprecated since:** -1

<!--Device-PhotoOutput-off(type: 'offlineDeliveryFinished', callback?: AsyncCallback<void>): void--><!--Device-PhotoOutput-off(type: 'offlineDeliveryFinished', callback?: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'offlineDeliveryFinished' | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## off_quickThumbnail

```TypeScript
off(type: 'quickThumbnail', callback?: AsyncCallback<image.PixelMap>): void
```

Unsubscribes from quick thumbnail output events.

**Since:** 10

**Deprecated since:** -1

<!--Device-PhotoOutput-off(type: 'quickThumbnail', callback?: AsyncCallback<image.PixelMap>): void--><!--Device-PhotoOutput-off(type: 'quickThumbnail', callback?: AsyncCallback<image.PixelMap>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'quickThumbnail' | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;image.PixelMap&gt; | No |

## Examples

```TypeScript
function unregisterQuickThumbnail(photoOutput: camera.PhotoOutput): void {
  photoOutput.off('quickThumbnail');
}
```

## onDeferredPhotoProxyAvailable

```TypeScript
onDeferredPhotoProxyAvailable(callback: AsyncCallback<DeferredPhotoProxy>): void
```

Subscribes deferred photo proxy available event callback.

**Since:** 23

**Deprecated since:** -1

<!--Device-PhotoOutput-onDeferredPhotoProxyAvailable(callback: AsyncCallback<DeferredPhotoProxy>): void--><!--Device-PhotoOutput-onDeferredPhotoProxyAvailable(callback: AsyncCallback<DeferredPhotoProxy>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[DeferredPhotoProxy](arkts-camera-camera-deferredphotoproxy-i-sys.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## onOfflineDeliveryFinished

```TypeScript
onOfflineDeliveryFinished(callback: AsyncCallback<void>): void
```

Subscribes offline Delivery finished events. This method is valid only after enableOffline() is called.

**Since:** 23

**Deprecated since:** -1

<!--Device-PhotoOutput-onOfflineDeliveryFinished(callback: AsyncCallback<void>): void--><!--Device-PhotoOutput-onOfflineDeliveryFinished(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## onQuickThumbnail

```TypeScript
onQuickThumbnail(callback: AsyncCallback<image.PixelMap>): void
```

Subscribes to camera thumbnail events. This method is valid only after enableQuickThumbnail(true) is called.

**Since:** 23

**Deprecated since:** -1

<!--Device-PhotoOutput-onQuickThumbnail(callback: AsyncCallback<image.PixelMap>): void--><!--Device-PhotoOutput-onQuickThumbnail(callback: AsyncCallback<image.PixelMap>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;image.PixelMap&gt; | Yes |

## on_deferredPhotoProxyAvailable

```TypeScript
on(type: 'deferredPhotoProxyAvailable', callback: AsyncCallback<DeferredPhotoProxy>): void
```

Subscribes to events indicating available thumbnail proxies. This API uses an asynchronous callback to return the result.

**Since:** 11

**Deprecated since:** -1

<!--Device-PhotoOutput-on(type: 'deferredPhotoProxyAvailable', callback: AsyncCallback<DeferredPhotoProxy>): void--><!--Device-PhotoOutput-on(type: 'deferredPhotoProxyAvailable', callback: AsyncCallback<DeferredPhotoProxy>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'deferredPhotoProxyAvailable' | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[DeferredPhotoProxy](arkts-camera-camera-deferredphotoproxy-i-sys.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { image } from '@kit.ImageKit';

function callback(err: BusinessError, proxyObj: camera.DeferredPhotoProxy): void {
  if (err !== undefined && err.code !== 0) {
    console.error(`Callback Error, errorCode: ${err.code}`);
    return;
  }
  proxyObj.getThumbnail().then((thumbnail: image.PixelMap) => {
    AppStorage.setOrCreate('proxyThumbnail', thumbnail);
  });
}

function registerPhotoOutputDeferredPhotoProxyAvailable(photoOutput: camera.PhotoOutput): void {
  photoOutput.on('deferredPhotoProxyAvailable', callback);
}
```

## on_offlineDeliveryFinished

```TypeScript
on(type: 'offlineDeliveryFinished', callback: AsyncCallback<void>): void
```

Subscribes offline Delivery finished events. This method is valid only after enableOffline() is called.

**Since:** 18

**Deprecated since:** -1

<!--Device-PhotoOutput-on(type: 'offlineDeliveryFinished', callback: AsyncCallback<void>): void--><!--Device-PhotoOutput-on(type: 'offlineDeliveryFinished', callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'offlineDeliveryFinished' | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## on_quickThumbnail

```TypeScript
on(type: 'quickThumbnail', callback: AsyncCallback<image.PixelMap>): void
```

Subscribes to quick thumbnail output events. This API uses an asynchronous callback to return the result. The listening takes effect after **enableQuickThumbnail(true)** is called.

**Since:** 10

**Deprecated since:** -1

<!--Device-PhotoOutput-on(type: 'quickThumbnail', callback: AsyncCallback<image.PixelMap>): void--><!--Device-PhotoOutput-on(type: 'quickThumbnail', callback: AsyncCallback<image.PixelMap>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'quickThumbnail' | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;image.PixelMap&gt; | Yes |

## Examples

```TypeScript
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { image } from '@kit.ImageKit';
import { camera } from '@kit.CameraKit';

function callback(err: BusinessError, pixelMap: image.PixelMap): void {
  if (err || pixelMap === undefined) {
      console.error('photoOutput on thumbnail failed');
      return;
  }
  // Display or save the PixelMap instance.
  // Execute the operation.
}

async function registerQuickThumbnail(context: common.BaseContext, mode: camera.SceneMode, photoProfile: camera.Profile): Promise<void> {
  let cameraManager: camera.CameraManager = camera.getCameraManager(context);
  let cameras: Array<camera.CameraDevice> = cameraManager.getSupportedCameras();
  // Create a CaptureSession instance.
  let session: camera.Session = cameraManager.createSession(mode);
  // Start configuration for the session.
  session.beginConfig();
  // Add a CameraInput instance to the session.
  let cameraInput: camera.CameraInput = cameraManager.createCameraInput(cameras[0]);
  await cameraInput.open();
  session.addInput(cameraInput);
  // Add a PhotoOutput instance to the session.
  let photoOutput: camera.PhotoOutput = cameraManager.createPhotoOutput(photoProfile);
  session.addOutput(photoOutput);
  let isSupported: boolean = photoOutput.isQuickThumbnailSupported();
  if (!isSupported) {
    console.info('Quick Thumbnail is not supported to be turned on.');
    return;
  }
  try {
    photoOutput.enableQuickThumbnail(true);
  } catch (error) {
    let err = error as BusinessError;
    console.error(`The enableQuickThumbnail call failed. error code: ${err.code}`);
  }

  photoOutput.on('quickThumbnail', callback);
}
```

## setEditData

```TypeScript
setEditData(editData: string): void
```

Set edit data.

**Since:** 24

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-PhotoOutput-setEditData(editData: string): void--><!--Device-PhotoOutput-setEditData(editData: string): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| editData | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [7400201](../errorcode-camera.md#7400201-camera-service-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
