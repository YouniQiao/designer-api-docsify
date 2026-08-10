# PixelMapFormat（系统接口）

Enumerates pixel map formats.

**起始版本：** 14

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为14。

<!--Device-unnamed-export declare enum PixelMapFormat--><!--Device-unnamed-export declare enum PixelMapFormat-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

## NV21

```TypeScript
NV21 = 2
```

Indicates that the storage order is to store Y first and then V U alternately each occupies 8 bits and are stored from the higher-order to the lower-order bits.

**起始版本：** 14

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为14。

<!--Device-PixelMapFormat-NV21 = 2--><!--Device-PixelMapFormat-NV21 = 2-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

## RGBA_8888

```TypeScript
RGBA_8888 = 1
```

Indicates that each pixel is stored on 32 bits. Each pixel contains 4 components：B(8bits), G(8bits), R(8bits), A(8bits)and are stored from the higher-order to the lower-order bits.

**起始版本：** 14

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为14。

<!--Device-PixelMapFormat-RGBA_8888 = 1--><!--Device-PixelMapFormat-RGBA_8888 = 1-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

## UNKNOWN

```TypeScript
UNKNOWN = 0
```

Indicates an unknown format.

**起始版本：** 14

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为14。

<!--Device-PixelMapFormat-UNKNOWN = 0--><!--Device-PixelMapFormat-UNKNOWN = 0-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

