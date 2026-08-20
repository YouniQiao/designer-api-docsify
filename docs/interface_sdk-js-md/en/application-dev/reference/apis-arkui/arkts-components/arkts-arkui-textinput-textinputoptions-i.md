# TextInputOptions

Defines the options of TextInput.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare interface TextInputOptions--><!--Device-unnamed-export declare interface TextInputOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## controller

```TypeScript
controller?: TextInputController
```

Called when the position of the insertion cursor is set.

**Type:** [TextInputController](arkts-arkui-textinput-textinputcontroller-c.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextInputOptions-controller?: TextInputController--><!--Device-TextInputOptions-controller?: TextInputController-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## placeholder

```TypeScript
placeholder?: ResourceStr
```

The place holder text string.

**Type:** [ResourceStr](../arkts-apis/arkts-arkui-resourcestr-t.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextInputOptions-placeholder?: ResourceStr--><!--Device-TextInputOptions-placeholder?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## text

```TypeScript
text?: ResourceStr | Bindable<ResourceStr> | Bindable<Resource> | Bindable<string>
```

Sets the current value of TextInput.

**Type:** [ResourceStr](../arkts-apis/arkts-arkui-resourcestr-t.md) \| [Bindable](../../apis-default/arkts-apis/arkts-common-bindable-i.md)&lt;[ResourceStr](../arkts-apis/arkts-arkui-resourcestr-t.md)&gt; \| [Bindable](../../apis-default/arkts-apis/arkts-common-bindable-i.md)&lt;[Resource](../arkts-apis/arkts-arkui-resource-t.md)&gt; \| [Bindable](../../apis-default/arkts-apis/arkts-common-bindable-i.md)&lt;string&gt;

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextInputOptions-text?: ResourceStr | Bindable<ResourceStr> | Bindable<Resource> | Bindable<string>--><!--Device-TextInputOptions-text?: ResourceStr | Bindable<ResourceStr> | Bindable<Resource> | Bindable<string>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

