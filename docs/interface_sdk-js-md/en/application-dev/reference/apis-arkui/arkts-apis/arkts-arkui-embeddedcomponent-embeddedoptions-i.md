# EmbeddedOptions

用于在EmbeddedComponent创建时传递可选的构造参数。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-unnamed-export declare interface EmbeddedOptions--><!--Device-unnamed-export declare interface EmbeddedOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## areaChangePlaceholder

```TypeScript
areaChangePlaceholder?: Record<string, ComponentContentBase>
```

设置尺寸变化占位符，在EmbeddedComponent尺寸发生变化并且内部渲染未完成时显示。&lt;br/&gt;key为尺寸变化场景类型（如"FOLD_TO_EXPAND"表示折叠展开场景），value为对应场景的占位符组件。 当前支持的键值包括：FOLD_TO_EXPAND。传入不支持的键值时，该占位符不生效。&lt;br/&gt;默认值：undefined，不设置尺寸变化占位符。

**Type:** [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, ComponentContentBase&gt;

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EmbeddedOptions-areaChangePlaceholder?: Record<string, ComponentContentBase>--><!--Device-EmbeddedOptions-areaChangePlaceholder?: Record<string, ComponentContentBase>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## dpiFollowStrategy

```TypeScript
dpiFollowStrategy?: EmbeddedDpiFollowStrategy
```

设置DPI，使其能够跟随宿主或EmbeddedUIExtensionAbility。

**Type:** [EmbeddedDpiFollowStrategy](arkts-arkui-embeddedcomponent-embeddeddpifollowstrategy-e.md)

**Default:** EmbeddedDpiFollowStrategy.FOLLOW_UI_EXTENSION_ABILITY_DPI

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EmbeddedOptions-dpiFollowStrategy?: EmbeddedDpiFollowStrategy--><!--Device-EmbeddedOptions-dpiFollowStrategy?: EmbeddedDpiFollowStrategy-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## placeholder

```TypeScript
placeholder?: ComponentContentBase
```

设置占位符，在EmbeddedComponent与EmbeddedUIExtensionAbility建立连接前显示。&lt;br/&gt;默认值：undefined，不设置占位符。

**Type:** [ComponentContentBase](arkts-arkui-componentcontent-componentcontentbase-c.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EmbeddedOptions-placeholder?: ComponentContentBase--><!--Device-EmbeddedOptions-placeholder?: ComponentContentBase-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## windowModeFollowStrategy

```TypeScript
windowModeFollowStrategy?: EmbeddedWindowModeFollowStrategy
```

设置窗口模式，使其能够跟随宿主或EmbeddedUIExtensionAbility。

**Type:** [EmbeddedWindowModeFollowStrategy](arkts-arkui-embeddedcomponent-embeddedwindowmodefollowstrategy-e.md)

**Default:** EmbeddedWindowModeFollowStrategy.FOLLOW_UI_EXTENSION_ABILITY_WINDOW_MODE

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EmbeddedOptions-windowModeFollowStrategy?: EmbeddedWindowModeFollowStrategy--><!--Device-EmbeddedOptions-windowModeFollowStrategy?: EmbeddedWindowModeFollowStrategy-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

