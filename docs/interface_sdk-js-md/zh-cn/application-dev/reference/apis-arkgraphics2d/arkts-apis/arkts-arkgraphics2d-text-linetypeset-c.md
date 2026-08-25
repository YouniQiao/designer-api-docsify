# LineTypeset

保存文本内容及样式的载体，可用于计算单行排版信息。下列API示例中都需先使用[ParagraphBuilder](arkts-arkgraphics2d-text-paragraphbuilder-c.md)类的 [buildLineTypeset()](arkts-arkgraphics2d-text-paragraphbuilder-c.md#buildlinetypeset)接口获取到LineTypeset对象实例，再通过此实例调用对应方法。

**起始版本：** 18

**系统能力：** SystemCapability.Graphics.Drawing

## 导入模块

```TypeScript
import { text } from 'kits/@kit.ArkGraphics2D';
```

## createLine

```TypeScript
createLine(startIndex: number, count: number): TextLine
```

根据指定的排版区间生成文本行对象。

**起始版本：** 18

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

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

## getLineBreak

```TypeScript
getLineBreak(startIndex: number, width: number): number
```

计算在限定宽度下，从指定位置开始可以排版的字符数。

**起始版本：** 18

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

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
