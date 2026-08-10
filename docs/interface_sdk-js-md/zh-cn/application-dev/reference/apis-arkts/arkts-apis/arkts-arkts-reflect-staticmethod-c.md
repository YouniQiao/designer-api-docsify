# StaticMethod

Represents static method of class

**继承/实现关系：** StaticMethod extends [Method](Method)

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

<!--Device-reflect-class StaticMethod extends Method--><!--Device-reflect-class StaticMethod extends Method-End-->

**系统能力：** SystemCapability.Utils.Lang

## equals

```TypeScript
equals(other: StaticMethod): boolean
```

Compare whether the current Static Method object is equal to another object.

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-StaticMethod-equals(other: StaticMethod): boolean--><!--Device-StaticMethod-equals(other: StaticMethod): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [StaticMethod](arkts-arkts-reflect-staticmethod-c.md) | 是 | Another Static Method object used for comparison. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | If two objects point to the same method, return true; otherwise, return false. |

## invoke

```TypeScript
invoke(args?: FixedArray<Any>): Any
```

Invokes a method

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-StaticMethod-invoke(args?: FixedArray<Any>): Any--><!--Device-StaticMethod-invoke(args?: FixedArray<Any>): Any-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| args | FixedArray&lt;Any&gt; | 否 | method parameters |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Any | method return value. `undefined` for `void`. |

## isAsyn

```TypeScript
isAsyn(): boolean
```

Determine whether the static method is an asynchronous method.

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-StaticMethod-isAsyn(): boolean--><!--Device-StaticMethod-isAsyn(): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | If it is an asynchronous method, return true; otherwise, return false. |

## isGetter

```TypeScript
isGetter(): boolean
```

Determine whether the static method is a getter visitor for a property.

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-StaticMethod-isGetter(): boolean--><!--Device-StaticMethod-isGetter(): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | If it is a getter visitor, return true; otherwise, return false. |

## isSetter

```TypeScript
isSetter(): boolean
```

Determine whether the static method is a setter visitor for a property.

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-StaticMethod-isSetter(): boolean--><!--Device-StaticMethod-isSetter(): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | If it is a setter visitor, return true; otherwise, return false. |

