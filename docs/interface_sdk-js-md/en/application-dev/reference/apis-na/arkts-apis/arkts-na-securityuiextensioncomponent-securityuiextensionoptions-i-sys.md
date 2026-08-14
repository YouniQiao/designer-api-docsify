# SecurityUIExtensionOptions (System API)

This interface is used to set the options for SecurityUIExtensionComponentAttribute during construction

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

<!--Device-unnamed-export declare interface SecurityUIExtensionOptions--><!--Device-unnamed-export declare interface SecurityUIExtensionOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## dpiFollowStrategy

```TypeScript
dpiFollowStrategy?: SecurityDpiFollowStrategy
```

Set SecurityUIExtensionComponent Content Dpi Follow Strategy.

**Type:** [SecurityDpiFollowStrategy](arkts-na-securityuiextensioncomponent-securitydpifollowstrategy-e-sys.md)

**Default:** SecurityDpiFollowStrategy.FOLLOW_UI_EXTENSION_ABILITY_DPI

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-SecurityUIExtensionOptions-dpiFollowStrategy?: SecurityDpiFollowStrategy--><!--Device-SecurityUIExtensionOptions-dpiFollowStrategy?: SecurityDpiFollowStrategy-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## isTransferringCaller

```TypeScript
isTransferringCaller?: boolean
```

Set whether the current capability is used as a Caller.<br/> If set to true, as a Caller, the current token of SecurityUIExtensionComponent is set to rootToken.

**Type:** boolean

**Default:** false

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-SecurityUIExtensionOptions-isTransferringCaller?: boolean--><!--Device-SecurityUIExtensionOptions-isTransferringCaller?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## placeholder

```TypeScript
placeholder?: ComponentContent
```

Set placeholder. If set placeholder ComponentContent, show placeholder node when connection is not established.

**Type:** [ComponentContent](arkts-na-componentcontent-c.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-SecurityUIExtensionOptions-placeholder?: ComponentContent--><!--Device-SecurityUIExtensionOptions-placeholder?: ComponentContent-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

