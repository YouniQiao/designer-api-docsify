# CameraManager

**CameraManager** implements camera management. Before calling any API in **CameraManager**, you must use [getCameraManager](arkts-camera-camera-getcameramanager-f.md) to obtain a **CameraManager** instance.

**Since:** 23

<!--Device-camera-interface CameraManager--><!--Device-camera-interface CameraManager-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## Modules to Import

```TypeScript
import { camera } from '@kit.CameraKit';
import { cameraPicker } from '@kit.CameraKit';
```

## createCameraInput

```TypeScript
createCameraInput(camera: CameraDevice): CameraInput
```

Creates a **CameraInput** instance with the specified **CameraDevice** instance. This API returns the result synchronously. Before calling this API, call [getSupportedCameras](#getsupportedcameras) to obtain the list of supported camera devices, select the camera device that meets the requirements based on the actual usage scenario, and then create the **CameraInput** instance.

**Since:** 23

**Required permissions:** ohos.permission.CAMERA

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-CameraManager-createCameraInput(camera: CameraDevice): CameraInput--><!--Device-CameraManager-createCameraInput(camera: CameraDevice): CameraInput-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| camera | [CameraDevice](arkts-camera-camera-cameradevice-i.md) | Yes | CameraDevice** instance, which is obtained through [getSupportedCameras](#getsupportedcameras). |

**Return value:**

| Type | Description |
| --- | --- |
| [CameraInput](arkts-camera-camera-camerainput-i.md) | CameraInput** instance created. If the operation fails, an error code defined in [CameraErrorCode]{ |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7400101](../errorcode-camera.md#7400101-invalid-parameter) | Parameter missing or parameter type incorrect. |
| [7400102](../errorcode-camera.md#7400102-invalid-operation) | Operation not allowed.<br>**Applicable version:** 12 and later |
| [7400201](../errorcode-camera.md#7400201-camera-service-error) | Camera service fatal error.<br>**Applicable version:** 12 and later |

## createCameraInput

```TypeScript
createCameraInput(position: CameraPosition, type: CameraType): CameraInput
```

Creates a **CameraInput** instance with the specified camera position and type. This API returns the result synchronously. Before calling this API, specify the camera position and type based on the usage scenario. For example, open the front camera for the selfie feature

**Since:** 23

**Required permissions:** ohos.permission.CAMERA

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-CameraManager-createCameraInput(position: CameraPosition, type: CameraType): CameraInput--><!--Device-CameraManager-createCameraInput(position: CameraPosition, type: CameraType): CameraInput-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| position | [CameraPosition](arkts-camera-camera-cameraposition-e.md) | Yes | Camera position. You need to obtain the supported camera object by calling [getSupportedCameras](#getsupportedcameras) and then obtain the device position information based on the returned camera object. |
| type | [CameraType](arkts-camera-camera-cameratype-e.md) | Yes | Camera type. You need to obtain the supported camera object by calling [getSupportedCameras](#getsupportedcameras) and then obtain the camera type based on the returned camera object. |

**Return value:**

| Type | Description |
| --- | --- |
| [CameraInput](arkts-camera-camera-camerainput-i.md) | CameraInput** instance created. If the operation fails, an error code defined in [CameraErrorCode]{ |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7400101](../errorcode-camera.md#7400101-invalid-parameter) | Parameter missing or parameter type incorrect. |
| [7400102](../errorcode-camera.md#7400102-invalid-operation) | Operation not allowed.<br>**Applicable version:** 12 and later |
| [7400201](../errorcode-camera.md#7400201-camera-service-error) | Camera service fatal error.<br>**Applicable version:** 12 and later |

## createCaptureSession

```TypeScript
createCaptureSession(): CaptureSession
```

Creates a **CaptureSession** instance. This API returns the result synchronously.

**Since:** 10

**Deprecated since:** 11

**Substitutes:** [createSession](#createsession)

<!--Device-CameraManager-createCaptureSession(): CaptureSession--><!--Device-CameraManager-createCaptureSession(): CaptureSession-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Return value:**

| Type | Description |
| --- | --- |
| [CaptureSession](arkts-camera-camera-capturesession-i.md) | CaptureSession** instance created. If the operation fails, an error code defined in [CameraErrorCode]{ |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7400201](../errorcode-camera.md#7400201-camera-service-error) | Camera service fatal error. |

## createMetadataOutput

```TypeScript
createMetadataOutput(metadataObjectTypes: Array<MetadataObjectType>): MetadataOutput
```

Creates a **MetadataOutput** instance. This API returns the result synchronously.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-CameraManager-createMetadataOutput(metadataObjectTypes: Array<MetadataObjectType>): MetadataOutput--><!--Device-CameraManager-createMetadataOutput(metadataObjectTypes: Array<MetadataObjectType>): MetadataOutput-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| metadataObjectTypes | Array&lt;[MetadataObjectType](arkts-camera-camera-metadataobjecttype-e.md)&gt; | Yes | Metadata object types, which are obtained through [getSupportedOutputCapability](#getsupportedoutputcapability). |

**Return value:**

| Type | Description |
| --- | --- |
| [MetadataOutput](arkts-camera-camera-metadataoutput-i.md) | MetadataOutput** instance created. If the operation fails, an error code defined in [CameraErrorCode]{ |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7400101](../errorcode-camera.md#7400101-invalid-parameter) | Parameter missing or parameter type incorrect. |
| [7400201](../errorcode-camera.md#7400201-camera-service-error) | Camera service fatal error.<br>**Applicable version:** 12 and later |

## createPhotoOutput

```TypeScript
createPhotoOutput(profile: Profile, surfaceId: string): PhotoOutput
```

Creates a **PhotoOutput** instance. This API returns the result synchronously. &gt; **NOTE：**&gt; &gt; - This API can only be used to create a **PhotoOutput** object in JPEG format.

**Since:** 10

**Deprecated since:** 11

**Substitutes:** [createPhotoOutput](#createphotooutput)(profile?: Profile)

<!--Device-CameraManager-createPhotoOutput(profile: Profile, surfaceId: string): PhotoOutput--><!--Device-CameraManager-createPhotoOutput(profile: Profile, surfaceId: string): PhotoOutput-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| profile | [Profile](arkts-camera-camera-profile-i.md) | Yes | Supported photo profile, which is obtained through [getSupportedOutputCapability](#getsupportedoutputcapability). |
| surfaceId | string | Yes | Surface ID, which is obtained from [ImageReceiver](../../apis-image-kit/arkts-apis/arkts-image-image-imagereceiver-i.md). |

**Return value:**

| Type | Description |
| --- | --- |
| [PhotoOutput](arkts-camera-camera-photooutput-i.md) | PhotoOutput** instance created. If the operation fails, an error code defined in [CameraErrorCode]{ |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7400101](../errorcode-camera.md#7400101-invalid-parameter) | Parameter missing or parameter type incorrect. |

## createPhotoOutput

```TypeScript
createPhotoOutput(profile?: Profile): PhotoOutput
```

Creates a **PhotoOutput** instance. This API returns the result synchronously.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-CameraManager-createPhotoOutput(profile?: Profile): PhotoOutput--><!--Device-CameraManager-createPhotoOutput(profile?: Profile): PhotoOutput-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| profile | [Profile](arkts-camera-camera-profile-i.md) | No | Supported photo profile, which is obtained through [getSupportedOutputCapability](#getsupportedoutputcapability). <br>In API version 11, this parameter is mandatory. Starting from API version 12, it will overwrite the preconfigured parameters passed in through [preconfig](arkts-camera-camera-photosession-i.md#preconfig). |

**Return value:**

| Type | Description |
| --- | --- |
| [PhotoOutput](arkts-camera-camera-photooutput-i.md) | PhotoOutput** instance created. If the operation fails, an error code defined in [CameraErrorCode]{ |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7400101](../errorcode-camera.md#7400101-invalid-parameter) | Parameter missing or parameter type incorrect. |
| [7400201](../errorcode-camera.md#7400201-camera-service-error) | Camera service fatal error.<br>**Applicable version:** 12 and later |

## createPreviewOutput

```TypeScript
createPreviewOutput(profile: Profile, surfaceId: string): PreviewOutput
```

Creates a **PreviewOutput** instance. This API returns the result synchronously.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-CameraManager-createPreviewOutput(profile: Profile, surfaceId: string): PreviewOutput--><!--Device-CameraManager-createPreviewOutput(profile: Profile, surfaceId: string): PreviewOutput-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| profile | [Profile](arkts-camera-camera-profile-i.md) | Yes | Supported preview profile, which is obtained through [getSupportedOutputCapability](#getsupportedoutputcapability). |
| surfaceId | string | Yes | Surface ID, which is obtained from XComponent or [ImageReceiver](../../apis-image-kit/arkts-apis/arkts-image-image-imagereceiver-i.md). |

**Return value:**

| Type | Description |
| --- | --- |
| [PreviewOutput](arkts-camera-camera-previewoutput-i.md) | PreviewOutput** instance created. If the operation fails, an error code defined in [CameraErrorCode]{ |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7400101](../errorcode-camera.md#7400101-invalid-parameter) | Parameter missing or parameter type incorrect. |
| [7400201](../errorcode-camera.md#7400201-camera-service-error) | Camera service fatal error.<br>**Applicable version:** 12 and later |

## createPreviewOutput

```TypeScript
createPreviewOutput(surfaceId: string): PreviewOutput
```

Creates a **PreviewOutput** instance without configuration. This API returns the result synchronously. It must be used with [preconfig](arkts-camera-camera-photosession-i.md#preconfig).

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-CameraManager-createPreviewOutput(surfaceId: string): PreviewOutput--><!--Device-CameraManager-createPreviewOutput(surfaceId: string): PreviewOutput-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| surfaceId | string | Yes | Surface ID, which is obtained from XComponent or [ImageReceiver](../../apis-image-kit/arkts-apis/arkts-image-image-imagereceiver-i.md). |

**Return value:**

| Type | Description |
| --- | --- |
| [PreviewOutput](arkts-camera-camera-previewoutput-i.md) | PreviewOutput** instance created. If the operation fails, an error code defined in [CameraErrorCode]{ |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7400101](../errorcode-camera.md#7400101-invalid-parameter) | Parameter missing or parameter type incorrect. |
| [7400201](../errorcode-camera.md#7400201-camera-service-error) | Camera service fatal error. |

## createSession

```TypeScript
createSession<T extends Session>(mode: SceneMode): T
```

Creates a **Session** instance with a given scene mode. This API returns the result synchronously.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-CameraManager-createSession<T extends Session>(mode: SceneMode): T--><!--Device-CameraManager-createSession<T extends Session>(mode: SceneMode): T-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mode | [SceneMode](arkts-camera-camera-scenemode-e.md) | Yes | Scene mode. The API does not take effect if the input parameter is invalid (for example, the value is out of range, null, or undefined). |

**Return value:**

| Type | Description |
| --- | --- |
| T | Session** instance created. If the operation fails, an error code defined in [CameraErrorCode]{ |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7400101](../errorcode-camera.md#7400101-invalid-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.<br>**Applicable version:** 19 and later |
| [7400201](../errorcode-camera.md#7400201-camera-service-error) | Camera service fatal error. |

## createVideoOutput

```TypeScript
createVideoOutput(profile: VideoProfile, surfaceId: string): VideoOutput
```

Creates a **VideoOutput** instance. This API returns the result synchronously. In video recording mode, if SDR or HDR VIVID is enabled, the camera format and color space must be configured according to the relationships specified in the table below. Configurations that do not match the table will cause issues such as preview exceptions. | SDR/HDR Photo Capture | CameraFormat | ColorSpace | |--------------------|--------------------------|------------------| | SDR | CAMERA_FORMAT_YUV_420_SP | BT709_LIMIT | | HDR_VIVID | CAMERA_FORMAT_YCRCB_P010<br>CAMERA_FORMAT_YCBCR_P010 | BT2020_HLG_LIMIT<br>BT2020_HLG_FULL |

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-CameraManager-createVideoOutput(profile: VideoProfile, surfaceId: string): VideoOutput--><!--Device-CameraManager-createVideoOutput(profile: VideoProfile, surfaceId: string): VideoOutput-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| profile | [VideoProfile](arkts-camera-camera-videoprofile-i.md) | Yes | Supported video profile, which is obtained through [getSupportedOutputCapability](#getsupportedoutputcapability). |
| surfaceId | string | Yes | Surface ID, which is obtained from [AVRecorder](../../apis-media-kit/arkts-apis/arkts-media-media-avrecorder-i.md). |

**Return value:**

| Type | Description |
| --- | --- |
| [VideoOutput](arkts-camera-camera-videooutput-i.md) | VideoOutput** instance created. If the operation fails, an error code defined in [CameraErrorCode]{ |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7400101](../errorcode-camera.md#7400101-invalid-parameter) | Parameter missing or parameter type incorrect. |
| [7400201](../errorcode-camera.md#7400201-camera-service-error) | Camera service fatal error.<br>**Applicable version:** 12 and later |

## createVideoOutput

```TypeScript
createVideoOutput(surfaceId: string): VideoOutput
```

Creates a **VideoOutput** instance without configuration. This API returns the result synchronously. It must be used with [preconfig](arkts-camera-camera-videosession-i.md#preconfig).

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-CameraManager-createVideoOutput(surfaceId: string): VideoOutput--><!--Device-CameraManager-createVideoOutput(surfaceId: string): VideoOutput-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| surfaceId | string | Yes | Surface ID, which is obtained from [AVRecorder](../../apis-media-kit/arkts-apis/arkts-media-media-avrecorder-i.md). |

**Return value:**

| Type | Description |
| --- | --- |
| [VideoOutput](arkts-camera-camera-videooutput-i.md) | VideoOutput** instance created. If the operation fails, an error code defined in [CameraErrorCode]{ |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7400101](../errorcode-camera.md#7400101-invalid-parameter) | Parameter missing or parameter type incorrect. |
| [7400201](../errorcode-camera.md#7400201-camera-service-error) | Camera service fatal error. |

## getCameraConcurrentInfos

```TypeScript
getCameraConcurrentInfos(cameras: Array<CameraDevice>): Array<CameraConcurrentInfo>
```

Obtains the concurrency information of the specified cameras. If the return value is an empty array, concurrency is not supported.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-CameraManager-getCameraConcurrentInfos(cameras: Array<CameraDevice>): Array<CameraConcurrentInfo>--><!--Device-CameraManager-getCameraConcurrentInfos(cameras: Array<CameraDevice>): Array<CameraConcurrentInfo>-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| cameras | Array&lt;[CameraDevice](arkts-camera-camera-cameradevice-i.md)&gt; | Yes | Array of **CameraDevice** objects. You are advised to use the front and rear cameras obtained by calling [getCameraDevice](#getcameradevice). |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;[CameraConcurrentInfo](arkts-camera-camera-cameraconcurrentinfo-i.md)&gt; | Array of concurrency information corresponding to the provided CameraDevice objects, with a one-to-one mapping. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7400201](../errorcode-camera.md#7400201-camera-service-error) | Camera service fatal error. |

## getCameraDevice

```TypeScript
getCameraDevice(position: CameraPosition, type: CameraType): CameraDevice
```

Obtains the specified camera based on the camera position and type. Obtains the camera lens of the specified [CameraPosition](arkts-camera-camera-cameraposition-e.md) and [CameraType](arkts-camera-camera-cameratype-e.md). If the returned result is undefined, the camera lens is not found on the current device.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-CameraManager-getCameraDevice(position: CameraPosition, type: CameraType): CameraDevice--><!--Device-CameraManager-getCameraDevice(position: CameraPosition, type: CameraType): CameraDevice-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| position | [CameraPosition](arkts-camera-camera-cameraposition-e.md) | Yes | Camera position. |
| type | [CameraType](arkts-camera-camera-cameratype-e.md) | Yes | Camera type. |

**Return value:**

| Type | Description |
| --- | --- |
| [CameraDevice](arkts-camera-camera-cameradevice-i.md) | Camera obtained. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7400201](../errorcode-camera.md#7400201-camera-service-error) | Camera service fatal error. |

## getCameraDevices

```TypeScript
getCameraDevices(position: CameraPosition, types: Array<CameraType>, connectType: ConnectionType): Array<CameraDevice>
```

Obtains the list of cameras that meet the search criteria based on the camera position, camera types, and connection type.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-CameraManager-getCameraDevices(position: CameraPosition, types: Array<CameraType>, connectType: ConnectionType): Array<CameraDevice>--><!--Device-CameraManager-getCameraDevices(position: CameraPosition, types: Array<CameraType>, connectType: ConnectionType): Array<CameraDevice>-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| position | [CameraPosition](arkts-camera-camera-cameraposition-e.md) | Yes | Camera position. |
| types | Array&lt;[CameraType](arkts-camera-camera-cameratype-e.md)&gt; | Yes | Array of camera types. |
| connectType | [ConnectionType](arkts-camera-camera-connectiontype-e.md) | Yes | Camera connection type. |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;[CameraDevice](arkts-camera-camera-cameradevice-i.md)&gt; | Array of cameras that meet the search criteria. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7400201](../errorcode-camera.md#7400201-camera-service-error) | Camera service fatal error. |

## getSupportedCameras

```TypeScript
getSupportedCameras(): Array<CameraDevice>
```

Obtains the supported cameras (such as the default camera whose **CameraType** is **CAMERA_TYPE_DEFAULT**). This API returns the result synchronously. Other cameras (such as the telephoto camera whose **CameraType** is **CAMERA_TYPE_TELEPHOTO**) can be obtained using [getCameraDevices](#getcameradevices) API.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-CameraManager-getSupportedCameras(): Array<CameraDevice>--><!--Device-CameraManager-getSupportedCameras(): Array<CameraDevice>-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;[CameraDevice](arkts-camera-camera-cameradevice-i.md)&gt; | Array of camera devices supported. |

## getSupportedFullOutputCapability

```TypeScript
getSupportedFullOutputCapability(camera: CameraDevice, mode: SceneMode): CameraOutputCapability
```

Obtains the complete output capabilities supported by a specified camera in a specified mode, including YUV, HEIF, and HDR. &gt; **NOTE：**&gt; &gt; Before using YUV, HEIF, or HDR, you need to explicitly call this method to ensure that the complete output &gt; capabilities are obtained.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-CameraManager-getSupportedFullOutputCapability(camera: CameraDevice, mode: SceneMode): CameraOutputCapability--><!--Device-CameraManager-getSupportedFullOutputCapability(camera: CameraDevice, mode: SceneMode): CameraOutputCapability-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| camera | [CameraDevice](arkts-camera-camera-cameradevice-i.md) | Yes | Camera device. |
| mode | [SceneMode](arkts-camera-camera-scenemode-e.md) | Yes | Scene mode. |

**Return value:**

| Type | Description |
| --- | --- |
| [CameraOutputCapability](arkts-camera-camera-cameraoutputcapability-i.md) | Camera output capability obtained. |

## getSupportedOutputCapability

```TypeScript
getSupportedOutputCapability(camera: CameraDevice): CameraOutputCapability
```

Obtains the output capability supported by a camera device. This API returns the result synchronously.

**Since:** 10

**Deprecated since:** 11

**Substitutes:** [getSupportedOutputCapability](#getsupportedoutputcapability)(camera: CameraDevice, mode: SceneMode)

<!--Device-CameraManager-getSupportedOutputCapability(camera: CameraDevice): CameraOutputCapability--><!--Device-CameraManager-getSupportedOutputCapability(camera: CameraDevice): CameraOutputCapability-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| camera | [CameraDevice](arkts-camera-camera-cameradevice-i.md) | Yes | Camera device. |

**Return value:**

| Type | Description |
| --- | --- |
| [CameraOutputCapability](arkts-camera-camera-cameraoutputcapability-i.md) | Camera output capability obtained. |

## getSupportedOutputCapability

```TypeScript
getSupportedOutputCapability(camera: CameraDevice, mode: SceneMode): CameraOutputCapability
```

Obtains the output capability supported by a camera device in a given scene mode. This API returns the result synchronously.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-CameraManager-getSupportedOutputCapability(camera: CameraDevice, mode: SceneMode): CameraOutputCapability--><!--Device-CameraManager-getSupportedOutputCapability(camera: CameraDevice, mode: SceneMode): CameraOutputCapability-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| camera | [CameraDevice](arkts-camera-camera-cameradevice-i.md) | Yes | Camera device. |
| mode | [SceneMode](arkts-camera-camera-scenemode-e.md) | Yes | Scene mode. |

**Return value:**

| Type | Description |
| --- | --- |
| [CameraOutputCapability](arkts-camera-camera-cameraoutputcapability-i.md) | Camera output capability obtained. |

## getSupportedSceneModes

```TypeScript
getSupportedSceneModes(camera: CameraDevice): Array<SceneMode>
```

Obtains the scene modes supported by a camera device. This API returns the result synchronously.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-CameraManager-getSupportedSceneModes(camera: CameraDevice): Array<SceneMode>--><!--Device-CameraManager-getSupportedSceneModes(camera: CameraDevice): Array<SceneMode>-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| camera | [CameraDevice](arkts-camera-camera-cameradevice-i.md) | Yes | Camera device. |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;[SceneMode](arkts-camera-camera-scenemode-e.md)&gt; | Array of scene modes supported. |

## getTorchMode

```TypeScript
getTorchMode(): TorchMode
```

Obtains the flashlight mode of this camera device.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-CameraManager-getTorchMode(): TorchMode--><!--Device-CameraManager-getTorchMode(): TorchMode-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Return value:**

| Type | Description |
| --- | --- |
| [TorchMode](arkts-camera-camera-torchmode-e.md) | Flashlight mode. |

## isCameraMuted

```TypeScript
isCameraMuted(): boolean
```

Checks whether this camera is muted.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-CameraManager-isCameraMuted(): boolean--><!--Device-CameraManager-isCameraMuted(): boolean-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Check result for whether the camera is muted. **true** if muted, **false** otherwise. |

## isTorchModeSupported

```TypeScript
isTorchModeSupported(mode: TorchMode): boolean
```

Checks whether a flashlight mode is supported.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-CameraManager-isTorchModeSupported(mode: TorchMode): boolean--><!--Device-CameraManager-isTorchModeSupported(mode: TorchMode): boolean-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mode | [TorchMode](arkts-camera-camera-torchmode-e.md) | Yes | Flashlight mode. If the input parameter is null or undefined, it is treated as 0 and the flashlight is turned off. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Check result for the support of the flashlight mode. **true** if supported, **false** otherwise. If the API call fails, undefined is returned. |

## isTorchSupported

```TypeScript
isTorchSupported(): boolean
```

Checks whether the camera device supports the flashlight.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-CameraManager-isTorchSupported(): boolean--><!--Device-CameraManager-isTorchSupported(): boolean-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Whether the device supports the flashlight. **true** if supported, **false** otherwise. <br>If **false** is returned, [isTorchModeSupported]{ |

## offCameraStatus

```TypeScript
offCameraStatus(callback?: AsyncCallback<CameraStatusInfo>): void
```

Unsubscribes from camera status change event callback.

**Since:** 23

<!--Device-CameraManager-offCameraStatus(callback?: AsyncCallback<CameraStatusInfo>): void--><!--Device-CameraManager-offCameraStatus(callback?: AsyncCallback<CameraStatusInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;[CameraStatusInfo](arkts-camera-camera-camerastatusinfo-i.md)&gt; | No | Callback used to get the camera status change. |

## offFoldStatusChange

```TypeScript
offFoldStatusChange(callback?: AsyncCallback<FoldStatusInfo>): void
```

Unsubscribes from fold status change event callback.

**Since:** 23

<!--Device-CameraManager-offFoldStatusChange(callback?: AsyncCallback<FoldStatusInfo>): void--><!--Device-CameraManager-offFoldStatusChange(callback?: AsyncCallback<FoldStatusInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;[FoldStatusInfo](arkts-camera-camera-foldstatusinfo-i.md)&gt; | No | Callback used to get the fold status change. |

## offTorchStatusChange

```TypeScript
offTorchStatusChange(callback?: AsyncCallback<TorchStatusInfo>): void
```

Unsubscribes torch status change event callback.

**Since:** 23

<!--Device-CameraManager-offTorchStatusChange(callback?: AsyncCallback<TorchStatusInfo>): void--><!--Device-CameraManager-offTorchStatusChange(callback?: AsyncCallback<TorchStatusInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;[TorchStatusInfo](arkts-camera-camera-torchstatusinfo-i.md)&gt; | No | Callback used to return the torch status change |

## off('cameraStatus')

```TypeScript
off(type: 'cameraStatus', callback?: AsyncCallback<CameraStatusInfo>): void
```

Unsubscribes from camera status events. This API uses an asynchronous callback to return the result.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-CameraManager-off(type: 'cameraStatus', callback?: AsyncCallback<CameraStatusInfo>): void--><!--Device-CameraManager-off(type: 'cameraStatus', callback?: AsyncCallback<CameraStatusInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'cameraStatus' | Yes | Event type. The value is fixed at **'cameraStatus'**. The event can be listened for when a **CameraManager** instance is obtained. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;[CameraStatusInfo](arkts-camera-camera-camerastatusinfo-i.md)&gt; | No | Callback used to return the result. If this parameter is specified, the subscription to the specified event with the specified callback is canceled. (The callback object cannot be an anonymous function.) Otherwise, the subscriptions to the specified event with all the callbacks are canceled. |

## off('foldStatusChange')

```TypeScript
off(type: 'foldStatusChange', callback?: AsyncCallback<FoldStatusInfo>): void
```

Unsubscribes from fold state change events of the foldable device.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-CameraManager-off(type: 'foldStatusChange', callback?: AsyncCallback<FoldStatusInfo>): void--><!--Device-CameraManager-off(type: 'foldStatusChange', callback?: AsyncCallback<FoldStatusInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'foldStatusChange' | Yes | Event type. The value is fixed at **'foldStatusChange'**. The event is triggered when the fold state of the foldable device changes. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;[FoldStatusInfo](arkts-camera-camera-foldstatusinfo-i.md)&gt; | No | Callback used to return the fold state information about the foldable device. If this parameter is specified, the subscription to the specified event with the specified callback is canceled. (The callback object cannot be an anonymous function.) Otherwise, the subscriptions to the specified event with all the callbacks are canceled. |

## off('torchStatusChange')

```TypeScript
off(type: 'torchStatusChange', callback?: AsyncCallback<TorchStatusInfo>): void
```

Unsubscribes from flashlight status change events. This API uses an asynchronous callback to return the result.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-CameraManager-off(type: 'torchStatusChange', callback?: AsyncCallback<TorchStatusInfo>): void--><!--Device-CameraManager-off(type: 'torchStatusChange', callback?: AsyncCallback<TorchStatusInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'torchStatusChange' | Yes | Event type. The value is fixed at **'torchStatusChange'**. The event can be listened for when a **CameraManager** instance is obtained. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;[TorchStatusInfo](arkts-camera-camera-torchstatusinfo-i.md)&gt; | No | Callback used to return the result. If this parameter is specified, the subscription to the specified event with the specified callback is canceled. (The callback object cannot be an anonymous function.) Otherwise, the subscriptions to the specified event with all the callbacks are canceled. |

## onCameraStatus

```TypeScript
onCameraStatus(callback: AsyncCallback<CameraStatusInfo>): void
```

Subscribes camera status change event callback.

**Since:** 23

<!--Device-CameraManager-onCameraStatus(callback: AsyncCallback<CameraStatusInfo>): void--><!--Device-CameraManager-onCameraStatus(callback: AsyncCallback<CameraStatusInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;[CameraStatusInfo](arkts-camera-camera-camerastatusinfo-i.md)&gt; | Yes | Callback used to get the camera status change. |

## onFoldStatusChange

```TypeScript
onFoldStatusChange(callback: AsyncCallback<FoldStatusInfo>): void
```

Subscribes fold status change event callback.

**Since:** 23

<!--Device-CameraManager-onFoldStatusChange(callback: AsyncCallback<FoldStatusInfo>): void--><!--Device-CameraManager-onFoldStatusChange(callback: AsyncCallback<FoldStatusInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;[FoldStatusInfo](arkts-camera-camera-foldstatusinfo-i.md)&gt; | Yes | Callback used to get the fold status change. |

## onTorchStatusChange

```TypeScript
onTorchStatusChange(callback: AsyncCallback<TorchStatusInfo>): void
```

Subscribes torch status change event callback.

**Since:** 23

<!--Device-CameraManager-onTorchStatusChange(callback: AsyncCallback<TorchStatusInfo>): void--><!--Device-CameraManager-onTorchStatusChange(callback: AsyncCallback<TorchStatusInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;[TorchStatusInfo](arkts-camera-camera-torchstatusinfo-i.md)&gt; | Yes | Callback used to return the torch status change |

## on('cameraStatus')

```TypeScript
on(type: 'cameraStatus', callback: AsyncCallback<CameraStatusInfo>): void
```

Subscribes to camera status events. This API uses an asynchronous callback to return the result. &gt; **NOTE：**&gt; &gt; Currently, you cannot use **off()** to unregister the callback in the callback method of **on()**.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-CameraManager-on(type: 'cameraStatus', callback: AsyncCallback<CameraStatusInfo>): void--><!--Device-CameraManager-on(type: 'cameraStatus', callback: AsyncCallback<CameraStatusInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'cameraStatus' | Yes | Event type. The value is fixed at **'cameraStatus'**. The event can be listened for when a **CameraManager** instance is obtained. This event is triggered and the corresponding information is returned only when the camera device is enabled or disabled. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;[CameraStatusInfo](arkts-camera-camera-camerastatusinfo-i.md)&gt; | Yes | Callback used to return the camera status change. |

## on('foldStatusChange')

```TypeScript
on(type: 'foldStatusChange', callback: AsyncCallback<FoldStatusInfo>): void
```

Subscribes to fold status change events of the foldable device. This API uses an asynchronous callback to return the result. &gt; **NOTE：**&gt; &gt; Currently, you cannot use **off()** to unregister the callback in the callback method of **on()**.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-CameraManager-on(type: 'foldStatusChange', callback: AsyncCallback<FoldStatusInfo>): void--><!--Device-CameraManager-on(type: 'foldStatusChange', callback: AsyncCallback<FoldStatusInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'foldStatusChange' | Yes | Event type. The value is fixed at **'foldStatusChange'**. The event is triggered when the fold state of the foldable device changes. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;[FoldStatusInfo](arkts-camera-camera-foldstatusinfo-i.md)&gt; | Yes | Callback used to return the fold state information about the foldable device. |

## on('torchStatusChange')

```TypeScript
on(type: 'torchStatusChange', callback: AsyncCallback<TorchStatusInfo>): void
```

Subscribes to flashlight status change events. This API uses an asynchronous callback to return the result. &gt; **NOTE：**&gt; &gt; Currently, you cannot use **off()** to unregister the callback in the callback method of **on()**.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-CameraManager-on(type: 'torchStatusChange', callback: AsyncCallback<TorchStatusInfo>): void--><!--Device-CameraManager-on(type: 'torchStatusChange', callback: AsyncCallback<TorchStatusInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'torchStatusChange' | Yes | Event type. The value is fixed at **'torchStatusChange'**. The event can be listened for when a **CameraManager** instance is obtained. Currently, this event is triggered only in the following scenarios: The flashlight is turned on or turned off, or becomes unavailable or available. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;[TorchStatusInfo](arkts-camera-camera-torchstatusinfo-i.md)&gt; | Yes | Callback used to return the flashlight status. |

## setTorchMode

```TypeScript
setTorchMode(mode: TorchMode): void
```

Sets the flashlight mode.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-CameraManager-setTorchMode(mode: TorchMode): void--><!--Device-CameraManager-setTorchMode(mode: TorchMode): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mode | [TorchMode](arkts-camera-camera-torchmode-e.md) | Yes | Flashlight mode. If the input parameter is null or undefined, it is treated as 0 and the flashlight is turned off. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7400101](../errorcode-camera.md#7400101-invalid-parameter) | Parameter missing or parameter type incorrect.<br>**Applicable version:** 11 - 17 |
| [7400102](../errorcode-camera.md#7400102-invalid-operation) | Operation not allowed.<br>**Applicable version:** 12 and later |
| [7400201](../errorcode-camera.md#7400201-camera-service-error) | Camera service fatal error.<br>**Applicable version:** 12 and later |

