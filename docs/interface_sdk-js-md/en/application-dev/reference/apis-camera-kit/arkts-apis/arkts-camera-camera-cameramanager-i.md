# CameraManager

相机管理器类，使用前需要通过[getCameraManager](arkts-camera-camera-getcameramanager-f.md#getcameramanager)接口获取相机管理实例。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-camera-interface CameraManager--><!--Device-camera-interface CameraManager-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## Modules to Import

```TypeScript
import { camera } from 'kits/@kit.CameraKit';
```

## createCameraInput

```TypeScript
createCameraInput(camera: CameraDevice): CameraInput
```

使用CameraDevice对象创建CameraInput实例，同步返回结果。

该接口使用前首先通过[getSupportedCameras](arkts-camera-camera-cameramanager-i.md#getsupportedcameras)接口查询当前设备支持的相机设备信息列表，开发者需要根据具体使用场景选择符合需求的相机设备，然后使用该接口创建CameraInput实例。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.CAMERA

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-CameraManager-createCameraInput(camera: CameraDevice): CameraInput--><!--Device-CameraManager-createCameraInput(camera: CameraDevice): CameraInput-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| camera | [CameraDevice](arkts-camera-camera-cameradevice-i.md) | Yes | CameraDevice对象，通过 [getSupportedCameras](arkts-camera-camera-cameramanager-i.md#getsupportedcameras) 接口获取。 |

**Return value:**

| Type | Description |
| --- | --- |
| [CameraInput](arkts-camera-camera-camerainput-i.md) | 返回CameraInput实例。接口调用失败会返回相应错误码，错误码类型为[CameraErrorCode]{ |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 7400101 | Parameter missing or parameter type incorrect. |
| 7400102 | Operation not allowed.<br>**Applicable version:** 12 and later |
| 7400201 | Camera service fatal error.<br>**Applicable version:** 12 and later |

## createCameraInput

```TypeScript
createCameraInput(position: CameraPosition, type: CameraType): CameraInput
```

根据相机位置和类型创建CameraInput实例，同步返回结果。

该接口使用前需要开发者根据应用具体使用场景自行指定相机位置和类型，例如打开前置相机进入自拍功能。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.CAMERA

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-CameraManager-createCameraInput(position: CameraPosition, type: CameraType): CameraInput--><!--Device-CameraManager-createCameraInput(position: CameraPosition, type: CameraType): CameraInput-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| position | [CameraPosition](arkts-camera-camera-cameraposition-e.md) | Yes | 相机位置，首先通过 [getSupportedCameras](arkts-camera-camera-cameramanager-i.md#getsupportedcameras) 接口获取支持的相机设备对象，然后根据返回的相机设备对象获取设备位置信息。 |
| type | [CameraType](arkts-camera-camera-cameratype-e.md) | Yes | 相机类型，首先通过 [getSupportedCameras](arkts-camera-camera-cameramanager-i.md#getsupportedcameras) 接口获取 支持的相机设备对象，然后根据返回的相机设备对象获取设备类型信息。 |

**Return value:**

| Type | Description |
| --- | --- |
| [CameraInput](arkts-camera-camera-camerainput-i.md) | 返回CameraInput实例。接口调用失败会返回相应错误码，错误码类型为[CameraErrorCode]{ |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 7400101 | Parameter missing or parameter type incorrect. |
| 7400102 | Operation not allowed.<br>**Applicable version:** 12 and later |
| 7400201 | Camera service fatal error.<br>**Applicable version:** 12 and later |

## createCaptureSession

```TypeScript
createCaptureSession(): CaptureSession
```

创建CaptureSession实例，同步返回结果。

> **说明：**
> 
> 从 API version 10开始支持，从API version 11开始废弃。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** 11

**Substitutes:** [camera.CameraManager.createSession](arkts-camera-camera-cameramanager-i.md#createsession)

<!--Device-CameraManager-createCaptureSession(): CaptureSession--><!--Device-CameraManager-createCaptureSession(): CaptureSession-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Return value:**

| Type | Description |
| --- | --- |
| [CaptureSession](arkts-camera-camera-capturesession-i.md) | CaptureSession实例。接口调用失败会返回相应错误码，错误码类型[CameraErrorCode]{ |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 7400201 | Camera service fatal error. |

## createDeferredPreviewOutput

```TypeScript
createDeferredPreviewOutput(profile: Profile): PreviewOutput
```

创建延迟预览输出对象，在配流时替代普通的预览输出对象加入数据流。

**Since:** 24

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-CameraManager-createDeferredPreviewOutput(profile: Profile): PreviewOutput--><!--Device-CameraManager-createDeferredPreviewOutput(profile: Profile): PreviewOutput-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| profile | [Profile](arkts-camera-camera-profile-i.md) | Yes | 支持的预览配置信息，通过 [getSupportedOutputCapability](arkts-camera-camera-cameramanager-i.md#getsupportedoutputcapability) 接口获取。 |

**Return value:**

| Type | Description |
| --- | --- |
| [PreviewOutput](arkts-camera-camera-previewoutput-i.md) | PreviewOutput实例。接口调用失败会返回相应错误码，错误码类型[CameraErrorCode]{ |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 7400101 | Parameter missing or parameter type incorrect. |
| 7400201 | Camera service fatal error.<br>**Applicable version:** 24 and later |
| 202 | Not System Application.<br>**Applicable version:** 12 - 23 |

## createMetadataOutput

```TypeScript
createMetadataOutput(metadataObjectTypes: Array<MetadataObjectType>): MetadataOutput
```

创建metadata流输出对象，同步返回结果。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-CameraManager-createMetadataOutput(metadataObjectTypes: Array<MetadataObjectType>): MetadataOutput--><!--Device-CameraManager-createMetadataOutput(metadataObjectTypes: Array<MetadataObjectType>): MetadataOutput-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| metadataObjectTypes | Array&lt;MetadataObjectType&gt; | Yes | metadata流类型信息，通过 [getSupportedOutputCapability](arkts-camera-camera-cameramanager-i.md#getsupportedoutputcapability) 接口获取。 |

**Return value:**

| Type | Description |
| --- | --- |
| [MetadataOutput](arkts-camera-camera-metadataoutput-i.md) | MetadataOutput实例。接口调用失败会返回相应错误码，错误码类型[CameraErrorCode]{ |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 7400101 | Parameter missing or parameter type incorrect. |
| 7400201 | Camera service fatal error.<br>**Applicable version:** 12 and later |

## createPhotoOutput

```TypeScript
createPhotoOutput(profile: Profile, surfaceId: string): PhotoOutput
```

创建拍照输出对象，同步返回结果。

> **说明：**
> 
> - 从API version 10开始支持，从API version 11开始废弃。
> 
> - 该接口只支持创建JPEG格式的拍照输出对象。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** 11

**Substitutes:** [camera.CameraManager.createPhotoOutput](arkts-camera-camera-cameramanager-i.md#createphotooutput)(profile?:

<!--Device-CameraManager-createPhotoOutput(profile: Profile, surfaceId: string): PhotoOutput--><!--Device-CameraManager-createPhotoOutput(profile: Profile, surfaceId: string): PhotoOutput-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| profile | [Profile](arkts-camera-camera-profile-i.md) | Yes | 支持的拍照配置信息，通过 [getSupportedOutputCapability](arkts-camera-camera-cameramanager-i.md#getsupportedoutputcapability) 接口获取。 |
| surfaceId | string | Yes | 从[ImageReceiver](../../apis-image-kit/arkts-apis/arkts-image-image-imagereceiver-i.md/arkts-image-image-imagereceiver-i.md)获取的surfaceId。 |

**Return value:**

| Type | Description |
| --- | --- |
| [PhotoOutput](arkts-camera-camera-photooutput-i.md) | PhotoOutput实例。接口调用失败会返回相应错误码，错误码类型[CameraErrorCode]{ |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 7400101 | Parameter missing or parameter type incorrect. |

## createPhotoOutput

```TypeScript
createPhotoOutput(profile?: Profile): PhotoOutput
```

创建拍照输出对象，同步返回结果。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-CameraManager-createPhotoOutput(profile?: Profile): PhotoOutput--><!--Device-CameraManager-createPhotoOutput(profile?: Profile): PhotoOutput-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| profile | [Profile](arkts-camera-camera-profile-i.md) | No | 支持的拍照配置信息，通过 [getSupportedOutputCapability](arkts-camera-camera-cameramanager-i.md#getsupportedoutputcapability) 接口获取。 &lt;br&gt;API version 11时，该参数必填；从API version 12开始，如果使用[preconfig](arkts-camera-camera-photosession-i.md#preconfig)进行预配置，传入 profile参数会覆盖preconfig的预配置参数。 |

**Return value:**

| Type | Description |
| --- | --- |
| [PhotoOutput](arkts-camera-camera-photooutput-i.md) | PhotoOutput实例。接口调用失败会返回相应错误码，错误码类型[CameraErrorCode]{ |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 7400101 | Parameter missing or parameter type incorrect. |
| 7400201 | Camera service fatal error.<br>**Applicable version:** 12 and later |

## createPreviewOutput

```TypeScript
createPreviewOutput(profile: Profile, surfaceId: string): PreviewOutput
```

创建预览输出对象，同步返回结果。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-CameraManager-createPreviewOutput(profile: Profile, surfaceId: string): PreviewOutput--><!--Device-CameraManager-createPreviewOutput(profile: Profile, surfaceId: string): PreviewOutput-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| profile | [Profile](arkts-camera-camera-profile-i.md) | Yes | 支持的预览配置信息，通过 [getSupportedOutputCapability](arkts-camera-camera-cameramanager-i.md#getsupportedoutputcapability) 接口获取。 |
| surfaceId | string | Yes | 从[XComponent](../../apis-arkui/arkts-apis/arkts-arkui-xcomponent-xcomponent-f.md/arkts-arkui-xcomponent-xcomponent-f.md#xcomponent)或者 [ImageReceiver](../../apis-image-kit/arkts-apis/arkts-image-image-imagereceiver-i.md/arkts-image-image-imagereceiver-i.md)组件获取的surfaceId。 |

**Return value:**

| Type | Description |
| --- | --- |
| [PreviewOutput](arkts-camera-camera-previewoutput-i.md) | PreviewOutput实例。接口调用失败会返回相应错误码，错误码类型[CameraErrorCode]{ |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 7400101 | Parameter missing or parameter type incorrect. |
| 7400201 | Camera service fatal error.<br>**Applicable version:** 12 and later |

## createPreviewOutput

```TypeScript
createPreviewOutput(surfaceId: string): PreviewOutput
```

创建无配置信息的预览输出对象，同步返回结果。该接口需配合[preconfig](arkts-camera-camera-photosession-i.md#preconfig)一起使用。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-CameraManager-createPreviewOutput(surfaceId: string): PreviewOutput--><!--Device-CameraManager-createPreviewOutput(surfaceId: string): PreviewOutput-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| surfaceId | string | Yes | 从[XComponent](../../apis-arkui/arkts-apis/arkts-arkui-xcomponent-xcomponent-f.md/arkts-arkui-xcomponent-xcomponent-f.md#xcomponent)或者 [ImageReceiver](../../apis-image-kit/arkts-apis/arkts-image-image-imagereceiver-i.md/arkts-image-image-imagereceiver-i.md)组件获取的surfaceId。 |

**Return value:**

| Type | Description |
| --- | --- |
| [PreviewOutput](arkts-camera-camera-previewoutput-i.md) | PreviewOutput实例。接口调用失败会返回相应错误码，错误码类型[CameraErrorCode]{ |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 7400101 | Parameter missing or parameter type incorrect. |
| 7400201 | Camera service fatal error. |

## createSession

```TypeScript
createSession<T extends Session>(mode: SceneMode): T
```

创建指定SceneMode的Session实例，同步返回结果。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-CameraManager-createSession<T extends Session>(mode: SceneMode): T--><!--Device-CameraManager-createSession<T extends Session>(mode: SceneMode): T-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mode | [SceneMode](arkts-camera-camera-scenemode-e.md) | Yes | 相机支持的模式。如果传入的参数异常（如超出范围、传入null或未定义等），实际接口不会生效。 |

**Return value:**

| Type | Description |
| --- | --- |
| T | Session实例。接口调用失败会返回相应的错误码，错误码类型为[CameraErrorCode]{ |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 7400101 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.<br>**Applicable version:** 19 and later |
| 7400201 | Camera service fatal error. |

## createVideoOutput

```TypeScript
createVideoOutput(profile: VideoProfile, surfaceId: string): VideoOutput
```

创建录像输出对象，同步返回结果。

在录像模式下，使能SDR或HDR_VIVID拍摄效果时，CameraFormat与ColorSpace必须按照下列表格中的对应关系配置，若不满足表格中CameraFormat与ColorSpace配置，会导致预览异常等问题。

| SDR/HDR拍摄 | CameraFormat | ColorSpace |  
|--------------------|--------------------------|------------------|  
| SDR | CAMERA_FORMAT_YUV_420_SP | BT709_LIMIT |  
| HDR_VIVID | CAMERA_FORMAT_YCRCB_P010&lt;br&gt;CAMERA_FORMAT_YCBCR_P010 | BT2020_HLG_LIMIT&lt;br&gt;BT2020_HLG_FULL |

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-CameraManager-createVideoOutput(profile: VideoProfile, surfaceId: string): VideoOutput--><!--Device-CameraManager-createVideoOutput(profile: VideoProfile, surfaceId: string): VideoOutput-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| profile | [VideoProfile](arkts-camera-camera-videoprofile-i.md) | Yes | 支持的录像配置信息，通过 [getSupportedOutputCapability](arkts-camera-camera-cameramanager-i.md#getsupportedoutputcapability) 接口获取。 |
| surfaceId | string | Yes | 从[AVRecorder](@ohos.multimedia.media:media.AVRecorder)获取的surfaceId。 |

**Return value:**

| Type | Description |
| --- | --- |
| [VideoOutput](arkts-camera-camera-videooutput-i.md) | VideoOutput实例。接口调用失败会返回相应错误码，错误码类型[CameraErrorCode]{ |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 7400101 | Parameter missing or parameter type incorrect. |
| 7400201 | Camera service fatal error.<br>**Applicable version:** 12 and later |

## createVideoOutput

```TypeScript
createVideoOutput(surfaceId: string): VideoOutput
```

创建无配置信息的录像输出对象，同步返回结果。该接口需配合[preconfig](arkts-camera-camera-videosession-i.md#preconfig)功能一起使用。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-CameraManager-createVideoOutput(surfaceId: string): VideoOutput--><!--Device-CameraManager-createVideoOutput(surfaceId: string): VideoOutput-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| surfaceId | string | Yes | 从[AVRecorder](@ohos.multimedia.media:media.AVRecorder)获取的surfaceId。 |

**Return value:**

| Type | Description |
| --- | --- |
| [VideoOutput](arkts-camera-camera-videooutput-i.md) | VideoOutput实例。接口调用失败会返回相应错误码，错误码类型[CameraErrorCode]{ |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 7400101 | Parameter missing or parameter type incorrect. |
| 7400201 | Camera service fatal error. |

## getCameraConcurrentInfos

```TypeScript
getCameraConcurrentInfos(cameras: Array<CameraDevice>): Array<CameraConcurrentInfo>
```

获取指定相机设备的并发信息。返回空数组表示不支持并发。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-CameraManager-getCameraConcurrentInfos(cameras: Array<CameraDevice>): Array<CameraConcurrentInfo>--><!--Device-CameraManager-getCameraConcurrentInfos(cameras: Array<CameraDevice>): Array<CameraConcurrentInfo>-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| cameras | Array&lt;CameraDevice&gt; | Yes | 一组CameraDevice相机设备，并得到与这一组CameraDevice对应的并发信息，推荐设置为由 [getCameraDevice](arkts-camera-camera-cameramanager-i.md#getcameradevice)获取的前置与后置两个用于并发的相机设备。 |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;CameraConcurrentInfo&gt; | 一组CameraDevice相机设备对象对应的并发信息，与CameraDevice相机设备一一对应。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 7400201 | Camera service fatal error. |

## getCameraDevice

```TypeScript
getCameraDevice(position: CameraPosition, type: CameraType): CameraDevice
```

根据相机位置和相机类型查询对应相机。

获取指定[CameraPosition](arkts-camera-camera-cameraposition-e.md)和[CameraType](arkts-camera-camera-cameratype-e.md)的相机镜头，如果该接口返回结果为undefined，表示当前设备未查询到该镜头。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-CameraManager-getCameraDevice(position: CameraPosition, type: CameraType): CameraDevice--><!--Device-CameraManager-getCameraDevice(position: CameraPosition, type: CameraType): CameraDevice-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| position | [CameraPosition](arkts-camera-camera-cameraposition-e.md) | Yes | 需要得到的CameraDevice对象对应的CameraPosition条件。 |
| type | [CameraType](arkts-camera-camera-cameratype-e.md) | Yes | 需要得到的CameraDevice对象对应的CameraType条件。 |

**Return value:**

| Type | Description |
| --- | --- |
| [CameraDevice](arkts-camera-camera-cameradevice-i.md) | 根据相机位置和相机类型查询的对应相机。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 7400201 | Camera service fatal error. |

## getCameraDevices

```TypeScript
getCameraDevices(position: CameraPosition, types: Array<CameraType>, connectType: ConnectionType): Array<CameraDevice>
```

根据相机位置、相机类型数组和连接类型查询符合条件的相机列表。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-CameraManager-getCameraDevices(position: CameraPosition, types: Array<CameraType>, connectType: ConnectionType): Array<CameraDevice>--><!--Device-CameraManager-getCameraDevices(position: CameraPosition, types: Array<CameraType>, connectType: ConnectionType): Array<CameraDevice>-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| position | [CameraPosition](arkts-camera-camera-cameraposition-e.md) | Yes | 相机的位置。 |
| types | Array&lt;CameraType&gt; | Yes | 相机类型数组。 |
| connectType | [ConnectionType](arkts-camera-camera-connectiontype-e.md) | Yes | 相机的连接类型。 |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;CameraDevice&gt; | 根据相机位置、相机类型数组和连接类型查询符合条件的相机列表。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 7400201 | Camera service fatal error. |

## getSupportedCameras

```TypeScript
getSupportedCameras(): Array<CameraDevice>
```

获取支持的基础相机设备对象（如获取CameraType为CAMERA_TYPE_DEFAULT的默认相机），同步返回结果。

如果需要获取额外的相机设备对象（如获取CameraType为CAMERA_TYPE_TELEPHOTO的长焦相机），可通过  
[getCameraDevices](arkts-camera-camera-cameramanager-i.md#getcameradevices)接口获取。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-CameraManager-getSupportedCameras(): Array<CameraDevice>--><!--Device-CameraManager-getSupportedCameras(): Array<CameraDevice>-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;CameraDevice&gt; | 相机设备列表。 |

## getSupportedFullOutputCapability

```TypeScript
getSupportedFullOutputCapability(camera: CameraDevice, mode: SceneMode): CameraOutputCapability
```

查询指定相机在指定模式下支持的完整输出能力，包括未压缩图（YUV）、HEIF和HDR等能力。

> **说明：**
> 
> 使用YUV，HEIF或HDR等能力前，需要先显式调用此方法确保获取完整输出能力。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

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
| [CameraOutputCapability](arkts-camera-camera-cameraoutputcapability-i.md) | 相机输出能力。 |

## getSupportedOutputCapability

```TypeScript
getSupportedOutputCapability(camera: CameraDevice): CameraOutputCapability
```

查询相机设备支持的输出能力，同步返回结果。

> **说明：**
> 
> 从 API version 10开始支持，从API version 11开始废弃。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** 11

**Substitutes:** [camera.CameraManager.getSupportedOutputCapability](arkts-camera-camera-cameramanager-i.md#getsupportedoutputcapability)(camera:

<!--Device-CameraManager-getSupportedOutputCapability(camera: CameraDevice): CameraOutputCapability--><!--Device-CameraManager-getSupportedOutputCapability(camera: CameraDevice): CameraOutputCapability-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| camera | [CameraDevice](arkts-camera-camera-cameradevice-i.md) | Yes | Camera device. |

**Return value:**

| Type | Description |
| --- | --- |
| [CameraOutputCapability](arkts-camera-camera-cameraoutputcapability-i.md) | 相机输出能力。 |

## getSupportedOutputCapability

```TypeScript
getSupportedOutputCapability(camera: CameraDevice, mode: SceneMode): CameraOutputCapability
```

查询相机设备在指定模式下支持的输出能力，同步返回结果。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

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
| [CameraOutputCapability](arkts-camera-camera-cameraoutputcapability-i.md) | 相机输出能力。 |

## getSupportedSceneModes

```TypeScript
getSupportedSceneModes(camera: CameraDevice): Array<SceneMode>
```

获取指定的相机设备对象支持的模式，同步返回结果。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

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
| Array&lt;SceneMode&gt; | 相机支持的模式列表。 |

## getTorchMode

```TypeScript
getTorchMode(): TorchMode
```

获取当前设备手电筒模式。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-CameraManager-getTorchMode(): TorchMode--><!--Device-CameraManager-getTorchMode(): TorchMode-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Return value:**

| Type | Description |
| --- | --- |
| [TorchMode](arkts-camera-camera-torchmode-e.md) | 返回设备当前手电筒模式。 |

## isCameraMuted

```TypeScript
isCameraMuted(): boolean
```

查询当前相机是否禁用。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-CameraManager-isCameraMuted(): boolean--><!--Device-CameraManager-isCameraMuted(): boolean-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 返回true表示相机被禁用，返回false表示相机未被禁用。 |

## isTorchLevelControlSupported

```TypeScript
isTorchLevelControlSupported(): boolean
```

检测设备是否支持手电筒亮度调节功能。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-CameraManager-isTorchLevelControlSupported(): boolean--><!--Device-CameraManager-isTorchLevelControlSupported(): boolean-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 表示设备是否支持手电筒亮度调节功能。返回true表示支持，返回false表示不支持。若接口调用失败，返回undefined。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 202 | Not System Application.<br>**Applicable version:** 23 - 24 |

## isTorchModeSupported

```TypeScript
isTorchModeSupported(mode: TorchMode): boolean
```

检测是否支持设置的手电筒模式。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-CameraManager-isTorchModeSupported(mode: TorchMode): boolean--><!--Device-CameraManager-isTorchModeSupported(mode: TorchMode): boolean-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mode | [TorchMode](arkts-camera-camera-torchmode-e.md) | Yes | 手电筒模式。传参为null或者undefined，作为0处理，手电筒关闭。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 返回true表示设备支持设置的手电筒模式，返回false表示设备不支持的手电筒模式。若接口调用失败，返回undefined。 |

## isTorchSupported

```TypeScript
isTorchSupported(): boolean
```

检测设备是否支持手电筒。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-CameraManager-isTorchSupported(): boolean--><!--Device-CameraManager-isTorchSupported(): boolean-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 表示设备是否支持手电筒，true表示设备支持手电筒，false表示设备不支持手电。 &lt;br&gt;如果返回false，则[isTorchModeSupported]{ |

## off('cameraStatus')

```TypeScript
off(type: 'cameraStatus', callback?: AsyncCallback<CameraStatusInfo>): void
```

相机设备状态注销回调，通过注销回调函数取消获取相机的状态变化。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-CameraManager-off(type: 'cameraStatus', callback?: AsyncCallback<CameraStatusInfo>): void--><!--Device-CameraManager-off(type: 'cameraStatus', callback?: AsyncCallback<CameraStatusInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'cameraStatus' | Yes | 监听事件，固定为'cameraStatus'。cameraManager对象获取成功后可监听。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;CameraStatusInfo&gt; | No | 回调函数，如果指定参数则取消对应callback（callback对象不可是匿名函数），否则取消所有callback。 |

## off('foldStatusChange')

```TypeScript
off(type: 'foldStatusChange', callback?: AsyncCallback<FoldStatusInfo>): void
```

关闭折叠设备折叠状态变化的监听。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-CameraManager-off(type: 'foldStatusChange', callback?: AsyncCallback<FoldStatusInfo>): void--><!--Device-CameraManager-off(type: 'foldStatusChange', callback?: AsyncCallback<FoldStatusInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'foldStatusChange' | Yes | 监听事件，固定为'foldStatusChange'。表示折叠设备折叠状态发生变化。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;FoldStatusInfo&gt; | No | 回调函数，返回折叠设备折叠信息。如果指定参数则取消对应callback（callback对象不可是匿名函数），否则取消所有 callback。 |

## off('torchStatusChange')

```TypeScript
off(type: 'torchStatusChange', callback?: AsyncCallback<TorchStatusInfo>): void
```

手电筒状态变化注销回调，通过注销回调函数取消获取手电筒状态变化。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-CameraManager-off(type: 'torchStatusChange', callback?: AsyncCallback<TorchStatusInfo>): void--><!--Device-CameraManager-off(type: 'torchStatusChange', callback?: AsyncCallback<TorchStatusInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'torchStatusChange' | Yes | 监听事件，固定为'torchStatusChange'。cameraManager对象获取成功后可监听。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;TorchStatusInfo&gt; | No | 回调函数，如果指定参数则取消对应callback（callback对象不可是匿名函数），否则取消所有callback。 |

## offCameraStatus

```TypeScript
offCameraStatus(callback?: AsyncCallback<CameraStatusInfo>): void
```

Unsubscribes from camera status change event callback.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-CameraManager-offCameraStatus(callback?: AsyncCallback<CameraStatusInfo>): void--><!--Device-CameraManager-offCameraStatus(callback?: AsyncCallback<CameraStatusInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;CameraStatusInfo&gt; | No | Callback used to get the camera status change. |

## offFoldStatusChange

```TypeScript
offFoldStatusChange(callback?: AsyncCallback<FoldStatusInfo>): void
```

Unsubscribes from fold status change event callback.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-CameraManager-offFoldStatusChange(callback?: AsyncCallback<FoldStatusInfo>): void--><!--Device-CameraManager-offFoldStatusChange(callback?: AsyncCallback<FoldStatusInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;FoldStatusInfo&gt; | No | Callback used to get the fold status change. |

## offTorchStatusChange

```TypeScript
offTorchStatusChange(callback?: AsyncCallback<TorchStatusInfo>): void
```

Unsubscribes torch status change event callback.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-CameraManager-offTorchStatusChange(callback?: AsyncCallback<TorchStatusInfo>): void--><!--Device-CameraManager-offTorchStatusChange(callback?: AsyncCallback<TorchStatusInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;TorchStatusInfo&gt; | No | Callback used to return the torch status change |

## on('cameraStatus')

```TypeScript
on(type: 'cameraStatus', callback: AsyncCallback<CameraStatusInfo>): void
```

相机设备状态回调，通过注册回调函数获取相机的状态变化。使用callback异步回调。

> **说明：**
> 
> 当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-CameraManager-on(type: 'cameraStatus', callback: AsyncCallback<CameraStatusInfo>): void--><!--Device-CameraManager-on(type: 'cameraStatus', callback: AsyncCallback<CameraStatusInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'cameraStatus' | Yes | 监听事件，固定为'cameraStatus'。cameraManager对象获取成功后可监听。目前只支持对设备打开或者关闭会触发该事件并返回对应信息。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;CameraStatusInfo&gt; | Yes | 回调函数，用于获取镜头状态变化信息。 |

## on('foldStatusChange')

```TypeScript
on(type: 'foldStatusChange', callback: AsyncCallback<FoldStatusInfo>): void
```

注册折叠设备折叠状态变化的监听。使用callback异步回调。

> **说明：**
> 
> 当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-CameraManager-on(type: 'foldStatusChange', callback: AsyncCallback<FoldStatusInfo>): void--><!--Device-CameraManager-on(type: 'foldStatusChange', callback: AsyncCallback<FoldStatusInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'foldStatusChange' | Yes | 监听事件，固定为'foldStatusChange'。表示折叠设备折叠状态发生变化。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;FoldStatusInfo&gt; | Yes | 回调函数。返回折叠设备折叠信息。 |

## on('torchStatusChange')

```TypeScript
on(type: 'torchStatusChange', callback: AsyncCallback<TorchStatusInfo>): void
```

手电筒状态变化回调，通过注册回调函数获取手电筒状态变化。使用callback异步回调。

> **说明：**
> 
> 当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-CameraManager-on(type: 'torchStatusChange', callback: AsyncCallback<TorchStatusInfo>): void--><!--Device-CameraManager-on(type: 'torchStatusChange', callback: AsyncCallback<TorchStatusInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'torchStatusChange' | Yes | 监听事件，固定为'torchStatusChange'。cameraManager对象获取成功后可监听。目前只支持手电筒打开，手电筒关闭，手电筒不可 用，手电筒恢复可用会触发该事件并返回对应信息。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;TorchStatusInfo&gt; | Yes | 回调函数，用于获取手电筒状态变化信息。 |

## onCameraStatus

```TypeScript
onCameraStatus(callback: AsyncCallback<CameraStatusInfo>): void
```

Subscribes camera status change event callback.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-CameraManager-onCameraStatus(callback: AsyncCallback<CameraStatusInfo>): void--><!--Device-CameraManager-onCameraStatus(callback: AsyncCallback<CameraStatusInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;CameraStatusInfo&gt; | Yes | Callback used to get the camera status change. |

## onFoldStatusChange

```TypeScript
onFoldStatusChange(callback: AsyncCallback<FoldStatusInfo>): void
```

Subscribes fold status change event callback.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-CameraManager-onFoldStatusChange(callback: AsyncCallback<FoldStatusInfo>): void--><!--Device-CameraManager-onFoldStatusChange(callback: AsyncCallback<FoldStatusInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;FoldStatusInfo&gt; | Yes | Callback used to get the fold status change. |

## onTorchStatusChange

```TypeScript
onTorchStatusChange(callback: AsyncCallback<TorchStatusInfo>): void
```

Subscribes torch status change event callback.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-CameraManager-onTorchStatusChange(callback: AsyncCallback<TorchStatusInfo>): void--><!--Device-CameraManager-onTorchStatusChange(callback: AsyncCallback<TorchStatusInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;TorchStatusInfo&gt; | Yes | Callback used to return the torch status change |

## setTorchMode

```TypeScript
setTorchMode(mode: TorchMode): void
```

设置设备手电筒模式。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-CameraManager-setTorchMode(mode: TorchMode): void--><!--Device-CameraManager-setTorchMode(mode: TorchMode): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mode | [TorchMode](arkts-camera-camera-torchmode-e.md) | Yes | 手电筒模式。传参为null或者undefined，作为0处理，手电筒关闭。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 7400101 | Parameter missing or parameter type incorrect.<br>**Applicable version:** 11 - 17 |
| 7400102 | Operation not allowed.<br>**Applicable version:** 12 and later |
| 7400201 | Camera service fatal error.<br>**Applicable version:** 12 and later |

## setTorchModeOnWithLevel

ArkTS-Dyn:
```TypeScript
setTorchModeOnWithLevel(torchLevel: number): void
```

ArkTS-Sta:
```TypeScript
setTorchModeOnWithLevel(torchLevel: double): void
```

手电筒设置指定亮度级别。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-CameraManager-setTorchModeOnWithLevel(torchLevel: double): void--><!--Device-CameraManager-setTorchModeOnWithLevel(torchLevel: double): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| torchLevel | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | 手电筒亮度级别。通常范围是[0.0, 1.0]（0.0为最暗，1.0为最亮）。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 7400102 | Operation not allowed. |
| 7400201 | Camera service fatal error. |
| 202 | Not System Application.<br>**Applicable version:** 23 - 24 |

