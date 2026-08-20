# RegExpResultArray

正则表达式匹配结果描述符。

**继承/实现关系：** RegExpResultArray extends Array<string | undefined>

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

<!--Device-unnamed-export class RegExpResultArray--><!--Device-unnamed-export class RegExpResultArray-End-->

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

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RegExpResultArray-$_get(index: string): string--><!--Device-RegExpResultArray-$_get(index: string): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | string | 是 | 字符串索引。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 以字符串形式返回的首个匹配结果，若不存在则返回null。 |

## $_get

```TypeScript
$_get(index: int): string | undefined
```

按索引返回结果字符串。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RegExpResultArray-$_get(index: int): string | undefined--><!--Device-RegExpResultArray-$_get(index: int): string | undefined-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | 整数索引。 <br>取值约束：应为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string \| undefined | 结果字符串。 |

## $_set

```TypeScript
public $_set(index: int, val: string | undefined): void
```

设置指定索引处的匹配结果。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RegExpResultArray-public $_set(index: int, val: string | undefined): void--><!--Device-RegExpResultArray-public $_set(index: int, val: string | undefined): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | 待设置的索引。 <br>取值约束：应为整数。 |
| val | string \| undefined | 是 | 待设置的值。 |

## constructor

```TypeScript
constructor(index: int, input: string, result: Array<string | undefined>, indices: Array<Array<int>>)
```

创建RegExpResultArray实例。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RegExpResultArray-constructor(index: int, input: string, result: Array<string | undefined>, indices: Array<Array<int>>)--><!--Device-RegExpResultArray-constructor(index: int, input: string, result: Array<string | undefined>, indices: Array<Array<int>>)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | 匹配结果的起始索引。 <br>取值约束：应为整数。 |
| input | string | 是 | 参与匹配的原始字符串。 |
| result | Array&lt;string \| undefined&gt; | 是 | 匹配到的字符串数组。 |
| indices | Array&lt;Array&lt;int&gt;&gt; | 是 | 每个匹配子串的起始与结束索引数组。 |

## postExecProcessing

```TypeScript
public postExecProcessing(res: RegExpResultArray, input: string, index: int, hasIndices: boolean): void
```

执行后的后处理。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RegExpResultArray-public postExecProcessing(res: RegExpResultArray, input: string, index: int, hasIndices: boolean): void--><!--Device-RegExpResultArray-public postExecProcessing(res: RegExpResultArray, input: string, index: int, hasIndices: boolean): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| res | [RegExpResultArray](arkts-arkts-regexp-regexpresultarray-c.md) | 是 | 结果数组。 |
| input | string | 是 | 输入字符串。 |
| index | int | 是 | 索引。 <br>取值约束：应为整数。 |
| hasIndices | boolean | 是 | 是否包含索引信息。 |

## toString

```TypeScript
public toString(): string
```

返回匹配结果的字符串表示。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RegExpResultArray-public toString(): string--><!--Device-RegExpResultArray-public toString(): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 表示匹配结果的字符串。 |

