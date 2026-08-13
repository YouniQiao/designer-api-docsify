# EmbeddedOptions

This interface is used to set the options for EmbeddedComponentAttribute during construction.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

<!--Device-unnamed-export declare interface EmbeddedOptions--><!--Device-unnamed-export declare interface EmbeddedOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## areaChangePlaceholder

```TypeScript
areaChangePlaceholder?: Record<string, ComponentContentBase>
```

Set Areachange placeholder. If the Areachange placeholder is set, the placeholder node is displayed until the EmbeddedComponent size change is complete.

**Type:** Record&lt;string, [ComponentContentBase](arkts-na-componentcontent-componentcontentbase-c.md)&gt;

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-EmbeddedOptions-areaChangePlaceholder?: Record<string, ComponentContentBase>--><!--Device-EmbeddedOptions-areaChangePlaceholder?: Record<string, ComponentContentBase>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## dpiFollowStrategy

```TypeScript
dpiFollowStrategy?: EmbeddedDpiFollowStrategy
```

Set EmbeddedComponent Content Dpi Follow Strategy.

**Type:** [EmbeddedDpiFollowStrategy](arkts-na-embeddedcomponent-embeddeddpifollowstrategy-e.md)

**Default:** EmbeddedDpiFollowStrategy.FOLLOW_UI_EXTENSION_ABILITY_DPI

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-EmbeddedOptions-dpiFollowStrategy?: EmbeddedDpiFollowStrategy--><!--Device-EmbeddedOptions-dpiFollowStrategy?: EmbeddedDpiFollowStrategy-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## placeholder

```TypeScript
placeholder?: ComponentContentBase
```

Set placeholder. If set placeholder ComponentContentBase, show placeholder node when connection is not established.

**Type:** [ComponentContentBase](arkts-na-componentcontent-componentcontentbase-c.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-EmbeddedOptions-placeholder?: ComponentContentBase--><!--Device-EmbeddedOptions-placeholder?: ComponentContentBase-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## windowModeFollowStrategy

```TypeScript
windowModeFollowStrategy?: EmbeddedWindowModeFollowStrategy
```

Set EmbeddedComponent Content Window Mode Follow Strategy.

**Type:** [EmbeddedWindowModeFollowStrategy](arkts-na-embeddedcomponent-embeddedwindowmodefollowstrategy-e.md)

**Default:** EmbeddedWindowModeFollowStrategy.FOLLOW_UI_EXTENSION_ABILITY_WINDOW_MODE

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-EmbeddedOptions-windowModeFollowStrategy?: EmbeddedWindowModeFollowStrategy--><!--Device-EmbeddedOptions-windowModeFollowStrategy?: EmbeddedWindowModeFollowStrategy-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

