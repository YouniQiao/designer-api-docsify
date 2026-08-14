# BottomTabBarStyle

Define BottomTabBarStyle, the style is icon and text.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-export declare class BottomTabBarStyle--><!--Device-unnamed-export declare class BottomTabBarStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(icon: ResourceStr | TabBarSymbol, text: ResourceStr)
```

constructor.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-BottomTabBarStyle-constructor(icon: ResourceStr | TabBarSymbol, text: ResourceStr)--><!--Device-BottomTabBarStyle-constructor(icon: ResourceStr | TabBarSymbol, text: ResourceStr)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| icon | [ResourceStr](../../apis-arkui/arkts-apis/arkts-arkui-resourcestr-t.md) \| TabBarSymbol | Yes | indicates the icon of the bottom tab bar |
| text | [ResourceStr](../../apis-arkui/arkts-apis/arkts-arkui-resourcestr-t.md) | Yes | indicates the text of the bottom tab bar |

## iconStyle

```TypeScript
iconStyle(style: TabBarIconStyle): BottomTabBarStyle
```

Sets the style of the label icon on the bottom tab.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-BottomTabBarStyle-iconStyle(style: TabBarIconStyle): BottomTabBarStyle--><!--Device-BottomTabBarStyle-iconStyle(style: TabBarIconStyle): BottomTabBarStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | [TabBarIconStyle](arkts-na-tabcontent-tabbariconstyle-i.md) | Yes | style of the label icon on the bottom tab. |

**Return value:**

| Type | Description |
| --- | --- |
| [BottomTabBarStyle](arkts-na-tabcontent-bottomtabbarstyle-c.md) | the style of the bottom tab bar |

## id

```TypeScript
id(value: string): BottomTabBarStyle
```

Set an id to the bottom tab bar to identify it

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-BottomTabBarStyle-id(value: string): BottomTabBarStyle--><!--Device-BottomTabBarStyle-id(value: string): BottomTabBarStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | string | Yes | id of the bottom tab bar to identify it |

**Return value:**

| Type | Description |
| --- | --- |
| [BottomTabBarStyle](arkts-na-tabcontent-bottomtabbarstyle-c.md) | the style of the bottom tab bar |

## labelStyle

```TypeScript
labelStyle(style: TabBarLabelStyle): BottomTabBarStyle
```

Set the label style of the bottom tab bar

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-BottomTabBarStyle-labelStyle(style: TabBarLabelStyle): BottomTabBarStyle--><!--Device-BottomTabBarStyle-labelStyle(style: TabBarLabelStyle): BottomTabBarStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | [TabBarLabelStyle](arkts-na-tabcontent-tabbarlabelstyle-i.md) | Yes | indicates the label style of the bottom tab bar |

**Return value:**

| Type | Description |
| --- | --- |
| [BottomTabBarStyle](arkts-na-tabcontent-bottomtabbarstyle-c.md) | the style of the bottom tab bar |

## layoutMode

```TypeScript
layoutMode(value: LayoutMode): BottomTabBarStyle
```

Sets the layout mode of the images and texts on the bottom tab.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-BottomTabBarStyle-layoutMode(value: LayoutMode): BottomTabBarStyle--><!--Device-BottomTabBarStyle-layoutMode(value: LayoutMode): BottomTabBarStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [LayoutMode](arkts-na-tabcontent-layoutmode-e.md) | Yes | layout mode of the images and text on the bottom tab. Default value is LayoutMode.VERTICAL. |

**Return value:**

| Type | Description |
| --- | --- |
| [BottomTabBarStyle](arkts-na-tabcontent-bottomtabbarstyle-c.md) | the style of the bottom tab bar |

## of

```TypeScript
static of(icon: ResourceStr | TabBarSymbol, text: ResourceStr): BottomTabBarStyle
```

Static constructor used to create a BottomTabBarStyle instance.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-BottomTabBarStyle-static of(icon: ResourceStr | TabBarSymbol, text: ResourceStr): BottomTabBarStyle--><!--Device-BottomTabBarStyle-static of(icon: ResourceStr | TabBarSymbol, text: ResourceStr): BottomTabBarStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| icon | [ResourceStr](../../apis-arkui/arkts-apis/arkts-arkui-resourcestr-t.md) \| TabBarSymbol | Yes | indicates the icon of the bottom tab bar |
| text | [ResourceStr](../../apis-arkui/arkts-apis/arkts-arkui-resourcestr-t.md) | Yes | indicates the text of the bottom tab bar |

**Return value:**

| Type | Description |
| --- | --- |
| [BottomTabBarStyle](arkts-na-tabcontent-bottomtabbarstyle-c.md) | the style of the bottom tab bar |

## padding

```TypeScript
padding(value: Padding | Dimension | LocalizedPadding): BottomTabBarStyle
```

Set the padding of the bottom tab bar &lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;: <br>It cannot be set in percentage. <br>When the parameter is of the Dimension type, the value applies to all sides. &lt;/p&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-BottomTabBarStyle-padding(value: Padding | Dimension | LocalizedPadding): BottomTabBarStyle--><!--Device-BottomTabBarStyle-padding(value: Padding | Dimension | LocalizedPadding): BottomTabBarStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [Padding](../../apis-arkui/arkts-apis/arkts-arkui-padding-t.md) \| [Dimension](../../apis-arkui/arkts-apis/arkts-arkui-dimension-t.md) \| [LocalizedPadding](../../apis-arkui/arkts-apis/arkts-arkui-localizedpadding-i.md) | Yes | indicates the padding of the bottom tab bar Default value is { left:4.0vp, right:4.0vp, top:0.0vp, bottom:0.0vp }. |

**Return value:**

| Type | Description |
| --- | --- |
| [BottomTabBarStyle](arkts-na-tabcontent-bottomtabbarstyle-c.md) | the style of the bottom tab bar |

## symmetricExtensible

```TypeScript
symmetricExtensible(value: boolean): BottomTabBarStyle
```

Sets whether the images and text on the bottom tab can be symmetrically extended by the minimum value of the available space on the left and right bottom tabs. &lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;: <br>This parameter is valid only between bottom tabs in fixed horizontal mode. &lt;/p&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-BottomTabBarStyle-symmetricExtensible(value: boolean): BottomTabBarStyle--><!--Device-BottomTabBarStyle-symmetricExtensible(value: boolean): BottomTabBarStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | boolean | Yes | indicates whether the bottom tab bar is extensible. Default value is false. |

**Return value:**

| Type | Description |
| --- | --- |
| [BottomTabBarStyle](arkts-na-tabcontent-bottomtabbarstyle-c.md) | the style of the bottom tab bar |

## verticalAlign

```TypeScript
verticalAlign(value: VerticalAlign): BottomTabBarStyle
```

Sets the vertical alignment mode of the images and text on the bottom tab.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-BottomTabBarStyle-verticalAlign(value: VerticalAlign): BottomTabBarStyle--><!--Device-BottomTabBarStyle-verticalAlign(value: VerticalAlign): BottomTabBarStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [VerticalAlign](../../apis-arkui/arkts-apis/arkts-arkui-verticalalign-e.md) | Yes | vertical alignment mode of the images and text on the bottom tab. Default value is VerticalAlign.Center. |

**Return value:**

| Type | Description |
| --- | --- |
| [BottomTabBarStyle](arkts-na-tabcontent-bottomtabbarstyle-c.md) | the style of the bottom tab bar |

