# createPixelMap

## 导入模块

```TypeScript
import { sendableImage } from 'kits/@kit.ImageKit';
```

## createPixelMap

```TypeScript
function createPixelMap(colors: ArrayBuffer, options: image.InitializationOptions): Promise<PixelMap>
```

Create PixelMap by data buffer.

**起始版本：** 12

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| colors | ArrayBuffer | 是 |
| options | image.InitializationOptions | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;PixelMap & gt; |
