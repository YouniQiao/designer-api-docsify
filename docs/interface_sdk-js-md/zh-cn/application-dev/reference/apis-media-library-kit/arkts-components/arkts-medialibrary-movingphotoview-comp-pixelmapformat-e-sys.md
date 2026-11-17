# PixelMapFormat（系统接口）

```TypeScript
export declare enum PixelMapFormat
```

位图格式的枚举定义。

**起始版本：** 14

<!--Device-unnamed-export declare enum PixelMapFormat--><!--Device-unnamed-export declare enum PixelMapFormat-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

## NV21

```TypeScript
NV21 = 2
```

表示存储顺序是先存储Y，然后交替存储V U各占8位和从高位到低位存储。

**起始版本：** 14

<!--Device-PixelMapFormat-NV21 = 2--><!--Device-PixelMapFormat-NV21 = 2-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

## RGBA_1010102

```TypeScript
RGBA_1010102 = 3
```

表示每个像素以32位为单位存储。每个像素包含4个分量：R(10bits)、G(10bits)、B(10bits)、A(2bits)，并从高位到低位存储。

**起始版本：** 14

<!--Device-PixelMapFormat-RGBA_1010102 = 3--><!--Device-PixelMapFormat-RGBA_1010102 = 3-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

## RGBA_8888

```TypeScript
RGBA_8888 = 1
```

表示每个像素以32位为单位存储。每个像素包含4个分量：B(8bits)、G(8bits)、R(8bits)、A(8bits)和从高位到低位存储。

**起始版本：** 14

<!--Device-PixelMapFormat-RGBA_8888 = 1--><!--Device-PixelMapFormat-RGBA_8888 = 1-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

## UNKNOWN

```TypeScript
UNKNOWN = 0
```

未知格式。

**起始版本：** 14

<!--Device-PixelMapFormat-UNKNOWN = 0--><!--Device-PixelMapFormat-UNKNOWN = 0-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

## YCBCR_P010

```TypeScript
YCBCR_P010 = 4
```

表示存储顺序是先存储Y，再存储U V，各占用10位和从高位到低位存储。

**起始版本：** 14

<!--Device-PixelMapFormat-YCBCR_P010 = 4--><!--Device-PixelMapFormat-YCBCR_P010 = 4-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

## YCRCB_P010

```TypeScript
YCRCB_P010 = 5
```

表示存储顺序是先存储Y，然后交替存储V U各占10位和从高位到低位存储。

**起始版本：** 14

<!--Device-PixelMapFormat-YCRCB_P010 = 5--><!--Device-PixelMapFormat-YCRCB_P010 = 5-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。
