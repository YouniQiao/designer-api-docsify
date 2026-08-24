# ContentSlotAttribute

Define ContentSlot attribute, to prevent improper recursive usage of ContentSlot@interface ContentSlotAttribute

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-unnamed-export declare interface ContentSlotAttribute--><!--Device-unnamed-export declare interface ContentSlotAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## applyAttributesFinish

```TypeScript
applyAttributesFinish(): void
```

Notify ContentSlot has finished setting up its attributes.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ContentSlotAttribute-applyAttributesFinish(): void--><!--Device-ContentSlotAttribute-applyAttributesFinish(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## debugLine

```TypeScript
debugLine(sourceLine: string, moduleName?: string): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-ContentSlotAttribute-debugLine(sourceLine: string, moduleName?: string): this--><!--Device-ContentSlotAttribute-debugLine(sourceLine: string, moduleName?: string): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| sourceLine | string | Yes |  |
| moduleName | string | No |  |

**Return value:**

| Type | Description |
| --- | --- |
## setContentSlotOptions

```TypeScript
setContentSlotOptions(content: Content): this
```

Sets content slot options.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ContentSlotAttribute-setContentSlotOptions(content: Content): this--><!--Device-ContentSlotAttribute-setContentSlotOptions(content: Content): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| content | Content | Yes | Content to display. |

**Return value:**

| Type | Description |
| --- | --- |
| this | ContentSlotAttribute instance |

## default

```TypeScript
default
```

Set the component's source code redirection information.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ContentSlotAttribute-default--><!--Device-ContentSlotAttribute-default-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

