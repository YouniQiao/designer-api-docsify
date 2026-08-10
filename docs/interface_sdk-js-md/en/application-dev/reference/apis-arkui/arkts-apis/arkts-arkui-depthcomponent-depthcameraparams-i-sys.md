# DepthCameraParams (System API)

相机参数。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-unnamed-export declare interface DepthCameraParams--><!--Device-unnamed-export declare interface DepthCameraParams-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## cameraBufferCrop

```TypeScript
cameraBufferCrop?: CameraBufferCrop
```

相机移轴裁剪参数。未设置时默认使用组件布局尺寸作为默认图像基准大小，裁剪偏移量为(0, 0)，缩放比例为1.0。

**Type:** [CameraBufferCrop](../arkts-components/arkts-arkui-camerabuffercrop-i-sys.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DepthCameraParams-cameraBufferCrop?: CameraBufferCrop--><!--Device-DepthCameraParams-cameraBufferCrop?: CameraBufferCrop-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## position

```TypeScript
position: DepthVector3
```

相机在三维空间中的位置。无单位，其值表示3D空间中的坐标。

**Type:** [DepthVector3](../arkts-components/arkts-arkui-depthvector3-i-sys.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DepthCameraParams-position: DepthVector3--><!--Device-DepthCameraParams-position: DepthVector3-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## quaternion

```TypeScript
quaternion: DepthVector4
```

相机旋转四元数，按(x, y, z, w)表示。无单位。

**Type:** [DepthVector4](../arkts-components/arkts-arkui-depthvector4-i-sys.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DepthCameraParams-quaternion: DepthVector4--><!--Device-DepthCameraParams-quaternion: DepthVector4-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## yFov

```TypeScript
yFov: double
```

相机垂直方向视场角，单位为弧度。

**Type:** double

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DepthCameraParams-yFov: double--><!--Device-DepthCameraParams-yFov: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## zFar

```TypeScript
zFar: double
```

远裁剪面距离。无单位。必须为正数。

**Type:** double

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DepthCameraParams-zFar: double--><!--Device-DepthCameraParams-zFar: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## zNear

```TypeScript
zNear: double
```

近裁剪面距离。无单位。必须为正数。

**Type:** double

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DepthCameraParams-zNear: double--><!--Device-DepthCameraParams-zNear: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

