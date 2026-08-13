# Font

Font类用于描述字型绘制时所使用的属性（如大小、字体、粗细、倾斜、缩放等），并支持文本测量、字形转换、路径轮廓获取、主题字体跟随等能力。 > **说明：** > > - 本模块使用屏幕物理像素单位px。 > > - 本模块为单线程模型策略，需要调用方自行管理线程安全和上下文状态的切换。

**起始版本：** 23

**废弃版本：** -1

<!--Device-drawing-class Font--><!--Device-drawing-class Font-End-->

**系统能力：** SystemCapability.Graphics.Drawing

## countText

```TypeScript
countText(text: string): number
```

获取文本所表示的字符数量。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-Font-countText(text: string): int--><!--Device-Font-countText(text: string): int-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| text | string | 是 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## createPathForGlyph

```TypeScript
createPathForGlyph(index: number): Path
```

获取指定字形的路径轮廓。

**起始版本：** 18

**废弃版本：** -1

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-Font-createPathForGlyph(index: number): Path--><!--Device-Font-createPathForGlyph(index: number): Path-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | number | 是 |

**返回值：**

| 类型 |
| --- |
| [Path](arkts-arkgraphics2d-drawing-path-c.md) |

## createPathForGlyph

```TypeScript
createPathForGlyph(index: number): Path | undefined
```

获取指定字形的路径轮廓。

**起始版本：** 23

**废弃版本：** -1

<!--Device-Font-createPathForGlyph(index: int): Path | undefined--><!--Device-Font-createPathForGlyph(index: int): Path | undefined-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | number | 是 |

**返回值：**

| 类型 |
| --- |
| [Path](arkts-arkgraphics2d-drawing-path-c.md) |

## enableEmbolden

```TypeScript
enableEmbolden(isEmbolden: boolean): void
```

使能字型粗体。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-Font-enableEmbolden(isEmbolden: boolean): void--><!--Device-Font-enableEmbolden(isEmbolden: boolean): void-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [isEmbolden](arkts-arkgraphics2d-drawing-font-c.md) | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## enableLinearMetrics

```TypeScript
enableLinearMetrics(isLinearMetrics: boolean): void
```

使能字型的线性缩放。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-Font-enableLinearMetrics(isLinearMetrics: boolean): void--><!--Device-Font-enableLinearMetrics(isLinearMetrics: boolean): void-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [isLinearMetrics](arkts-arkgraphics2d-drawing-font-c.md) | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## enableSubpixel

```TypeScript
enableSubpixel(isSubpixel: boolean): void
```

使能字型亚像素级别的文字绘制，显示效果平滑。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-Font-enableSubpixel(isSubpixel: boolean): void--><!--Device-Font-enableSubpixel(isSubpixel: boolean): void-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [isSubpixel](arkts-arkgraphics2d-drawing-font-c.md) | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## getBounds

```TypeScript
getBounds(glyphs: Array<number>): Array<common2D.Rect>
```

获取字形数组中每个字形的边界矩形。

**起始版本：** 18

**废弃版本：** -1

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-Font-getBounds(glyphs: Array<number>): Array<common2D.Rect>--><!--Device-Font-getBounds(glyphs: Array<number>): Array<common2D.Rect>-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| glyphs | Array & lt;number & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Array & lt;common2D.Rect & gt; |

## getBounds

```TypeScript
getBounds(glyphs: Array<number>): Array<common2D.Rect> | undefined
```

获取字形数组中每个字形的边界矩形。

**起始版本：** 23

**废弃版本：** -1

<!--Device-Font-getBounds(glyphs: Array<int>): Array<common2D.Rect> | undefined--><!--Device-Font-getBounds(glyphs: Array<int>): Array<common2D.Rect> | undefined-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| glyphs | Array & lt;number & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Array & lt;common2D.Rect & gt; |

## getEdging

```TypeScript
getEdging(): FontEdging
```

获取字型边缘效果。

**起始版本：** 12

**废弃版本：** -1

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-Font-getEdging(): FontEdging--><!--Device-Font-getEdging(): FontEdging-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| [FontEdging](arkts-arkgraphics2d-drawing-fontedging-e.md) |

## getEdging

```TypeScript
getEdging(): FontEdging | undefined
```

获取字型边缘效果。

**起始版本：** 23

**废弃版本：** -1

<!--Device-Font-getEdging(): FontEdging | undefined--><!--Device-Font-getEdging(): FontEdging | undefined-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| [FontEdging](arkts-arkgraphics2d-drawing-fontedging-e.md) |

## getHinting

```TypeScript
getHinting(): FontHinting
```

获取字型轮廓效果。

**起始版本：** 12

