# Region

区域对象，用于描述所绘制图形的区域信息。Region支持设置矩形区域和路径区域，提供区域间的合并运算、相交判断、平移、边界获取等操作。 > **说明：** > > - 本Class首批接口从API version 12开始支持。 > > - 本模块使用屏幕物理像素单位px。 > > - 本模块为单线程模型策略，需要调用方自行管理线程安全和上下文状态的切换。

**起始版本：** 23

**废弃版本：** -1

<!--Device-drawing-class Region--><!--Device-drawing-class Region-End-->

**系统能力：** SystemCapability.Graphics.Drawing

## constructor

```TypeScript
constructor()
```

构造一个区域对象。

**起始版本：** 23

**废弃版本：** -1

<!--Device-Region-constructor()--><!--Device-Region-constructor()-End-->

**系统能力：** SystemCapability.Graphics.Drawing

## constructor

```TypeScript
constructor(region: Region)
```

拷贝一个区域对象。

**起始版本：** 23

**废弃版本：** -1

<!--Device-Region-constructor(region: Region)--><!--Device-Region-constructor(region: Region)-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| region | [Region](../../apis-image-kit/arkts-apis/arkts-image-image-region-i.md) | 是 |

## constructor

```TypeScript
constructor(left: number, top: number, right: number, bottom: number)
```

构造矩形区域。

**起始版本：** 23

**废弃版本：** -1

<!--Device-Region-constructor(left: int, top: int, right: int, bottom: int)--><!--Device-Region-constructor(left: int, top: int, right: int, bottom: int)-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| left | number | 是 |
| top | number | 是 |
| right | number | 是 |
| bottom | number | 是 |

## getBoundaryPath

```TypeScript
getBoundaryPath(): Path
```

返回一个新路径，该路径取自当前区域的边界。

**起始版本：** 20

**废弃版本：** -1

<!--Device-Region-getBoundaryPath(): Path--><!--Device-Region-getBoundaryPath(): Path-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| [Path](arkts-arkgraphics2d-drawing-path-c.md) |

## getBoundaryPath

```TypeScript
getBoundaryPath(): Path | undefined
```

返回一个新路径，该路径取自当前区域的边界。

**起始版本：** 24

**废弃版本：** -1

<!--Device-Region-getBoundaryPath(): Path | undefined--><!--Device-Region-getBoundaryPath(): Path | undefined-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| [Path](arkts-arkgraphics2d-drawing-path-c.md) |

## getBounds

```TypeScript
getBounds(): common2D.Rect
```

获取区域的边界。

**起始版本：** 20

**废弃版本：** -1

<!--Device-Region-getBounds(): common2D.Rect--><!--Device-Region-getBounds(): common2D.Rect-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| common2D.Rect |

## getBounds

```TypeScript
getBounds(): common2D.Rect | undefined
```

获取区域的边界。

**起始版本：** 24

**废弃版本：** -1

<!--Device-Region-getBounds(): common2D.Rect | undefined--><!--Device-Region-getBounds(): common2D.Rect | undefined-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| common2D.Rect |

## isComplex

```TypeScript
isComplex(): boolean
```

判断当前区域是否包含多个矩形。

**起始版本：** 24

**废弃版本：** -1

<!--Device-Region-isComplex(): boolean--><!--Device-Region-isComplex(): boolean-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| boolean |

## isEmpty

```TypeScript
isEmpty(): boolean
```

判断当前区域是否为空。

**起始版本：** 24

**废弃版本：** -1

<!--Device-Region-isEmpty(): boolean--><!--Device-Region-isEmpty(): boolean-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| boolean |

## isEqual

```TypeScript
isEqual(other: Region): boolean
```

判断指定区域是否与当前区域相等。

**起始版本：** 24

**废弃版本：** -1

