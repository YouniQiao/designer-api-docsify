# RegExpMatchArray

表示string.prototype.matchAll()返回的匹配结果， 或全局模式下RegExp.prototype.exec()的非迭代结果。

**继承/实现关系：** RegExpMatchArray extends [RegExpResultArray](arkts-arkts-regexp-regexpresultarray-c.md)

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
```

## constructor

```TypeScript
constructor(index: int, input: string, result: Array<string | undefined>, indices: Array<Array<int>>)
```

创建包含匹配结果的RegExpMatchArray实例。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [index](#index) | int | 是 |
| [input](#input) | string | 是 |
| result | Array & lt;string \ | undefined & gt; | 是 |
| indices | Array & lt;Array & lt;int & gt; & gt; | 是 |

## constructor

```TypeScript
constructor(index: int, input: string, result: Array<string | undefined>)
```

创建包含匹配结果的RegExpMatchArray实例。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [index](#index) | int | 是 |
| [input](#input) | string | 是 |
| result | Array & lt;string \ | undefined & gt; | 是 |

## index

```TypeScript
public set index(val: int | undefined)
```

设置匹配结果的起始索引。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

## input

```TypeScript
public set input(val: string | undefined)
```

设置参与匹配的原始字符串。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang
