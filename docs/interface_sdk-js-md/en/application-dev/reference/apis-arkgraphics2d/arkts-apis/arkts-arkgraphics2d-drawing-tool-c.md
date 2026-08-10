# Tool

本模块定义的工具类，仅提供静态的方法，主要完成其他模块和[common2D](arkts-graphics-common2d.md)中定义的数据结构的转换功能。

> **说明：**
> 
> - 本Class首批接口从API version 15开始支持。
> 
> - 本模块使用屏幕物理像素单位px。
> 
> - 本模块为单线程模型策略，需要调用方自行管理线程安全和上下文状态的切换。

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

<!--Device-drawing-class Tool--><!--Device-drawing-class Tool-End-->

**System capability:** SystemCapability.Graphics.Drawing

## Modules to Import

```TypeScript
import { drawing } from 'kits/@kit.ArkGraphics2D';
```

## makeColorFromResourceColor

```TypeScript
static makeColorFromResourceColor(resourceColor: ResourceColor): common2D.Color
```

将ResourceColor类型的值转换为common2D.Color对象。

**Since:** 15

**ArkTS mode:** ArkTS-Dyn only, since version 15.

<!--Device-Tool-static makeColorFromResourceColor(resourceColor: ResourceColor): common2D.Color--><!--Device-Tool-static makeColorFromResourceColor(resourceColor: ResourceColor): common2D.Color-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| resourceColor | [ResourceColor](../../apis-arkui/arkts-apis/arkts-arkui-resourcecolor-t.md) | Yes | ResourceColor格式的颜色值（支持所有的4种输入，示例中提供10个示例输入）。其中第4种类型 [Resource](../../apis-arkui/arkts-apis/arkts-arkui-resource-t.md/arkts-arkui-resource-t.md)只接受``\\$r('belonging.type.name')``构造方法，需要确保该资源在main/resources/base/element目录下已定义(app支 持color、string和integer，sys只支持color)。 |

**Return value:**

| Type | Description |
| --- | --- |
| common2D.Color | 转换后的common2D.Color颜色对象，若转换失败则返回undefined。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types. |

## makeColorFromResourceColor

```TypeScript
static makeColorFromResourceColor(resourceColor: ResourceColor): common2D.Color | undefined
```

将ResourceColor类型的值转换为common2D.Color对象。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-Tool-static makeColorFromResourceColor(resourceColor: ResourceColor): common2D.Color | undefined--><!--Device-Tool-static makeColorFromResourceColor(resourceColor: ResourceColor): common2D.Color | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| resourceColor | [ResourceColor](../../apis-arkui/arkts-apis/arkts-arkui-resourcecolor-t.md) | Yes | ResourceColor格式的颜色值（支持所有的4种输入，示例中提供10个示例输入）。其中第4种类型 [Resource](../../apis-arkui/arkts-apis/arkts-arkui-resource-t.md/arkts-arkui-resource-t.md)只接受``\\$r('belonging.type.name')``构造方法，需要确保该资源在main/resources/base/element目录下已定义(app支 持color、string和integer，sys只支持color)。 |

**Return value:**

| Type | Description |
| --- | --- |
| common2D.Color | 转换后的common2D.Color颜色对象，若转换失败则返回undefined。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types. |

