# IncrementalScope

Define the IncrementalScope interface to manage state management.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## param

```TypeScript
param<T>(index: int, value: T): ReadableState<T>
```

创建状态变量参数

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | int | 是 |
| value | T | 是 |

**返回值：**

| 类型 |
| --- |
| [ReadableState](arkts-arkui-state-readablestate-i.md)&lt;T&gt; |

## recache

```TypeScript
recache(newValue?: Value): Value
```

Internal value updated after the computation.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| newValue | [Value](../../apis-arkdata/arkts-apis/arkts-arkdata-distributeddata-value-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [Value](../../apis-arkdata/arkts-apis/arkts-arkdata-distributeddata-value-i.md) |

## cached

```TypeScript
get cached(): Value
```

State variable cache, internal value if it is already computed

**类型：** Value

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## unchanged

```TypeScript
get unchanged(): boolean
```

Get the flag whether the state variable is changed, true if internal value can be returned as is

**类型：** boolean

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full
