# ExtendableButton

Defines the Extendable Button.

@implements ButtonAttribute

**Inheritance/Implementation:** ExtendableButton implements [ButtonAttribute](arkts-button-attribute.md#buttonattribute)

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-unnamed-export declare abstract class ExtendableButton--><!--Device-unnamed-export declare abstract class ExtendableButton-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## $_instantiate

```TypeScript
@ComponentBuilder
    static $_instantiate<T extends ExtendableButton>(
        factory: ConstructorT<T>, 
        label: ResourceStr, 
        options?: ButtonOptions, 
        content_?: CustomBuilder
    ): T
```

Constructor of Extendable Button.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExtendableButton-@ComponentBuilder    static $_instantiate<T extends ExtendableButton>(        factory: ConstructorT<T>,         label: ResourceStr,         options?: ButtonOptions,         content_?: CustomBuilder    ): T--><!--Device-ExtendableButton-@ComponentBuilder    static $_instantiate<T extends ExtendableButton>(        factory: ConstructorT<T>,         label: ResourceStr,         options?: ButtonOptions,         content_?: CustomBuilder    ): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| factory | [ConstructorT](../arkts-apis/arkts-constructort-t.md)&lt;T&gt; | Yes |  |
| label | [ResourceStr](../../apis-arkui/arkts-apis/arkts-arkui-resourcestr-t.md) | Yes |  |
| options | [ButtonOptions](arkts-button-buttonoptions-i.md) | No | Button Component Options |
| content_ | [CustomBuilder](../arkts-apis/arkts-custombuilder-t.md) | No | subcomponent trailing closure |

**Return value:**

| Type | Description |
| --- | --- |
| T |  |

## $_instantiate

```TypeScript
@ComponentBuilder
    static $_instantiate<T extends ExtendableButton>(
        factory: ConstructorT<T>, 
        options?: ButtonOptions,
        content_?: CustomBuilder
    ): T
```

Constructor of Extendable Button.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExtendableButton-@ComponentBuilder    static $_instantiate<T extends ExtendableButton>(        factory: ConstructorT<T>,         options?: ButtonOptions,        content_?: CustomBuilder    ): T--><!--Device-ExtendableButton-@ComponentBuilder    static $_instantiate<T extends ExtendableButton>(        factory: ConstructorT<T>,         options?: ButtonOptions,        content_?: CustomBuilder    ): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| factory | [ConstructorT](../arkts-apis/arkts-constructort-t.md)&lt;T&gt; | Yes |  |
| options | [ButtonOptions](arkts-button-buttonoptions-i.md) | No |  |
| content_ | [CustomBuilder](../arkts-apis/arkts-custombuilder-t.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| T |  |

## _instantiateImpl

```TypeScript
@Builder
    static _instantiateImpl<T extends ExtendableButton>(
        styles: CustomBuilderT<T>, 
        factory: ConstructorT<T>, 
        content_?: CustomBuilder
    ): void
```

Entry of Extendable Button.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExtendableButton-@Builder    static _instantiateImpl<T extends ExtendableButton>(        styles: CustomBuilderT<T>,         factory: ConstructorT<T>,         content_?: CustomBuilder    ): void--><!--Device-ExtendableButton-@Builder    static _instantiateImpl<T extends ExtendableButton>(        styles: CustomBuilderT<T>,         factory: ConstructorT<T>,         content_?: CustomBuilder    ): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| styles | [CustomBuilderT](../arkts-apis/arkts-custombuildert-t.md)&lt;T&gt; | Yes |  |
| factory | [ConstructorT](../arkts-apis/arkts-constructort-t.md)&lt;T&gt; | Yes |  |
| content_ | [CustomBuilder](../arkts-apis/arkts-custombuilder-t.md) | No |  |

## setButtonOptions

```TypeScript
public setButtonOptions(
        label: ResourceStr, 
        options?: ButtonOptions
    ): this
```

Set the Button Options.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExtendableButton-public setButtonOptions(        label: ResourceStr,         options?: ButtonOptions    ): this--><!--Device-ExtendableButton-public setButtonOptions(        label: ResourceStr,         options?: ButtonOptions    ): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| label | [ResourceStr](../../apis-arkui/arkts-apis/arkts-arkui-resourcestr-t.md) | Yes |  |
| options | [ButtonOptions](arkts-button-buttonoptions-i.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| [ExtendableButton](arkts-button-extendablebutton-c.md) |  |

## setButtonOptions

```TypeScript
public setButtonOptions(options?: ButtonOptions): this
```

Set the Button Options.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExtendableButton-public setButtonOptions(options?: ButtonOptions): this--><!--Device-ExtendableButton-public setButtonOptions(options?: ButtonOptions): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [ButtonOptions](arkts-button-buttonoptions-i.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| [ExtendableButton](arkts-button-extendablebutton-c.md) |  |

