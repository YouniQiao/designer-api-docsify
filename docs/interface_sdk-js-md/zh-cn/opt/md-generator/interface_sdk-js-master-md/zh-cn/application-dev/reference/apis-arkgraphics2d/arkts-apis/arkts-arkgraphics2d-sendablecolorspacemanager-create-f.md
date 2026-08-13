# create

## create

```TypeScript
function create(colorSpaceName: colorSpaceManager.ColorSpace): ColorSpaceManager
```

创建标准可共享的色彩管理实例。

**起始版本：** 12

**废弃版本：** -1

<!--Device-sendableColorSpaceManager-function create(colorSpaceName: colorSpaceManager.ColorSpace): ColorSpaceManager--><!--Device-sendableColorSpaceManager-function create(colorSpaceName: colorSpaceManager.ColorSpace): ColorSpaceManager-End-->

**系统能力：** SystemCapability.Graphic.Graphic2D.ColorManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| colorSpaceName | colorSpaceManager.ColorSpace | 是 |

**返回值：**

| 类型 |
| --- |
| [ColorSpaceManager](arkts-arkgraphics2d-sendablecolorspacemanager-colorspacemanager-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [18600001](../errorcode-colorspace-manager.md#18600001-参数值异常) |

## 示例

```TypeScript
import { colorSpaceManager, sendableColorSpaceManager } from '@kit.ArkGraphics2D';
let colorSpace: sendableColorSpaceManager.ColorSpaceManager;
// 创建标准SRGB色域的色彩管理实例
colorSpace = sendableColorSpaceManager.create(colorSpaceManager.ColorSpace.SRGB);
```


## create

```TypeScript
function create(primaries: colorSpaceManager.ColorSpacePrimaries, gamma: number): ColorSpaceManager
```

创建用户自定义可共享的色彩管理实例。

**起始版本：** 12

**废弃版本：** -1

<!--Device-sendableColorSpaceManager-function create(primaries: colorSpaceManager.ColorSpacePrimaries, gamma: number): ColorSpaceManager--><!--Device-sendableColorSpaceManager-function create(primaries: colorSpaceManager.ColorSpacePrimaries, gamma: number): ColorSpaceManager-End-->

**系统能力：** SystemCapability.Graphic.Graphic2D.ColorManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| primaries | colorSpaceManager.ColorSpacePrimaries | 是 |
| gamma | number | 是 |

**返回值：**

| 类型 |
| --- |
| [ColorSpaceManager](arkts-arkgraphics2d-sendablecolorspacemanager-colorspacemanager-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [18600001](../errorcode-colorspace-manager.md#18600001-参数值异常) |

## 示例

```TypeScript
import { colorSpaceManager, sendableColorSpaceManager } from '@kit.ArkGraphics2D';
let colorSpace: sendableColorSpaceManager.ColorSpaceManager;
// 定义色域标准三原色参数
let primaries: colorSpaceManager.ColorSpacePrimaries = {
  redX: 0.1,
  redY: 0.1,
  greenX: 0.2,
  greenY: 0.2,
  blueX: 0.3,
  blueY: 0.3,
  whitePointX: 0.4,
  whitePointY: 0.4
};
// 定义色域gamma值
let gamma: number = 2.2;
// 创建自定义可共享的色彩管理实例
colorSpace = sendableColorSpaceManager.create(primaries, gamma);
```
