# ExtendableGrid

Defines the Extendable Grid.

**Inheritance/Implementation:** ExtendableGrid implements [GridAttribute](arkts-grid-attribute.md#gridattribute)

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-unnamed-export declare abstract class ExtendableGrid--><!--Device-unnamed-export declare abstract class ExtendableGrid-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## $_instantiate

```TypeScript
@ComponentBuilder
  static $_instantiate<T extends ExtendableGrid>(
    factory: ConstructorT<T>, 
    scroller?: Scroller, 
    layoutOptions?: GridLayoutOptions, 
    content_?: CustomBuilder
  ): T
```

Constructor of Extendable Grid.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExtendableGrid-@ComponentBuilder  static $_instantiate<T extends ExtendableGrid>(    factory: ConstructorT<T>,     scroller?: Scroller,     layoutOptions?: GridLayoutOptions,     content_?: CustomBuilder  ): T--><!--Device-ExtendableGrid-@ComponentBuilder  static $_instantiate<T extends ExtendableGrid>(    factory: ConstructorT<T>,     scroller?: Scroller,     layoutOptions?: GridLayoutOptions,     content_?: CustomBuilder  ): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| factory | [ConstructorT](../arkts-apis/arkts-constructort-t.md)&lt;T&gt; | Yes |  |
| scroller | [Scroller](../../apis-arkui/arkts-components/arkts-arkui-scroller-c.md) | No |  |
| layoutOptions | [GridLayoutOptions](arkts-grid-gridlayoutoptions-i.md) | No |  |
| content_ | [CustomBuilder](../arkts-apis/arkts-custombuilder-t.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| T |  |

## _instantiateImpl

```TypeScript
@Builder
  static _instantiateImpl<T extends ExtendableGrid>(
    styles: CustomBuilderT<T>, 
    factory: ConstructorT<T>, 
    content_?: CustomBuilder
  ): void
```

Entry of Extendable Grid.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExtendableGrid-@Builder  static _instantiateImpl<T extends ExtendableGrid>(    styles: CustomBuilderT<T>,     factory: ConstructorT<T>,     content_?: CustomBuilder  ): void--><!--Device-ExtendableGrid-@Builder  static _instantiateImpl<T extends ExtendableGrid>(    styles: CustomBuilderT<T>,     factory: ConstructorT<T>,     content_?: CustomBuilder  ): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| styles | [CustomBuilderT](../arkts-apis/arkts-custombuildert-t.md)&lt;T&gt; | Yes |  |
| factory | [ConstructorT](../arkts-apis/arkts-constructort-t.md)&lt;T&gt; | Yes |  |
| content_ | [CustomBuilder](../arkts-apis/arkts-custombuilder-t.md) | No |  |

## setGridOptions

```TypeScript
public setGridOptions(
    scroller?: Scroller, 
    layoutOptions?: GridLayoutOptions
  ): this
```

Set the Grid Options.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExtendableGrid-public setGridOptions(    scroller?: Scroller,     layoutOptions?: GridLayoutOptions  ): this--><!--Device-ExtendableGrid-public setGridOptions(    scroller?: Scroller,     layoutOptions?: GridLayoutOptions  ): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| scroller | [Scroller](../../apis-arkui/arkts-components/arkts-arkui-scroller-c.md) | No |  |
| layoutOptions | [GridLayoutOptions](arkts-grid-gridlayoutoptions-i.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| [ExtendableGrid](arkts-grid-extendablegrid-c.md) |  |

