# ExtendableStack

Defines the Extendable Stack.

**Inheritance/Implementation:** ExtendableStack implements [StackAttribute](stack-stackattribute-i.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-unnamed-export declare abstract class ExtendableStack implements StackAttribute--><!--Device-unnamed-export declare abstract class ExtendableStack implements StackAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## $_instantiate

```TypeScript
static $_instantiate<T extends ExtendableStack>(
        factory: ConstructorT<T>, 
        options?: StackOptions,
        content_?: CustomBuilder
    ): T
```

Constructor of Extendable Stack.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExtendableStack-static $_instantiate<T extends ExtendableStack>(        factory: ConstructorT<T>,         options?: StackOptions,        content_?: CustomBuilder    ): T--><!--Device-ExtendableStack-static $_instantiate<T extends ExtendableStack>(        factory: ConstructorT<T>,         options?: StackOptions,        content_?: CustomBuilder    ): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| factory | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;T&gt; | Yes |  |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No |  |
| content\_ | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| T |  |

## _instantiateImpl

```TypeScript
static _instantiateImpl<T extends ExtendableStack>(
        styles: CustomBuilderT<T>, 
        factory: ConstructorT<T>, 
        content_?: CustomBuilder
    ): void
```

Entry of Extendable Stack.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExtendableStack-static _instantiateImpl<T extends ExtendableStack>(        styles: CustomBuilderT<T>,         factory: ConstructorT<T>,         content_?: CustomBuilder    ): void--><!--Device-ExtendableStack-static _instantiateImpl<T extends ExtendableStack>(        styles: CustomBuilderT<T>,         factory: ConstructorT<T>,         content_?: CustomBuilder    ): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| styles | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;T&gt; | Yes |  |
| factory | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;T&gt; | Yes |  |
| content\_ | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No |  |

## setStackOptions

```TypeScript
public setStackOptions(options?: StackOptions): this
```

Set the Stack Options.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExtendableStack-public setStackOptions(options?: StackOptions): this--><!--Device-ExtendableStack-public setStackOptions(options?: StackOptions): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

