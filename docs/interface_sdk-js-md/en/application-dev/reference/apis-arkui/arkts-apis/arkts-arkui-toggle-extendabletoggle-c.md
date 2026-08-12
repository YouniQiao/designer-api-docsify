# ExtendableToggle

Defines the Extendable Toggle.

**Inheritance/Implementation:** ExtendableToggle implements [ToggleAttribute](arkts-arkui-toggle-toggleattribute-i.md#ToggleAttribute)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-unnamed-export declare abstract class ExtendableToggle implements ToggleAttribute--><!--Device-unnamed-export declare abstract class ExtendableToggle implements ToggleAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## $_instantiate

```TypeScript
static $_instantiate<T extends ExtendableToggle>(
        factory: ConstructorT<T>, 
        options: ToggleOptions,
        content_?: CustomBuilder
    ): T
```

Constructor of Extendable Toggle.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExtendableToggle-static $_instantiate<T extends ExtendableToggle>(        factory: ConstructorT<T>,         options: ToggleOptions,        content_?: CustomBuilder    ): T--><!--Device-ExtendableToggle-static $_instantiate<T extends ExtendableToggle>(        factory: ConstructorT<T>,         options: ToggleOptions,        content_?: CustomBuilder    ): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| factory | [ConstructorT](arkts-arkui-constructort-t.md)&lt;T&gt; | Yes |  |
| options | [ToggleOptions](arkts-arkui-toggle-toggleoptions-i.md) | Yes |  |
| content_ | [CustomBuilder](arkts-arkui-custombuilder-t.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| T |  |

## _instantiateImpl

```TypeScript
static _instantiateImpl<T extends ExtendableToggle>(
        styles: CustomBuilderT<T>,  
        factory: ConstructorT<T>, 
        content_?: CustomBuilder
    ): void
```

Entry of Extendable Toggle.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExtendableToggle-static _instantiateImpl<T extends ExtendableToggle>(        styles: CustomBuilderT<T>,          factory: ConstructorT<T>,         content_?: CustomBuilder    ): void--><!--Device-ExtendableToggle-static _instantiateImpl<T extends ExtendableToggle>(        styles: CustomBuilderT<T>,          factory: ConstructorT<T>,         content_?: CustomBuilder    ): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| styles | [CustomBuilderT](arkts-arkui-custombuildert-t.md)&lt;T&gt; | Yes |  |
| factory | [ConstructorT](arkts-arkui-constructort-t.md)&lt;T&gt; | Yes |  |
| content_ | [CustomBuilder](arkts-arkui-custombuilder-t.md) | No |  |

## setToggleOptions

```TypeScript
public setToggleOptions(options: ToggleOptions): this
```

Set the Toggle Options.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExtendableToggle-public setToggleOptions(options: ToggleOptions): this--><!--Device-ExtendableToggle-public setToggleOptions(options: ToggleOptions): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [ToggleOptions](arkts-arkui-toggle-toggleoptions-i.md) | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

