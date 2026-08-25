# create

## 导入模块

```TypeScript
import { colorSpaceManager } from 'kits/@kit.ArkGraphics2D';
```

## create

```TypeScript
function create(colorSpaceName: ColorSpace): ColorSpaceManager
```

创建标准色域对象。

**起始版本：** 9

**系统能力：** SystemCapability.Graphic.Graphic2D.ColorManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| colorSpaceName | [ColorSpace](../../apis-arkui/arkts-apis/arkts-arkui-window-colorspace-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [ColorSpaceManager](arkts-arkgraphics2d-sendablecolorspacemanager-colorspacemanager-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [18600001](../errorcode-colorspace-manager.md#18600001-参数值异常) |


## create

```TypeScript
function create(primaries: ColorSpacePrimaries, gamma: number): ColorSpaceManager
```

创建用户自定义色域对象。

**起始版本：** 9

**系统能力：** SystemCapability.Graphic.Graphic2D.ColorManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| primaries | [ColorSpacePrimaries](arkts-arkgraphics2d-colorspacemanager-colorspaceprimaries-i.md) | 是 |
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
