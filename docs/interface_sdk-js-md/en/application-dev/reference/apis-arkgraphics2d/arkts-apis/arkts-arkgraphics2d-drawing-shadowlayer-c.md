# ShadowLayer

阴影层对象，通过设置模糊半径、偏移量和颜色，可为图形、文本等绘制内容添加阴影渲染效果。

> **说明：**
> 
> - 本Class首批接口从API version 12开始支持。
> 
> - 本模块使用屏幕物理像素单位px。
> 
> - 本模块为单线程模型策略，需要调用方自行管理线程安全和上下文状态的切换。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-drawing-class ShadowLayer--><!--Device-drawing-class ShadowLayer-End-->

**System capability:** SystemCapability.Graphics.Drawing

## Modules to Import

```TypeScript
import { drawing } from 'kits/@kit.ArkGraphics2D';
```

## create

```TypeScript
static create(blurRadius: number, x: number, y: number, color: common2D.Color): ShadowLayer
```

创建阴影层对象。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-ShadowLayer-static create(blurRadius: number, x: number, y: number, color: common2D.Color): ShadowLayer--><!--Device-ShadowLayer-static create(blurRadius: number, x: number, y: number, color: common2D.Color): ShadowLayer-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| blurRadius | number | Yes | 阴影的半径，必须为大于0的浮点数。单位为物理像素px。 |
| x | number | Yes | x轴上的偏移量，该参数为浮点数。单位为物理像素px。 |
| y | number | Yes | y轴上的偏移量，该参数为浮点数。单位为物理像素px。 |
| color | common2D.Color | Yes | ARGB格式的颜色。每个颜色通道的值是[0, 255]的整数。 |

**Return value:**

| Type | Description |
| --- | --- |
| [ShadowLayer](arkts-arkgraphics2d-drawing-shadowlayer-c.md) | 返回创建的阴影层对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |

## create

```TypeScript
static create(blurRadius: double, x: double, y: double, color: common2D.Color): ShadowLayer | undefined
```

创建阴影层对象。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-ShadowLayer-static create(blurRadius: double, x: double, y: double, color: common2D.Color): ShadowLayer | undefined--><!--Device-ShadowLayer-static create(blurRadius: double, x: double, y: double, color: common2D.Color): ShadowLayer | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| blurRadius | double | Yes | 阴影的半径，必须为大于0的浮点数。单位为物理像素px。 |
| x | double | Yes | x轴上的偏移量，该参数为浮点数。单位为物理像素px。 |
| y | double | Yes | y轴上的偏移量，该参数为浮点数。单位为物理像素px。 |
| color | common2D.Color | Yes | ARGB格式的颜色。每个颜色通道的值是[0, 255]的整数。 |

**Return value:**

| Type | Description |
| --- | --- |
| [ShadowLayer](arkts-arkgraphics2d-drawing-shadowlayer-c.md) | 返回创建的阴影层对象。创建失败时返回undefined。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |

## create

```TypeScript
static create(blurRadius: number, x: number, y: number, color: common2D.Color | number): ShadowLayer
```

创建阴影层对象。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

<!--Device-ShadowLayer-static create(blurRadius: number, x: number, y: number, color: common2D.Color | number): ShadowLayer--><!--Device-ShadowLayer-static create(blurRadius: number, x: number, y: number, color: common2D.Color | number): ShadowLayer-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| blurRadius | number | Yes | 阴影的半径，必须为大于0的浮点数。单位为物理像素px。 |
| x | number | Yes | x轴上的偏移量，该参数为浮点数。单位为物理像素px。 |
| y | number | Yes | y轴上的偏移量，该参数为浮点数。单位为物理像素px。 |
| color | common2D.Color \| number | Yes | 颜色。为common2D.Color类型时，每个颜色通道的值是[0, 255]的整数；为number类型时，必须是16进制ARGB格式的无符 号整数，取值范围为[0, 0xFFFFFFFF]。 |

**Return value:**

| Type | Description |
| --- | --- |
| [ShadowLayer](arkts-arkgraphics2d-drawing-shadowlayer-c.md) | 返回创建的阴影层对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |

## create

```TypeScript
static create(blurRadius: double, x: double, y: double, color: common2D.Color | int): ShadowLayer | undefined
```

创建阴影层对象。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-ShadowLayer-static create(blurRadius: double, x: double, y: double, color: common2D.Color | int): ShadowLayer | undefined--><!--Device-ShadowLayer-static create(blurRadius: double, x: double, y: double, color: common2D.Color | int): ShadowLayer | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| blurRadius | double | Yes | 阴影的半径，必须为大于0的浮点数。单位为物理像素px。 |
| x | double | Yes | x轴上的偏移量，该参数为浮点数。单位为物理像素px。 |
| y | double | Yes | y轴上的偏移量，该参数为浮点数。单位为物理像素px。 |
| color | common2D.Color \| int | Yes | 颜色。为common2D.Color类型时，每个颜色通道的值是[0, 255]的整数；为number类型时，必须是16进制ARGB格式的无符 号整数，取值范围为[0, 0xFFFFFFFF]。 |

**Return value:**

| Type | Description |
| --- | --- |
| [ShadowLayer](arkts-arkgraphics2d-drawing-shadowlayer-c.md) | 返回创建的阴影层对象。创建失败时返回undefined。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |

