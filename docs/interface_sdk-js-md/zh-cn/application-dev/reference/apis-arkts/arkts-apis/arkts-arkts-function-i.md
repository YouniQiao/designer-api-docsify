# Function

Function

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

<!--Device-unnamed-export interface Function--><!--Device-unnamed-export interface Function-End-->

**系统能力：** SystemCapability.Utils.Lang

## unsafeCall

```TypeScript
unsafeCall(...r: FixedArray<Any>): Any
```

Calls the function with the specified arguments.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Function-unsafeCall(...r: FixedArray<Any>): Any--><!--Device-Function-unsafeCall(...r: FixedArray<Any>): Any-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| r | FixedArray&lt;Any&gt; | 是 | the arguments. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Any | the result of the call. |

## name

```TypeScript
get name(): string
```

Gets the name of the function.

**类型：** string

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Function-get name(): string--><!--Device-Function-get name(): string-End-->

**系统能力：** SystemCapability.Utils.Lang