**废弃版本：** -1

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-Font-getHinting(): FontHinting--><!--Device-Font-getHinting(): FontHinting-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| [FontHinting](arkts-arkgraphics2d-drawing-fonthinting-e.md) |

## getHinting

```TypeScript
getHinting(): FontHinting | undefined
```

获取字型轮廓效果。

**起始版本：** 23

**废弃版本：** -1

<!--Device-Font-getHinting(): FontHinting | undefined--><!--Device-Font-getHinting(): FontHinting | undefined-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| [FontHinting](arkts-arkgraphics2d-drawing-fonthinting-e.md) |

## getMetrics

```TypeScript
getMetrics(): FontMetrics
```

获取与字体关联的FontMetrics属性。

**起始版本：** 11

**废弃版本：** -1

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-Font-getMetrics(): FontMetrics--><!--Device-Font-getMetrics(): FontMetrics-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| [FontMetrics](arkts-arkgraphics2d-drawing-fontmetrics-i.md) |

## getMetrics

```TypeScript
getMetrics(): FontMetrics | undefined
```

获取与字体关联的FontMetrics属性。

**起始版本：** 23

**废弃版本：** -1

<!--Device-Font-getMetrics(): FontMetrics | undefined--><!--Device-Font-getMetrics(): FontMetrics | undefined-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| [FontMetrics](arkts-arkgraphics2d-drawing-fontmetrics-i.md) |

## getScaleX

```TypeScript
getScaleX(): number
```

获取字型在x轴方向上的缩放比例。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-Font-getScaleX(): double--><!--Device-Font-getScaleX(): double-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| number |

## getSize

```TypeScript
getSize(): number
```

获取字型大小。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-Font-getSize(): double--><!--Device-Font-getSize(): double-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| number |

## getSkewX

```TypeScript
getSkewX(): number
```

获取字型在x轴方向上的倾斜比例。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-Font-getSkewX(): double--><!--Device-Font-getSkewX(): double-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| number |

## getTextPath

```TypeScript
getTextPath(text: string, byteLength: number, x: number, y: number): Path
```

获取文字的路径轮廓。

**起始版本：** 18

**废弃版本：** -1

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-Font-getTextPath(text: string, byteLength: number, x: number, y: number): Path--><!--Device-Font-getTextPath(text: string, byteLength: number, x: number, y: number): Path-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| text | string | 是 |
| byteLength | number | 是 |
| x | number | 是 |
| y | number | 是 |

**返回值：**

