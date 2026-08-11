# Matrix

矩阵对象，用于图形的坐标变换，支持平移、旋转、缩放和倾斜等变换操作。通过矩阵变换可实现不同坐标系之间的映射。

表示为3×3的矩阵，如下图所示：

![matrix_3x3](../../../reference/apis-arkgraphics2d/figures/matrix3X3.PNG)

矩阵中的元素从左到右，从上到下分别表示水平缩放因子、水平倾斜系数、水平位移系数、垂直倾斜系数、垂直缩放因子、垂直位移系数、x轴透视系数、y轴透视系数、透视缩放因子。

设(x&lt;sub&gt;1&lt;/sub&gt;, y&lt;sub&gt;1&lt;/sub&gt;)为源坐标点，(x&lt;sub&gt;2&lt;/sub&gt;, y&lt;sub&gt;2&lt;/sub&gt;)为源坐标点通过矩阵变换后的坐标点，则两个坐标点的关系如下：

![matrix-xy](../../../reference/apis-arkgraphics2d/figures/matrix-xy.PNG)

> **说明：**
> 
> - 本Class首批接口从API version 12开始支持。
> 
> - 本模块使用屏幕物理像素单位px。
> 
> - 本模块为单线程模型策略，需要调用方自行管理线程安全和上下文状态的切换。

**起始版本：** 12

<!--Device-drawing-class Matrix--><!--Device-drawing-class Matrix-End-->

**系统能力：** SystemCapability.Graphics.Drawing

## constructor

```TypeScript
constructor()
```

构造一个矩阵对象。

**起始版本：** 12

<!--Device-Matrix-constructor()--><!--Device-Matrix-constructor()-End-->

**系统能力：** SystemCapability.Graphics.Drawing

## constructor

```TypeScript
constructor(matrix: Matrix)
```

拷贝一个矩阵。

**起始版本：** 20

<!--Device-Matrix-constructor(matrix: Matrix)--><!--Device-Matrix-constructor(matrix: Matrix)-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| matrix | [Matrix](arkts-arkgraphics2d-drawing-matrix-c.md) | 是 |

## getAll

```TypeScript
getAll(): Array<number>
```

获取矩阵的所有元素值。

**起始版本：** 12

<!--Device-Matrix-getAll(): Array<number>--><!--Device-Matrix-getAll(): Array<number>-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| Array&lt;number&gt; |

## getValue

```TypeScript
getValue(index: number): number
```

获取矩阵给定索引位的值。索引范围0-8。

**起始版本：** 12

<!--Device-Matrix-getValue(index: int): double--><!--Device-Matrix-getValue(index: int): double-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | number | 是 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |

## invert

```TypeScript
invert(matrix: Matrix): boolean
```

将矩阵matrix设置为当前矩阵的逆矩阵，并返回是否设置成功的结果。

**起始版本：** 12

