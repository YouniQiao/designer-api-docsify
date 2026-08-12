# IncrementalScope

Define the IncrementalScope interface to manage state management.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface IncrementalScope<Value>--><!--Device-unnamed-export declare interface IncrementalScope<Value>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## param

```TypeScript
param<T>(index: int, value: T): ReadableState<T>
```

Internal state for parameter.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IncrementalScope-param<T>(index: int, value: T): ReadableState<T>--><!--Device-IncrementalScope-param<T>(index: int, value: T): ReadableState<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | index |
| value | T | Yes | the value to be updated |

**Return value:**

| Type | Description |
| --- | --- |
| [ReadableState](arkts-arkui-state-readablestate-i.md)&lt;T&gt; | return state variable Value |

## recache

```TypeScript
recache(newValue?: Value): Value
```

Internal value updated after the computation.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IncrementalScope-recache(newValue?: Value): Value--><!--Device-IncrementalScope-recache(newValue?: Value): Value-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| newValue | Value | No | new value |

**Return value:**

| Type | Description |
| --- | --- |
| Value | return the Value from cached |

## cached

```TypeScript
get cached(): Value
```

State variable cache, internal value if it is already computed

**Type:** Value

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IncrementalScope-get cached(): Value--><!--Device-IncrementalScope-get cached(): Value-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## unchanged

```TypeScript
get unchanged(): boolean
```

Get the flag whether the state variable is changed, true if internal value can be returned as is

**Type:** boolean

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IncrementalScope-get unchanged(): boolean--><!--Device-IncrementalScope-get unchanged(): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

