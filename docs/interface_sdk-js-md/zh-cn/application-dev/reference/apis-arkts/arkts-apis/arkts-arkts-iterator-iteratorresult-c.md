# IteratorResult

表示迭代结果对象，包含迭代是否完成以及当前元素的值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
```

## constructor

```TypeScript
constructor()
```

创建表示迭代已完成的IteratorResult对象。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

## constructor

```TypeScript
constructor(done: boolean, value: T | undefined)
```

创建具有指定done状态和值的IteratorResult对象。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [done](#done) | boolean | 是 |
| [value](#value) | T \| undefined | 是 |

## constructor

```TypeScript
constructor(value: T)
```

创建表示迭代未完成并带有指定值的IteratorResult对象。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [value](#value) | T | 是 |

## done

```TypeScript
done: boolean
```

表示迭代是否已完成。为true时，迭代器已结束产出值， value为undefined；为false时，value包含当前元素。

**类型：** boolean

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

## value

```TypeScript
readonly value: T | undefined
```

迭代器返回的当前元素值。当done为true时，value为undefined； 当done为false时，value包含类型为T的当前迭代元素。

**类型：** T \| undefined

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang
