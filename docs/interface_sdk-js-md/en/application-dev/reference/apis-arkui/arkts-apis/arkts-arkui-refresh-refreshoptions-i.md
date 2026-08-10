# RefreshOptions

用于设置Refresh组件参数。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export interface RefreshOptions--><!--Device-unnamed-export interface RefreshOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## builder

```TypeScript
builder?: CustomBuilder
```

自定义刷新区域显示内容。

**Type:** [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RefreshOptions-builder?: CustomBuilder--><!--Device-RefreshOptions-builder?: CustomBuilder-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## promptText

```TypeScript
promptText?: ResourceStr
```

设置刷新区域底部显示的自定义文本。

**Type:** [ResourceStr](arkts-arkui-resourcestr-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RefreshOptions-promptText?: ResourceStr--><!--Device-RefreshOptions-promptText?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## refreshing

```TypeScript
refreshing: boolean | Bindable<boolean>
```

组件当前是否处于刷新中状态。该参数支持\$用于双向绑定变量。

**Type:** boolean \| Bindable&lt;boolean&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RefreshOptions-refreshing: boolean | Bindable<boolean>--><!--Device-RefreshOptions-refreshing: boolean | Bindable<boolean>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## refreshingContent

```TypeScript
refreshingContent?: ComponentContentBase
```

自定义刷新区域显示内容。

**Type:** [ComponentContentBase](arkts-arkui-componentcontent-componentcontentbase-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RefreshOptions-refreshingContent?: ComponentContentBase--><!--Device-RefreshOptions-refreshingContent?: ComponentContentBase-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

