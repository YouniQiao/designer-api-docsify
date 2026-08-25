# PointUtils

本Class是提供处理坐标点的工具类，支持对坐标点进行取反、偏移等操作，适用于需要对坐标点进行变换处理的图形绘制场景。

> **说明：**&gt;
> - 本Class首批接口从API版本26.0.0开始支持。&gt;
> - 本模块使用屏幕物理像素单位px。&gt;
> - 本模块为单线程模型策略，需要调用方自行管理线程安全和上下文状态的切换。

**起始版本：** 26.0.0

**系统能力：** SystemCapability.Graphics.Drawing

## 导入模块

```TypeScript
import { drawing } from 'kits/@kit.ArkGraphics2D';
```

## negate

```TypeScript
static negate(point: common2D.Point): void
```

对点的坐标取反。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| point | common2D.Point | 是 |

## offset

```TypeScript
static offset(point: common2D.Point, dx: number, dy: number): void
```

将指定坐标点沿着x轴和y轴方向偏移一定距离。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| point | common2D.Point | 是 |
| [dx](../../apis-arkui/arkts-apis/arkts-arkui-actionsheetoffset-i.md) | number | 是 |
| [dy](../../apis-arkui/arkts-apis/arkts-arkui-actionsheetoffset-i.md) | number | 是 |
