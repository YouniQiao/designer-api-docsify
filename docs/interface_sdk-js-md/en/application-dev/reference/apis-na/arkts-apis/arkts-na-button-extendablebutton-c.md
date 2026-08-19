# ExtendableButton

Defines the Extendable Button.

**Inheritance/Implementation:** ExtendableButton implements [ButtonAttribute](arkts-na-button-buttonattribute-i.md)

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
| factory | [ConstructorT](arkts-na-constructort-t.md)&lt;T&gt; | Yes |  |
| label | [ResourceStr](../../apis-arkui/arkts-apis/arkts-arkui-resourcestr-t.md) | Yes |  |
| options | [ButtonOptions](arkts-na-button-buttonoptions-i.md) | No | Button Component Options |
| content_ | CustomBuilder | No | subcomponent trailing closure |

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
| factory | [ConstructorT](arkts-na-constructort-t.md)&lt;T&gt; | Yes |  |
| options | [ButtonOptions](arkts-na-button-buttonoptions-i.md) | No |  |
| content_ | CustomBuilder | No |  |

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
| styles | CustomBuilderT&lt;T&gt; | Yes |  |
| factory | [ConstructorT](arkts-na-constructort-t.md)&lt;T&gt; | Yes |  |
| content_ | CustomBuilder | No |  |

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
| options | [ButtonOptions](arkts-na-button-buttonoptions-i.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| [ExtendableButton](arkts-na-button-extendablebutton-c.md) |  |

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
| options | [ButtonOptions](arkts-na-button-buttonoptions-i.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| [ExtendableButton](arkts-na-button-extendablebutton-c.md) |  |

