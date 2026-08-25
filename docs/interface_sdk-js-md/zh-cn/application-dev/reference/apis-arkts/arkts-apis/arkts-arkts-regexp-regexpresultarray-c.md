# RegExpResultArray

正则表达式匹配结果描述符。

**继承/实现关系：** RegExpResultArray extends Array<string | undefined>

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
```

## $_get

```TypeScript
$_get(index: string): string
```

当传入"0"且首个匹配存在时，返回该匹配结果。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | string | 是 |

**返回值：**

| 类型 |
| --- |
| string |

## $_get

```TypeScript
$_get(index: int): string | undefined
```

按索引返回结果字符串。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | int | 是 |

**返回值：**

| 类型 |
| --- |
| string \| undefined |

## $_set

```TypeScript
public $_set(index: int, val: string | undefined): void
```

设置指定索引处的匹配结果。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | int | 是 |
| val | string \| undefined | 是 |

## constructor

```TypeScript
constructor(index: int, input: string, result: Array<string | undefined>, indices: Array<Array<int>>)
```

创建RegExpResultArray实例。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | int | 是 |
| input | string | 是 |
| [result](#result) | Array & lt;string \ | undefined & gt; | 是 |
| [indices](#indices) | Array & lt;Array & lt;int & gt; & gt; | 是 |

## postExecProcessing

```TypeScript
public postExecProcessing(res: RegExpResultArray, input: string, index: int, hasIndices: boolean): void
```

执行后的后处理。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| res | [RegExpResultArray](arkts-arkts-regexp-regexpresultarray-c.md) | 是 |
| input | string | 是 |
| index | int | 是 |
| [hasIndices](arkts-arkts-regexp-c.md) | boolean | 是 |

## toString

```TypeScript
public toString(): string
```

返回匹配结果的字符串表示。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| string |

## indices

```TypeScript
public get indices(): Array<Array<int>>
```

获取包含每个匹配子串起始与结束索引的数组。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

## result

```TypeScript
public get result(): Array<string | undefined>
```

获取匹配结果数组本身。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang
