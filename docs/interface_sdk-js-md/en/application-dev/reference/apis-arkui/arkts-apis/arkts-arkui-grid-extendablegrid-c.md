# ExtendableGrid

Defines the Extendable Grid.

**Inheritance/Implementation:** ExtendableGrid implements [GridAttribute](../arkts-components/arkts-arkui-grid-attribute.md/arkts-arkui-grid-attribute.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-unnamed-export declare abstract class ExtendableGrid implements GridAttribute--><!--Device-unnamed-export declare abstract class ExtendableGrid implements GridAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## $_instantiate

```TypeScript
static $_instantiate<T extends ExtendableGrid>(
    factory: ConstructorT<T>, 
    scroller?: Scroller, 
    layoutOptions?: GridLayoutOptions, 
    content_?: CustomBuilder
  ): T
```

Constructor of Extendable Grid.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExtendableGrid-static $_instantiate<T extends ExtendableGrid>(    factory: ConstructorT<T>,     scroller?: Scroller,     layoutOptions?: GridLayoutOptions,     content_?: CustomBuilder  ): T--><!--Device-ExtendableGrid-static $_instantiate<T extends ExtendableGrid>(    factory: ConstructorT<T>,     scroller?: Scroller,     layoutOptions?: GridLayoutOptions,     content_?: CustomBuilder  ): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| factory | [ConstructorT](arkts-arkui-constructort-t.md)&lt;T&gt; | Yes |  |
| scroller | [Scroller](../arkts-components/arkts-arkui-scroller-c.md) | No |  |
| layoutOptions | [GridLayoutOptions](arkts-arkui-grid-gridlayoutoptions-i.md) | No |  |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| T |  |

## _instantiateImpl

```TypeScript
static _instantiateImpl<T extends ExtendableGrid>(
    styles: CustomBuilderT<T>, 
    factory: ConstructorT<T>, 
    content_?: CustomBuilder
  ): void
```

Entry of Extendable Grid.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExtendableGrid-static _instantiateImpl<T extends ExtendableGrid>(    styles: CustomBuilderT<T>,     factory: ConstructorT<T>,     content_?: CustomBuilder  ): void--><!--Device-ExtendableGrid-static _instantiateImpl<T extends ExtendableGrid>(    styles: CustomBuilderT<T>,     factory: ConstructorT<T>,     content_?: CustomBuilder  ): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| styles | [CustomBuilderT](../arkts-components/arkts-arkui-custombuildert-t.md)&lt;T&gt; | Yes |  |
| factory | [ConstructorT](arkts-arkui-constructort-t.md)&lt;T&gt; | Yes |  |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | No |  |

## setGridOptions

```TypeScript
public setGridOptions(
    scroller?: Scroller, 
    layoutOptions?: GridLayoutOptions
  ): this
```

Set the Grid Options.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExtendableGrid-public setGridOptions(    scroller?: Scroller,     layoutOptions?: GridLayoutOptions  ): this--><!--Device-ExtendableGrid-public setGridOptions(    scroller?: Scroller,     layoutOptions?: GridLayoutOptions  ): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| scroller | [Scroller](../arkts-components/arkts-arkui-scroller-c.md) | No |  |
| layoutOptions | [GridLayoutOptions](arkts-arkui-grid-gridlayoutoptions-i.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