| 类型 |
| --- |
| [Path](arkts-arkgraphics2d-drawing-path-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## getTextPath

```TypeScript
getTextPath(text: string, byteLength: number, x: number, y: number): Path | undefined
```

获取文字的路径轮廓。

**起始版本：** 23

**废弃版本：** -1

<!--Device-Font-getTextPath(text: string, byteLength: int, x: double, y: double): Path | undefined--><!--Device-Font-getTextPath(text: string, byteLength: int, x: double, y: double): Path | undefined-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| text | string | 是 |
| byteLength | number | 是 |
| x | number | 是 |
| y | number | 是 |

**返回值：**

| 类型 |
| --- |
| [Path](arkts-arkgraphics2d-drawing-path-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## getTextPathWithFallback

```TypeScript
getTextPathWithFallback(text: string, byteLength: number, x: number, y: number): Path
```

获取文字的轮廓路径，支持字体回退能力。

**起始版本：** 26.0.0

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Font-getTextPathWithFallback(text: string, byteLength: number, x: number, y: number): Path--><!--Device-Font-getTextPathWithFallback(text: string, byteLength: number, x: number, y: number): Path-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| text | string | 是 |
| byteLength | number | 是 |
| x | number | 是 |
| y | number | 是 |

**返回值：**

| 类型 |
| --- |
| [Path](arkts-arkgraphics2d-drawing-path-c.md) |

## getTextPathWithFallback

```TypeScript
getTextPathWithFallback(text: string, byteLength: number, x: number, y: number): Path | undefined
```

获取文字的轮廓路径，支持字体回退能力。

**起始版本：** 26.0.0

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Font-getTextPathWithFallback(text: string, byteLength: int, x: double, y: double): Path | undefined--><!--Device-Font-getTextPathWithFallback(text: string, byteLength: int, x: double, y: double): Path | undefined-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| text | string | 是 |
| byteLength | number | 是 |
| x | number | 是 |
| y | number | 是 |

**返回值：**

| 类型 |
| --- |
| [Path](arkts-arkgraphics2d-drawing-path-c.md) |

## getTypeface

```TypeScript
getTypeface(): Typeface
```

获取字体。

**起始版本：** 11

**废弃版本：** -1

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-Font-getTypeface(): Typeface--><!--Device-Font-getTypeface(): Typeface-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| [Typeface](arkts-arkgraphics2d-drawing-typeface-c.md) |

## getTypeface

```TypeScript
getTypeface(): Typeface | undefined
```

获取字体。

**起始版本：** 23

**废弃版本：** -1

<!--Device-Font-getTypeface(): Typeface | undefined--><!--Device-Font-getTypeface(): Typeface | undefined-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| [Typeface](arkts-arkgraphics2d-drawing-typeface-c.md) |

## getWidths

```TypeScript
getWidths(glyphs: Array<number>): Array<number>
```

获取字形数组中每个字形对应的宽度。

**起始版本：** 12

**废弃版本：** -1

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-Font-getWidths(glyphs: Array<number>): Array<number>--><!--Device-Font-getWidths(glyphs: Array<number>): Array<number>-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| glyphs | Array & lt;number & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Array & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## getWidths

```TypeScript
getWidths(glyphs: Array<number>): Array<number> | undefined
```

获取字形数组中每个字形对应的宽度。

**起始版本：** 23

**废弃版本：** -1

<!--Device-Font-getWidths(glyphs: Array<int>): Array<double> | undefined--><!--Device-Font-getWidths(glyphs: Array<int>): Array<double> | undefined-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| glyphs | Array & lt;number & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Array & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## isBaselineSnap

```TypeScript
isBaselineSnap(): boolean
```

当前画布矩阵轴对齐时，获取字型基线是否与像素对齐的结果。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-Font-isBaselineSnap(): boolean--><!--Device-Font-isBaselineSnap(): boolean-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| boolean |

## isEmbeddedBitmaps

```TypeScript
isEmbeddedBitmaps(): boolean
```

获取字型是否使用内嵌位图渲染的结果。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-Font-isEmbeddedBitmaps(): boolean--><!--Device-Font-isEmbeddedBitmaps(): boolean-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| boolean |

## isEmbolden

```TypeScript
isEmbolden(): boolean
```

获取字型是否设置了粗体效果。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-Font-isEmbolden(): boolean--><!--Device-Font-isEmbolden(): boolean-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| boolean |

## isForceAutoHinting

```TypeScript
isForceAutoHinting(): boolean
```

获取字型是否自动调整轮廓以优化渲染效果的结果。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-Font-isForceAutoHinting(): boolean--><!--Device-Font-isForceAutoHinting(): boolean-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| boolean |

## isLinearMetrics

```TypeScript
isLinearMetrics(): boolean
```

获取字型是否可以线性缩放。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-Font-isLinearMetrics(): boolean--><!--Device-Font-isLinearMetrics(): boolean-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| boolean |

## isSubpixel

```TypeScript
isSubpixel(): boolean
```

获取字型是否使用亚像素渲染。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-Font-isSubpixel(): boolean--><!--Device-Font-isSubpixel(): boolean-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| boolean |

## isThemeFontFollowed

```TypeScript
isThemeFontFollowed(): boolean
```

获取字型中的字体是否跟随主题字体。默认不跟随。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-Font-isThemeFontFollowed(): boolean--><!--Device-Font-isThemeFontFollowed(): boolean-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| boolean |

## measureSingleCharacter

```TypeScript
measureSingleCharacter(text: string): number
```

测量单个字符的宽度。当前字型中的字体不支持待测量字符时，退化到使用系统字体测量字符宽度。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-Font-measureSingleCharacter(text: string): double--><!--Device-Font-measureSingleCharacter(text: string): double-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| text | string | 是 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## measureSingleCharacterWithFeatures

```TypeScript
measureSingleCharacterWithFeatures(text: string, features: Array<FontFeature>): number
```

测量单个字符的宽度，字符带有字体特征。当前字型中的字体不支持待测量字符时，退化到使用系统字体测量字符宽度。

**起始版本：** 24

**废弃版本：** -1

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-Font-measureSingleCharacterWithFeatures(text: string, features: Array<FontFeature>): double--><!--Device-Font-measureSingleCharacterWithFeatures(text: string, features: Array<FontFeature>): double-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| text | string | 是 |
| features | Array & lt;FontFeature & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [25900001](../errorcode-drawing.md#25900001-参数值异常) |

## measureText

```TypeScript
measureText(text: string, encoding: TextEncoding): number
```

测量文本的宽度。 > **说明：** > > 此接口用于测量原始字符串的文本宽度，若想测量排版后的文本宽度，建议使用 > [measure.measureText](../../../reference/apis-arkui/arkts-apis-uicontext-measureutils.md#measuretext12)替代。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-Font-measureText(text: string, encoding: TextEncoding): double--><!--Device-Font-measureText(text: string, encoding: TextEncoding): double-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| text | string | 是 |
| encoding | [TextEncoding](../../apis-arkui/arkts-apis/arkts-arkui-textcommon-textencoding-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## setBaselineSnap

```TypeScript
setBaselineSnap(isBaselineSnap: boolean): void
```

当前画布矩阵轴对齐时，设置字型基线是否与像素对齐。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-Font-setBaselineSnap(isBaselineSnap: boolean): void--><!--Device-Font-setBaselineSnap(isBaselineSnap: boolean): void-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [isBaselineSnap](arkts-arkgraphics2d-drawing-font-c.md) | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## setEdging

```TypeScript
setEdging(edging: FontEdging): void
```

设置字型边缘效果。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-Font-setEdging(edging: FontEdging): void--><!--Device-Font-setEdging(edging: FontEdging): void-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| edging | [FontEdging](arkts-arkgraphics2d-drawing-fontedging-e.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## setEmbeddedBitmaps

```TypeScript
setEmbeddedBitmaps(isEmbeddedBitmaps: boolean): void
```

设置字型是否使用字体文件中内嵌的位图字形进行渲染。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-Font-setEmbeddedBitmaps(isEmbeddedBitmaps: boolean): void--><!--Device-Font-setEmbeddedBitmaps(isEmbeddedBitmaps: boolean): void-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [isEmbeddedBitmaps](arkts-arkgraphics2d-drawing-font-c.md) | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## setForceAutoHinting

```TypeScript
setForceAutoHinting(isForceAutoHinting: boolean): void
```

设置是否自动调整字型轮廓以优化渲染效果。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-Font-setForceAutoHinting(isForceAutoHinting: boolean): void--><!--Device-Font-setForceAutoHinting(isForceAutoHinting: boolean): void-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [isForceAutoHinting](arkts-arkgraphics2d-drawing-font-c.md) | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## setHinting

```TypeScript
setHinting(hinting: FontHinting): void
```

设置字型轮廓效果。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-Font-setHinting(hinting: FontHinting): void--><!--Device-Font-setHinting(hinting: FontHinting): void-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| hinting | [FontHinting](arkts-arkgraphics2d-drawing-fonthinting-e.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## setScaleX

```TypeScript
setScaleX(scaleX: number): void
```

设置字型在x轴方向上的缩放比例。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-Font-setScaleX(scaleX: double): void--><!--Device-Font-setScaleX(scaleX: double): void-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| scaleX | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## setSize

```TypeScript
setSize(textSize: number): void
```

设置字型大小。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-Font-setSize(textSize: double): void--><!--Device-Font-setSize(textSize: double): void-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| textSize | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## setSkewX

```TypeScript
setSkewX(skewX: number): void
```

设置字型在x轴方向上的倾斜比例。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-Font-setSkewX(skewX: double): void--><!--Device-Font-setSkewX(skewX: double): void-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| skewX | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## setThemeFontFollowed

```TypeScript
setThemeFontFollowed(followed: boolean): void
```

设置字型中的字体是否跟随主题字体。设置跟随主题字体后，若系统启用主题字体并且字型未被设置字体，字型会使用该主题字体。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-Font-setThemeFontFollowed(followed: boolean): void--><!--Device-Font-setThemeFontFollowed(followed: boolean): void-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| followed | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## setTypeface

```TypeScript
setTypeface(typeface: Typeface): void
```

为字型设置字体样式（包括字体名称、粗细、斜体等属性）。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-Font-setTypeface(typeface: Typeface): void--><!--Device-Font-setTypeface(typeface: Typeface): void-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| typeface | [Typeface](arkts-arkgraphics2d-drawing-typeface-c.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## textToGlyphs

```TypeScript
textToGlyphs(text: string, glyphCount?: number): Array<number>
```

将文本转换为字形索引。

**起始版本：** 12

**废弃版本：** -1

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-Font-textToGlyphs(text: string, glyphCount?: number): Array<number>--><!--Device-Font-textToGlyphs(text: string, glyphCount?: number): Array<number>-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| text | string | 是 |
| glyphCount | number | 否 |

**返回值：**

| 类型 |
| --- |
| Array & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## textToGlyphs

```TypeScript
textToGlyphs(text: string, glyphCount?: number): Array<number> | undefined
```

将文本转换为字形索引。

**起始版本：** 23

**废弃版本：** -1

<!--Device-Font-textToGlyphs(text: string, glyphCount?: int): Array<int> | undefined--><!--Device-Font-textToGlyphs(text: string, glyphCount?: int): Array<int> | undefined-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| text | string | 是 |
| glyphCount | number | 否 |

**返回值：**

| 类型 |
| --- |
| Array & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
