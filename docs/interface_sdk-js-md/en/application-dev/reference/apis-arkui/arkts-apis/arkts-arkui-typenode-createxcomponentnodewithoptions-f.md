# createXComponentNodeWithOptions

## createXComponentNodeWithOptions

```TypeScript
export function createXComponentNodeWithOptions(
    context: UIContext, value: XComponentOptions, options?: FrameNodeOptions): XComponent
```

Create a FrameNode of XComponent type with options. On API 26.0.0 and above, It can also create a FrameNode of XComponent type with options and FrameNode options.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes |
| value | [XComponentOptions](../arkts-components/arkts-arkui-xcomponentoptions-i.md) | Yes |
| options | [FrameNodeOptions](arkts-arkui-framenode-framenodeoptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [XComponent](arkts-arkui-typenode-xcomponent-t.md) |
