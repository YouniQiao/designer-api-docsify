# ExtendableToggle

Defines the Extendable Toggle.

**Inheritance/Implementation:** ExtendableToggle implements [ToggleAttribute](arkts-na-toggle-toggleattribute-i.md)

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-unnamed-export declare abstract class ExtendableToggle--><!--Device-unnamed-export declare abstract class ExtendableToggle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## $_instantiate

```TypeScript
@ComponentBuilder
    static $_instantiate<T extends ExtendableToggle>(
        factory: ConstructorT<T>, 
        options: ToggleOptions,
        content_?: CustomBuilder
    ): T
```

Constructor of Extendable Toggle.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExtendableToggle-@ComponentBuilder    static $_instantiate<T extends ExtendableToggle>(        factory: ConstructorT<T>,         options: ToggleOptions,        content_?: CustomBuilder    ): T--><!--Device-ExtendableToggle-@ComponentBuilder    static $_instantiate<T extends ExtendableToggle>(        factory: ConstructorT<T>,         options: ToggleOptions,        content_?: CustomBuilder    ): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| factory | [ConstructorT](arkts-na-constructort-t.md)&lt;T&gt; | Yes |  |
| options | [ToggleOptions](arkts-na-toggle-toggleoptions-i.md) | Yes |  |
| content_ | CustomBuilder | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| T |  |

## _instantiateImpl

```TypeScript
@Builder
    static _instantiateImpl<T extends ExtendableToggle>(
        styles: CustomBuilderT<T>,  
        factory: ConstructorT<T>, 
        content_?: CustomBuilder
    ): void
```

Entry of Extendable Toggle.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExtendableToggle-@Builder    static _instantiateImpl<T extends ExtendableToggle>(        styles: CustomBuilderT<T>,          factory: ConstructorT<T>,         content_?: CustomBuilder    ): void--><!--Device-ExtendableToggle-@Builder    static _instantiateImpl<T extends ExtendableToggle>(        styles: CustomBuilderT<T>,          factory: ConstructorT<T>,         content_?: CustomBuilder    ): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| styles | CustomBuilderT&lt;T&gt; | Yes |  |
| factory | [ConstructorT](arkts-na-constructort-t.md)&lt;T&gt; | Yes |  |
| content_ | CustomBuilder | No |  |

## setToggleOptions

```TypeScript
public setToggleOptions(options: ToggleOptions): this
```

Set the Toggle Options.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExtendableToggle-public setToggleOptions(options: ToggleOptions): this--><!--Device-ExtendableToggle-public setToggleOptions(options: ToggleOptions): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [ToggleOptions](arkts-na-toggle-toggleoptions-i.md) | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

