# Repeat

## Repeat

```TypeScript
export declare function Repeat<T>(arr: RepeatArray<T>): RepeatAttribute<T>
```

Indicates the type of Repeat.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function Repeat<T>(arr: RepeatArray<T>): RepeatAttribute<T>--><!--Device-unnamed-export declare function Repeat<T>(arr: RepeatArray<T>): RepeatAttribute<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| arr | [RepeatArray](arkts-arkui-repeatarray-t.md)&lt;T&gt; | Yes | The Data Source. |

**Return value:**

| Type | Description |
| --- | --- |
| [RepeatAttribute](arkts-arkui-repeatattribute-c.md)&lt;T&gt; |  |


## Repeat

```TypeScript
export declare function Repeat<T>(
     style: CustomBuilderT<RepeatAttribute<T>>
 ): RepeatAttribute<T>
```

定义Repeat组件。需要在组件属性设置开始时调用setRepeatOptions，并在组件属性设置结束时调用applyAttributeFinish。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function Repeat<T>(     style: CustomBuilderT<RepeatAttribute<T>> ): RepeatAttribute<T>--><!--Device-unnamed-export declare function Repeat<T>(     style: CustomBuilderT<RepeatAttribute<T>> ): RepeatAttribute<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | [CustomBuilderT](../arkts-components/arkts-arkui-custombuildert-t.md)&lt;RepeatAttribute&lt;T&gt;&gt; | Yes | 用于设置Repeat属性的回调。 |

**Return value:**

| Type | Description |
| --- | --- |
| [RepeatAttribute](arkts-arkui-repeatattribute-c.md)&lt;T&gt; | Repeat属性实例。 |