<!--Device-Matrix-invert(matrix: Matrix): boolean--><!--Device-Matrix-invert(matrix: Matrix): boolean-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| matrix | [Matrix](arkts-arkgraphics2d-drawing-matrix-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |

## isAffine

```TypeScript
isAffine(): boolean
```

判断当前矩阵是否为仿射矩阵。仿射矩阵是一种包括平移、旋转、缩放等变换的矩阵。

**起始版本：** 20

<!--Device-Matrix-isAffine(): boolean--><!--Device-Matrix-isAffine(): boolean-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| boolean |

## isEqual

```TypeScript
isEqual(matrix: Matrix): boolean
```

判断两个矩阵是否相等。

**起始版本：** 12

<!--Device-Matrix-isEqual(matrix: Matrix): boolean--><!--Device-Matrix-isEqual(matrix: Matrix): boolean-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| matrix | [Matrix](arkts-arkgraphics2d-drawing-matrix-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |

## isIdentity

```TypeScript
isIdentity(): boolean
```

判断矩阵是否是单位矩阵。

**起始版本：** 12

<!--Device-Matrix-isIdentity(): boolean--><!--Device-Matrix-isIdentity(): boolean-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| boolean |

## mapPoints

```TypeScript
mapPoints(src: Array<common2D.Point>): Array<common2D.Point>
```

通过矩阵变换将源点数组映射到目标点数组。

**起始版本：** 12

<!--Device-Matrix-mapPoints(src: Array<common2D.Point>): Array<common2D.Point>--><!--Device-Matrix-mapPoints(src: Array<common2D.Point>): Array<common2D.Point>-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| src | Array&lt;common2D.Point&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Array&lt;common2D.Point&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |

## mapRadius

```TypeScript
mapRadius(radius: number): number
```

返回半径为radius的圆经过当前矩阵映射形成的椭圆的平均半径。平均半径的平方为椭圆长轴长度和短轴长度的乘积。若当前矩阵包含透视变换，则该结果无意义。

**起始版本：** 20

<!--Device-Matrix-mapRadius(radius: double): double--><!--Device-Matrix-mapRadius(radius: double): double-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| radius | number | 是 |

**返回值：**

| 类型 |
| --- |
| number |

## mapRect

```TypeScript
mapRect(dst: common2D.Rect, src: common2D.Rect): boolean
```

将目标矩形设置为源矩形通过矩阵变换后的图形的外接矩形。如下图所示，蓝色矩形为源矩形，假设黄色矩形为源矩形通过矩阵变换形成的图形，此时黄色矩形的边不与坐标轴平行，无法使用矩形对象表示，因此，将目标矩形设置为黄色矩形的外接矩形，即黑色矩形。

![mapRect](../../../reference/apis-arkgraphics2d/figures/matrix-mapRect.png)

**起始版本：** 12

<!--Device-Matrix-mapRect(dst: common2D.Rect, src: common2D.Rect): boolean--><!--Device-Matrix-mapRect(dst: common2D.Rect, src: common2D.Rect): boolean-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| dst | common2D.Rect | 是 |
| src | common2D.Rect | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |

## postConcat

```TypeScript
postConcat(matrix: Matrix): void
```

将一个矩阵乘在当前矩阵的左侧，即新的变换在当前矩阵的变换之后应用。如果需要在当前矩阵的变换之前应用新变换，使用preConcat方法。

**起始版本：** 20

<!--Device-Matrix-postConcat(matrix: Matrix): void--><!--Device-Matrix-postConcat(matrix: Matrix): void-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| matrix | [Matrix](arkts-arkgraphics2d-drawing-matrix-c.md) | 是 |

## postRotate

```TypeScript
postRotate(degree: number, px: number, py: number): void
```

将矩阵设置为矩阵右乘围绕旋转中心点旋转degree角度的单位矩阵后得到的矩阵，即新的旋转变换在当前矩阵的变换之后应用。如果需要在当前矩阵的变换之前应用旋转变换，使用preRotate方法。

**起始版本：** 12

<!--Device-Matrix-postRotate(degree: double, px: double, py: double): void--><!--Device-Matrix-postRotate(degree: double, px: double, py: double): void-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| degree | number | 是 |
| px | number | 是 |
| py | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |

## postScale

```TypeScript
postScale(sx: number, sy: number, px: number, py: number): void
```

将矩阵设置为矩阵右乘围绕缩放中心点按sx和sy缩放系数缩放后的单位矩阵后得到的矩阵，即新的缩放变换在当前矩阵的变换之后应用。如果需要在当前矩阵的变换之前应用缩放变换，使用preScale方法。

**起始版本：** 12

<!--Device-Matrix-postScale(sx: double, sy: double, px: double, py: double): void--><!--Device-Matrix-postScale(sx: double, sy: double, px: double, py: double): void-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sx | number | 是 |
| sy | number | 是 |
| px | number | 是 |
| py | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |

## postSkew

```TypeScript
postSkew(kx: number, ky: number, px: number, py: number): void
```

当前矩阵右乘一个倾斜变换矩阵。

**起始版本：** 20

<!--Device-Matrix-postSkew(kx: double, ky: double, px: double, py: double): void--><!--Device-Matrix-postSkew(kx: double, ky: double, px: double, py: double): void-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| kx | number | 是 |
| ky | number | 是 |
| px | number | 是 |
| py | number | 是 |

## postTranslate

```TypeScript
postTranslate(dx: number, dy: number): void
```

将矩阵设置为矩阵右乘平移dx和dy距离后的单位矩阵后得到的矩阵，即新的平移变换在当前矩阵的变换之后应用。如果需要在当前矩阵的变换之前应用平移变换，使用preTranslate方法。

**起始版本：** 12

<!--Device-Matrix-postTranslate(dx: double, dy: double): void--><!--Device-Matrix-postTranslate(dx: double, dy: double): void-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| dx | number | 是 |
| dy | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |

## preConcat

```TypeScript
preConcat(matrix: Matrix): void
```

将一个矩阵乘在当前矩阵的右侧，即新的变换在当前矩阵的变换之前应用。如果需要在当前矩阵的变换之后应用新变换，使用postConcat方法。

**起始版本：** 12

<!--Device-Matrix-preConcat(matrix: Matrix): void--><!--Device-Matrix-preConcat(matrix: Matrix): void-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| matrix | [Matrix](arkts-arkgraphics2d-drawing-matrix-c.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |

## preRotate

```TypeScript
preRotate(degree: number, px: number, py: number): void
```

将矩阵设置为矩阵左乘围绕旋转中心点旋转degree角度的单位矩阵后得到的矩阵，即新的旋转变换在当前矩阵的变换之前应用。如果需要在当前矩阵的变换之后应用旋转变换，使用postRotate方法。

**起始版本：** 12

<!--Device-Matrix-preRotate(degree: double, px: double, py: double): void--><!--Device-Matrix-preRotate(degree: double, px: double, py: double): void-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| degree | number | 是 |
| px | number | 是 |
| py | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |

## preScale

```TypeScript
preScale(sx: number, sy: number, px: number, py: number): void
```

将矩阵设置为矩阵左乘围绕缩放中心点按sx和sy缩放系数缩放后的单位矩阵后得到的矩阵，即新的缩放变换在当前矩阵的变换之前应用。如果需要在当前矩阵的变换之后应用缩放变换，使用postScale方法。

**起始版本：** 12

<!--Device-Matrix-preScale(sx: double, sy: double, px: double, py: double): void--><!--Device-Matrix-preScale(sx: double, sy: double, px: double, py: double): void-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sx | number | 是 |
| sy | number | 是 |
| px | number | 是 |
| py | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |

## preSkew

```TypeScript
preSkew(kx: number, ky: number, px: number, py: number): void
```

当前矩阵左乘一个倾斜变换矩阵。

**起始版本：** 20

<!--Device-Matrix-preSkew(kx: double, ky: double, px: double, py: double): void--><!--Device-Matrix-preSkew(kx: double, ky: double, px: double, py: double): void-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| kx | number | 是 |
| ky | number | 是 |
| px | number | 是 |
| py | number | 是 |

## preTranslate

```TypeScript
preTranslate(dx: number, dy: number): void
```

将矩阵设置为矩阵左乘平移dx和dy距离后的单位矩阵后得到的矩阵，即新的平移变换在当前矩阵的变换之前应用。如果需要在当前矩阵的变换之后应用平移变换，使用postTranslate方法。

**起始版本：** 12

<!--Device-Matrix-preTranslate(dx: double, dy: double): void--><!--Device-Matrix-preTranslate(dx: double, dy: double): void-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| dx | number | 是 |
| dy | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |

## rectStaysRect

```TypeScript
rectStaysRect(): boolean
```

判断经过该矩阵映射后的矩形的形状是否仍为矩形。

**起始版本：** 20

<!--Device-Matrix-rectStaysRect(): boolean--><!--Device-Matrix-rectStaysRect(): boolean-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| boolean |

## reset

```TypeScript
reset(): void
```

重置当前矩阵为单位矩阵。

**起始版本：** 12

<!--Device-Matrix-reset(): void--><!--Device-Matrix-reset(): void-End-->

**系统能力：** SystemCapability.Graphics.Drawing

## setConcat

```TypeScript
setConcat(matrixA: Matrix, matrixB: Matrix): void
```

用两个矩阵的乘积更新当前矩阵，即当前矩阵 = matrixA × matrixB。

**起始版本：** 20

<!--Device-Matrix-setConcat(matrixA: Matrix, matrixB: Matrix): void--><!--Device-Matrix-setConcat(matrixA: Matrix, matrixB: Matrix): void-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| matrixA | [Matrix](arkts-arkgraphics2d-drawing-matrix-c.md) | 是 |
| matrixB | [Matrix](arkts-arkgraphics2d-drawing-matrix-c.md) | 是 |

## setMatrix

```TypeScript
setMatrix(values: Array<number>): void
```

设置矩阵对象的各项参数。

**起始版本：** 12

<!--Device-Matrix-setMatrix(values: Array<double>): void--><!--Device-Matrix-setMatrix(values: Array<double>): void-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| values | Array&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |

## setMatrix

```TypeScript
setMatrix(matrix: Array<number> | Matrix): void
```

用一个矩阵对当前矩阵进行更新。

**起始版本：** 20

<!--Device-Matrix-setMatrix(matrix: Array<double> | Matrix): void--><!--Device-Matrix-setMatrix(matrix: Array<double> | Matrix): void-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| matrix | Array&lt;number&gt; \| [Matrix](arkts-arkgraphics2d-drawing-matrix-c.md) | 是 |

## setPolyToPoly

```TypeScript
setPolyToPoly(src: Array<common2D.Point>, dst: Array<common2D.Point>, count: number): boolean
```

将当前矩阵设置为能够将源点数组映射到目标点数组的变换矩阵。源点和目标点的个数必须大于等于0，小于等于4。

**起始版本：** 12

<!--Device-Matrix-setPolyToPoly(src: Array<common2D.Point>, dst: Array<common2D.Point>, count: int): boolean--><!--Device-Matrix-setPolyToPoly(src: Array<common2D.Point>, dst: Array<common2D.Point>, count: int): boolean-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| src | Array&lt;common2D.Point&gt; | 是 |
| dst | Array&lt;common2D.Point&gt; | 是 |
| count | number | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |

## setRectToRect

```TypeScript
setRectToRect(src: common2D.Rect, dst: common2D.Rect, scaleToFit: ScaleToFit): boolean
```

将当前矩阵设置为能使源矩形映射到目标矩形的变换矩阵。

**起始版本：** 12

<!--Device-Matrix-setRectToRect(src: common2D.Rect, dst: common2D.Rect, scaleToFit: ScaleToFit): boolean--><!--Device-Matrix-setRectToRect(src: common2D.Rect, dst: common2D.Rect, scaleToFit: ScaleToFit): boolean-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| src | common2D.Rect | 是 |
| dst | common2D.Rect | 是 |
| scaleToFit | [ScaleToFit](arkts-arkgraphics2d-drawing-scaletofit-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |

## setRotation

```TypeScript
setRotation(degree: number, px: number, py: number): void
```

设置矩阵为单位矩阵，并围绕旋转中心点(px, py)进行旋转。

**起始版本：** 12

<!--Device-Matrix-setRotation(degree: double, px: double, py: double): void--><!--Device-Matrix-setRotation(degree: double, px: double, py: double): void-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| degree | number | 是 |
| px | number | 是 |
| py | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |

## setScale

```TypeScript
setScale(sx: number, sy: number, px: number, py: number): void
```

设置矩阵为单位矩阵，并围绕缩放中心点(px, py)按sx和sy进行缩放。

**起始版本：** 12

<!--Device-Matrix-setScale(sx: double, sy: double, px: double, py: double): void--><!--Device-Matrix-setScale(sx: double, sy: double, px: double, py: double): void-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sx | number | 是 |
| sy | number | 是 |
| px | number | 是 |
| py | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |

## setSinCos

```TypeScript
setSinCos(sinValue: number, cosValue: number, px: number, py: number): void
```

设置矩阵为单位矩阵，使其围绕旋转中心点(px, py)以指定的正弦值和余弦值旋转。与[setRotation](arkts-arkgraphics2d-drawing-matrix-c.md#setrotation)功能类似，但setRotation直接传入角度值，而本方法传入正弦值和余弦值。

**起始版本：** 20

<!--Device-Matrix-setSinCos(sinValue: double, cosValue: double, px: double, py: double): void--><!--Device-Matrix-setSinCos(sinValue: double, cosValue: double, px: double, py: double): void-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sinValue | number | 是 |
| cosValue | number | 是 |
| px | number | 是 |
| py | number | 是 |

## setSkew

```TypeScript
setSkew(kx: number, ky: number, px: number, py: number): void
```

设置矩阵为单位矩阵，并围绕倾斜中心点(px, py)按(kx, ky)进行倾斜变换。与[setRotation](arkts-arkgraphics2d-drawing-matrix-c.md#setrotation)、  
[setScale](arkts-arkgraphics2d-drawing-matrix-c.md#setscale)、[setTranslation](arkts-arkgraphics2d-drawing-matrix-c.md#settranslation)类似，均为重置矩阵后施加单一变换。

**起始版本：** 20

<!--Device-Matrix-setSkew(kx: double, ky: double, px: double, py: double): void--><!--Device-Matrix-setSkew(kx: double, ky: double, px: double, py: double): void-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| kx | number | 是 |
| ky | number | 是 |
| px | number | 是 |
| py | number | 是 |

## setTranslation

```TypeScript
setTranslation(dx: number, dy: number): void
```

设置矩阵为单位矩阵，并平移(dx, dy)。

**起始版本：** 12

<!--Device-Matrix-setTranslation(dx: double, dy: double): void--><!--Device-Matrix-setTranslation(dx: double, dy: double): void-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| dx | number | 是 |
| dy | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
