# ParseInfo

当前XML解析信息。

**起始版本：** 8

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
import { xml } from 'kits/@kit.ArkTS';
```

## getAttributeCount

```TypeScript
getAttributeCount(): number
```

ArkTS-Sta: getAttributeCount(): int当前开始标记的属性数量，用于遍历和处理XML属性。

**起始版本：** 8

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| number |

## getColumnNumber

```TypeScript
getColumnNumber(): number
```

ArkTS-Sta: getColumnNumber(): int获取当前列号，从1开始计数。

**起始版本：** 8

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| number |

## getDepth

```TypeScript
getDepth(): number
```

ArkTS-Sta: getDepth(): int获取元素的当前深度。

> **说明：**&gt;
> 标签内的空白事件深度与标签的深度保持一致。

**起始版本：** 8

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| number |

## getLineNumber

```TypeScript
getLineNumber(): number
```

ArkTS-Sta: getLineNumber(): int获取当前行号，从1开始。

**起始版本：** 8

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| number |

## getName

```TypeScript
getName(): string
```

获取当前元素名称。

**起始版本：** 8

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| string |

## getNamespace

```TypeScript
getNamespace(): string
```

获取当前元素的命名空间。

**起始版本：** 8

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| string |

## getPrefix

```TypeScript
getPrefix(): string
```

获取当前元素的命名空间前缀。

**起始版本：** 8

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| string |

## getText

```TypeScript
getText(): string
```

获取当前事件的文本内容。

**起始版本：** 8

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| string |

## isEmptyElementTag

```TypeScript
isEmptyElementTag(): boolean
```

判断当前元素是否为空元素。

**起始版本：** 8

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| boolean |

## isWhitespace

```TypeScript
isWhitespace(): boolean
```

判断当前事件是否只包含空格字符。

**起始版本：** 8

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| boolean |
