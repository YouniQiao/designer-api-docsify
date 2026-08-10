# DecodingOptionsForPicture

图像解码设置选项。

**Since:** 13

**ArkTS mode:** ArkTS-Dyn since version 13; ArkTS-Sta since version 23.

<!--Device-image-interface DecodingOptionsForPicture--><!--Device-image-interface DecodingOptionsForPicture-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

## Modules to Import

```TypeScript
import { image } from 'kits/@kit.ImageKit';
```

## desiredAuxiliaryPictures

```TypeScript
desiredAuxiliaryPictures: Array<AuxiliaryPictureType>
```

设置AuxiliaryPicture类型，当未指定或传入空的Array时，系统会解码所有可用的AuxiliaryPicture类型。 

如果不希望解码任何辅助图，可以直接解码为PixelMap，使用PixelMap创建仅包含主图的Picture。

**Type:** Array&lt;AuxiliaryPictureType&gt;

**Since:** 13

**ArkTS mode:** ArkTS-Dyn since version 13; ArkTS-Sta since version 23.

<!--Device-DecodingOptionsForPicture-desiredAuxiliaryPictures: Array<AuxiliaryPictureType>--><!--Device-DecodingOptionsForPicture-desiredAuxiliaryPictures: Array<AuxiliaryPictureType>-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

## desiredPixelFormat

```TypeScript
desiredPixelFormat?: PixelMapFormat
```

解码的像素格式。默认值为RGBA_8888。

仅支持设置：RGBA_8888、BGRA_8888、RGB_565、NV12及NV21。

当设置其他不支持的像素格式时，返回解码失败。

**Type:** [PixelMapFormat](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-multimedia-movingphotoview-pixelmapformat-e.md)

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DecodingOptionsForPicture-desiredPixelFormat?: PixelMapFormat--><!--Device-DecodingOptionsForPicture-desiredPixelFormat?: PixelMapFormat-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

## desiredSizeForMainPixelMap

```TypeScript
desiredSizeForMainPixelMap?: Size
```

期望输出主图大小（必须为正整数），默认为主图原始尺寸。单位：像素（px）。

若主图原始尺寸与指定尺寸不一致，则会进行拉伸/缩放到指定尺寸。

辅助图的宽度与高度均与主图按照同比例进行相应拉伸/缩放。

**Type:** [Size](../../apis-arkui/arkts-apis/arkts-arkui-window-size-i.md)

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DecodingOptionsForPicture-desiredSizeForMainPixelMap?: Size--><!--Device-DecodingOptionsForPicture-desiredSizeForMainPixelMap?: Size-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

