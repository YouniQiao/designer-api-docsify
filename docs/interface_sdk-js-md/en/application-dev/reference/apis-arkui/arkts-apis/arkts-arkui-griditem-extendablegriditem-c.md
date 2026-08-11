# ExtendableGridItem

Defines the Extendable GridItem.

**Inheritance/Implementation:** ExtendableGridItem implements [GridItemAttribute](../arkts-components/arkts-arkui-griditem-attribute.md/arkts-arkui-griditem-attribute.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-unnamed-export declare abstract class ExtendableGridItem implements GridItemAttribute--><!--Device-unnamed-export declare abstract class ExtendableGridItem implements GridItemAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## $_instantiate

```TypeScript
static $_instantiate<T extends ExtendableGridItem>(
    factory: ConstructorT<T>, 
    value?: GridItemOptions, 
    content_?: CustomBuilder
  ): T
```

Constructor of Extendable GridItem.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExtendableGridItem-static $_instantiate<T extends ExtendableGridItem>(    factory: ConstructorT<T>,     value?: GridItemOptions,     content_?: CustomBuilder  ): T--><!--Device-ExtendableGridItem-static $_instantiate<T extends ExtendableGridItem>(    factory: ConstructorT<T>,     value?: GridItemOptions,     content_?: CustomBuilder  ): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| factory | [ConstructorT](arkts-arkui-constructort-t.md)&lt;T&gt; | Yes |  |
| value | [GridItemOptions](../arkts-components/arkts-arkui-griditemoptions-i.md) | No |  |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| T |  |

## _instantiateImpl

```TypeScript
static _instantiateImpl<T extends ExtendableGridItem>(
    styles: CustomBuilderT<T>, 
    factory: ConstructorT<T>, 
    content_?: CustomBuilder
  ): void
```

Entry of Extendable GridItem.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExtendableGridItem-static _instantiateImpl<T extends ExtendableGridItem>(    styles: CustomBuilderT<T>,     factory: ConstructorT<T>,     content_?: CustomBuilder  ): void--><!--Device-ExtendableGridItem-static _instantiateImpl<T extends ExtendableGridItem>(    styles: CustomBuilderT<T>,     factory: ConstructorT<T>,     content_?: CustomBuilder  ): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| styles | [CustomBuilderT](../arkts-components/arkts-arkui-custombuildert-t.md)&lt;T&gt; | Yes |  |
| factory | [ConstructorT](arkts-arkui-constructort-t.md)&lt;T&gt; | Yes |  |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | No |  |

## setGridItemOptions

```TypeScript
public setGridItemOptions(value?: GridItemOptions): this
```

Set the GridItem Options.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExtendableGridItem-public setGridItemOptions(value?: GridItemOptions): this--><!--Device-ExtendableGridItem-public setGridItemOptions(value?: GridItemOptions): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [GridItemOptions](../arkts-components/arkts-arkui-griditemoptions-i.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

