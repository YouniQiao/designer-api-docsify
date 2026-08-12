# ForEach

## ForEach

```TypeScript
export declare function ForEach<T = Any>(arr: Array<T>,
    itemGenerator: ItemGeneratorFunc<T>,
    keyGenerator?: KeyGeneratorFunc<T>,
): ForEachAttribute
```

Defines ForEach Component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function ForEach<T = Any>(arr: Array<T>,    itemGenerator: ItemGeneratorFunc<T>,    keyGenerator?: KeyGeneratorFunc<T>,): ForEachAttribute--><!--Device-unnamed-export declare function ForEach<T = Any>(arr: Array<T>,    itemGenerator: ItemGeneratorFunc<T>,    keyGenerator?: KeyGeneratorFunc<T>,): ForEachAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| arr | Array&lt;T&gt; | Yes | the array collection to be used in UI. |
| itemGenerator | [ItemGeneratorFunc](arkts-arkui-itemgeneratorfunc-t.md)&lt;T&gt; | Yes | item generator function. |
| keyGenerator | [KeyGeneratorFunc](arkts-arkui-keygeneratorfunc-t.md)&lt;T&gt; | No | key generator function. |

**Return value:**

| Type | Description |
| --- | --- |
| [ForEachAttribute](arkts-arkui-foreach-foreachattribute-i.md) | The attribute of ForEach. |


## ForEach

```TypeScript
export declare function ForEach(
    style: CustomBuilderT<ForEachAttribute>
): ForEachAttribute
```

Defines ForEach Component. It requires calling setForEachOptions at start of component attribute set-up,and it requires calling applyAttributesFinish at end of component attribute set-up.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function ForEach(    style: CustomBuilderT<ForEachAttribute>): ForEachAttribute--><!--Device-unnamed-export declare function ForEach(    style: CustomBuilderT<ForEachAttribute>): ForEachAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | [CustomBuilderT](arkts-arkui-custombuildert-t.md)&lt;[ForEachAttribute](arkts-arkui-foreach-foreachattribute-i.md)&gt; | Yes | callback to set up ForEach's attributes. |

**Return value:**

| Type | Description |
| --- | --- |
| [ForEachAttribute](arkts-arkui-foreach-foreachattribute-i.md) | The attribute of ForEach. |

