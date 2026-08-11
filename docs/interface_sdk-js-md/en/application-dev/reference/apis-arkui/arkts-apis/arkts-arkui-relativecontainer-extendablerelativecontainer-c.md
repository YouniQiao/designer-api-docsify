# ExtendableRelativeContainer

Defines the Extendable RelativeContainer.

**Inheritance/Implementation:** ExtendableRelativeContainer implements [RelativeContainerAttribute](arkts-arkui-relativecontainer-relativecontainerattribute-i.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-unnamed-export declare abstract class ExtendableRelativeContainer implements RelativeContainerAttribute--><!--Device-unnamed-export declare abstract class ExtendableRelativeContainer implements RelativeContainerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## $_instantiate

```TypeScript
static $_instantiate<T extends ExtendableRelativeContainer>(
    factory: ConstructorT<T>,
    content_?: CustomBuilder
  ): T
```

Constructor of Extendable RelativeContainer.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExtendableRelativeContainer-static $_instantiate<T extends ExtendableRelativeContainer>(    factory: ConstructorT<T>,    content_?: CustomBuilder  ): T--><!--Device-ExtendableRelativeContainer-static $_instantiate<T extends ExtendableRelativeContainer>(    factory: ConstructorT<T>,    content_?: CustomBuilder  ): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| factory | [ConstructorT](arkts-arkui-constructort-t.md)&lt;T&gt; | Yes |  |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| T |  |

## _instantiateImpl

```TypeScript
static _instantiateImpl<T extends ExtendableRelativeContainer>(
    styles: CustomBuilderT<T>,
    factory: ConstructorT<T>,
    content_?: CustomBuilder
  ): void
```

Entry of Extendable RelativeContainer.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExtendableRelativeContainer-static _instantiateImpl<T extends ExtendableRelativeContainer>(    styles: CustomBuilderT<T>,    factory: ConstructorT<T>,    content_?: CustomBuilder  ): void--><!--Device-ExtendableRelativeContainer-static _instantiateImpl<T extends ExtendableRelativeContainer>(    styles: CustomBuilderT<T>,    factory: ConstructorT<T>,    content_?: CustomBuilder  ): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| styles | [CustomBuilderT](../arkts-components/arkts-arkui-custombuildert-t.md)&lt;T&gt; | Yes |  |
| factory | [ConstructorT](arkts-arkui-constructort-t.md)&lt;T&gt; | Yes |  |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | No |  |

## setRelativeContainerOptions

```TypeScript
public setRelativeContainerOptions(): this
```

Set the RelativeContainer Options.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExtendableRelativeContainer-public setRelativeContainerOptions(): this--><!--Device-ExtendableRelativeContainer-public setRelativeContainerOptions(): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

