# ToolBarModifier

Provides APIs for setting the height (**height**), background color (**backgroundColor**), left and right padding ( **padding**, which only takes effect when there are fewer than five items) of the toolbar, and whether to display the pressed state effect (**stateEffect**).

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare class ToolBarModifier--><!--Device-unnamed-export declare class ToolBarModifier-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## backgroundColor

```TypeScript
public backgroundColor(backgroundColor: ResourceColor): ToolBarModifier
```

Sets the background color of the toolbar. By overriding this API, you can implement custom drawing for the background color of the toolbar.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ToolBarModifier-public backgroundColor(backgroundColor: ResourceColor): ToolBarModifier--><!--Device-ToolBarModifier-public backgroundColor(backgroundColor: ResourceColor): ToolBarModifier-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| backgroundColor | ResourceColor | Yes | Toolbar background color <br>Default value: **\\$r('sys.color.ohos_id_color_toolbar_bg') |

**Return value:**

| Type | Description |
| --- | --- |
| [ToolBarModifier](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-toolbar-toolbarmodifier-c.md) | ToolBarModifier** object after the background color is set. |

## height

```TypeScript
public height(height: LengthMetrics): ToolBarModifier
```

Sets the height of the toolbar. By overriding this API, you can implement custom drawing for the height of the toolbar, which does not include the height of the divider.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ToolBarModifier-public height(height: LengthMetrics): ToolBarModifier--><!--Device-ToolBarModifier-public height(height: LengthMetrics): ToolBarModifier-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| height | LengthMetrics | Yes | Height of the toolbar. <br>The default height of the toolbar is 56 vp, which does not include the divider. |

**Return value:**

| Type | Description |
| --- | --- |
| [ToolBarModifier](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-toolbar-toolbarmodifier-c.md) | ToolBarModifier** object after the height is set. |

## padding

```TypeScript
public padding(padding: LengthMetrics): ToolBarModifier
```

Sets the left and right padding of the toolbar. By overriding this API, you can implement custom drawing for the left and right padding of the toolbar.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ToolBarModifier-public padding(padding: LengthMetrics): ToolBarModifier--><!--Device-ToolBarModifier-public padding(padding: LengthMetrics): ToolBarModifier-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| padding | LengthMetrics | Yes | Left and right padding of the toolbar, which is effective only when there are fewer than five items. <br>By default, the padding is 24 vp when there are fewer than five items and 0 when there are five or more items. |

**Return value:**

| Type | Description |
| --- | --- |
| [ToolBarModifier](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-toolbar-toolbarmodifier-c.md) | ToolBarModifier** object after the padding is set. |

## stateEffect

```TypeScript
public stateEffect(stateEffect: boolean): ToolBarModifier
```

Sets whether to display the pressed state effect.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ToolBarModifier-public stateEffect(stateEffect: boolean): ToolBarModifier--><!--Device-ToolBarModifier-public stateEffect(stateEffect: boolean): ToolBarModifier-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| stateEffect | boolean | Yes | Whether to display the pressed state effect on the toolbar. <br>The value **true** means to display the pressed state effect on the toolbar, and **false** means the opposite. <br>Default value: **true |

**Return value:**

| Type | Description |
| --- | --- |
| [ToolBarModifier](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-toolbar-toolbarmodifier-c.md) | ToolBarModifier** object after the pressed state effect is set. |

