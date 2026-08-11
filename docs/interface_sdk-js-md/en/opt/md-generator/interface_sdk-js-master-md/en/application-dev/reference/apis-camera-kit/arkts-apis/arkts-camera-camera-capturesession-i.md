# CaptureSession

**CaptureSession** implements a capture session, which saves all [CameraInput](arkts-camera-camera-camerainput-i.md) and   
[CameraOutput](arkts-camera-camera-cameraoutput-i.md) instances required to run the camera and requests the camera to complete shooting or video recording.

**Since:** 10

**Deprecated since:** 11

**Substitutes:** [camera.VideoSession](arkts-camera-camera-videosession-i.md)

<!--Device-camera-interface CaptureSession--><!--Device-camera-interface CaptureSession-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## Modules to Import

```TypeScript
import { camera } from 'kits/@kit.CameraKit';
```

## addInput

```TypeScript
addInput(cameraInput: CameraInput): void
```

Adds a [CameraInput](arkts-camera-camera-camerainput-i.md) instance to this session.

**Since:** 10

**Deprecated since:** 11

**Substitutes:** [camera.Session.addInput](arkts-camera-camera-session-i.md#addinput)

<!--Device-CaptureSession-addInput(cameraInput: CameraInput): void--><!--Device-CaptureSession-addInput(cameraInput: CameraInput): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| cameraInput | [CameraInput](arkts-camera-camera-camerainput-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [7400101](../errorcode-camera.md#7400101-invalid-parameter) |
| [7400102](../errorcode-camera.md#7400102-invalid-operation) |

## addOutput

```TypeScript
addOutput(cameraOutput: CameraOutput): void
```

Adds a [CameraOutput](arkts-camera-camera-cameraoutput-i.md) instance to this session.

**Since:** 10

**Deprecated since:** 11

**Substitutes:** [camera.Session.addOutput](arkts-camera-camera-session-i.md#addoutput)

<!--Device-CaptureSession-addOutput(cameraOutput: CameraOutput): void--><!--Device-CaptureSession-addOutput(cameraOutput: CameraOutput): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| cameraOutput | [CameraOutput](arkts-camera-camera-cameraoutput-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [7400101](../errorcode-camera.md#7400101-invalid-parameter) |
| [7400102](../errorcode-camera.md#7400102-invalid-operation) |

## beginConfig

```TypeScript
beginConfig(): void
```

Starts configuration for the session.

**Since:** 10

**Deprecated since:** 11

**Substitutes:** [camera.Session.beginConfig](arkts-camera-camera-session-i.md#beginconfig)

<!--Device-CaptureSession-beginConfig(): void--><!--Device-CaptureSession-beginConfig(): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Error codes:**

| Error Code ID |
| --- |
| [7400105](../errorcode-camera.md#7400105-session-configuration-locked) |

## commitConfig

```TypeScript
commitConfig(callback: AsyncCallback<void>): void
```

Commits the configuration for this session. This API uses an asynchronous callback to return the result.

**Since:** 10

**Deprecated since:** 11

**Substitutes:** [camera.Session.commitConfig](arkts-camera-camera-session-i.md#commitconfig)(callback:

<!--Device-CaptureSession-commitConfig(callback: AsyncCallback<void>): void--><!--Device-CaptureSession-commitConfig(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [7400102](../errorcode-camera.md#7400102-invalid-operation) |
| [7400201](../errorcode-camera.md#7400201-camera-service-error) |

## commitConfig

```TypeScript
commitConfig(): Promise<void>
```

Commits the configuration for this session. This API uses a promise to return the result.

**Since:** 10

**Deprecated since:** 11

**Substitutes:** [camera.Session.commitConfig](arkts-camera-camera-session-i.md#commitconfig)()

<!--Device-CaptureSession-commitConfig(): Promise<void>--><!--Device-CaptureSession-commitConfig(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [7400102](../errorcode-camera.md#7400102-invalid-operation) |
| [7400201](../errorcode-camera.md#7400201-camera-service-error) |

## getActiveVideoStabilizationMode

```TypeScript
getActiveVideoStabilizationMode(): VideoStabilizationMode
```

Obtains the video stabilization mode in use.

**Since:** 10

**Deprecated since:** 11

**Substitutes:** [camera.Stabilization.getActiveVideoStabilizationMode](arkts-camera-camera-stabilization-i.md#getactivevideostabilizationmode)

<!--Device-CaptureSession-getActiveVideoStabilizationMode(): VideoStabilizationMode--><!--Device-CaptureSession-getActiveVideoStabilizationMode(): VideoStabilizationMode-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [VideoStabilizationMode](arkts-camera-camera-videostabilizationmode-e.md) |

**Error codes:**

| Error Code ID |
| --- |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) |

## getExposureBiasRange

```TypeScript
getExposureBiasRange(): Array<number>
```

Obtains the exposure compensation values of the camera device.

**Since:** 10

**Deprecated since:** 11

**Substitutes:** [camera.AutoExposureQuery.getExposureBiasRange](arkts-camera-camera-autoexposurequery-i.md#getexposurebiasrange)

<!--Device-CaptureSession-getExposureBiasRange(): Array<number>--><!--Device-CaptureSession-getExposureBiasRange(): Array<number>-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array&lt;number&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) |

## getExposureMode

```TypeScript
getExposureMode(): ExposureMode
```

Obtains the exposure mode in use.

**Since:** 10

**Deprecated since:** 11

**Substitutes:** [camera.AutoExposure.getExposureMode](arkts-camera-camera-autoexposure-i.md#getexposuremode)

<!--Device-CaptureSession-getExposureMode(): ExposureMode--><!--Device-CaptureSession-getExposureMode(): ExposureMode-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ExposureMode](arkts-camera-camera-exposuremode-e.md) |

**Error codes:**

| Error Code ID |
| --- |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) |

## getExposureValue

```TypeScript
getExposureValue(): number
```

Obtains the exposure value in use.

**Since:** 10

**Deprecated since:** 11

**Substitutes:** [camera.AutoExposure.getExposureValue](arkts-camera-camera-autoexposure-i.md#getexposurevalue)

<!--Device-CaptureSession-getExposureValue(): number--><!--Device-CaptureSession-getExposureValue(): number-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) |

## getFlashMode

```TypeScript
getFlashMode(): FlashMode
```

Obtains the flash mode in use.

**Since:** 10

**Deprecated since:** 11

**Substitutes:** [camera.Flash.getFlashMode](arkts-camera-camera-flash-i.md#getflashmode)

<!--Device-CaptureSession-getFlashMode(): FlashMode--><!--Device-CaptureSession-getFlashMode(): FlashMode-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [FlashMode](arkts-camera-camera-flashmode-e.md) |

**Error codes:**

| Error Code ID |
| --- |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) |

## getFocalLength

```TypeScript
getFocalLength(): number
```

Obtains the focal length of the camera device.

**Since:** 10

**Deprecated since:** 11

**Substitutes:** [camera.Focus.getFocalLength](arkts-camera-camera-focus-i.md#getfocallength)

<!--Device-CaptureSession-getFocalLength(): number--><!--Device-CaptureSession-getFocalLength(): number-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) |

## getFocusMode

```TypeScript
getFocusMode(): FocusMode
```

Obtains the focus mode in use.

**Since:** 10

**Deprecated since:** 11

**Substitutes:** [camera.Focus.getFocusMode](arkts-camera-camera-focus-i.md#getfocusmode)

<!--Device-CaptureSession-getFocusMode(): FocusMode--><!--Device-CaptureSession-getFocusMode(): FocusMode-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [FocusMode](arkts-camera-camera-focusmode-e.md) |

**Error codes:**

| Error Code ID |
| --- |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) |

## getFocusPoint

```TypeScript
getFocusPoint(): Point
```

Obtains the focal point of the camera device.

**Since:** 10

**Deprecated since:** 11

**Substitutes:** [camera.Focus.getFocusPoint](arkts-camera-camera-focus-i.md#getfocuspoint)

<!--Device-CaptureSession-getFocusPoint(): Point--><!--Device-CaptureSession-getFocusPoint(): Point-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Point](../../apis-test-kit/arkts-apis/arkts-test-uitest-point-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) |

## getMeteringPoint

```TypeScript
getMeteringPoint(): Point
```

Obtains the metering point of the camera device.

**Since:** 10

**Deprecated since:** 11

**Substitutes:** [camera.AutoExposure.getMeteringPoint](arkts-camera-camera-autoexposure-i.md#getmeteringpoint)

<!--Device-CaptureSession-getMeteringPoint(): Point--><!--Device-CaptureSession-getMeteringPoint(): Point-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Point](../../apis-test-kit/arkts-apis/arkts-test-uitest-point-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) |

## getZoomRatio

```TypeScript
getZoomRatio(): number
```

Obtains the zoom ratio in use.

**Since:** 10

**Deprecated since:** 11

**Substitutes:** [camera.Zoom.getZoomRatio](arkts-camera-camera-zoom-i.md#getzoomratio)

<!--Device-CaptureSession-getZoomRatio(): number--><!--Device-CaptureSession-getZoomRatio(): number-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) |

## getZoomRatioRange

```TypeScript
getZoomRatioRange(): Array<number>
```

Obtains the supported zoom ratio range.

**Since:** 10

**Deprecated since:** 11

**Substitutes:** [camera.ZoomQuery.getZoomRatioRange](arkts-camera-camera-zoomquery-i.md#getzoomratiorange)

<!--Device-CaptureSession-getZoomRatioRange(): Array<number>--><!--Device-CaptureSession-getZoomRatioRange(): Array<number>-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array&lt;number&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) |

## hasFlash

```TypeScript
hasFlash(): boolean
```

Checks whether the camera device has flash.

**Since:** 10

**Deprecated since:** 11

**Substitutes:** [camera.FlashQuery.hasFlash](arkts-camera-camera-flashquery-i.md#hasflash)

<!--Device-CaptureSession-hasFlash(): boolean--><!--Device-CaptureSession-hasFlash(): boolean-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) |

## isExposureModeSupported

```TypeScript
isExposureModeSupported(aeMode: ExposureMode): boolean
```

Checks whether an exposure mode is supported.

**Since:** 10

**Deprecated since:** 11

**Substitutes:** [camera.AutoExposureQuery.isExposureModeSupported](arkts-camera-camera-autoexposurequery-i.md#isexposuremodesupported)

<!--Device-CaptureSession-isExposureModeSupported(aeMode: ExposureMode): boolean--><!--Device-CaptureSession-isExposureModeSupported(aeMode: ExposureMode): boolean-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| aeMode | [ExposureMode](arkts-camera-camera-exposuremode-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) |

## isFlashModeSupported

```TypeScript
isFlashModeSupported(flashMode: FlashMode): boolean
```

Checks whether the flash mode is supported.

**Since:** 10

**Deprecated since:** 11

**Substitutes:** [camera.FlashQuery.isFlashModeSupported](arkts-camera-camera-flashquery-i.md#isflashmodesupported)

<!--Device-CaptureSession-isFlashModeSupported(flashMode: FlashMode): boolean--><!--Device-CaptureSession-isFlashModeSupported(flashMode: FlashMode): boolean-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| flashMode | [FlashMode](arkts-camera-camera-flashmode-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) |

## isFocusModeSupported

```TypeScript
isFocusModeSupported(afMode: FocusMode): boolean
```

Checks whether a focus mode is supported.

**Since:** 10

**Deprecated since:** 11

**Substitutes:** [camera.FocusQuery.isFocusModeSupported](arkts-camera-camera-focusquery-i.md#isfocusmodesupported)

<!--Device-CaptureSession-isFocusModeSupported(afMode: FocusMode): boolean--><!--Device-CaptureSession-isFocusModeSupported(afMode: FocusMode): boolean-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| afMode | [FocusMode](arkts-camera-camera-focusmode-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) |

## isVideoStabilizationModeSupported

```TypeScript
isVideoStabilizationModeSupported(vsMode: VideoStabilizationMode): boolean
```

Checks whether a video stabilization mode is supported.

**Since:** 10

**Deprecated since:** 11

**Substitutes:** [camera.StabilizationQuery.isVideoStabilizationModeSupported](arkts-camera-camera-stabilizationquery-i.md#isvideostabilizationmodesupported)

<!--Device-CaptureSession-isVideoStabilizationModeSupported(vsMode: VideoStabilizationMode): boolean--><!--Device-CaptureSession-isVideoStabilizationModeSupported(vsMode: VideoStabilizationMode): boolean-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| vsMode | [VideoStabilizationMode](arkts-camera-camera-videostabilizationmode-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) |

## off('focusStateChange')

```TypeScript
off(type: 'focusStateChange', callback?: AsyncCallback<FocusState>): void
```

Unsubscribes from focus state change events.

**Since:** 10

**Deprecated since:** 11

**Substitutes:** camera.VideoSession.off(type:

<!--Device-CaptureSession-off(type: 'focusStateChange', callback?: AsyncCallback<FocusState>): void--><!--Device-CaptureSession-off(type: 'focusStateChange', callback?: AsyncCallback<FocusState>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'focusStateChange' | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;FocusState&gt; | No |

## off('error')

```TypeScript
off(type: 'error', callback?: ErrorCallback): void
```

Unsubscribes from CaptureSession error events. This API uses a callback to return the result.

**Since:** 10

**Deprecated since:** 11

**Substitutes:** camera.VideoSession.off(type:

<!--Device-CaptureSession-off(type: 'error', callback?: ErrorCallback): void--><!--Device-CaptureSession-off(type: 'error', callback?: ErrorCallback): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'error' | Yes |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | No |

## on('focusStateChange')

```TypeScript
on(type: 'focusStateChange', callback: AsyncCallback<FocusState>): void
```

Subscribes to focus state change events. This API uses an asynchronous callback to return the result.

> **NOTE：**
> 
> Currently, you cannot use **off()** to unregister the callback in the callback method of **on()**.

**Since:** 10

**Deprecated since:** 11

**Substitutes:** camera.VideoSession.on(type:

<!--Device-CaptureSession-on(type: 'focusStateChange', callback: AsyncCallback<FocusState>): void--><!--Device-CaptureSession-on(type: 'focusStateChange', callback: AsyncCallback<FocusState>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'focusStateChange' | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;FocusState&gt; | Yes |

## on('error')

```TypeScript
on(type: 'error', callback: ErrorCallback): void
```

Subscribes to CaptureSession error events. This API uses an asynchronous callback to return the result.

> **NOTE：**
> 
> Currently, you cannot use **off()** to unregister the callback in the callback method of **on()**.

**Since:** 10

**Deprecated since:** 11

**Substitutes:** camera.VideoSession.on(type:

<!--Device-CaptureSession-on(type: 'error', callback: ErrorCallback): void--><!--Device-CaptureSession-on(type: 'error', callback: ErrorCallback): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'error' | Yes |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | Yes |

## release

```TypeScript
release(callback: AsyncCallback<void>): void
```

Releases this session. This API uses an asynchronous callback to return the result.

**Since:** 10

**Deprecated since:** 11

**Substitutes:** [camera.Session.release](arkts-camera-camera-session-i.md#release)(callback:

<!--Device-CaptureSession-release(callback: AsyncCallback<void>): void--><!--Device-CaptureSession-release(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [7400201](../errorcode-camera.md#7400201-camera-service-error) |

## release

```TypeScript
release(): Promise<void>
```

Releases this session. This API uses a promise to return the result.

**Since:** 10

**Deprecated since:** 11

**Substitutes:** [camera.Session.release](arkts-camera-camera-session-i.md#release)()

<!--Device-CaptureSession-release(): Promise<void>--><!--Device-CaptureSession-release(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [7400201](../errorcode-camera.md#7400201-camera-service-error) |

## removeInput

```TypeScript
removeInput(cameraInput: CameraInput): void
```

Removes a [CameraInput](arkts-camera-camera-camerainput-i.md) instance from this session.

**Since:** 10

**Deprecated since:** 11

**Substitutes:** [camera.Session.removeInput](arkts-camera-camera-session-i.md#removeinput)

<!--Device-CaptureSession-removeInput(cameraInput: CameraInput): void--><!--Device-CaptureSession-removeInput(cameraInput: CameraInput): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| cameraInput | [CameraInput](arkts-camera-camera-camerainput-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [7400101](../errorcode-camera.md#7400101-invalid-parameter) |
| [7400102](../errorcode-camera.md#7400102-invalid-operation) |

## removeOutput

```TypeScript
removeOutput(cameraOutput: CameraOutput): void
```

Removes a [CameraOutput](arkts-camera-camera-cameraoutput-i.md) instance from this session.

**Since:** 10

**Deprecated since:** 11

**Substitutes:** [camera.Session.removeOutput](arkts-camera-camera-session-i.md#removeoutput)

<!--Device-CaptureSession-removeOutput(cameraOutput: CameraOutput): void--><!--Device-CaptureSession-removeOutput(cameraOutput: CameraOutput): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| cameraOutput | [CameraOutput](arkts-camera-camera-cameraoutput-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [7400101](../errorcode-camera.md#7400101-invalid-parameter) |
| [7400102](../errorcode-camera.md#7400102-invalid-operation) |

## setExposureBias

```TypeScript
setExposureBias(exposureBias: number): void
```

Sets an exposure compensation value (EV).

Before the setting, you are advised to use   
[getExposureBiasRange](arkts-camera-camera-capturesession-i.md#getexposurebiasrange) to obtain the supported values.

**Since:** 10

**Deprecated since:** 11

**Substitutes:** [camera.AutoExposure.setExposureBias](arkts-camera-camera-autoexposure-i.md#setexposurebias)

<!--Device-CaptureSession-setExposureBias(exposureBias: number): void--><!--Device-CaptureSession-setExposureBias(exposureBias: number): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| exposureBias | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) |

## setExposureMode

```TypeScript
setExposureMode(aeMode: ExposureMode): void
```

Sets an exposure mode. Before the setting, call   
[isExposureModeSupported](arkts-camera-camera-capturesession-i.md#isexposuremodesupported) to check whether the target exposure mode is supported.

**Since:** 10

**Deprecated since:** 11

**Substitutes:** [camera.AutoExposure.setExposureMode](arkts-camera-camera-autoexposure-i.md#setexposuremode)

<!--Device-CaptureSession-setExposureMode(aeMode: ExposureMode): void--><!--Device-CaptureSession-setExposureMode(aeMode: ExposureMode): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| aeMode | [ExposureMode](arkts-camera-camera-exposuremode-e.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) |

## setFlashMode

```TypeScript
setFlashMode(flashMode: FlashMode): void
```

Sets a flash mode.

Before the setting, do the following checks:

1. Use [hasFlash](arkts-camera-camera-capturesession-i.md#hasflash) to check whether the camera device has flash.2. Use [isFlashModeSupported](arkts-camera-camera-capturesession-i.md#isflashmodesupported) to check whether the camera device supports the flash mode.

**Since:** 10

**Deprecated since:** 11

**Substitutes:** [camera.Flash.setFlashMode](arkts-camera-camera-flash-i.md#setflashmode)

<!--Device-CaptureSession-setFlashMode(flashMode: FlashMode): void--><!--Device-CaptureSession-setFlashMode(flashMode: FlashMode): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| flashMode | [FlashMode](arkts-camera-camera-flashmode-e.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) |

## setFocusMode

```TypeScript
setFocusMode(afMode: FocusMode): void
```

Sets a focus mode.

Before the setting, call [isFocusModeSupported](arkts-camera-camera-capturesession-i.md#isfocusmodesupported) to check whether the focus mode is supported.

**Since:** 10

**Deprecated since:** 11

**Substitutes:** [camera.Focus.setFocusMode](arkts-camera-camera-focus-i.md#setfocusmode)

<!--Device-CaptureSession-setFocusMode(afMode: FocusMode): void--><!--Device-CaptureSession-setFocusMode(afMode: FocusMode): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| afMode | [FocusMode](arkts-camera-camera-focusmode-e.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) |

## setFocusPoint

```TypeScript
setFocusPoint(point: Point): void
```

Sets the focal point. The focal point must be in the coordinate system (0-1), where the top-left corner is {0, 0}and the bottom-right corner is {1, 1}.

The coordinate system is based on the horizontal device direction with the device's charging port on the right. If the layout of the preview screen of an application is based on the vertical direction with the charging port on the lower side, the layout width and height are {w, h}, and the touch point is {x, y}, then the coordinate point after conversion is {y/h, 1-x/w}.

**Since:** 10

**Deprecated since:** 11

**Substitutes:** [camera.Focus.setFocusPoint](arkts-camera-camera-focus-i.md#setfocuspoint)

<!--Device-CaptureSession-setFocusPoint(point: Point): void--><!--Device-CaptureSession-setFocusPoint(point: Point): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| point | [Point](../../apis-test-kit/arkts-apis/arkts-test-uitest-point-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) |

## setMeteringPoint

```TypeScript
setMeteringPoint(point: Point): void
```

Sets the metering point, which is the center point of the metering rectangle. The metering point must be in the coordinate system (0-1), where the top-left corner is {0, 0} and the bottom-right corner is {1, 1}.

The coordinate system is based on the horizontal device direction with the device's charging port on the right. If the layout of the preview screen of an application is based on the vertical direction with the charging port on the lower side, the layout width and height are {w, h}, and the touch point is {x, y}, then the coordinate point after conversion is {y/h, 1-x/w}.

**Since:** 10

**Deprecated since:** 11

**Substitutes:** [camera.AutoExposure.setMeteringPoint](arkts-camera-camera-autoexposure-i.md#setmeteringpoint)

<!--Device-CaptureSession-setMeteringPoint(point: Point): void--><!--Device-CaptureSession-setMeteringPoint(point: Point): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| point | [Point](../../apis-test-kit/arkts-apis/arkts-test-uitest-point-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) |

## setVideoStabilizationMode

```TypeScript
setVideoStabilizationMode(mode: VideoStabilizationMode): void
```

Sets a video stabilization mode. Before the setting, call   
[isVideoStabilizationModeSupported](arkts-camera-camera-capturesession-i.md#isvideostabilizationmodesupported) to check whether the target video stabilization mode is supported.

**Since:** 10

**Deprecated since:** 11

**Substitutes:** [camera.Stabilization.setVideoStabilizationMode](arkts-camera-camera-stabilization-i.md#setvideostabilizationmode)

<!--Device-CaptureSession-setVideoStabilizationMode(mode: VideoStabilizationMode): void--><!--Device-CaptureSession-setVideoStabilizationMode(mode: VideoStabilizationMode): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mode | [VideoStabilizationMode](arkts-camera-camera-videostabilizationmode-e.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) |

## setZoomRatio

```TypeScript
setZoomRatio(zoomRatio: number): void
```

Sets a zoom ratio, with a maximum precision of two decimal places.

**Since:** 10

**Deprecated since:** 11

**Substitutes:** [camera.Zoom.setZoomRatio](arkts-camera-camera-zoom-i.md#setzoomratio)

<!--Device-CaptureSession-setZoomRatio(zoomRatio: number): void--><!--Device-CaptureSession-setZoomRatio(zoomRatio: number): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| zoomRatio | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) |

## start

```TypeScript
start(callback: AsyncCallback<void>): void
```

Starts this session. This API uses an asynchronous callback to return the result.

**Since:** 10

**Deprecated since:** 11

**Substitutes:** [camera.Session.start](arkts-camera-camera-session-i.md#start)(callback:

<!--Device-CaptureSession-start(callback: AsyncCallback<void>): void--><!--Device-CaptureSession-start(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) |
| [7400201](../errorcode-camera.md#7400201-camera-service-error) |

## start

```TypeScript
start(): Promise<void>
```

Starts this session. This API uses a promise to return the result.

**Since:** 10

**Deprecated since:** 11

**Substitutes:** [camera.Session.start](arkts-camera-camera-session-i.md#start)()

<!--Device-CaptureSession-start(): Promise<void>--><!--Device-CaptureSession-start(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) |
| [7400201](../errorcode-camera.md#7400201-camera-service-error) |

## stop

```TypeScript
stop(callback: AsyncCallback<void>): void
```

Stops this session. This API uses an asynchronous callback to return the result.

**Since:** 10

**Deprecated since:** 11

**Substitutes:** [camera.Session.stop](arkts-camera-camera-session-i.md#stop)(callback:

<!--Device-CaptureSession-stop(callback: AsyncCallback<void>): void--><!--Device-CaptureSession-stop(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [7400201](../errorcode-camera.md#7400201-camera-service-error) |

## stop

```TypeScript
stop(): Promise<void>
```

Stops this session. This API uses a promise to return the result.

**Since:** 10

**Deprecated since:** 11

**Substitutes:** [camera.Session.stop](arkts-camera-camera-session-i.md#stop)()

<!--Device-CaptureSession-stop(): Promise<void>--><!--Device-CaptureSession-stop(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [7400201](../errorcode-camera.md#7400201-camera-service-error) |
