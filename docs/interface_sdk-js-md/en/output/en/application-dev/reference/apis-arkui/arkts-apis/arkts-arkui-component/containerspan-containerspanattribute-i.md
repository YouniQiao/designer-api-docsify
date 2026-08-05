# ContainerSpanAttribute

Define the ContainerSpan attribute functions.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface ContainerSpanAttribute--><!--Device-unnamed-export declare interface ContainerSpanAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## applyAttributesFinish

```TypeScript
default applyAttributesFinish(): void
```

Notify the component is finished setting up its attributes.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ContainerSpanAttribute-default applyAttributesFinish(): void--><!--Device-ContainerSpanAttribute-default applyAttributesFinish(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<ContainerSpanAttribute> | undefined): this
```

Sets the attribute modifier.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ContainerSpanAttribute-default attributeModifier(modifier: AttributeModifier<ContainerSpanAttribute> | undefined): this--><!--Device-ContainerSpanAttribute-default attributeModifier(modifier: AttributeModifier<ContainerSpanAttribute> | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| modifier | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;\_\_\_MD\_LINK\_USD\_1\_\_\_&gt; \| undefined | Yes | . |

**Return value:**

| Type | Description |
| --- | --- |
| this | the attribute of the ContainerSpanAttribute. |

## debugLine

```TypeScript
default debugLine(sourceLine: string, moduleName?: string): this
```

Set the component's source code redirection information.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ContainerSpanAttribute-default debugLine(sourceLine: string, moduleName?: string): this--><!--Device-ContainerSpanAttribute-default debugLine(sourceLine: string, moduleName?: string): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| sourceLine | string | Yes | the source code line. |
| moduleName | string | No | module to which the component belongs. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## setContainerSpanOptions

```TypeScript
default setContainerSpanOptions(): this
```

Set ContainerSpan options.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ContainerSpanAttribute-default setContainerSpanOptions(): this--><!--Device-ContainerSpanAttribute-default setContainerSpanOptions(): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| this | Returns the instance of the ContainerSpanAttribute. |

## textBackgroundStyle

```TypeScript
default textBackgroundStyle(style: TextBackgroundStyle | undefined): this
```

Span background style.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ContainerSpanAttribute-default textBackgroundStyle(style: TextBackgroundStyle | undefined): this--><!--Device-ContainerSpanAttribute-default textBackgroundStyle(style: TextBackgroundStyle | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | \_\_\_MD\_LINK\_USD\_0\_\_\_ \| undefined | Yes | The background style of span. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

