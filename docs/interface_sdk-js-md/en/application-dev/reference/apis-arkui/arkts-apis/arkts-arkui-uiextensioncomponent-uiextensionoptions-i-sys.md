# UIExtensionOptions (System API)

用于在UIExtensionComponent进行构造时传递可选的构造参数。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface UIExtensionOptions--><!--Device-unnamed-export declare interface UIExtensionOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## areaChangePlaceholder

```TypeScript
areaChangePlaceholder?: Record<string, ComponentContentBase>
```

设置尺寸变化占位符，在UIExtensionComponent尺寸发生变化并且UIExtensionAbility内部渲染未完成时显示，key值仅支持"FOLD_TO_EXPAND"（折叠展开尺寸变化）、 "UNDEFINED"（默认尺寸变化），传入其他key值时不生效。不设置时默认不显示尺寸变化占位内容。

**Type:** [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, ComponentContentBase&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIExtensionOptions-areaChangePlaceholder?: Record<string, ComponentContentBase>--><!--Device-UIExtensionOptions-areaChangePlaceholder?: Record<string, ComponentContentBase>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## dpiFollowStrategy

```TypeScript
dpiFollowStrategy?: DpiFollowStrategy
```

提供接口支持设置DPI跟随宿主或跟随UIExtensionAbility。

**Type:** [DpiFollowStrategy](arkts-arkui-uiextensioncomponent-dpifollowstrategy-e-sys.md)

**Default:** DpiFollowStrategy.FOLLOW_UI_EXTENSION_ABILITY_DPI

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIExtensionOptions-dpiFollowStrategy?: DpiFollowStrategy--><!--Device-UIExtensionOptions-dpiFollowStrategy?: DpiFollowStrategy-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## isTransferringCaller

```TypeScript
isTransferringCaller?: boolean
```

在使用UIExtensionComponent嵌套时，设置当前UIExtensionComponent是否转发上一级的Caller信息。&lt;br/&gt;true表示转发上一级的Caller信息，false表示不转发上一级的Caller信息。&lt;br/&gt;默认值：false

**Type:** boolean

**Default:** false

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIExtensionOptions-isTransferringCaller?: boolean--><!--Device-UIExtensionOptions-isTransferringCaller?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## placeholder

```TypeScript
placeholder?: ComponentContentBase
```

设置占位符，在UIExtensionComponent与UIExtensionAbility建立连接前显示。当需要在连接建立前向用户展示加载状态或提示内容时传入此参数，不设置时默认不显示占位内容。

**Type:** [ComponentContentBase](arkts-arkui-componentcontent-componentcontentbase-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIExtensionOptions-placeholder?: ComponentContentBase--><!--Device-UIExtensionOptions-placeholder?: ComponentContentBase-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## windowModeFollowStrategy

```TypeScript
windowModeFollowStrategy?: WindowModeFollowStrategy
```

提供接口以支持设置窗口Mode，使其能够跟随宿主或UIExtensionAbility。

**Type:** [WindowModeFollowStrategy](../arkts-components/arkts-arkui-windowmodefollowstrategy-e-sys.md)

**Default:** WindowModeFollowStrategy.FOLLOW_UI_EXTENSION_ABILITY_WINDOW_MODE

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIExtensionOptions-windowModeFollowStrategy?: WindowModeFollowStrategy--><!--Device-UIExtensionOptions-windowModeFollowStrategy?: WindowModeFollowStrategy-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

