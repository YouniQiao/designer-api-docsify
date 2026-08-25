# decomposeToPicture（系统接口）

## 导入模块

```TypeScript
import { image } from 'kits/@kit.ImageKit';
```

## decomposeToPicture

```TypeScript
function decomposeToPicture(hdrPixelMap : PixelMap, options?: HdrDecomposeOptions): Promise<Picture | undefined>
```

将HDR PixelMap分解为包含SDR PixelMap和增益图（gainmap）的Picture对象。使用Promise异步回调。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| hdrPixelMap | [PixelMap](arkts-image-image-pixelmap-i.md) | 是 |
| options | [HdrDecomposeOptions](arkts-image-image-hdrdecomposeoptions-i-sys.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[Picture](arkts-image-image-picture-i.md) \| undefined & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [7600201](../errorcode-image.md#7600201-不支持的操作) |
| [7600206](../errorcode-image.md#7600206-无效参数) |
| [7600208](../errorcode-image.md#7600208-hdr图片分解失败) |
| [7600301](../errorcode-image.md#7600301-申请内存失败) |
