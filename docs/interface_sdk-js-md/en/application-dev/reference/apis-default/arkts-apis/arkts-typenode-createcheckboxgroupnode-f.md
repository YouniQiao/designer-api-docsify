# createCheckboxGroupNode

## createCheckboxGroupNode

```TypeScript
export function createCheckboxGroupNode(context: UIContext, options?: FrameNodeOptions): CheckboxGroup
```

Create a FrameNode of CheckboxGroup type. On API 26.0.0 and above, It can also create a FrameNode of CheckboxGroup type with options.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-typeNode-export function createCheckboxGroupNode(context: UIContext, options?: FrameNodeOptions): CheckboxGroup--><!--Device-typeNode-export function createCheckboxGroupNode(context: UIContext, options?: FrameNodeOptions): CheckboxGroup-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [UIContext](../../apis-arkui/arkts-apis/arkts-arkui-arkuiuicontext-uicontext-c.md) | Yes | uiContext used to create the FrameNode. |
| options | [FrameNodeOptions](arkts-framenode-framenodeoptions-i.md) | No | Options for configuring FrameNode creation.<br>**Since:** 26.0.0 |

**Return value:**

| Type | Description |
| --- | --- |
| CheckboxGroup | Return CheckboxGroup type FrameNode. |

