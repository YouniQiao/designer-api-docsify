# CameraManager

相机管理器类，使用前需要通过[getCameraManager](arkts-camera-camera-getcameramanager-f.md#getCameraManager)接口获取相机管理实例。

**起始版本：** 23

**废弃版本：** -1

<!--Device-camera-interface CameraManager--><!--Device-camera-interface CameraManager-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

## createCameraInput

```TypeScript
createCameraInput(camera: CameraDevice): CameraInput
```

使用CameraDevice对象创建CameraInput实例，同步返回结果。 该接口使用前首先通过[getSupportedCameras](#getSupportedCameras)接口查询当前设备支持的相机设备信息列表，开发者需要根据具体使用场景选 择符合需求的相机设备，然后使用该接口创建CameraInput实例。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.CAMERA

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-CameraManager-createCameraInput(camera: CameraDevice): CameraInput--><!--Device-CameraManager-createCameraInput(camera: CameraDevice): CameraInput-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [camera](arkts-multimedia-camera.md) | [CameraDevice](arkts-camera-camera-cameradevice-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [CameraInput](arkts-camera-camera-camerainput-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [7400101](../errorcode-camera.md#7400101-无效入参) |
| [7400102](../errorcode-camera.md#7400102-非法操作) |
| [7400201](../errorcode-camera.md#7400201-相机服务异常) |

## createCameraInput

```TypeScript
createCameraInput(position: CameraPosition, type: CameraType): CameraInput
```

根据相机位置和类型创建CameraInput实例，同步返回结果。 该接口使用前需要开发者根据应用具体使用场景自行指定相机位置和类型，例如打开前置相机进入自拍功能。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.CAMERA

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-CameraManager-createCameraInput(position: CameraPosition, type: CameraType): CameraInput--><!--Device-CameraManager-createCameraInput(position: CameraPosition, type: CameraType): CameraInput-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| position | [CameraPosition](arkts-camera-camera-cameraposition-e.md) | 是 |
| type | [CameraType](arkts-camera-camera-cameratype-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [CameraInput](arkts-camera-camera-camerainput-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [7400101](../errorcode-camera.md#7400101-无效入参) |
| [7400102](../errorcode-camera.md#7400102-非法操作) |
| [7400201](../errorcode-camera.md#7400201-相机服务异常) |

## createCaptureSession

```TypeScript
createCaptureSession(): CaptureSession
```

创建CaptureSession实例，同步返回结果。 > **说明：** > > 从 API version 10开始支持，从API version 11开始废弃。

**起始版本：** 10

**废弃版本：** 11

**替代接口：** [createSession](#createSession)

<!--Device-CameraManager-createCaptureSession(): CaptureSession--><!--Device-CameraManager-createCaptureSession(): CaptureSession-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 |
| --- |
| [CaptureSession](arkts-camera-camera-capturesession-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [7400201](../errorcode-camera.md#7400201-相机服务异常) |

## createMetadataOutput

```TypeScript
createMetadataOutput(metadataObjectTypes: Array<MetadataObjectType>): MetadataOutput
```

创建metadata流输出对象，同步返回结果。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-CameraManager-createMetadataOutput(metadataObjectTypes: Array<MetadataObjectType>): MetadataOutput--><!--Device-CameraManager-createMetadataOutput(metadataObjectTypes: Array<MetadataObjectType>): MetadataOutput-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| metadataObjectTypes | Array&lt;[MetadataObjectType](arkts-camera-camera-metadataobjecttype-e.md)&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| [MetadataOutput](arkts-camera-camera-metadataoutput-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [7400101](../errorcode-camera.md#7400101-无效入参) |
| [7400201](../errorcode-camera.md#7400201-相机服务异常) |

## createPhotoOutput

```TypeScript
createPhotoOutput(profile: Profile, surfaceId: string): PhotoOutput
```

创建拍照输出对象，同步返回结果。 > **说明：** > > - 从API version 10开始支持，从API version 11开始废弃。 > > - 该接口只支持创建JPEG格式的拍照输出对象。

**起始版本：** 10

**废弃版本：** 11

**替代接口：** [createPhotoOutput](#createPhotoOutput)(profile?: Profile)

<!--Device-CameraManager-createPhotoOutput(profile: Profile, surfaceId: string): PhotoOutput--><!--Device-CameraManager-createPhotoOutput(profile: Profile, surfaceId: string): PhotoOutput-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| profile | [Profile](arkts-camera-camera-profile-i.md) | 是 |
| surfaceId | string | 是 |

**返回值：**

| 类型 |
| --- |
| [PhotoOutput](arkts-camera-camera-photooutput-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [7400101](../errorcode-camera.md#7400101-无效入参) |

## createPhotoOutput

```TypeScript
createPhotoOutput(profile?: Profile): PhotoOutput
```

创建拍照输出对象，同步返回结果。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-CameraManager-createPhotoOutput(profile?: Profile): PhotoOutput--><!--Device-CameraManager-createPhotoOutput(profile?: Profile): PhotoOutput-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| profile | [Profile](arkts-camera-camera-profile-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [PhotoOutput](arkts-camera-camera-photooutput-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [7400101](../errorcode-camera.md#7400101-无效入参) |
| [7400201](../errorcode-camera.md#7400201-相机服务异常) |

## createPreviewOutput

```TypeScript
createPreviewOutput(profile: Profile, surfaceId: string): PreviewOutput
```

创建预览输出对象，同步返回结果。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-CameraManager-createPreviewOutput(profile: Profile, surfaceId: string): PreviewOutput--><!--Device-CameraManager-createPreviewOutput(profile: Profile, surfaceId: string): PreviewOutput-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| profile | [Profile](arkts-camera-camera-profile-i.md) | 是 |
| surfaceId | string | 是 |

**返回值：**

| 类型 |
| --- |
| [PreviewOutput](arkts-camera-camera-previewoutput-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [7400101](../errorcode-camera.md#7400101-无效入参) |
| [7400201](../errorcode-camera.md#7400201-相机服务异常) |

## createPreviewOutput

```TypeScript
createPreviewOutput(surfaceId: string): PreviewOutput
```

创建无配置信息的预览输出对象，同步返回结果。该接口需配合[preconfig](arkts-camera-camera-photosession-i.md#preconfig)一起使用。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-CameraManager-createPreviewOutput(surfaceId: string): PreviewOutput--><!--Device-CameraManager-createPreviewOutput(surfaceId: string): PreviewOutput-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| surfaceId | string | 是 |

**返回值：**

| 类型 |
| --- |
| [PreviewOutput](arkts-camera-camera-previewoutput-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [7400101](../errorcode-camera.md#7400101-无效入参) |
| [7400201](../errorcode-camera.md#7400201-相机服务异常) |

## createSession

```TypeScript
createSession<T extends Session>(mode: SceneMode): T
```

创建指定SceneMode的Session实例，同步返回结果。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-CameraManager-createSession<T extends Session>(mode: SceneMode): T--><!--Device-CameraManager-createSession<T extends Session>(mode: SceneMode): T-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mode | [SceneMode](arkts-camera-camera-scenemode-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

**错误码：**

| 错误码ID |
| --- |
| [7400101](../errorcode-camera.md#7400101-无效入参) |
| [7400201](../errorcode-camera.md#7400201-相机服务异常) |

## createVideoOutput

```TypeScript
createVideoOutput(profile: VideoProfile, surfaceId: string): VideoOutput
```

创建录像输出对象，同步返回结果。 在录像模式下，使能SDR或HDR_VIVID拍摄效果时，CameraFormat与ColorSpace必须按照下列表格中的对应关系配置，若不满足表格中CameraFormat与ColorSpace配置，会导致预览异常等问题。 | SDR/HDR拍摄 | CameraFormat | ColorSpace | |--------------------|--------------------------|------------------| | SDR | CAMERA_FORMAT_YUV_420_SP | BT709_LIMIT | | HDR_VIVID | CAMERA_FORMAT_YCRCB_P010&lt;br&gt;CAMERA_FORMAT_YCBCR_P010 | BT2020_HLG_LIMIT&lt;br&gt;BT2020_HLG_FULL |

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-CameraManager-createVideoOutput(profile: VideoProfile, surfaceId: string): VideoOutput--><!--Device-CameraManager-createVideoOutput(profile: VideoProfile, surfaceId: string): VideoOutput-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| profile | [VideoProfile](arkts-camera-camera-videoprofile-i.md) | 是 |
| surfaceId | string | 是 |

**返回值：**

| 类型 |
| --- |
| [VideoOutput](arkts-camera-camera-videooutput-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [7400101](../errorcode-camera.md#7400101-无效入参) |
| [7400201](../errorcode-camera.md#7400201-相机服务异常) |

## createVideoOutput

```TypeScript
createVideoOutput(surfaceId: string): VideoOutput
```

创建无配置信息的录像输出对象，同步返回结果。该接口需配合[preconfig](arkts-camera-camera-videosession-i.md#preconfig)功能一起使用。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-CameraManager-createVideoOutput(surfaceId: string): VideoOutput--><!--Device-CameraManager-createVideoOutput(surfaceId: string): VideoOutput-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| surfaceId | string | 是 |

**返回值：**

| 类型 |
| --- |
| [VideoOutput](arkts-camera-camera-videooutput-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [7400101](../errorcode-camera.md#7400101-无效入参) |
| [7400201](../errorcode-camera.md#7400201-相机服务异常) |

## getCameraConcurrentInfos

```TypeScript
getCameraConcurrentInfos(cameras: Array<CameraDevice>): Array<CameraConcurrentInfo>
```

获取指定相机设备的并发信息。返回空数组表示不支持并发。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-CameraManager-getCameraConcurrentInfos(cameras: Array<CameraDevice>): Array<CameraConcurrentInfo>--><!--Device-CameraManager-getCameraConcurrentInfos(cameras: Array<CameraDevice>): Array<CameraConcurrentInfo>-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| cameras | Array&lt;[CameraDevice](arkts-camera-camera-cameradevice-i.md)&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Array&lt;[CameraConcurrentInfo](arkts-camera-camera-cameraconcurrentinfo-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [7400201](../errorcode-camera.md#7400201-相机服务异常) |

## getCameraDevice

```TypeScript
getCameraDevice(position: CameraPosition, type: CameraType): CameraDevice
```

根据相机位置和相机类型查询对应相机。 获取指定[CameraPosition](arkts-camera-camera-cameraposition-e.md#CameraPosition)和[CameraType](arkts-camera-camera-cameratype-e.md#CameraType)的相机镜头，如果该接口返回结果为undefined， 表示当前设备未查询到该镜头。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-CameraManager-getCameraDevice(position: CameraPosition, type: CameraType): CameraDevice--><!--Device-CameraManager-getCameraDevice(position: CameraPosition, type: CameraType): CameraDevice-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| position | [CameraPosition](arkts-camera-camera-cameraposition-e.md) | 是 |
| type | [CameraType](arkts-camera-camera-cameratype-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [CameraDevice](arkts-camera-camera-cameradevice-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [7400201](../errorcode-camera.md#7400201-相机服务异常) |

## getCameraDevices

```TypeScript
getCameraDevices(position: CameraPosition, types: Array<CameraType>, connectType: ConnectionType): Array<CameraDevice>
```

根据相机位置、相机类型数组和连接类型查询符合条件的相机列表。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-CameraManager-getCameraDevices(position: CameraPosition, types: Array<CameraType>, connectType: ConnectionType): Array<CameraDevice>--><!--Device-CameraManager-getCameraDevices(position: CameraPosition, types: Array<CameraType>, connectType: ConnectionType): Array<CameraDevice>-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| position | [CameraPosition](arkts-camera-camera-cameraposition-e.md) | 是 |
| [types](../../apis-na/arkts-apis/arkts-na-util-types-c.md) | Array&lt;[CameraType](arkts-camera-camera-cameratype-e.md)&gt; | 是 |
| connectType | [ConnectionType](arkts-camera-camera-connectiontype-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Array&lt;[CameraDevice](arkts-camera-camera-cameradevice-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [7400201](../errorcode-camera.md#7400201-相机服务异常) |

## getSupportedCameras

```TypeScript
getSupportedCameras(): Array<CameraDevice>
```

获取支持的基础相机设备对象（如获取CameraType为CAMERA_TYPE_DEFAULT的默认相机），同步返回结果。 如果需要获取额外的相机设备对象（如获取CameraType为CAMERA_TYPE_TELEPHOTO的长焦相机），可通过 [getCameraDevices](#getCameraDevices)接口获取。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-CameraManager-getSupportedCameras(): Array<CameraDevice>--><!--Device-CameraManager-getSupportedCameras(): Array<CameraDevice>-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 |
| --- |
| Array&lt;[CameraDevice](arkts-camera-camera-cameradevice-i.md)&gt; |

## getSupportedFullOutputCapability

```TypeScript
getSupportedFullOutputCapability(camera: CameraDevice, mode: SceneMode): CameraOutputCapability
```

查询指定相机在指定模式下支持的完整输出能力，包括未压缩图（YUV）、HEIF和HDR等能力。 > **说明：** > > 使用YUV，HEIF或HDR等能力前，需要先显式调用此方法确保获取完整输出能力。

**起始版本：** 23

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-CameraManager-getSupportedFullOutputCapability(camera: CameraDevice, mode: SceneMode): CameraOutputCapability--><!--Device-CameraManager-getSupportedFullOutputCapability(camera: CameraDevice, mode: SceneMode): CameraOutputCapability-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [camera](arkts-multimedia-camera.md) | [CameraDevice](arkts-camera-camera-cameradevice-i.md) | 是 |
| mode | [SceneMode](arkts-camera-camera-scenemode-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [CameraOutputCapability](arkts-camera-camera-cameraoutputcapability-i.md) |

## getSupportedOutputCapability

```TypeScript
getSupportedOutputCapability(camera: CameraDevice): CameraOutputCapability
```

查询相机设备支持的输出能力，同步返回结果。 > **说明：** > > 从 API version 10开始支持，从API version 11开始废弃。

**起始版本：** 10

**废弃版本：** 11

**替代接口：** [getSupportedOutputCapability](#getSupportedOutputCapability)(camera: CameraDevice, mode: SceneMode)

<!--Device-CameraManager-getSupportedOutputCapability(camera: CameraDevice): CameraOutputCapability--><!--Device-CameraManager-getSupportedOutputCapability(camera: CameraDevice): CameraOutputCapability-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [camera](arkts-multimedia-camera.md) | [CameraDevice](arkts-camera-camera-cameradevice-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [CameraOutputCapability](arkts-camera-camera-cameraoutputcapability-i.md) |

## getSupportedOutputCapability

```TypeScript
getSupportedOutputCapability(camera: CameraDevice, mode: SceneMode): CameraOutputCapability
```

查询相机设备在指定模式下支持的输出能力，同步返回结果。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-CameraManager-getSupportedOutputCapability(camera: CameraDevice, mode: SceneMode): CameraOutputCapability--><!--Device-CameraManager-getSupportedOutputCapability(camera: CameraDevice, mode: SceneMode): CameraOutputCapability-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [camera](arkts-multimedia-camera.md) | [CameraDevice](arkts-camera-camera-cameradevice-i.md) | 是 |
| mode | [SceneMode](arkts-camera-camera-scenemode-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [CameraOutputCapability](arkts-camera-camera-cameraoutputcapability-i.md) |

## getSupportedSceneModes

```TypeScript
getSupportedSceneModes(camera: CameraDevice): Array<SceneMode>
```

获取指定的相机设备对象支持的模式，同步返回结果。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-CameraManager-getSupportedSceneModes(camera: CameraDevice): Array<SceneMode>--><!--Device-CameraManager-getSupportedSceneModes(camera: CameraDevice): Array<SceneMode>-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [camera](arkts-multimedia-camera.md) | [CameraDevice](arkts-camera-camera-cameradevice-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Array&lt;[SceneMode](arkts-camera-camera-scenemode-e.md)&gt; |

## getTorchMode

```TypeScript
getTorchMode(): TorchMode
```

获取当前设备手电筒模式。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-CameraManager-getTorchMode(): TorchMode--><!--Device-CameraManager-getTorchMode(): TorchMode-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 |
| --- |
| [TorchMode](arkts-camera-camera-torchmode-e.md) |

## isCameraMuted

```TypeScript
isCameraMuted(): boolean
```

查询当前相机是否禁用。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-CameraManager-isCameraMuted(): boolean--><!--Device-CameraManager-isCameraMuted(): boolean-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 |
| --- |
| boolean |

## isTorchModeSupported

```TypeScript
isTorchModeSupported(mode: TorchMode): boolean
```

检测是否支持设置的手电筒模式。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-CameraManager-isTorchModeSupported(mode: TorchMode): boolean--><!--Device-CameraManager-isTorchModeSupported(mode: TorchMode): boolean-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mode | [TorchMode](arkts-camera-camera-torchmode-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## isTorchSupported

```TypeScript
isTorchSupported(): boolean
```

检测设备是否支持手电筒。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-CameraManager-isTorchSupported(): boolean--><!--Device-CameraManager-isTorchSupported(): boolean-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 |
| --- |
| boolean |

## offCameraStatus

```TypeScript
offCameraStatus(callback?: AsyncCallback<CameraStatusInfo>): void
```

Unsubscribes from camera status change event callback.

**起始版本：** 23

**废弃版本：** -1

<!--Device-CameraManager-offCameraStatus(callback?: AsyncCallback<CameraStatusInfo>): void--><!--Device-CameraManager-offCameraStatus(callback?: AsyncCallback<CameraStatusInfo>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[CameraStatusInfo](arkts-camera-camera-camerastatusinfo-i.md)&gt; | 否 |

## offFoldStatusChange

```TypeScript
offFoldStatusChange(callback?: AsyncCallback<FoldStatusInfo>): void
```

Unsubscribes from fold status change event callback.

**起始版本：** 23

**废弃版本：** -1

<!--Device-CameraManager-offFoldStatusChange(callback?: AsyncCallback<FoldStatusInfo>): void--><!--Device-CameraManager-offFoldStatusChange(callback?: AsyncCallback<FoldStatusInfo>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[FoldStatusInfo](arkts-camera-camera-foldstatusinfo-i.md)&gt; | 否 |

## offTorchStatusChange

```TypeScript
offTorchStatusChange(callback?: AsyncCallback<TorchStatusInfo>): void
```

Unsubscribes torch status change event callback.

**起始版本：** 23

**废弃版本：** -1

<!--Device-CameraManager-offTorchStatusChange(callback?: AsyncCallback<TorchStatusInfo>): void--><!--Device-CameraManager-offTorchStatusChange(callback?: AsyncCallback<TorchStatusInfo>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[TorchStatusInfo](arkts-camera-camera-torchstatusinfo-i.md)&gt; | 否 |

## off_cameraStatus

```TypeScript
off(type: 'cameraStatus', callback?: AsyncCallback<CameraStatusInfo>): void
```

相机设备状态注销回调，通过注销回调函数取消获取相机的状态变化。

**起始版本：** 10

**废弃版本：** -1

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-CameraManager-off(type: 'cameraStatus', callback?: AsyncCallback<CameraStatusInfo>): void--><!--Device-CameraManager-off(type: 'cameraStatus', callback?: AsyncCallback<CameraStatusInfo>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'cameraStatus' | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[CameraStatusInfo](arkts-camera-camera-camerastatusinfo-i.md)&gt; | 否 |

## off_foldStatusChange

```TypeScript
off(type: 'foldStatusChange', callback?: AsyncCallback<FoldStatusInfo>): void
```

关闭折叠设备折叠状态变化的监听。

**起始版本：** 12

**废弃版本：** -1

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-CameraManager-off(type: 'foldStatusChange', callback?: AsyncCallback<FoldStatusInfo>): void--><!--Device-CameraManager-off(type: 'foldStatusChange', callback?: AsyncCallback<FoldStatusInfo>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'foldStatusChange' | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[FoldStatusInfo](arkts-camera-camera-foldstatusinfo-i.md)&gt; | 否 |

## off_torchStatusChange

```TypeScript
off(type: 'torchStatusChange', callback?: AsyncCallback<TorchStatusInfo>): void
```

手电筒状态变化注销回调，通过注销回调函数取消获取手电筒状态变化。

**起始版本：** 11

**废弃版本：** -1

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-CameraManager-off(type: 'torchStatusChange', callback?: AsyncCallback<TorchStatusInfo>): void--><!--Device-CameraManager-off(type: 'torchStatusChange', callback?: AsyncCallback<TorchStatusInfo>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'torchStatusChange' | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[TorchStatusInfo](arkts-camera-camera-torchstatusinfo-i.md)&gt; | 否 |

## onCameraStatus

```TypeScript
onCameraStatus(callback: AsyncCallback<CameraStatusInfo>): void
```

Subscribes camera status change event callback.

**起始版本：** 23

**废弃版本：** -1

<!--Device-CameraManager-onCameraStatus(callback: AsyncCallback<CameraStatusInfo>): void--><!--Device-CameraManager-onCameraStatus(callback: AsyncCallback<CameraStatusInfo>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[CameraStatusInfo](arkts-camera-camera-camerastatusinfo-i.md)&gt; | 是 |

## onFoldStatusChange

```TypeScript
onFoldStatusChange(callback: AsyncCallback<FoldStatusInfo>): void
```

Subscribes fold status change event callback.

**起始版本：** 23

**废弃版本：** -1

<!--Device-CameraManager-onFoldStatusChange(callback: AsyncCallback<FoldStatusInfo>): void--><!--Device-CameraManager-onFoldStatusChange(callback: AsyncCallback<FoldStatusInfo>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[FoldStatusInfo](arkts-camera-camera-foldstatusinfo-i.md)&gt; | 是 |

## onTorchStatusChange

```TypeScript
onTorchStatusChange(callback: AsyncCallback<TorchStatusInfo>): void
```

Subscribes torch status change event callback.

**起始版本：** 23

**废弃版本：** -1

<!--Device-CameraManager-onTorchStatusChange(callback: AsyncCallback<TorchStatusInfo>): void--><!--Device-CameraManager-onTorchStatusChange(callback: AsyncCallback<TorchStatusInfo>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[TorchStatusInfo](arkts-camera-camera-torchstatusinfo-i.md)&gt; | 是 |

## on_cameraStatus

```TypeScript
on(type: 'cameraStatus', callback: AsyncCallback<CameraStatusInfo>): void
```

相机设备状态回调，通过注册回调函数获取相机的状态变化。使用callback异步回调。 > **说明：** > > 当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。

**起始版本：** 10

**废弃版本：** -1

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-CameraManager-on(type: 'cameraStatus', callback: AsyncCallback<CameraStatusInfo>): void--><!--Device-CameraManager-on(type: 'cameraStatus', callback: AsyncCallback<CameraStatusInfo>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'cameraStatus' | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[CameraStatusInfo](arkts-camera-camera-camerastatusinfo-i.md)&gt; | 是 |

## on_foldStatusChange

```TypeScript
on(type: 'foldStatusChange', callback: AsyncCallback<FoldStatusInfo>): void
```

注册折叠设备折叠状态变化的监听。使用callback异步回调。 > **说明：** > > 当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。

**起始版本：** 12

**废弃版本：** -1

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-CameraManager-on(type: 'foldStatusChange', callback: AsyncCallback<FoldStatusInfo>): void--><!--Device-CameraManager-on(type: 'foldStatusChange', callback: AsyncCallback<FoldStatusInfo>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'foldStatusChange' | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[FoldStatusInfo](arkts-camera-camera-foldstatusinfo-i.md)&gt; | 是 |

## on_torchStatusChange

```TypeScript
on(type: 'torchStatusChange', callback: AsyncCallback<TorchStatusInfo>): void
```

手电筒状态变化回调，通过注册回调函数获取手电筒状态变化。使用callback异步回调。 > **说明：** > > 当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。

**起始版本：** 11

**废弃版本：** -1

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-CameraManager-on(type: 'torchStatusChange', callback: AsyncCallback<TorchStatusInfo>): void--><!--Device-CameraManager-on(type: 'torchStatusChange', callback: AsyncCallback<TorchStatusInfo>): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'torchStatusChange' | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[TorchStatusInfo](arkts-camera-camera-torchstatusinfo-i.md)&gt; | 是 |

## setTorchMode

```TypeScript
setTorchMode(mode: TorchMode): void
```

设置设备手电筒模式。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-CameraManager-setTorchMode(mode: TorchMode): void--><!--Device-CameraManager-setTorchMode(mode: TorchMode): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mode | [TorchMode](arkts-camera-camera-torchmode-e.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [7400101](../errorcode-camera.md#7400101-无效入参) |
| [7400102](../errorcode-camera.md#7400102-非法操作) |
| [7400201](../errorcode-camera.md#7400201-相机服务异常) |
