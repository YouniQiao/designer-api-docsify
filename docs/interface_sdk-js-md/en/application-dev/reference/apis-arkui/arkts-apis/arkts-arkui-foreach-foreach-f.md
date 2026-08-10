# ForEach

## ForEach

```TypeScript
export declare function ForEach<T = Any>(arr: Array<T>,
    itemGenerator: ItemGeneratorFunc<T>,
    keyGenerator?: KeyGeneratorFunc<T>,
): ForEachAttribute
```

定义ForEach组件。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function ForEach<T = Any>(arr: Array<T>,    itemGenerator: ItemGeneratorFunc<T>,    keyGenerator?: KeyGeneratorFunc<T>,): ForEachAttribute--><!--Device-unnamed-export declare function ForEach<T = Any>(arr: Array<T>,    itemGenerator: ItemGeneratorFunc<T>,    keyGenerator?: KeyGeneratorFunc<T>,): ForEachAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| arr | Array&lt;T&gt; | Yes | 在UI中使用的数组集合。 |
| itemGenerator | [ItemGeneratorFunc](arkts-arkui-itemgeneratorfunc-t.md)&lt;T&gt; | Yes | 项生成函数。 |
| keyGenerator | [KeyGeneratorFunc](arkts-arkui-keygeneratorfunc-t.md)&lt;T&gt; | No | 键生成函数。 |

**Return value:**

| Type | Description |
| --- | --- |
| [ForEachAttribute](arkts-arkui-foreach-foreachattribute-i.md) | ForEach的属性。 |


## ForEach

```TypeScript
export declare function ForEach(
    style: CustomBuilderT<ForEachAttribute>
): ForEachAttribute
```

定义ForEach组件。需要在组件属性设置开始时调用setForEachOptions，并在组件属性设置结束时调用applyAttributeFinish。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function ForEach(    style: CustomBuilderT<ForEachAttribute>): ForEachAttribute--><!--Device-unnamed-export declare function ForEach(    style: CustomBuilderT<ForEachAttribute>): ForEachAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | [CustomBuilderT](../arkts-components/arkts-arkui-custombuildert-t.md)&lt;ForEachAttribute&gt; | Yes | 用于设置ForEach属性的回调。 |

**Return value:**

| Type | Description |
| --- | --- |
| [ForEachAttribute](arkts-arkui-foreach-foreachattribute-i.md) | ForEach属性实例。 |

