# ImageItem（系统接口）

Image information for AI-generated images.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-imageGeneration-interface ImageItem--><!--Device-imageGeneration-interface ImageItem-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { imageGeneration } from 'kits/@kit.ArkUI';
```

## image

```TypeScript
image?: image.PixelMap
```

Image decoding information for preview in the page of ImageGeneratorDialog.

&lt;p&gt;**NOTE：**:Displayed within the canvas in the ImageGeneratorDialog; if not provided, the image will be decoded from the url.&lt;/p&gt;

**类型：** image.PixelMap

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ImageItem-image?: image.PixelMap--><!--Device-ImageItem-image?: image.PixelMap-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

## isHandwrite

```TypeScript
isHandwrite?: boolean
```

whether the image type is a hand-drawn line art.

&lt;p&gt;**NOTE：**:it is recommended to be provided in Hand-drawn line art scenarios to achieve better results.&lt;/p&gt;

**类型：** boolean

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ImageItem-isHandwrite?: boolean--><!--Device-ImageItem-isHandwrite?: boolean-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

## rect

```TypeScript
rect?: common2D.Rect
```

The size and position of the container used to display images in the preview canvas.

&lt;p&gt;**NOTE：**:it is recommended to be provided in multi-image fusion scenarios to achieve better results.&lt;/p&gt;

**类型：** common2D.Rect

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ImageItem-rect?: common2D.Rect--><!--Device-ImageItem-rect?: common2D.Rect-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

## rotation

```TypeScript
rotation?: componentUtils.Rotation2D
```

The rotation of the container used to display images in the preview canvas.

&lt;p&gt;**NOTE：**:it is recommended to be provided in multi-image fusion scenarios to achieve better results.&lt;/p&gt;

**类型：** componentUtils.Rotation2D

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ImageItem-rotation?: componentUtils.Rotation2D--><!--Device-ImageItem-rotation?: componentUtils.Rotation2D-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

## url

```TypeScript
url?: ResourceStr
```

Original image path information for image generation;

&lt;p&gt;**NOTE：**:for high-resolution scenarios, it is best to provide the original image path; if not provided, the image.PixelMap will be used for image generation.&lt;/p&gt;

**类型：** [ResourceStr](arkts-arkui-resourcestr-t.md)

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ImageItem-url?: ResourceStr--><!--Device-ImageItem-url?: ResourceStr-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

## zIndex

```TypeScript
zIndex?: int
```

In scenarios with multiple images, information about image rendering hierarchy.

&lt;p&gt;**NOTE：**:it is recommended to be provided in multi-image fusion scenarios to achieve better results.&lt;/p&gt;

**类型：** int

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ImageItem-zIndex?: int--><!--Device-ImageItem-zIndex?: int-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

