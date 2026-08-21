# ToolBarV2ItemText

Defines the text of a toolbar item.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare class ToolBarV2ItemText--><!--Device-unnamed-export declare class ToolBarV2ItemText-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## constructor

```TypeScript
constructor(options: ToolBarV2ItemTextOptions)
```

A constructor used to create a **ToolBarV2ItemText** instance.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ToolBarV2ItemText-constructor(options: ToolBarV2ItemTextOptions)--><!--Device-ToolBarV2ItemText-constructor(options: ToolBarV2ItemTextOptions)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [ToolBarV2ItemTextOptions](../../apis-arkui/arkts-apis/arkts-arkui-arkuiadvancedtoolbarv2-toolbarv2itemtextoptions-i.md) | Yes | text info. |

## activatedColor

```TypeScript
@Trace
  public activatedColor?: ColorMetrics
```

Font color of the toolbar item in the activated state.

&lt;/div&gt;Default value: **\$r('sys.color.font_emphasize')**.

Decorator: @Trace

**Type:** [ColorMetrics](arkts-graphics-colormetrics-c.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ToolBarV2ItemText-@Trace  public activatedColor?: ColorMetrics--><!--Device-ToolBarV2ItemText-@Trace  public activatedColor?: ColorMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## color

```TypeScript
@Trace
  public color?: ColorMetrics
```

Font color of the toolbar item.

Default value: **\$r('sys.color.font_primary')**.

Decorator: @Trace

**Type:** [ColorMetrics](arkts-graphics-colormetrics-c.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ToolBarV2ItemText-@Trace  public color?: ColorMetrics--><!--Device-ToolBarV2ItemText-@Trace  public color?: ColorMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## text

```TypeScript
@Trace
  public text: ResourceStr
```

Text of the toolbar item.

Decorator: @Trace

**Type:** ResourceStr

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ToolBarV2ItemText-@Trace  public text: ResourceStr--><!--Device-ToolBarV2ItemText-@Trace  public text: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

