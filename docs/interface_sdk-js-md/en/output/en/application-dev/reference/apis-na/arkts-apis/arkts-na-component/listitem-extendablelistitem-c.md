# ExtendableListItem

Defines the Extendable ListItem.

**Inheritance/Implementation:** ExtendableListItem implements [ListItemAttribute](listitem-listitemattribute-i.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-unnamed-export declare abstract class ExtendableListItem implements ListItemAttribute--><!--Device-unnamed-export declare abstract class ExtendableListItem implements ListItemAttribute-End-->

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

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExtendableListItem-static $_instantiate<T extends ExtendableListItem>(    factory: ConstructorT<T>,     value?: ListItemOptions,     content_?: CustomBuilder  ): T--><!--Device-ExtendableListItem-static $_instantiate<T extends ExtendableListItem>(    factory: ConstructorT<T>,     value?: ListItemOptions,     content_?: CustomBuilder  ): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| factory | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;T&gt; | Yes |  |
| value | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No |  |
| content\_ | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No |  |

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

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExtendableListItem-static _instantiateImpl<T extends ExtendableListItem>(    styles: CustomBuilderT<T>,     factory: ConstructorT<T>,     content_?: CustomBuilder  ): void--><!--Device-ExtendableListItem-static _instantiateImpl<T extends ExtendableListItem>(    styles: CustomBuilderT<T>,     factory: ConstructorT<T>,     content_?: CustomBuilder  ): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| styles | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;T&gt; | Yes |  |
| factory | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;T&gt; | Yes |  |
| content\_ | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No |  |

## setListItemOptions

```TypeScript
public setListItemOptions(value?: ListItemOptions): this
```

Set the ListItem Options.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExtendableListItem-public setListItemOptions(value?: ListItemOptions): this--><!--Device-ExtendableListItem-public setListItemOptions(value?: ListItemOptions): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

