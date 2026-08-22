# ToolBarV2ItemImage

Defines the icon content of a toolbar item.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-unnamed-export declare class ToolBarV2ItemImage--><!--Device-unnamed-export declare class ToolBarV2ItemImage-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## constructor

```TypeScript
constructor(options: ToolBarV2ItemImageOptions)
```

A constructor used to create a **ToolBarV2ItemImage** instance.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ToolBarV2ItemImage-constructor(options: ToolBarV2ItemImageOptions)--><!--Device-ToolBarV2ItemImage-constructor(options: ToolBarV2ItemImageOptions)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [ToolBarV2ItemImageOptions](../../apis-arkui/arkts-apis/arkts-arkui-arkuiadvancedtoolbarv2-toolbarv2itemimageoptions-i.md) | Yes | text info. |

## activatedColor

```TypeScript
@Trace
  public activatedColor?: ColorMetrics
```

Color of the icon when the toolbar item is activated.

Default value: **\$r('sys.color.icon_emphasize')**.

Decorator: @Trace

**Type:** [ColorMetrics](arkts-graphics-colormetrics-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ToolBarV2ItemImage-@Trace  public activatedColor?: ColorMetrics--><!--Device-ToolBarV2ItemImage-@Trace  public activatedColor?: ColorMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## color

```TypeScript
@Trace
  public color?: ColorMetrics
```

Color of the icon.

Default value: **\$r('sys.color.icon_primary')**.

Decorator: @Trace

**Type:** [ColorMetrics](arkts-graphics-colormetrics-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ToolBarV2ItemImage-@Trace  public color?: ColorMetrics--><!--Device-ToolBarV2ItemImage-@Trace  public color?: ColorMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## src

```TypeScript
@Trace
  public src: ResourceStr
```

Icon of the toolbar item.

Decorator: @Trace

**Type:** ResourceStr

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ToolBarV2ItemImage-@Trace  public src: ResourceStr--><!--Device-ToolBarV2ItemImage-@Trace  public src: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

