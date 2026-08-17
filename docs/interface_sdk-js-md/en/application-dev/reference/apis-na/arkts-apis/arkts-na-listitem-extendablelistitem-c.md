# ExtendableListItem

Defines the Extendable ListItem.

**Inheritance/Implementation:** ExtendableListItem implements ListItemAttribute

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-unnamed-export declare abstract class ExtendableListItem--><!--Device-unnamed-export declare abstract class ExtendableListItem-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## $_instantiate

```TypeScript
@ComponentBuilder
  static $_instantiate<T extends ExtendableListItem>(
    factory: ConstructorT<T>, 
    value?: ListItemOptions, 
    content_?: CustomBuilder
  ): T
```

Constructor of Extendable ListItem.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExtendableListItem-@ComponentBuilder  static $_instantiate<T extends ExtendableListItem>(    factory: ConstructorT<T>,     value?: ListItemOptions,     content_?: CustomBuilder  ): T--><!--Device-ExtendableListItem-@ComponentBuilder  static $_instantiate<T extends ExtendableListItem>(    factory: ConstructorT<T>,     value?: ListItemOptions,     content_?: CustomBuilder  ): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| factory | [ConstructorT](arkts-na-constructort-t.md)&lt;T&gt; | Yes |  |
| value | [ListItemOptions](arkts-na-listitem-listitemoptions-i.md) | No |  |
| content_ | CustomBuilder | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| T |  |

## _instantiateImpl

```TypeScript
@Builder
  static _instantiateImpl<T extends ExtendableListItem>(
    styles: CustomBuilderT<T>, 
    factory: ConstructorT<T>, 
    content_?: CustomBuilder
  ): void
```

Entry of Extendable ListItem.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExtendableListItem-@Builder  static _instantiateImpl<T extends ExtendableListItem>(    styles: CustomBuilderT<T>,     factory: ConstructorT<T>,     content_?: CustomBuilder  ): void--><!--Device-ExtendableListItem-@Builder  static _instantiateImpl<T extends ExtendableListItem>(    styles: CustomBuilderT<T>,     factory: ConstructorT<T>,     content_?: CustomBuilder  ): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| styles | CustomBuilderT&lt;T&gt; | Yes |  |
| factory | [ConstructorT](arkts-na-constructort-t.md)&lt;T&gt; | Yes |  |
| content_ | CustomBuilder | No |  |

## setListItemOptions

```TypeScript
public setListItemOptions(value?: ListItemOptions): this
```

Set the ListItem Options.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExtendableListItem-public setListItemOptions(value?: ListItemOptions): this--><!--Device-ExtendableListItem-public setListItemOptions(value?: ListItemOptions): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ListItemOptions](arkts-na-listitem-listitemoptions-i.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

