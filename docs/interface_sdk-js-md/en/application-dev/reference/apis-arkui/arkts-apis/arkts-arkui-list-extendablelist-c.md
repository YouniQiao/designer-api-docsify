# ExtendableList

定义可扩展List组件。

**Inheritance/Implementation:** ExtendableList implements [ListAttribute](../arkts-components/arkts-arkui-list-attribute.md/arkts-arkui-list-attribute.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-unnamed-export declare abstract class ExtendableList implements ListAttribute--><!--Device-unnamed-export declare abstract class ExtendableList implements ListAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## $_instantiate

```TypeScript
static $_instantiate<T extends ExtendableList>(
    factory: ConstructorT<T>, 
    options?: ListOptions, 
    content_?: CustomBuilder
  ): T
```

可扩展List组件的构造函数。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExtendableList-static $_instantiate<T extends ExtendableList>(    factory: ConstructorT<T>,     options?: ListOptions,     content_?: CustomBuilder  ): T--><!--Device-ExtendableList-static $_instantiate<T extends ExtendableList>(    factory: ConstructorT<T>,     options?: ListOptions,     content_?: CustomBuilder  ): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| factory | [ConstructorT](arkts-arkui-constructort-t.md)&lt;T&gt; | Yes |  |
| options | [ListOptions](../arkts-components/arkts-arkui-listoptions-i.md) | No |  |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| T |  |

## _instantiateImpl

```TypeScript
static _instantiateImpl<T extends ExtendableList>(
    styles: CustomBuilderT<T>, 
    factory: ConstructorT<T>,
    content_?: CustomBuilder
  ): void
```

扩展列表组件入口

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExtendableList-static _instantiateImpl<T extends ExtendableList>(    styles: CustomBuilderT<T>,     factory: ConstructorT<T>,    content_?: CustomBuilder  ): void--><!--Device-ExtendableList-static _instantiateImpl<T extends ExtendableList>(    styles: CustomBuilderT<T>,     factory: ConstructorT<T>,    content_?: CustomBuilder  ): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| styles | [CustomBuilderT](../arkts-components/arkts-arkui-custombuildert-t.md)&lt;T&gt; | Yes |  |
| factory | [ConstructorT](arkts-arkui-constructort-t.md)&lt;T&gt; | Yes |  |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | No |  |

## setListOptions

```TypeScript
public setListOptions(options?: ListOptions): this
```

设置List组件参数。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExtendableList-public setListOptions(options?: ListOptions): this--><!--Device-ExtendableList-public setListOptions(options?: ListOptions): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [ListOptions](../arkts-components/arkts-arkui-listoptions-i.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

