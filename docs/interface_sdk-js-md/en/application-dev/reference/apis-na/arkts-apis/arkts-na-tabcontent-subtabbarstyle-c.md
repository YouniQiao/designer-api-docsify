# SubTabBarStyle

Define SubTabBarStyle, the style is text and underline.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare class SubTabBarStyle--><!--Device-unnamed-export declare class SubTabBarStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## board

```TypeScript
board(value: BoardStyle): SubTabBarStyle
```

Sets the background style (board style) of the selected subtab. &lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;: <br>It takes effect only in the horizontal layout. &lt;/p&gt;

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SubTabBarStyle-board(value: BoardStyle): SubTabBarStyle--><!--Device-SubTabBarStyle-board(value: BoardStyle): SubTabBarStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [BoardStyle](arkts-na-tabcontent-boardstyle-i.md) | Yes | background style object for the selected subtab. |

**Return value:**

| Type | Description |
| --- | --- |
| [SubTabBarStyle](arkts-na-tabcontent-subtabbarstyle-c.md) | the style of the sub tab bar |

## constructor

```TypeScript
constructor(content: ResourceStr | ComponentContentBase)
```

constructor.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SubTabBarStyle-constructor(content: ResourceStr | ComponentContentBase)--><!--Device-SubTabBarStyle-constructor(content: ResourceStr | ComponentContentBase)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| content | [ResourceStr](../../apis-arkui/arkts-apis/arkts-arkui-resourcestr-t.md) \| [ComponentContentBase](arkts-na-componentcontent-componentcontentbase-c.md) | Yes | indicates the content of the sub tab bar |

## id

```TypeScript
id(value: string): SubTabBarStyle
```

Set an id to the sub tab bar to identify it

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SubTabBarStyle-id(value: string): SubTabBarStyle--><!--Device-SubTabBarStyle-id(value: string): SubTabBarStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | string | Yes | id of the sub tab bar to identify it |

**Return value:**

| Type | Description |
| --- | --- |
| [SubTabBarStyle](arkts-na-tabcontent-subtabbarstyle-c.md) | the style of the sub tab bar |

## indicator

```TypeScript
indicator(style: SubTabBarIndicatorStyle): SubTabBarStyle
```

Set the style of the indicator when selected

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SubTabBarStyle-indicator(style: SubTabBarIndicatorStyle): SubTabBarStyle--><!--Device-SubTabBarStyle-indicator(style: SubTabBarIndicatorStyle): SubTabBarStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | [SubTabBarIndicatorStyle](arkts-na-tabcontent-subtabbarindicatorstyle-i.md) | Yes | indicates the indicator style of the sub tab bar |

**Return value:**

| Type | Description |
| --- | --- |
| [SubTabBarStyle](arkts-na-tabcontent-subtabbarstyle-c.md) | the style of the sub tab bar |

## indicator

```TypeScript
indicator(value: SubTabBarIndicatorStyle | DrawableTabBarIndicator): SubTabBarStyle
```

Sets the indicator style of the selected subtab. Use DrawableTabBarIndicator to set image for the indicator.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SubTabBarStyle-indicator(value: SubTabBarIndicatorStyle | DrawableTabBarIndicator): SubTabBarStyle--><!--Device-SubTabBarStyle-indicator(value: SubTabBarIndicatorStyle | DrawableTabBarIndicator): SubTabBarStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [SubTabBarIndicatorStyle](arkts-na-tabcontent-subtabbarindicatorstyle-i.md) \| [DrawableTabBarIndicator](arkts-na-tabcontent-drawabletabbarindicator-i.md) | Yes | indicator style object for the selected subtab. |

**Return value:**

| Type | Description |
| --- | --- |
| [SubTabBarStyle](arkts-na-tabcontent-subtabbarstyle-c.md) | the style of the sub tab bar |

## labelStyle

```TypeScript
labelStyle(style: TabBarLabelStyle): SubTabBarStyle
```

