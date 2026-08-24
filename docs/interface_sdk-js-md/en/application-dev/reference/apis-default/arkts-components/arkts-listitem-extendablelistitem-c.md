# ExtendableListItem

Defines the Extendable ListItem.

**Inheritance/Implementation:** ExtendableListItem implements [ListItemAttribute](arkts-listitem-attribute.md#listitemattribute)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

<!--Device-unnamed-export declare abstract class ExtendableListItem--><!--Device-unnamed-export declare abstract class ExtendableListItem-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## $_instantiate

```TypeScript
static $_instantiate<T extends ExtendableListItem>(
    factory: ConstructorT<T>, 
    value?: ListItemOptions, 
    content_?: CustomBuilder
  ): T
```

Constructor of Extendable ListItem.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Decorator:** @ComponentBuilder

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExtendableListItem-@ComponentBuilder  static $_instantiate<T extends ExtendableListItem>(    factory: ConstructorT<T>,     value?: ListItemOptions,     content_?: CustomBuilder  ): T--><!--Device-ExtendableListItem-@ComponentBuilder  static $_instantiate<T extends ExtendableListItem>(    factory: ConstructorT<T>,     value?: ListItemOptions,     content_?: CustomBuilder  ): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| factory | [ConstructorT](../arkts-apis/arkts-constructort-t.md)&lt;T&gt; | Yes |  |
| value | [ListItemOptions](arkts-listitem-listitemoptions-i.md) | No |  |
| content_ | [CustomBuilder](../arkts-apis/arkts-custombuilder-t.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| T |  |

## _instantiateImpl

```TypeScript
static _instantiateImpl<T extends ExtendableListItem>(
    styles: CustomBuilderT<T>, 
    factory: ConstructorT<T>, 
    content_?: CustomBuilder
  ): void
```

Entry of Extendable ListItem.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExtendableListItem-@Builder  static _instantiateImpl<T extends ExtendableListItem>(    styles: CustomBuilderT<T>,     factory: ConstructorT<T>,     content_?: CustomBuilder  ): void--><!--Device-ExtendableListItem-@Builder  static _instantiateImpl<T extends ExtendableListItem>(    styles: CustomBuilderT<T>,     factory: ConstructorT<T>,     content_?: CustomBuilder  ): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| styles | [CustomBuilderT](../arkts-apis/arkts-custombuildert-t.md)&lt;T&gt; | Yes |  |
| factory | [ConstructorT](../arkts-apis/arkts-constructort-t.md)&lt;T&gt; | Yes |  |
| content_ | [CustomBuilder](../arkts-apis/arkts-custombuilder-t.md) | No |  |

## setListItemOptions

```TypeScript
public setListItemOptions(value?: ListItemOptions): this
```

Set the ListItem Options.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExtendableListItem-public setListItemOptions(value?: ListItemOptions): this--><!--Device-ExtendableListItem-public setListItemOptions(value?: ListItemOptions): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ListItemOptions](arkts-listitem-listitemoptions-i.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| [ExtendableListItem](arkts-listitem-extendablelistitem-c.md) |  |

