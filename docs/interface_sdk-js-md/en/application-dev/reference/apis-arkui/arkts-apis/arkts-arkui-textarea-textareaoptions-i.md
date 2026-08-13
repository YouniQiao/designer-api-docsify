# TextAreaOptions

Defines the options of TextArea.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-export declare interface TextAreaOptions--><!--Device-unnamed-export declare interface TextAreaOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## controller

```TypeScript
controller?: TextAreaController
```

Called when the position of the insertion cursor is set.

**Type:** [TextAreaController](arkts-arkui-textarea-textareacontroller-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextAreaOptions-controller?: TextAreaController--><!--Device-TextAreaOptions-controller?: TextAreaController-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## placeholder

```TypeScript
placeholder?: ResourceStr
```

The place holder text string. Text displayed when there is no input. &lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;: &lt;br&gt;When only the placeholder attribute is set, the text selection handle is still available. &lt;br&gt;The caret stays at the beginning of the placeholder text when the handle is released. &lt;/p&gt;

**Type:** [ResourceStr](arkts-arkui-resourcestr-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextAreaOptions-placeholder?: ResourceStr--><!--Device-TextAreaOptions-placeholder?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## text

```TypeScript
text?: ResourceStr | Bindable<ResourceStr> | Bindable<Resource> | Bindable<string>
```

Sets the current value of TextArea.

**Type:** [ResourceStr](arkts-arkui-resourcestr-t.md) \| [Bindable](../../apis-na/arkts-apis/arkts-na-common-bindable-i.md)&lt;[ResourceStr](arkts-arkui-resourcestr-t.md)&gt; \| [Bindable](../../apis-na/arkts-apis/arkts-na-common-bindable-i.md)&lt;[Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md)&gt; \| [Bindable](../../apis-na/arkts-apis/arkts-na-common-bindable-i.md)&lt;string&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextAreaOptions-text?: ResourceStr | Bindable<ResourceStr> | Bindable<Resource> | Bindable<string>--><!--Device-TextAreaOptions-text?: ResourceStr | Bindable<ResourceStr> | Bindable<Resource> | Bindable<string>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

