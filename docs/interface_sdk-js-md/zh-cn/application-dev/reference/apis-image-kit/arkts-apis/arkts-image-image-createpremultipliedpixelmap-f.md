# createPremultipliedPixelMap

## 导入模块

```TypeScript
import { image } from 'kits/@kit.ImageKit';
```

## createPremultipliedPixelMap

```TypeScript
function createPremultipliedPixelMap(src: PixelMap, dst: PixelMap, callback: AsyncCallback<void>): void
```

Transforms pixelmap from unpremultiplied alpha format to premultiplied alpha format.

**起始版本：** 12

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| src | [PixelMap](arkts-image-image-pixelmap-i.md) | 是 |
| [dst](../../apis-arkui/arkts-apis/arkts-arkui-matrix4-polytopolyoptions-i.md) | [PixelMap](arkts-image-image-pixelmap-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [62980103](../errorcode-image.md#62980103-图片类型不支持) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [62980246](../errorcode-image.md#62980246-读取pixelmap失败) |
| [62980248](../errorcode-image.md#62980248-pixelmap不允许修改) |


## createPremultipliedPixelMap

```TypeScript
function createPremultipliedPixelMap(src: PixelMap, dst: PixelMap): Promise<void>
```

Transforms pixelmap from premultiplied alpha format to unpremultiplied alpha format.

**起始版本：** 12

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| src | [PixelMap](arkts-image-image-pixelmap-i.md) | 是 |
| [dst](../../apis-arkui/arkts-apis/arkts-arkui-matrix4-polytopolyoptions-i.md) | [PixelMap](arkts-image-image-pixelmap-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [62980103](../errorcode-image.md#62980103-图片类型不支持) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [62980246](../errorcode-image.md#62980246-读取pixelmap失败) |
| [62980248](../errorcode-image.md#62980248-pixelmap不允许修改) |
