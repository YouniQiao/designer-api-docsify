# ExtendableText

Defines the Extendable Text.

**Inheritance/Implementation:** ExtendableText implements [TextAttribute](arkts-arkui-text-attribute.md#textattribute)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

<!--Device-unnamed-export declare abstract class ExtendableText--><!--Device-unnamed-export declare abstract class ExtendableText-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## $_instantiate

```TypeScript
@ComponentBuilder
    static $_instantiate<T extends ExtendableText>(
      factory: ConstructorT<T>, 
      content?: string | Resource, 
      value?: TextOptions, 
      content_?: CustomBuilder
    ): T
```

Constructor of Extendable Text.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExtendableText-@ComponentBuilder    static $_instantiate<T extends ExtendableText>(      factory: ConstructorT<T>,       content?: string | Resource,       value?: TextOptions,       content_?: CustomBuilder    ): T--><!--Device-ExtendableText-@ComponentBuilder    static $_instantiate<T extends ExtendableText>(      factory: ConstructorT<T>,       content?: string | Resource,       value?: TextOptions,       content_?: CustomBuilder    ): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| factory | [ConstructorT](../../apis-default/arkts-apis/arkts-constructort-t.md)&lt;T&gt; | Yes |  |
| content | string \| [Resource](../arkts-apis/arkts-arkui-resource-t.md) | No |  |
| value | [TextOptions](arkts-arkui-text-textoptions-i.md) | No |  |
| content_ | [CustomBuilder](../../apis-default/arkts-apis/arkts-custombuilder-t.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| T |  |

## _instantiateImpl

```TypeScript
@Builder
    static _instantiateImpl<T extends ExtendableText>(
        styles: CustomBuilderT<T>,  
        factory: ConstructorT<T>, 
        content_?: CustomBuilder
    ): void
```

Entry of Extendable Text.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExtendableText-@Builder    static _instantiateImpl<T extends ExtendableText>(        styles: CustomBuilderT<T>,          factory: ConstructorT<T>,         content_?: CustomBuilder    ): void--><!--Device-ExtendableText-@Builder    static _instantiateImpl<T extends ExtendableText>(        styles: CustomBuilderT<T>,          factory: ConstructorT<T>,         content_?: CustomBuilder    ): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| styles | [CustomBuilderT](../../apis-default/arkts-apis/arkts-custombuildert-t.md)&lt;T&gt; | Yes |  |
| factory | [ConstructorT](../../apis-default/arkts-apis/arkts-constructort-t.md)&lt;T&gt; | Yes |  |
| content_ | [CustomBuilder](../../apis-default/arkts-apis/arkts-custombuilder-t.md) | No |  |

## setTextOptions

```TypeScript
public setTextOptions(
      content?: string | Resource, 
      value?: TextOptions
    ): this
```

Set the Text Options.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExtendableText-public setTextOptions(      content?: string | Resource,       value?: TextOptions    ): this--><!--Device-ExtendableText-public setTextOptions(      content?: string | Resource,       value?: TextOptions    ): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| content | string \| [Resource](../arkts-apis/arkts-arkui-resource-t.md) | No |  |
| value | [TextOptions](arkts-arkui-text-textoptions-i.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| [ExtendableText](arkts-arkui-text-extendabletext-c.md) |  |

