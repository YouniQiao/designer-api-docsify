# ExtendableText

Defines the Extendable Text.

**Inheritance/Implementation:** ExtendableText implements [TextAttribute](text-textattribute-i.md)

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

Constructor of Extendable Text.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExtendableText-static $_instantiate<T extends ExtendableText>(      factory: ConstructorT<T>,       content?: string | Resource,       value?: TextOptions,       content_?: CustomBuilder    ): T--><!--Device-ExtendableText-static $_instantiate<T extends ExtendableText>(      factory: ConstructorT<T>,       content?: string | Resource,       value?: TextOptions,       content_?: CustomBuilder    ): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| factory | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;T&gt; | Yes |  |
| content | string \| Resource | No |  |
| value | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No |  |
| content\_ | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No |  |

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

Entry of Extendable Text.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExtendableText-static _instantiateImpl<T extends ExtendableText>(        styles: CustomBuilderT<T>,          factory: ConstructorT<T>,         content_?: CustomBuilder    ): void--><!--Device-ExtendableText-static _instantiateImpl<T extends ExtendableText>(        styles: CustomBuilderT<T>,          factory: ConstructorT<T>,         content_?: CustomBuilder    ): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| styles | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;T&gt; | Yes |  |
| factory | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;T&gt; | Yes |  |
| content\_ | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No |  |

## setTextOptions

```TypeScript
public setTextOptions(
      content?: string | Resource, 
      value?: TextOptions
    ): this
```

Set the Text Options.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExtendableText-public setTextOptions(      content?: string | Resource,       value?: TextOptions    ): this--><!--Device-ExtendableText-public setTextOptions(      content?: string | Resource,       value?: TextOptions    ): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| content | string \| Resource | No |  |
| value | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

