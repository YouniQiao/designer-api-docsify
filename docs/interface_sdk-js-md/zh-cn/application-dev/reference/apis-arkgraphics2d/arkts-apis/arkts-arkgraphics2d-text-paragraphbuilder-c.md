# ParagraphBuilder

段落生成器，采用建造者模式构建段落对象。开发者通过构造函数传入[ParagraphStyle](arkts-arkgraphics2d-text-paragraphstyle-i.md)和 [FontCollection](arkts-arkgraphics2d-text-fontcollection-c.md)初始化ParagraphBuilder，然后通过 [pushStyle](#pushstyle)设置文本样式、[addText](#addtext)添加文本内容，最终调用 [build()](#build)接口生成[Paragraph](arkts-arkgraphics2d-text-paragraph-c.md)对象进行排版和绘制。

**起始版本：** 12

**系统能力：** SystemCapability.Graphics.Drawing

## 导入模块

```TypeScript
import { text } from 'kits/@kit.ArkGraphics2D';
```

## addPlaceholder

```TypeScript
addPlaceholder(placeholderSpan: PlaceholderSpan): void
```

用于构建文本段落时插入占位符。插入后，占位符将在段落排版中按照指定的宽度、高度和对齐方式占据相应空间，并影响文本的换行和布局。

**起始版本：** 12

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| placeholderSpan | [PlaceholderSpan](arkts-arkgraphics2d-text-placeholderspan-i.md) | 是 |

## addSymbol

```TypeScript
addSymbol(symbolId: number): void
```

向正在构建的文本段落中插入具体符号。

**起始版本：** 12

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| symbolId | number | 是 |

## addText

```TypeScript
addText(text: string): void
```

向正在构建的文本段落中插入具体的文本字符串。

**起始版本：** 12

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [text](arkts-graphics-text.md) | string | 是 |

## build

```TypeScript
build(): Paragraph
```

用于构建段落，生成可用于后续排版渲染的段落对象。调用build()后，如需再次构建文本，必须创建新的ParagraphBuilder实例。

**起始版本：** 12

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| [Paragraph](../../apis-arkui/arkts-apis/arkts-arkui-paragraph-t.md) |

## buildLineTypeset

```TypeScript
buildLineTypeset(): LineTypeset
```

构建行排版器，生成可用于逐行排版计算的LineTypeset对象。

**起始版本：** 18

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| [LineTypeset](arkts-arkgraphics2d-text-linetypeset-c.md) |

## constructor

```TypeScript
constructor(paragraphStyle: ParagraphStyle, fontCollection: FontCollection)
```

ParagraphBuilder对象的构造函数。

**起始版本：** 12

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| paragraphStyle | [ParagraphStyle](arkts-arkgraphics2d-text-paragraphstyle-i.md) | 是 |
| fontCollection | [FontCollection](arkts-arkgraphics2d-text-fontcollection-c.md) | 是 |

## popStyle

```TypeScript
popStyle(): void
```

弹出当前文本样式。

> **说明：**&gt;
> 必须在调用[pushStyle()](#pushstyle)之后才能调用此方法。调用后，后续添加的文本将使用弹出前的文本样式。如果样式栈为空，将使用
> [ParagraphStyle](arkts-arkgraphics2d-text-paragraphstyle-i.md)中的textStyle作为默认样式。

**起始版本：** 12

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Graphics.Drawing

## pushStyle

```TypeScript
pushStyle(textStyle: TextStyle): void
```

更新当前文本块的样式。

> **说明：**&gt;
> 更新当前文本块的样式，之后添加文字均采用该样式。

**起始版本：** 12

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| textStyle | [TextStyle](arkts-arkgraphics2d-text-textstyle-i.md) | 是 |
