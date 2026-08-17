# ExtendableRelativeContainer

Defines the Extendable RelativeContainer.

**Inheritance/Implementation:** ExtendableRelativeContainer implements RelativeContainerAttribute

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-unnamed-export declare abstract class ExtendableRelativeContainer--><!--Device-unnamed-export declare abstract class ExtendableRelativeContainer-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## $_instantiate

```TypeScript
@ComponentBuilder
  static $_instantiate<T extends ExtendableRelativeContainer>(
    factory: ConstructorT<T>,
    content_?: CustomBuilder
  ): T
```

Constructor of Extendable RelativeContainer.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExtendableRelativeContainer-@ComponentBuilder  static $_instantiate<T extends ExtendableRelativeContainer>(    factory: ConstructorT<T>,    content_?: CustomBuilder  ): T--><!--Device-ExtendableRelativeContainer-@ComponentBuilder  static $_instantiate<T extends ExtendableRelativeContainer>(    factory: ConstructorT<T>,    content_?: CustomBuilder  ): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| factory | [ConstructorT](../../apis-na/arkts-apis/arkts-na-constructort-t.md)&lt;T&gt; | Yes |  |
| content_ | CustomBuilder | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| T |  |

## _instantiateImpl

```TypeScript
@Builder
  static _instantiateImpl<T extends ExtendableRelativeContainer>(
    styles: CustomBuilderT<T>,
    factory: ConstructorT<T>,
    content_?: CustomBuilder
  ): void
```

Entry of Extendable RelativeContainer.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExtendableRelativeContainer-@Builder  static _instantiateImpl<T extends ExtendableRelativeContainer>(    styles: CustomBuilderT<T>,    factory: ConstructorT<T>,    content_?: CustomBuilder  ): void--><!--Device-ExtendableRelativeContainer-@Builder  static _instantiateImpl<T extends ExtendableRelativeContainer>(    styles: CustomBuilderT<T>,    factory: ConstructorT<T>,    content_?: CustomBuilder  ): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| styles | CustomBuilderT&lt;T&gt; | Yes |  |
| factory | [ConstructorT](../../apis-na/arkts-apis/arkts-na-constructort-t.md)&lt;T&gt; | Yes |  |
| content_ | CustomBuilder | No |  |

## setRelativeContainerOptions

```TypeScript
public setRelativeContainerOptions(): this
```

Set the RelativeContainer Options.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExtendableRelativeContainer-public setRelativeContainerOptions(): this--><!--Device-ExtendableRelativeContainer-public setRelativeContainerOptions(): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

