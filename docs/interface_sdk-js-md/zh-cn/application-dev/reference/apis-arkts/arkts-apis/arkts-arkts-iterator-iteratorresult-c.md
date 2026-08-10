# IteratorResult

Represents an iterator result object containing whether iteration is done and the current element value

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

<!--Device-unnamed-export class IteratorResult<out T>--><!--Device-unnamed-export class IteratorResult<out T>-End-->

**系统能力：** SystemCapability.Utils.Lang

## constructor

```TypeScript
constructor()
```

Creates an IteratorResult object representing completed iteration

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-IteratorResult-constructor()--><!--Device-IteratorResult-constructor()-End-->

**系统能力：** SystemCapability.Utils.Lang

## constructor

```TypeScript
constructor(done: boolean, value: T | undefined)
```

Creates an IteratorResult object with the specified done status and value

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-IteratorResult-constructor(done: boolean, value: T | undefined)--><!--Device-IteratorResult-constructor(done: boolean, value: T | undefined)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| done | boolean | 是 | Indicates whether iteration is completed |
| value | T \| undefined | 是 | The element value returned by the iterator |

## constructor

```TypeScript
constructor(value: T)
```

Creates an IteratorResult object representing incomplete iteration with the specified value

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-IteratorResult-constructor(value: T)--><!--Device-IteratorResult-constructor(value: T)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | T | 是 | The element value returned by the iterator |

## done

```TypeScript
done: boolean
```

Indicates whether the iteration has completed. When true, the iterator has finished producing values and value will be undefined; when false, value contains the current element.

**类型：** boolean

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-IteratorResult-done: boolean--><!--Device-IteratorResult-done: boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

## value

```TypeScript
readonly value: T | undefined
```

The current element value returned by the iterator. When done is true, value is undefined;when done is false, value contains the current iteration element of type T.

**类型：** T \| undefined

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-IteratorResult-readonly value: T | undefined--><!--Device-IteratorResult-readonly value: T | undefined-End-->

**系统能力：** SystemCapability.Utils.Lang

