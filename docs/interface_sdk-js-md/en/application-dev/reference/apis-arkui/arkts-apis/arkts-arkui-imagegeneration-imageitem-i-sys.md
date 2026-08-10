# ImageItem (System API)

Image information for AI-generated images.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-imageGeneration-interface ImageItem--><!--Device-imageGeneration-interface ImageItem-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { imageGeneration } from 'kits/@kit.ArkUI';
```

## image

```TypeScript
image?: image.PixelMap
```

Image decoding information for preview in the page of ImageGeneratorDialog.

&lt;p&gt;**NOTE：**:Displayed within the canvas in the ImageGeneratorDialog; if not provided, the image will be decoded from the url.&lt;/p&gt;

**Type:** image.PixelMap

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ImageItem-image?: image.PixelMap--><!--Device-ImageItem-image?: image.PixelMap-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## isHandwrite

```TypeScript
isHandwrite?: boolean
```

whether the image type is a hand-drawn line art.

&lt;p&gt;**NOTE：**:it is recommended to be provided in Hand-drawn line art scenarios to achieve better results.&lt;/p&gt;

**Type:** boolean

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ImageItem-isHandwrite?: boolean--><!--Device-ImageItem-isHandwrite?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## rect

```TypeScript
rect?: common2D.Rect
```

The size and position of the container used to display images in the preview canvas.

&lt;p&gt;**NOTE：**:it is recommended to be provided in multi-image fusion scenarios to achieve better results.&lt;/p&gt;

**Type:** common2D.Rect

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ImageItem-rect?: common2D.Rect--><!--Device-ImageItem-rect?: common2D.Rect-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## rotation

```TypeScript
rotation?: componentUtils.Rotation2D
```

The rotation of the container used to display images in the preview canvas.

&lt;p&gt;**NOTE：**:it is recommended to be provided in multi-image fusion scenarios to achieve better results.&lt;/p&gt;

**Type:** componentUtils.Rotation2D

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ImageItem-rotation?: componentUtils.Rotation2D--><!--Device-ImageItem-rotation?: componentUtils.Rotation2D-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## url

```TypeScript
url?: ResourceStr
```

Original image path information for image generation;

&lt;p&gt;**NOTE：**:for high-resolution scenarios, it is best to provide the original image path; if not provided, the image.PixelMap will be used for image generation.&lt;/p&gt;

**Type:** [ResourceStr](arkts-arkui-resourcestr-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ImageItem-url?: ResourceStr--><!--Device-ImageItem-url?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## zIndex

```TypeScript
zIndex?: int
```

In scenarios with multiple images, information about image rendering hierarchy.

&lt;p&gt;**NOTE：**:it is recommended to be provided in multi-image fusion scenarios to achieve better results.&lt;/p&gt;

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ImageItem-zIndex?: int--><!--Device-ImageItem-zIndex?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

