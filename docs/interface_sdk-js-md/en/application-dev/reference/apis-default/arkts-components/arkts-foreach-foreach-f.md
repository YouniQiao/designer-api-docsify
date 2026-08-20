# ForEach

## ForEach

```TypeScript
@ComponentBuilder
export declare function ForEach<T = Any>(arr: Array<T>,
    itemGenerator: ItemGeneratorFunc<T>,
    keyGenerator?: KeyGeneratorFunc<T>,
): ForEachAttribute
```

Defines ForEach Component.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@ComponentBuilderexport declare function ForEach<T = Any>(arr: Array<T>,    itemGenerator: ItemGeneratorFunc<T>,    keyGenerator?: KeyGeneratorFunc<T>,): ForEachAttribute--><!--Device-unnamed-@ComponentBuilderexport declare function ForEach<T = Any>(arr: Array<T>,    itemGenerator: ItemGeneratorFunc<T>,    keyGenerator?: KeyGeneratorFunc<T>,): ForEachAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| arr | Array&lt;T&gt; | Yes | the array collection to be used in UI. |
| itemGenerator | [ItemGeneratorFunc](arkts-itemgeneratorfunc-t.md)&lt;T&gt; | Yes | item generator function. |
| keyGenerator | [KeyGeneratorFunc](arkts-keygeneratorfunc-t.md)&lt;T&gt; | No | key generator function. |

**Return value:**

| Type | Description |
| --- | --- |
| [ForEachAttribute](arkts-foreach-attribute.md) | The attribute of ForEach. |


## ForEach

```TypeScript
@Builder
export declare function ForEach(
    style: CustomBuilderT<ForEachAttribute>
): ForEachAttribute
```

Defines ForEach Component. It requires calling setForEachOptions at start of component attribute set-up, and it requires calling applyAttributesFinish at end of component attribute set-up.

**Since:** 26.1.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@Builderexport declare function ForEach(    style: CustomBuilderT<ForEachAttribute>): ForEachAttribute--><!--Device-unnamed-@Builderexport declare function ForEach(    style: CustomBuilderT<ForEachAttribute>): ForEachAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | [CustomBuilderT](../arkts-apis/arkts-custombuildert-t.md)&lt;[ForEachAttribute](arkts-foreach-attribute.md)&gt; | Yes | callback to set up ForEach's attributes. |

**Return value:**

| Type | Description |
| --- | --- |
| [ForEachAttribute](arkts-foreach-attribute.md) | The attribute of ForEach. |

