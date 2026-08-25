# TextAreaOptions

Defines the options of TextArea.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## controller

```TypeScript
controller?: TextAreaController
```

Called when the position of the insertion cursor is set.

**Type:** [TextAreaController](arkts-arkui-textarea-textareacontroller-c.md)

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## placeholder

```TypeScript
placeholder?: ResourceStr
```

The place holder text string. Text displayed when there is no input.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>When only the placeholder attribute is set, the text selection handle is still available. <br>The caret stays at the beginning of the placeholder text when the handle is released. </p>

**Type:** [ResourceStr](arkts-arkui-resourcestr-t.md)

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## text

```TypeScript
text?: ResourceStr | Bindable<ResourceStr> | Bindable<Resource> | Bindable<string>
```

Sets the current value of TextArea.

**Type:** [ResourceStr](arkts-arkui-resourcestr-t.md) \| [Bindable](arkts-arkui-common-bindable-i.md)&lt;[ResourceStr](arkts-arkui-resourcestr-t.md)&gt; \| [Bindable](arkts-arkui-common-bindable-i.md)&lt;[Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md)&gt; \| [Bindable](arkts-arkui-common-bindable-i.md)&lt;string&gt;

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full
