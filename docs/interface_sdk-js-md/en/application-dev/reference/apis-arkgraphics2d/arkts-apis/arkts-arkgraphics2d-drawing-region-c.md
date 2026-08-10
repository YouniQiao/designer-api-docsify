# Region

区域对象，用于描述所绘制图形的区域信息。Region支持设置矩形区域和路径区域，提供区域间的合并运算、相交判断、平移、边界获取等操作。

> **说明：**
> 
> - 本Class首批接口从API version 12开始支持。
> 
> - 本模块使用屏幕物理像素单位px。
> 
> - 本模块为单线程模型策略，需要调用方自行管理线程安全和上下文状态的切换。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-drawing-class Region--><!--Device-drawing-class Region-End-->

**System capability:** SystemCapability.Graphics.Drawing

## Modules to Import

```TypeScript
import { drawing } from 'kits/@kit.ArkGraphics2D';
```

## constructor

```TypeScript
constructor()
```

构造一个区域对象。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-Region-constructor()--><!--Device-Region-constructor()-End-->

**System capability:** SystemCapability.Graphics.Drawing

## constructor

```TypeScript
constructor(region: Region)
```

拷贝一个区域对象。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-Region-constructor(region: Region)--><!--Device-Region-constructor(region: Region)-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| region | [Region](arkts-arkgraphics2d-drawing-region-c.md) | Yes | 用于拷贝的区域。 |

## constructor

ArkTS-Dyn:
```TypeScript
constructor(left: number, top: number, right: number, bottom: number)
```

ArkTS-Sta:
```TypeScript
constructor(left: int, top: int, right: int, bottom: int)
```

构造矩形区域。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-Region-constructor(left: int, top: int, right: int, bottom: int)--><!--Device-Region-constructor(left: int, top: int, right: int, bottom: int)-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| left | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 矩形区域的左侧位置（矩形左上角横坐标）。该参数必须为整数。0表示坐标原点，负数表示位于坐标原点左侧，正数表示位于坐标原点右侧。单位为物理像素px。 |
| top | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 矩形区域的顶部位置（矩形左上角纵坐标）。该参数必须为整数。0表示坐标原点，负数表示位于坐标原点上侧，正数表示位于坐标原点下侧。单位为物理像素px。 |
| right | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 矩形区域的右侧位置（矩形右下角横坐标）。该参数必须为整数。0表示坐标原点，负数表示位于坐标原点左侧，正数表示位于坐标原点右侧。单位为物理像素px。 |
| bottom | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 矩形区域的底部位置（矩形右下角纵坐标）。该参数必须为整数。0表示坐标原点，负数表示位于坐标原点上侧，正数表示位于坐标原点下侧。单位为物理像素px。 |

## getBoundaryPath

```TypeScript
getBoundaryPath(): Path
```

返回一个新路径，该路径取自当前区域的边界。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

<!--Device-Region-getBoundaryPath(): Path--><!--Device-Region-getBoundaryPath(): Path-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| [Path](arkts-arkgraphics2d-drawing-path-c.md) | 返回当前区域边界的路径。 |

## getBoundaryPath

```TypeScript
getBoundaryPath(): Path | undefined
```

返回一个新路径，该路径取自当前区域的边界。

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

<!--Device-Region-getBoundaryPath(): Path | undefined--><!--Device-Region-getBoundaryPath(): Path | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| [Path](arkts-arkgraphics2d-drawing-path-c.md) | 返回当前区域边界的路径。 |

## getBounds

```TypeScript
getBounds(): common2D.Rect
```

获取区域的边界。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

<!--Device-Region-getBounds(): common2D.Rect--><!--Device-Region-getBounds(): common2D.Rect-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| common2D.Rect | 返回当前区域的边界矩形。 |

## getBounds

```TypeScript
getBounds(): common2D.Rect | undefined
```

获取区域的边界。

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

<!--Device-Region-getBounds(): common2D.Rect | undefined--><!--Device-Region-getBounds(): common2D.Rect | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| common2D.Rect | 返回当前区域的边界矩形。 |

## isComplex

```TypeScript
isComplex(): boolean
```

判断当前区域是否包含多个矩形。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 24.

<!--Device-Region-isComplex(): boolean--><!--Device-Region-isComplex(): boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 返回当前区域是否包含多个矩形的结果。true表示当前区域包含多个矩形，false表示当前区域不包含多个矩形。 |

## isEmpty

```TypeScript
isEmpty(): boolean
```

判断当前区域是否为空。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 24.

<!--Device-Region-isEmpty(): boolean--><!--Device-Region-isEmpty(): boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 返回当前区域是否为空的结果。true表示当前区域为空，false表示当前区域不为空。 |

## isEqual

