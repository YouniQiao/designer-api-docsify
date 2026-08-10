# RoundRect

圆角矩形对象。支持设置和获取指定圆角位置的圆角半径，以及对圆角矩形进行平移操作。

> **说明：**
> 
> - 本Class首批接口从API version 12开始支持。
> 
> - 本模块使用屏幕物理像素单位px。
> 
> - 本模块为单线程模型策略，需要调用方自行管理线程安全和上下文状态的切换。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-drawing-class RoundRect--><!--Device-drawing-class RoundRect-End-->

**System capability:** SystemCapability.Graphics.Drawing

## Modules to Import

```TypeScript
import { drawing } from 'kits/@kit.ArkGraphics2D';
```

## constructor

```TypeScript
constructor(roundRect: RoundRect)
```

拷贝一个圆角矩形。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-RoundRect-constructor(roundRect: RoundRect)--><!--Device-RoundRect-constructor(roundRect: RoundRect)-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| roundRect | [RoundRect](arkts-arkgraphics2d-drawing-roundrect-c.md) | Yes | 用于拷贝的圆角矩形。 |

## constructor

ArkTS-Dyn:
```TypeScript
constructor(rect: common2D.Rect, xRadii: number, yRadii: number)
```

ArkTS-Sta:
```TypeScript
constructor(rect: common2D.Rect, xRadii: double, yRadii: double)
```

构造一个圆角矩形对象，当且仅当xRadii和yRadii均大于0时，圆角生效，否则只会构造一个矩形。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-RoundRect-constructor(rect: common2D.Rect, xRadii: double, yRadii: double)--><!--Device-RoundRect-constructor(rect: common2D.Rect, xRadii: double, yRadii: double)-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| rect | common2D.Rect | Yes | 需要创建的圆角矩形区域。 |
| xRadii | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | x轴方向的圆角半径，该参数为浮点数，取值大于0时圆角生效，小于等于0时圆角不生效。 单位为物理像素px。 |
| yRadii | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | y轴方向的圆角半径，该参数为浮点数，取值大于0时圆角生效，小于等于0时圆角不生效。 单位为物理像素px。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types. |

## getCorner

```TypeScript
getCorner(pos: CornerPos): common2D.Point
```

获取圆角矩形中指定圆角位置的圆角半径。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-RoundRect-getCorner(pos: CornerPos): common2D.Point--><!--Device-RoundRect-getCorner(pos: CornerPos): common2D.Point-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pos | [CornerPos](arkts-arkgraphics2d-drawing-cornerpos-e.md) | Yes | 圆角位置。 |

**Return value:**

| Type | Description |
| --- | --- |
| common2D.Point | 返回一个点，其横坐标表示圆角x轴方向上的半径，纵坐标表示y轴方向上的半径。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |

## getCorner

```TypeScript
getCorner(pos: CornerPos): common2D.Point | undefined
```

获取圆角矩形中指定圆角位置的圆角半径。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-RoundRect-getCorner(pos: CornerPos): common2D.Point | undefined--><!--Device-RoundRect-getCorner(pos: CornerPos): common2D.Point | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pos | [CornerPos](arkts-arkgraphics2d-drawing-cornerpos-e.md) | Yes | 圆角位置。 |

**Return value:**

| Type | Description |
| --- | --- |
| common2D.Point | 返回一个点，其横坐标表示圆角x轴方向上的半径，纵坐标表示y轴方向上的半径。 获取失败时返回undefined。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |

## offset

ArkTS-Dyn:
```TypeScript
offset(dx: number, dy: number): void
```

ArkTS-Sta:
```TypeScript
offset(dx: double, dy: double): void
```

将圆角矩形沿x轴方向平移dx、沿y轴方向平移dy。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-RoundRect-offset(dx: double, dy: double): void--><!--Device-RoundRect-offset(dx: double, dy: double): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| dx | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | 表示x轴方向上的偏移量。正数表示向x轴正方向平移，负数表示向x轴负方向平移，该参数为浮点数。单位为物理像素px。 |
| dy | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | 表示y轴方向上的偏移量。正数表示向y轴正方向平移，负数表示向y轴负方向平移，该参数为浮点数。单位为物理像素px。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types. |

## setCorner

ArkTS-Dyn:
```TypeScript
setCorner(pos: CornerPos, x: number, y: number): void
```

ArkTS-Sta:
```TypeScript
setCorner(pos: CornerPos, x: double, y: double): void
```

设置圆角矩形中指定圆角位置的圆角半径。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-RoundRect-setCorner(pos: CornerPos, x: double, y: double): void--><!--Device-RoundRect-setCorner(pos: CornerPos, x: double, y: double): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pos | [CornerPos](arkts-arkgraphics2d-drawing-cornerpos-e.md) | Yes | 圆角位置。 |
| x | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | x轴方向的圆角半径，该参数为浮点数，取值大于0时该圆角半径设置生效，小于等于0时该圆角半径设置不生效。 单位为物理像素px。 |
| y | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | y轴方向的圆角半径，该参数为浮点数，取值大于0时该圆角半径设置生效，小于等于0时该圆角半径设置不生效。 单位为物理像素px。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |

