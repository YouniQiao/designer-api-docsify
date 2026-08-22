# ForEachAttribute

Declare ForEachAttribute.

**Inheritance/Implementation:** ForEachAttribute extends DynamicNode

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-unnamed-export interface ForEachAttribute--><!--Device-unnamed-export interface ForEachAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## applyAttributesFinish

```TypeScript
applyAttributesFinish(): void
```

Notify ForEach has finished setting up its attributes.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ForEachAttribute-applyAttributesFinish(): void--><!--Device-ForEachAttribute-applyAttributesFinish(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## debugLine

```TypeScript
debugLine(sourceLine: string, moduleName?: string): this
```

Set the component's source code redirection information.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ForEachAttribute-debugLine(sourceLine: string, moduleName?: string): this--><!--Device-ForEachAttribute-debugLine(sourceLine: string, moduleName?: string): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| sourceLine | string | Yes | the source code line. |
| moduleName | string | No | module to which the component belongs. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## setForEachOptions

```TypeScript
setForEachOptions<T>(arr: () => Array<T>,
        itemGenerator: ItemGeneratorFunc<T>,
        keyGenerator?: KeyGeneratorFunc<T>): this
```

Sets ForEach options.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ForEachAttribute-setForEachOptions<T>(arr: () => Array<T>,        itemGenerator: ItemGeneratorFunc<T>,        keyGenerator?: KeyGeneratorFunc<T>): this--><!--Device-ForEachAttribute-setForEachOptions<T>(arr: () => Array<T>,        itemGenerator: ItemGeneratorFunc<T>,        keyGenerator?: KeyGeneratorFunc<T>): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| arr | () =&gt; Array&lt;T&gt; | Yes | Function that returns array collection to be used in UI. |
| itemGenerator | [ItemGeneratorFunc](arkts-itemgeneratorfunc-t.md)&lt;T&gt; | Yes | Item generator function. |
| keyGenerator | [KeyGeneratorFunc](arkts-keygeneratorfunc-t.md)&lt;T&gt; | No | Key generator function. |

**Return value:**

| Type | Description |
| --- | --- |
| this | ForEachAttribute instance |

