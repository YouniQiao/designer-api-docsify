# CustomCursor

自定义光标资源。

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

<!--Device-pointer-interface CustomCursor--><!--Device-pointer-interface CustomCursor-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Pointer

## Modules to Import

```TypeScript
import { pointer } from 'kits/@kit.InputKit';
```

## focusX

```TypeScript
focusX?: int
```

自定义光标焦点的水平坐标。该坐标受自定义光标大小的限制。最小值为0，最大值为资源图的宽度最大值该参数缺省时默认为0，单位为像素（px）。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

<!--Device-CustomCursor-focusX?: int--><!--Device-CustomCursor-focusX?: int-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Pointer

## focusY

```TypeScript
focusY?: int
```

自定义光标焦点的垂直坐标。该坐标受自定义光标大小的限制。最小值为0，最大值为资源图的高度最大值该参数缺省时默认为0，单位为像素（px）。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

<!--Device-CustomCursor-focusY?: int--><!--Device-CustomCursor-focusY?: int-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Pointer

## pixelMap

```TypeScript
pixelMap: image.PixelMap
```

自定义光标。最小限制为资源图本身的最小限制。最大限制为256 x 256px。

**Type:** image.PixelMap

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

<!--Device-CustomCursor-pixelMap: image.PixelMap--><!--Device-CustomCursor-pixelMap: image.PixelMap-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Pointer

