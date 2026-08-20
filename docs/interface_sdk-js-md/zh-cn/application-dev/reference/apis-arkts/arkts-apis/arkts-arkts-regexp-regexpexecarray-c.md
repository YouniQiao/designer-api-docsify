# RegExpExecArray

表示exec()的返回结果，其中包含单次匹配的详细信息。

**继承/实现关系：** RegExpExecArray extends [RegExpResultArray](arkts-arkts-regexp-regexpresultarray-c.md)

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

<!--Device-unnamed-export class RegExpExecArray--><!--Device-unnamed-export class RegExpExecArray-End-->

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
```

## constructor

```TypeScript
constructor(index: int, input: string, result: Array<string | undefined>, indices: Array<Array<int>>)
```

创建包含匹配结果的RegExpExecArray实例。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RegExpExecArray-constructor(index: int, input: string, result: Array<string | undefined>, indices: Array<Array<int>>)--><!--Device-RegExpExecArray-constructor(index: int, input: string, result: Array<string | undefined>, indices: Array<Array<int>>)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | 匹配结果的起始索引。 <br>取值约束：应为整数。 |
| input | string | 是 | 参与匹配的原始字符串。 |
| result | Array&lt;string \| undefined&gt; | 是 | 匹配到的字符串数组。 |
| indices | Array&lt;Array&lt;int&gt;&gt; | 是 | 每个匹配子串的起始与结束索引数组。 |

## constructor

```TypeScript
constructor(index: int, input: string, result: Array<string | undefined>)
```

创建包含匹配结果的RegExpExecArray实例（不含索引信息）。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RegExpExecArray-constructor(index: int, input: string, result: Array<string | undefined>)--><!--Device-RegExpExecArray-constructor(index: int, input: string, result: Array<string | undefined>)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | 匹配结果的起始索引。 <br>取值约束：应为整数。 |
| input | string | 是 | 参与匹配的原始字符串。 |
| result | Array&lt;string \| undefined&gt; | 是 | 匹配到的字符串数组。 |

