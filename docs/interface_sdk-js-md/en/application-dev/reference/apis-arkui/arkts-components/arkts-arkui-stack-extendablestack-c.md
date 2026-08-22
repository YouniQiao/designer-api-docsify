# ExtendableStack

Defines the Extendable Stack.

@implements StackAttribute

**Inheritance/Implementation:** ExtendableStack implements [StackAttribute](arkts-arkui-stack-attribute.md#stackattribute)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

<!--Device-unnamed-export declare abstract class ExtendableStack--><!--Device-unnamed-export declare abstract class ExtendableStack-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## $_instantiate

```TypeScript
@ComponentBuilder
    static $_instantiate<T extends ExtendableStack>(
        factory: ConstructorT<T>, 
        options?: StackOptions,
        content_?: CustomBuilder
    ): T
```

Constructor of Extendable Stack.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExtendableStack-@ComponentBuilder    static $_instantiate<T extends ExtendableStack>(        factory: ConstructorT<T>,         options?: StackOptions,        content_?: CustomBuilder    ): T--><!--Device-ExtendableStack-@ComponentBuilder    static $_instantiate<T extends ExtendableStack>(        factory: ConstructorT<T>,         options?: StackOptions,        content_?: CustomBuilder    ): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| factory | [ConstructorT](../../apis-default/arkts-apis/arkts-constructort-t.md)&lt;T&gt; | Yes |  |
| options | [StackOptions](arkts-arkui-stack-stackoptions-i.md) | No |  |
| content_ | [CustomBuilder](../../apis-default/arkts-apis/arkts-custombuilder-t.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| T |  |

## _instantiateImpl

```TypeScript
@Builder
    static _instantiateImpl<T extends ExtendableStack>(
        styles: CustomBuilderT<T>, 
        factory: ConstructorT<T>, 
        content_?: CustomBuilder
    ): void
```

Entry of Extendable Stack.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExtendableStack-@Builder    static _instantiateImpl<T extends ExtendableStack>(        styles: CustomBuilderT<T>,         factory: ConstructorT<T>,         content_?: CustomBuilder    ): void--><!--Device-ExtendableStack-@Builder    static _instantiateImpl<T extends ExtendableStack>(        styles: CustomBuilderT<T>,         factory: ConstructorT<T>,         content_?: CustomBuilder    ): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| styles | [CustomBuilderT](../../apis-default/arkts-apis/arkts-custombuildert-t.md)&lt;T&gt; | Yes |  |
| factory | [ConstructorT](../../apis-default/arkts-apis/arkts-constructort-t.md)&lt;T&gt; | Yes |  |
| content_ | [CustomBuilder](../../apis-default/arkts-apis/arkts-custombuilder-t.md) | No |  |

## setStackOptions

```TypeScript
public setStackOptions(options?: StackOptions): this
```

Set the Stack Options.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExtendableStack-public setStackOptions(options?: StackOptions): this--><!--Device-ExtendableStack-public setStackOptions(options?: StackOptions): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [StackOptions](arkts-arkui-stack-stackoptions-i.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| [ExtendableStack](arkts-arkui-stack-extendablestack-c.md) |  |

