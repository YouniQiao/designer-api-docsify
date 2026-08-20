# RefreshOptions

Defines the options of refresh component.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export interface RefreshOptions--><!--Device-unnamed-export interface RefreshOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## builder

```TypeScript
builder?: CustomBuilder
```

Custom component to display during dragging.

**Type:** [CustomBuilder](../arkts-apis/arkts-custombuilder-t.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RefreshOptions-builder?: CustomBuilder--><!--Device-RefreshOptions-builder?: CustomBuilder-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## promptText

```TypeScript
promptText?: ResourceStr
```

The text displayed during refreshing.

**Type:** [ResourceStr](../../apis-arkui/arkts-apis/arkts-arkui-resourcestr-t.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RefreshOptions-promptText?: ResourceStr--><!--Device-RefreshOptions-promptText?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## refreshing

```TypeScript
refreshing: boolean | Bindable<boolean>
```

Whether the current component is being refreshed. This parameter supports \$ for two-way binding of variables.

**Type:** boolean \| [Bindable](../arkts-apis/arkts-common-bindable-i.md)&lt;boolean&gt;

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RefreshOptions-refreshing: boolean | Bindable<boolean>--><!--Device-RefreshOptions-refreshing: boolean | Bindable<boolean>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## refreshingContent

```TypeScript
refreshingContent?: ComponentContentBase
```

Custom component to display during dragging.

**Type:** [ComponentContentBase](../arkts-apis/arkts-componentcontent-componentcontentbase-c.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RefreshOptions-refreshingContent?: ComponentContentBase--><!--Device-RefreshOptions-refreshingContent?: ComponentContentBase-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

