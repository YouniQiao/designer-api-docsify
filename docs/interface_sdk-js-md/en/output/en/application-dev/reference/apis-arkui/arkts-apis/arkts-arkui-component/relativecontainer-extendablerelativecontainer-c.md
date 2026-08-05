# ExtendableRelativeContainer

Defines the Extendable RelativeContainer.

**Inheritance/Implementation:** ExtendableRelativeContainer implements [RelativeContainerAttribute](relativecontainer-relativecontainerattribute-i.md)

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
| factory | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;T&gt; | Yes |  |
| content\_ | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No |  |

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
| styles | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;T&gt; | Yes |  |
| factory | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;T&gt; | Yes |  |
| content\_ | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No |  |

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

