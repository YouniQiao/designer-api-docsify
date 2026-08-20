# ExtendableList

Defines the Extendable List.

**Inheritance/Implementation:** ExtendableList implements [ListAttribute](arkts-list-attribute.md#listattribute)

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-unnamed-export declare abstract class ExtendableList--><!--Device-unnamed-export declare abstract class ExtendableList-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## $_instantiate

```TypeScript
@ComponentBuilder
  static $_instantiate<T extends ExtendableList>(
    factory: ConstructorT<T>, 
    options?: ListOptions, 
    content_?: CustomBuilder
  ): T
```

Constructor of Extendable List.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExtendableList-@ComponentBuilder  static $_instantiate<T extends ExtendableList>(    factory: ConstructorT<T>,     options?: ListOptions,     content_?: CustomBuilder  ): T--><!--Device-ExtendableList-@ComponentBuilder  static $_instantiate<T extends ExtendableList>(    factory: ConstructorT<T>,     options?: ListOptions,     content_?: CustomBuilder  ): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| factory | [ConstructorT](../arkts-apis/arkts-constructort-t.md)&lt;T&gt; | Yes |  |
| options | [ListOptions](arkts-list-listoptions-i.md) | No |  |
| content_ | [CustomBuilder](../arkts-apis/arkts-custombuilder-t.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| T |  |

## _instantiateImpl

```TypeScript
@Builder
  static _instantiateImpl<T extends ExtendableList>(
    styles: CustomBuilderT<T>, 
    factory: ConstructorT<T>,
    content_?: CustomBuilder
  ): void
```

Entry of Extendable List.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExtendableList-@Builder  static _instantiateImpl<T extends ExtendableList>(    styles: CustomBuilderT<T>,     factory: ConstructorT<T>,    content_?: CustomBuilder  ): void--><!--Device-ExtendableList-@Builder  static _instantiateImpl<T extends ExtendableList>(    styles: CustomBuilderT<T>,     factory: ConstructorT<T>,    content_?: CustomBuilder  ): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| styles | [CustomBuilderT](../arkts-apis/arkts-custombuildert-t.md)&lt;T&gt; | Yes |  |
| factory | [ConstructorT](../arkts-apis/arkts-constructort-t.md)&lt;T&gt; | Yes |  |
| content_ | [CustomBuilder](../arkts-apis/arkts-custombuilder-t.md) | No |  |

## setListOptions

```TypeScript
public setListOptions(options?: ListOptions): this
```

Set the List Options.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExtendableList-public setListOptions(options?: ListOptions): this--><!--Device-ExtendableList-public setListOptions(options?: ListOptions): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [ListOptions](arkts-list-listoptions-i.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| [ExtendableList](arkts-list-extendablelist-c.md) |  |