```TypeScript
isEqual(other: Region): boolean
```

判断指定区域是否与当前区域相等。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 24.

<!--Device-Region-isEqual(other: Region): boolean--><!--Device-Region-isEqual(other: Region): boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| other | [Region](arkts-arkgraphics2d-drawing-region-c.md) | Yes | 用于与当前区域进行比较的其他区域对象。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 返回其他区域是否与当前区域相等的结果。true表示相等，false表示不相等。 |

## isPointContained

ArkTS-Dyn:
```TypeScript
isPointContained(x: number, y:number): boolean
```

ArkTS-Sta:
```TypeScript
isPointContained(x: int, y:int): boolean
```

判断测试点是否在区域内。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-Region-isPointContained(x: int, y:int): boolean--><!--Device-Region-isPointContained(x: int, y:int): boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| x | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 测试点的x轴坐标。该参数必须为整数。当输入的数字带小数时，小数部分会被舍去。单位为物理像素px。 |
| y | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 测试点的y轴坐标。该参数必须为整数。当输入的数字带小数时，小数部分会被舍去。单位为物理像素px。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 返回测试点是否在区域内的结果。true表示测试点在区域内，false表示测试点不在区域内。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types. |

## isRect

```TypeScript
isRect(): boolean
```

判断当前区域是否等同于单个矩形。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Region-isRect(): boolean--><!--Device-Region-isRect(): boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 返回当前区域是否等同于单个矩形的结果。true表示当前区域等同于单个矩形，false表示当前区域不等同于单个矩形。 |

## isRegionContained

```TypeScript
isRegionContained(other: Region): boolean
```

判断其他区域是否在当前区域内。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-Region-isRegionContained(other: Region): boolean--><!--Device-Region-isRegionContained(other: Region): boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| other | [Region](arkts-arkgraphics2d-drawing-region-c.md) | Yes | 用于判断是否在当前区域内的其他区域对象。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 返回其他区域是否在当前区域内的结果。true表示其他区域在当前区域内，false表示其他区域不在当前区域内。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types. |

## offset

ArkTS-Dyn:
```TypeScript
offset(dx: number, dy: number): void
```

ArkTS-Sta:
```TypeScript
offset(dx: int, dy: int): void
```

对区域进行平移。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 24.

<!--Device-Region-offset(dx: int, dy: int): void--><!--Device-Region-offset(dx: int, dy: int): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| dx | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | x轴方向平移量，正数往x轴正方向平移，负数往x轴负方向平移，该参数必须为整数。当输入的数字带小数时，小数部分会被舍去。单位为物理像素px。 |
| dy | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | y轴方向平移量，正数往y轴正方向平移，负数往y轴负方向平移，该参数必须为整数。当输入的数字带小数时，小数部分会被舍去。单位为物理像素px。 |

## op

```TypeScript
op(region: Region, regionOp: RegionOp): boolean
```

将当前区域与指定区域进行运算，并替换为运算结果。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-Region-op(region: Region, regionOp: RegionOp): boolean--><!--Device-Region-op(region: Region, regionOp: RegionOp): boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| region | [Region](arkts-arkgraphics2d-drawing-region-c.md) | Yes | 用于与当前区域进行运算的指定区域对象。 |
| regionOp | [RegionOp](arkts-arkgraphics2d-drawing-regionop-e.md) | Yes | 区域运算操作类型。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 返回区域运算结果是否成功替换当前区域的结果。true表示区域运算结果替换当前区域成功，false表示区域运算结果替换当前区域失败。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types. |

## quickContains

ArkTS-Dyn:
```TypeScript
quickContains(left: number, top: number, right: number, bottom: number): boolean
```

ArkTS-Sta:
```TypeScript
quickContains(left: int, top: int, right: int, bottom: int): boolean
```

判断当前区域是否等同于单个矩形并且包含指定矩形。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Region-quickContains(left: int, top: int, right: int, bottom: int): boolean--><!--Device-Region-quickContains(left: int, top: int, right: int, bottom: int): boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| left | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 矩形区域的左侧位置。该参数必须为整数。当输入的数字带小数时，小数部分会被舍去。单位为物理像素px。 |
| top | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 矩形区域的顶部位置。该参数必须为整数。当输入的数字带小数时，小数部分会被舍去。单位为物理像素px。 |
| right | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 矩形区域的右侧位置。该参数必须为整数。当输入的数字带小数时，小数部分会被舍去。单位为物理像素px。 |
| bottom | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 矩形区域的底部位置。该参数必须为整数。当输入的数字带小数时，小数部分会被舍去。单位为物理像素px。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 返回判断结果。true表示当前区域等同于单个矩形且包含指定矩形，false表示当前区域不等同于单个矩形或不包含指定矩形。 |

