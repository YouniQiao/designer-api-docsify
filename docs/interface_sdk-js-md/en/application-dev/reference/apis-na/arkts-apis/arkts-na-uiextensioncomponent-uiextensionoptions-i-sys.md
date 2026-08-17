# UIExtensionOptions (System API)

This interface is used to set the options for UIExtensionComponentAttribute during construction

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare interface UIExtensionOptions--><!--Device-unnamed-export declare interface UIExtensionOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## areaChangePlaceholder

```TypeScript
areaChangePlaceholder?: Record<string, ComponentContentBase>
```

Set Areachange placeholder. If the Areachange placeholder ComponentContentBase is set, the placeholder node is displayed until the UIExtensionComponent size change is complete.

**Type:** Record&lt;string, [ComponentContentBase](arkts-na-componentcontent-componentcontentbase-c.md)&gt;

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIExtensionOptions-areaChangePlaceholder?: Record<string, ComponentContentBase>--><!--Device-UIExtensionOptions-areaChangePlaceholder?: Record<string, ComponentContentBase>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## dpiFollowStrategy

```TypeScript
dpiFollowStrategy?: DpiFollowStrategy
```

Set UIExtensionComponent Content Dpi Follow Strategy.

**Type:** [DpiFollowStrategy](arkts-na-uiextensioncomponent-dpifollowstrategy-e-sys.md)

**Default:** DpiFollowStrategy.FOLLOW_UI_EXTENSION_ABILITY_DPI

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIExtensionOptions-dpiFollowStrategy?: DpiFollowStrategy--><!--Device-UIExtensionOptions-dpiFollowStrategy?: DpiFollowStrategy-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## isTransferringCaller

```TypeScript
isTransferringCaller?: boolean
```

Set whether the current capability is used as a Caller.<br/> If set to true, as a Caller, the current token of UIExtensionComponent is set to rootToken.

**Type:** boolean

**Default:** false

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIExtensionOptions-isTransferringCaller?: boolean--><!--Device-UIExtensionOptions-isTransferringCaller?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## placeholder

```TypeScript
placeholder?: ComponentContentBase
```

Set placeholder. If set placeholder ComponentContentBase, show placeholder node when connection is not established.

**Type:** [ComponentContentBase](arkts-na-componentcontent-componentcontentbase-c.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIExtensionOptions-placeholder?: ComponentContentBase--><!--Device-UIExtensionOptions-placeholder?: ComponentContentBase-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## windowModeFollowStrategy

```TypeScript
windowModeFollowStrategy?: WindowModeFollowStrategy
```

Set UIExtensionComponent Content Window Mode Follow Strategy.

**Type:** [WindowModeFollowStrategy](arkts-na-uiextensioncomponent-windowmodefollowstrategy-e-sys.md)

**Default:** WindowModeFollowStrategy.FOLLOW_UI_EXTENSION_ABILITY_WINDOW_MODE

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIExtensionOptions-windowModeFollowStrategy?: WindowModeFollowStrategy--><!--Device-UIExtensionOptions-windowModeFollowStrategy?: WindowModeFollowStrategy-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

