# PixelMapFormat（系统接口）

Enumerates pixel map formats.

**起始版本：** 14

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为14。

<!--Device-unnamed-export declare enum PixelMapFormat--><!--Device-unnamed-export declare enum PixelMapFormat-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

## YCBCR_P010

```TypeScript
YCBCR_P010 = 4
```

Indicates that the storage order is to store Y first and then U V alternately each occupies 10 bits and are stored from the higher-order to the lower-order bits.

**起始版本：** 14

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为14。

<!--Device-PixelMapFormat-YCBCR_P010 = 4--><!--Device-PixelMapFormat-YCBCR_P010 = 4-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## RGBA_1010102

```TypeScript
RGBA_1010102 = 3
```

Indicates that each pixel is stored on 32 bits. Each pixel contains 4 components：R(10bits), G(10bits), B(10bits), A(2bits) and are stored from the higher-order to the lower-order bits.

**起始版本：** 14

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为14。

<!--Device-PixelMapFormat-RGBA_1010102 = 3--><!--Device-PixelMapFormat-RGBA_1010102 = 3-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## YCRCB_P010

```TypeScript
YCRCB_P010 = 5
```

Indicates that the storage order is to store Y first and then V U alternately each occupies 10 bits and are stored from the higher-order to the lower-order bits.

**起始版本：** 14

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为14。

<!--Device-PixelMapFormat-YCRCB_P010 = 5--><!--Device-PixelMapFormat-YCRCB_P010 = 5-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

