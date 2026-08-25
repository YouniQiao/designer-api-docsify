# ColorSpaceManager

当前色域对象实例。下列API示例中都需先使用[create()](arkts-arkgraphics2d-colorspacemanager-create-f.md)获取到ColorSpaceManager实例，再通过此实例调用对应方法。

**起始版本：** 9

**系统能力：** SystemCapability.Graphic.Graphic2D.ColorManager.Core

## 导入模块

```TypeScript
import { colorSpaceManager } from 'kits/@kit.ArkGraphics2D';
```

## getColorSpaceName

```TypeScript
getColorSpaceName(): ColorSpace
```

获取色域类型。

**起始版本：** 9

**系统能力：** SystemCapability.Graphic.Graphic2D.ColorManager.Core

**返回值：**

| 类型 |
| --- |
| [ColorSpace](../../apis-arkui/arkts-apis/arkts-arkui-window-colorspace-e.md) |

**错误码：**

| 错误码ID |
| --- |
| [18600001](../errorcode-colorspace-manager.md#18600001-参数值异常) |

## getGamma

```TypeScript
getGamma(): number
```

获取色域gamma值。

**起始版本：** 9

**系统能力：** SystemCapability.Graphic.Graphic2D.ColorManager.Core

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [18600001](../errorcode-colorspace-manager.md#18600001-参数值异常) |

## getWhitePoint

```TypeScript
getWhitePoint(): Array<number>
```

获取色域白点值。

**起始版本：** 9

**系统能力：** SystemCapability.Graphic.Graphic2D.ColorManager.Core

**返回值：**

| 类型 |
| --- |
| Array & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [18600001](../errorcode-colorspace-manager.md#18600001-参数值异常) |
