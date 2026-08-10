# CameraBufferCrop (System API)

相机移轴裁剪参数。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-unnamed-export declare interface CameraBufferCrop--><!--Device-unnamed-export declare interface CameraBufferCrop-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## bufferHeight

```TypeScript
bufferHeight: int
```

基准图高度，单位为像素。需确保传入图片的高度与实际图片高度一致，否则可能导致显示异常，如位置偏移。

**Type:** int

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CameraBufferCrop-bufferHeight: int--><!--Device-CameraBufferCrop-bufferHeight: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## bufferWidth

```TypeScript
bufferWidth: int
```

基准图宽度，单位为像素。需确保传入图片的宽度与实际图片宽度一致，否则可能导致显示异常，如位置偏移。

**Type:** int

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CameraBufferCrop-bufferWidth: int--><!--Device-CameraBufferCrop-bufferWidth: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## cropOffset

```TypeScript
cropOffset: CropOffset
```

裁剪区域偏移量。

**Type:** [CropOffset](../arkts-components/arkts-arkui-cropoffset-i-sys.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CameraBufferCrop-cropOffset: CropOffset--><!--Device-CameraBufferCrop-cropOffset: CropOffset-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## cropScale

```TypeScript
cropScale: double
```

裁剪区域缩放比例，裁剪区基础大小为DepthComponent组件大小。

**Type:** double

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CameraBufferCrop-cropScale: double--><!--Device-CameraBufferCrop-cropScale: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

