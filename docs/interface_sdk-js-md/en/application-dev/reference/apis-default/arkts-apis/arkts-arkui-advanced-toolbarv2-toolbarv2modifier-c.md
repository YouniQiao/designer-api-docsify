# ToolBarV2Modifier

Provides APIs for setting the height (**height**), background color (**backgroundColor**), left and right padding ( **padding**, which only takes effect when there are fewer than five items) of the toolbar, and whether to display the pressed state effect (**stateEffect**).

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-unnamed-export declare class ToolBarV2Modifier--><!--Device-unnamed-export declare class ToolBarV2Modifier-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## backgroundColor

```TypeScript
public backgroundColor(backgroundColor: ColorMetrics): ToolBarV2Modifier
```

Sets the background color of the toolbar. By overriding this API, you can implement custom drawing for the background color of the toolbar.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-ToolBarV2Modifier-public backgroundColor(backgroundColor: ColorMetrics): ToolBarV2Modifier--><!--Device-ToolBarV2Modifier-public backgroundColor(backgroundColor: ColorMetrics): ToolBarV2Modifier-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| backgroundColor | [ColorMetrics](arkts-graphics-colormetrics-c.md) | Yes | toolBarV2's backgroundColor. |

**Return value:**

| Type | Description |
| --- | --- |
| [ToolBarV2Modifier](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-toolbarv2-toolbarv2modifier-c.md) | ToolBarV2Modifier** object after the background color is set. |

## height

```TypeScript
public height(height: LengthMetrics): ToolBarV2Modifier
```

Sets the height of the toolbar. By overriding this API, you can implement custom drawing for the height of the toolbar, which does not include the height of the divider.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ToolBarV2Modifier-public height(height: LengthMetrics): ToolBarV2Modifier--><!--Device-ToolBarV2Modifier-public height(height: LengthMetrics): ToolBarV2Modifier-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| height | [LengthMetrics](arkts-graphics-lengthmetrics-c.md) | Yes | toolBarV2's height. |

**Return value:**

| Type | Description |
| --- | --- |
| [ToolBarV2Modifier](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-toolbarv2-toolbarv2modifier-c.md) | ToolBarV2Modifier** object after the height is set. |

## padding

```TypeScript
public padding(padding: LengthMetrics): ToolBarV2Modifier
```

Sets the left and right padding of the toolbar. By overriding this API, you can implement custom drawing for the left and right padding of the toolbar.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ToolBarV2Modifier-public padding(padding: LengthMetrics): ToolBarV2Modifier--><!--Device-ToolBarV2Modifier-public padding(padding: LengthMetrics): ToolBarV2Modifier-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| padding | [LengthMetrics](arkts-graphics-lengthmetrics-c.md) | Yes | left and right padding. |

**Return value:**

| Type | Description |
| --- | --- |
| [ToolBarV2Modifier](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-toolbarv2-toolbarv2modifier-c.md) | ToolBarV2Modifier** object after the padding is set. |

## stateEffect

```TypeScript
public stateEffect(stateEffect: boolean): ToolBarV2Modifier
```

Sets whether to display the pressed state effect.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ToolBarV2Modifier-public stateEffect(stateEffect: boolean): ToolBarV2Modifier--><!--Device-ToolBarV2Modifier-public stateEffect(stateEffect: boolean): ToolBarV2Modifier-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| stateEffect | boolean | Yes | press status effect. |

**Return value:**

| Type | Description |
| --- | --- |
| [ToolBarV2Modifier](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-toolbarv2-toolbarv2modifier-c.md) | ToolBarV2Modifier** object after the pressed state effect is set. |