Set the label style of the sub tab bar

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SubTabBarStyle-labelStyle(style: TabBarLabelStyle): SubTabBarStyle--><!--Device-SubTabBarStyle-labelStyle(style: TabBarLabelStyle): SubTabBarStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | [TabBarLabelStyle](arkts-na-tabcontent-tabbarlabelstyle-i.md) | Yes | indicates the label style of the sub tab bar |

**Return value:**

| Type | Description |
| --- | --- |
| [SubTabBarStyle](arkts-na-tabcontent-subtabbarstyle-c.md) | the style of the sub tab bar |

## of

```TypeScript
static of(content: ResourceStr | ComponentContentBase): SubTabBarStyle
```

Static constructor used to create a SubTabBarStyle instance. You can set custom content with ComponentContentBase.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SubTabBarStyle-static of(content: ResourceStr | ComponentContentBase): SubTabBarStyle--><!--Device-SubTabBarStyle-static of(content: ResourceStr | ComponentContentBase): SubTabBarStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| content | [ResourceStr](../../apis-arkui/arkts-apis/arkts-arkui-resourcestr-t.md) \| [ComponentContentBase](arkts-na-componentcontent-componentcontentbase-c.md) | Yes | indicates the content of the sub tab bar |

**Return value:**

| Type | Description |
| --- | --- |
| [SubTabBarStyle](arkts-na-tabcontent-subtabbarstyle-c.md) | the style of the sub tab bar |

## padding

```TypeScript
padding(value: Padding | Dimension): SubTabBarStyle
```

Set the padding of the sub tab bar &lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;: <br>It cannot be set in percentage. <br>When the parameter is of the Dimension type, the value applies to all sides. &lt;/p&gt;

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SubTabBarStyle-padding(value: Padding | Dimension): SubTabBarStyle--><!--Device-SubTabBarStyle-padding(value: Padding | Dimension): SubTabBarStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [Padding](../../apis-arkui/arkts-apis/arkts-arkui-padding-t.md) \| [Dimension](../../apis-arkui/arkts-apis/arkts-arkui-dimension-t.md) | Yes | indicates the padding of the sub tab bar |

**Return value:**

| Type | Description |
| --- | --- |
| [SubTabBarStyle](arkts-na-tabcontent-subtabbarstyle-c.md) | the style of the sub tab bar |

## padding

```TypeScript
padding(padding: LocalizedPadding): SubTabBarStyle
```

Set the padding of the sub tab bar &lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;: <br>This API supports mirroring but does not support percentage-based settings. &lt;/p&gt;

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SubTabBarStyle-padding(padding: LocalizedPadding): SubTabBarStyle--><!--Device-SubTabBarStyle-padding(padding: LocalizedPadding): SubTabBarStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| padding | [LocalizedPadding](../../apis-arkui/arkts-apis/arkts-arkui-localizedpadding-i.md) | Yes | indicates the padding of the sub tab bar |

**Return value:**

| Type | Description |
| --- | --- |
| [SubTabBarStyle](arkts-na-tabcontent-subtabbarstyle-c.md) | the style of the sub tab bar |

## selectedMode

```TypeScript
selectedMode(value: SelectedMode): SubTabBarStyle
```

Sets the display mode of the selected subtab. &lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;: <br>It takes effect only in the horizontal layout. &lt;/p&gt;

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SubTabBarStyle-selectedMode(value: SelectedMode): SubTabBarStyle--><!--Device-SubTabBarStyle-selectedMode(value: SelectedMode): SubTabBarStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [SelectedMode](arkts-na-tabcontent-selectedmode-e.md) | Yes | display mode of the selected subtab. Default value is SelectedMode.INDICATOR. |

**Return value:**

| Type | Description |
| --- | --- |
| [SubTabBarStyle](arkts-na-tabcontent-subtabbarstyle-c.md) | the style of the sub tab bar |