## quickReject

ArkTS-Dyn:
```TypeScript
quickReject(left: number, top: number, right: number, bottom: number): boolean
```

ArkTS-Sta:
```TypeScript
quickReject(left: int, top: int, right: int, bottom: int): boolean
```

快速判断矩形和区域是否不相交。实际上比较的是矩形和区域的外接矩形是否不相交，因此当外接矩形相交但实际区域不相交时，会返回false（即误判为相交）。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-Region-quickReject(left: int, top: int, right: int, bottom: int): boolean--><!--Device-Region-quickReject(left: int, top: int, right: int, bottom: int): boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| left | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 矩形区域的左侧位置（矩形左上角横坐标）。该参数必须为整数。当输入的数字带小数时，小数部分会被舍去。单位为物理像素px。 |
| top | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 矩形区域的顶部位置（矩形左上角纵坐标）。该参数必须为整数。当输入的数字带小数时，小数部分会被舍去。单位为物理像素px。 |
| right | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 矩形区域的右侧位置（矩形右下角横坐标）。该参数必须为整数。当输入的数字带小数时，小数部分会被舍去。单位为物理像素px。 |
| bottom | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 矩形区域的底部位置（矩形右下角纵坐标）。该参数必须为整数。当输入的数字带小数时，小数部分会被舍去。单位为物理像素px。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 返回矩形是否与区域不相交的结果。true表示矩形与区域不相交，false表示矩形与区域相交。当矩形与区域仅点或边相交时，也返回true。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types. |

## quickRejectRegion

```TypeScript
quickRejectRegion(region: Region): boolean
```

判断当前区域是否与指定区域不相交。实际上比较的是两个区域的外接矩形是否不相交，因此当外接矩形相交但实际区域不相交时，会返回false（即误判为相交）。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 24.

<!--Device-Region-quickRejectRegion(region: Region): boolean--><!--Device-Region-quickRejectRegion(region: Region): boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| region | [Region](arkts-arkgraphics2d-drawing-region-c.md) | Yes | 用于判断是否与当前区域不相交的指定区域对象。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 返回当前区域与另一个区域是否不相交的结果。true表示不相交，false表示相交。当两个区域仅点或边相交时，也返回true。 |

## setEmpty

```TypeScript
setEmpty(): void
```

设置当前区域为空。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-Region-setEmpty(): void--><!--Device-Region-setEmpty(): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

## setPath

```TypeScript
setPath(path: Path, clip: Region): boolean
```

设置一个与裁剪区域内路径轮廓相匹配的区域。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-Region-setPath(path: Path, clip: Region): boolean--><!--Device-Region-setPath(path: Path, clip: Region): boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | [Path](arkts-arkgraphics2d-drawing-path-c.md) | Yes | 用于设置区域轮廓的路径对象。 |
| clip | [Region](arkts-arkgraphics2d-drawing-region-c.md) | Yes | 裁剪区域对象，用于限定路径轮廓的有效范围，仅路径在裁剪区域内的部分会被用于设置区域。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 返回设置区域是否成功的结果。true表示设置成功，false表示设置失败。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types. |

## setRect

ArkTS-Dyn:
```TypeScript
setRect(left: number, top: number, right: number, bottom: number): boolean
```

ArkTS-Sta:
```TypeScript
setRect(left: int, top: int, right: int, bottom: int): boolean
```

设置一个矩形区域。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-Region-setRect(left: int, top: int, right: int, bottom: int): boolean--><!--Device-Region-setRect(left: int, top: int, right: int, bottom: int): boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| left | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 矩形区域的左侧位置（矩形左上角横坐标）。该参数必须为整数。当输入的数字带小数时，小数部分会被舍去。单位为物理像素px。 |
| top | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 矩形区域的顶部位置（矩形左上角纵坐标）。该参数必须为整数。当输入的数字带小数时，小数部分会被舍去。单位为物理像素px。 |
| right | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 矩形区域的右侧位置（矩形右下角横坐标）。该参数必须为整数。当输入的数字带小数时，小数部分会被舍去。单位为物理像素px。 |
| bottom | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 矩形区域的底部位置（矩形右下角纵坐标）。该参数必须为整数。当输入的数字带小数时，小数部分会被舍去。单位为物理像素px。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 返回设置矩形区域是否成功的结果。true表示设置矩形区域成功，false表示设置矩形区域失败。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types. |

## setRegion

```TypeScript
setRegion(region: Region): void
```

设置当前区域为指定区域。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 24.

<!--Device-Region-setRegion(region: Region): void--><!--Device-Region-setRegion(region: Region): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| region | [Region](arkts-arkgraphics2d-drawing-region-c.md) | Yes | 用于设置当前区域内容的源区域对象。 |