<!--Device-Region-isEqual(other: Region): boolean--><!--Device-Region-isEqual(other: Region): boolean-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| other | [Region](../../apis-image-kit/arkts-apis/arkts-image-image-region-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## isPointContained

```TypeScript
isPointContained(x: number, y:number): boolean
```

判断测试点是否在区域内。

**起始版本：** 23

**废弃版本：** -1

<!--Device-Region-isPointContained(x: int, y:int): boolean--><!--Device-Region-isPointContained(x: int, y:int): boolean-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| x | number | 是 |
| y | number | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## isRect

```TypeScript
isRect(): boolean
```

判断当前区域是否等同于单个矩形。

**起始版本：** 23

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Region-isRect(): boolean--><!--Device-Region-isRect(): boolean-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| boolean |

## isRegionContained

```TypeScript
isRegionContained(other: Region): boolean
```

判断其他区域是否在当前区域内。

**起始版本：** 23

**废弃版本：** -1

<!--Device-Region-isRegionContained(other: Region): boolean--><!--Device-Region-isRegionContained(other: Region): boolean-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| other | [Region](../../apis-image-kit/arkts-apis/arkts-image-image-region-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## offset

```TypeScript
offset(dx: number, dy: number): void
```

对区域进行平移。

**起始版本：** 24

**废弃版本：** -1

<!--Device-Region-offset(dx: int, dy: int): void--><!--Device-Region-offset(dx: int, dy: int): void-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| dx | number | 是 |
| dy | number | 是 |

## op

```TypeScript
op(region: Region, regionOp: RegionOp): boolean
```

将当前区域与指定区域进行运算，并替换为运算结果。

**起始版本：** 23

**废弃版本：** -1

<!--Device-Region-op(region: Region, regionOp: RegionOp): boolean--><!--Device-Region-op(region: Region, regionOp: RegionOp): boolean-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| region | [Region](../../apis-image-kit/arkts-apis/arkts-image-image-region-i.md) | 是 |
| regionOp | [RegionOp](arkts-arkgraphics2d-drawing-regionop-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## quickContains

```TypeScript
quickContains(left: number, top: number, right: number, bottom: number): boolean
```

判断当前区域是否等同于单个矩形并且包含指定矩形。

**起始版本：** 23

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Region-quickContains(left: int, top: int, right: int, bottom: int): boolean--><!--Device-Region-quickContains(left: int, top: int, right: int, bottom: int): boolean-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| left | number | 是 |
| top | number | 是 |
| right | number | 是 |
| bottom | number | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## quickReject

```TypeScript
quickReject(left: number, top: number, right: number, bottom: number): boolean
```

快速判断矩形和区域是否不相交。实际上比较的是矩形和区域的外接矩形是否不相交，因此当外接矩形相交但实际区域不相交时，会返回false（即误判为相交）。

**起始版本：** 23

**废弃版本：** -1

<!--Device-Region-quickReject(left: int, top: int, right: int, bottom: int): boolean--><!--Device-Region-quickReject(left: int, top: int, right: int, bottom: int): boolean-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| left | number | 是 |
| top | number | 是 |
| right | number | 是 |
| bottom | number | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## quickRejectRegion

```TypeScript
quickRejectRegion(region: Region): boolean
```

判断当前区域是否与指定区域不相交。实际上比较的是两个区域的外接矩形是否不相交，因此当外接矩形相交但实际区域不相交时，会返回false（即误判为相交）。

**起始版本：** 24

**废弃版本：** -1

<!--Device-Region-quickRejectRegion(region: Region): boolean--><!--Device-Region-quickRejectRegion(region: Region): boolean-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| region | [Region](../../apis-image-kit/arkts-apis/arkts-image-image-region-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## setEmpty

```TypeScript
setEmpty(): void
```

设置当前区域为空。

**起始版本：** 23

**废弃版本：** -1

<!--Device-Region-setEmpty(): void--><!--Device-Region-setEmpty(): void-End-->

**系统能力：** SystemCapability.Graphics.Drawing

## setPath

```TypeScript
setPath(path: Path, clip: Region): boolean
```

设置一个与裁剪区域内路径轮廓相匹配的区域。

**起始版本：** 23

**废弃版本：** -1

<!--Device-Region-setPath(path: Path, clip: Region): boolean--><!--Device-Region-setPath(path: Path, clip: Region): boolean-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | [Path](arkts-arkgraphics2d-drawing-path-c.md) | 是 |
| clip | [Region](../../apis-image-kit/arkts-apis/arkts-image-image-region-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## setRect

```TypeScript
setRect(left: number, top: number, right: number, bottom: number): boolean
```

设置一个矩形区域。

**起始版本：** 23

**废弃版本：** -1

<!--Device-Region-setRect(left: int, top: int, right: int, bottom: int): boolean--><!--Device-Region-setRect(left: int, top: int, right: int, bottom: int): boolean-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| left | number | 是 |
| top | number | 是 |
| right | number | 是 |
| bottom | number | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## setRegion

```TypeScript
setRegion(region: Region): void
```

设置当前区域为指定区域。

**起始版本：** 24

**废弃版本：** -1

<!--Device-Region-setRegion(region: Region): void--><!--Device-Region-setRegion(region: Region): void-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| region | [Region](../../apis-image-kit/arkts-apis/arkts-image-image-region-i.md) | 是 |
