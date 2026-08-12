# MetadataDogFaceObject

相机检测到的狗脸元数据信息，继承自[MetadataObject](arkts-camera-camera-metadataobject-i.md#MetadataObject)。[CameraInput](arkts-camera-camera-camerainput-i.md#CameraInput)相机信息中的数据来源，通过metadataOutput.  
[on('metadataObjectsAvailable')](camera.MetadataOutput.on(type: 'metadataObjectsAvailable', callback: AsyncCallback&lt;Array<MetadataObject>&gt;&lt;MetadataObject&gt;>))接口获取。

**继承/实现关系：** MetadataDogFaceObject extends [MetadataObject](arkts-camera-camera-metadataobject-i.md#MetadataObject)

**起始版本：** 26.0.0

<!--Device-camera-interface MetadataDogFaceObject extends MetadataObject--><!--Device-camera-interface MetadataDogFaceObject extends MetadataObject-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

## leftEyeBoundingBox

```TypeScript
readonly leftEyeBoundingBox: Rect
```

左眼区域框。

**类型：** Rect

**起始版本：** 26.0.0

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-MetadataDogFaceObject-readonly leftEyeBoundingBox: Rect--><!--Device-MetadataDogFaceObject-readonly leftEyeBoundingBox: Rect-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

## rightEyeBoundingBox

```TypeScript
readonly rightEyeBoundingBox: Rect
```

右眼区域框。

**类型：** Rect

**起始版本：** 26.0.0

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-MetadataDogFaceObject-readonly rightEyeBoundingBox: Rect--><!--Device-MetadataDogFaceObject-readonly rightEyeBoundingBox: Rect-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core
