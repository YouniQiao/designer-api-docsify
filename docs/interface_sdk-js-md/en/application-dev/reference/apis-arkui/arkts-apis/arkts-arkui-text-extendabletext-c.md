# ExtendableText

定义扩展文本组件

**Inheritance/Implementation:** ExtendableText implements [TextAttribute](../arkts-components/arkts-arkui-text-attribute.md/arkts-arkui-text-attribute.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-unnamed-export declare abstract class ExtendableText implements TextAttribute--><!--Device-unnamed-export declare abstract class ExtendableText implements TextAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## $_instantiate

```TypeScript
static $_instantiate<T extends ExtendableText>(
    factory: ConstructorT<T>, 
    content?: string | Resource, 
    value?: TextOptions, 
    content_?: CustomBuilder
  ): T
```

扩展文本组件构造器

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExtendableText-static $_instantiate<T extends ExtendableText>(    factory: ConstructorT<T>,     content?: string | Resource,     value?: TextOptions,     content_?: CustomBuilder  ): T--><!--Device-ExtendableText-static $_instantiate<T extends ExtendableText>(    factory: ConstructorT<T>,     content?: string | Resource,     value?: TextOptions,     content_?: CustomBuilder  ): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| factory | [ConstructorT](arkts-arkui-constructort-t.md)&lt;T&gt; | Yes |  |
| content | string \| Resource | No |  |
| value | [TextOptions](../arkts-components/arkts-arkui-textoptions-i.md) | No |  |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| T |  |

## _instantiateImpl

```TypeScript
static _instantiateImpl<T extends ExtendableText>(
      styles: CustomBuilderT<T>, 
      factory: ConstructorT<T>, 
      content_?: CustomBuilder
  ): void
```

扩展文本组件入口

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExtendableText-static _instantiateImpl<T extends ExtendableText>(      styles: CustomBuilderT<T>,       factory: ConstructorT<T>,       content_?: CustomBuilder  ): void--><!--Device-ExtendableText-static _instantiateImpl<T extends ExtendableText>(      styles: CustomBuilderT<T>,       factory: ConstructorT<T>,       content_?: CustomBuilder  ): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| styles | [CustomBuilderT](../arkts-components/arkts-arkui-custombuildert-t.md)&lt;T&gt; | Yes |  |
| factory | [ConstructorT](arkts-arkui-constructort-t.md)&lt;T&gt; | Yes |  |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | No |  |

## setTextOptions

```TypeScript
public setTextOptions(
    content?: string | Resource, 
    value?: TextOptions
  ): this
```

设置文本组件的选项

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExtendableText-public setTextOptions(    content?: string | Resource,     value?: TextOptions  ): this--><!--Device-ExtendableText-public setTextOptions(    content?: string | Resource,     value?: TextOptions  ): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| content | string \| Resource | No |  |
| value | [TextOptions](../arkts-components/arkts-arkui-textoptions-i.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

