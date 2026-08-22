# RepeatAttribute

Defines the Repeat component attribute functions.

**Inheritance/Implementation:** RepeatAttribute extends DynamicNode

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-unnamed-export interface RepeatAttribute--><!--Device-unnamed-export interface RepeatAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## applyAttributesFinish

```TypeScript
applyAttributesFinish(): void
```

Notify the Repeat has finished setting up its attributes.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RepeatAttribute-applyAttributesFinish(): void--><!--Device-RepeatAttribute-applyAttributesFinish(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## debugLine

```TypeScript
debugLine(sourceLine: string, moduleName?: string): this
```

Set the component's source code redirection information.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RepeatAttribute-debugLine(sourceLine: string, moduleName?: string): this--><!--Device-RepeatAttribute-debugLine(sourceLine: string, moduleName?: string): this-End-->

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

## each

```TypeScript
each(itemGenerator: RepeatItemBuilder<T>): this
```

Executes itemGenerator of each item.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RepeatAttribute-each(itemGenerator: RepeatItemBuilder<T>): this--><!--Device-RepeatAttribute-each(itemGenerator: RepeatItemBuilder<T>): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| itemGenerator | [RepeatItemBuilder](arkts-repeatitembuilder-t.md)&lt;T&gt; | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this | RepeatAttribute instance |

## key

```TypeScript
key(keyGenerator: KeyGeneratorFunc<T>): this
```

Obtains key of each item.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RepeatAttribute-key(keyGenerator: KeyGeneratorFunc<T>): this--><!--Device-RepeatAttribute-key(keyGenerator: KeyGeneratorFunc<T>): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| keyGenerator | [KeyGeneratorFunc](arkts-keygeneratorfunc-t.md)&lt;T&gt; | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this | RepeatAttribute instance |

## setRepeatOptions

```TypeScript
setRepeatOptions<T>(arr: RepeatArray<T>): this
```

Sets Repeat options.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RepeatAttribute-setRepeatOptions<T>(arr: RepeatArray<T>): this--><!--Device-RepeatAttribute-setRepeatOptions<T>(arr: RepeatArray<T>): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| arr | [RepeatArray](arkts-repeatarray-t.md)&lt;T&gt; | Yes | Data source array. |

**Return value:**

| Type | Description |
| --- | --- |
| this | RepeatAttribute instance |

## template

```TypeScript
template(type: string, itemBuilder: RepeatItemBuilder<T>, templateOptions?: TemplateOptions): this
```

Type builder function to render specific type of data item.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RepeatAttribute-template(type: string, itemBuilder: RepeatItemBuilder<T>, templateOptions?: TemplateOptions): this--><!--Device-RepeatAttribute-template(type: string, itemBuilder: RepeatItemBuilder<T>, templateOptions?: TemplateOptions): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | string | Yes | that defines the template id. |
| itemBuilder | [RepeatItemBuilder](arkts-repeatitembuilder-t.md)&lt;T&gt; | Yes | that defines UI builder function. |
| templateOptions | [TemplateOptions](arkts-repeat-templateoptions-i.md) | No | that defines a builder template option parameter. |

**Return value:**

| Type | Description |
| --- | --- |
| this | RepeatAttribute instance |

## templateId

```TypeScript
templateId(typedFunc: TemplateTypedFunc<T>): this
```

Typed function to render specific type of data item.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RepeatAttribute-templateId(typedFunc: TemplateTypedFunc<T>): this--><!--Device-RepeatAttribute-templateId(typedFunc: TemplateTypedFunc<T>): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| typedFunc | [TemplateTypedFunc](arkts-templatetypedfunc-t.md)&lt;T&gt; | Yes | that defines template typed function. |

**Return value:**

| Type | Description |
| --- | --- |
| this | RepeatAttribute instance |

## virtualScroll

```TypeScript
virtualScroll(virtualScrollOptions?: VirtualScrollOptions): this
```

Enable UI lazy loading when scroll up or down.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RepeatAttribute-virtualScroll(virtualScrollOptions?: VirtualScrollOptions): this--><!--Device-RepeatAttribute-virtualScroll(virtualScrollOptions?: VirtualScrollOptions): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| virtualScrollOptions | [VirtualScrollOptions](arkts-repeat-virtualscrolloptions-i.md) | No | that defines the options of repeat virtual scroll to implement reuse and lazy loading. |

**Return value:**

| Type | Description |
| --- | --- |
| this | RepeatAttribute instance |

