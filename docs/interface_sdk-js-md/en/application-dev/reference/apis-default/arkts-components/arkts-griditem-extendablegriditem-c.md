# ExtendableGridItem

Defines the Extendable GridItem.

**Inheritance/Implementation:** ExtendableGridItem implements [GridItemAttribute](arkts-griditem-attribute.md#griditemattribute)

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-unnamed-export declare abstract class ExtendableGridItem--><!--Device-unnamed-export declare abstract class ExtendableGridItem-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## $_instantiate

```TypeScript
@ComponentBuilder
  static $_instantiate<T extends ExtendableGridItem>(
    factory: ConstructorT<T>, 
    value?: GridItemOptions, 
    content_?: CustomBuilder
  ): T
```

Constructor of Extendable GridItem.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExtendableGridItem-@ComponentBuilder  static $_instantiate<T extends ExtendableGridItem>(    factory: ConstructorT<T>,     value?: GridItemOptions,     content_?: CustomBuilder  ): T--><!--Device-ExtendableGridItem-@ComponentBuilder  static $_instantiate<T extends ExtendableGridItem>(    factory: ConstructorT<T>,     value?: GridItemOptions,     content_?: CustomBuilder  ): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| factory | [ConstructorT](../arkts-apis/arkts-constructort-t.md)&lt;T&gt; | Yes |  |
| value | [GridItemOptions](arkts-griditem-griditemoptions-i.md) | No |  |
| content_ | [CustomBuilder](../arkts-apis/arkts-custombuilder-t.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| T |  |

## _instantiateImpl

```TypeScript
@Builder
  static _instantiateImpl<T extends ExtendableGridItem>(
    styles: CustomBuilderT<T>, 
    factory: ConstructorT<T>, 
    content_?: CustomBuilder
  ): void
```

Entry of Extendable GridItem.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExtendableGridItem-@Builder  static _instantiateImpl<T extends ExtendableGridItem>(    styles: CustomBuilderT<T>,     factory: ConstructorT<T>,     content_?: CustomBuilder  ): void--><!--Device-ExtendableGridItem-@Builder  static _instantiateImpl<T extends ExtendableGridItem>(    styles: CustomBuilderT<T>,     factory: ConstructorT<T>,     content_?: CustomBuilder  ): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| styles | [CustomBuilderT](../arkts-apis/arkts-custombuildert-t.md)&lt;T&gt; | Yes |  |
| factory | [ConstructorT](../arkts-apis/arkts-constructort-t.md)&lt;T&gt; | Yes |  |
| content_ | [CustomBuilder](../arkts-apis/arkts-custombuilder-t.md) | No |  |

## setGridItemOptions

```TypeScript
public setGridItemOptions(value?: GridItemOptions): this
```

Set the GridItem Options.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExtendableGridItem-public setGridItemOptions(value?: GridItemOptions): this--><!--Device-ExtendableGridItem-public setGridItemOptions(value?: GridItemOptions): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [GridItemOptions](arkts-griditem-griditemoptions-i.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| [ExtendableGridItem](arkts-griditem-extendablegriditem-c.md) |  |

