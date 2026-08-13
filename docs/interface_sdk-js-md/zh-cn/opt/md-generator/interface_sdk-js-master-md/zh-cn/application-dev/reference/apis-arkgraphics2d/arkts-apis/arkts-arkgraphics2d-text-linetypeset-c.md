# LineTypeset

保存文本内容及样式的载体，可用于计算单行排版信息。 下列API示例中都需先使用[ParagraphBuilder](arkts-arkgraphics2d-text-paragraphbuilder-c.md#ParagraphBuilder)类的 [buildLineTypeset()](arkts-arkgraphics2d-text-paragraphbuilder-c.md#buildLineTypeset)接口获取到LineTypeset对象实例，再通过此实例调用对应方法。

**起始版本：** 23

**废弃版本：** -1

<!--Device-text-class LineTypeset--><!--Device-text-class LineTypeset-End-->

**系统能力：** SystemCapability.Graphics.Drawing

## createLine

```TypeScript
createLine(startIndex: number, count: number): TextLine
```

根据指定的排版区间生成文本行对象。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-LineTypeset-createLine(startIndex: int, count: int): TextLine--><!--Device-LineTypeset-createLine(startIndex: int, count: int): TextLine-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| startIndex | number | 是 |
| count | number | 是 |

**返回值：**

| 类型 |
| --- |
| [TextLine](arkts-arkgraphics2d-text-textline-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## 示例

```TypeScript
let startIndex = 0;
let width = 100.0;
let count = lineTypeset.getLineBreak(startIndex, width);
let line : text.TextLine = lineTypeset.createLine(startIndex, count);
```

## getLineBreak

```TypeScript
getLineBreak(startIndex: number, width: number): number
```

计算在限定宽度下，从指定位置开始可以排版的字符数。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-LineTypeset-getLineBreak(startIndex: int, width: double): int--><!--Device-LineTypeset-getLineBreak(startIndex: int, width: double): int-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| startIndex | number | 是 |
| width | number | 是 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## 示例

```TypeScript
let startIndex = 0;
let width = 100.0;
let count = lineTypeset.getLineBreak(startIndex, width);
```
