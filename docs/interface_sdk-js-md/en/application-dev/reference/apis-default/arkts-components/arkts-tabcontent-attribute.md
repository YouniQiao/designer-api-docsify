# TabContentAttribute

Define the TabContentAttribute.

**Inheritance/Implementation:** TabContentAttribute extends CommonMethod

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-unnamed-export declare interface TabContentAttribute--><!--Device-unnamed-export declare interface TabContentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
attributeModifier(modifier: AttributeModifier<TabContentAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

Set the attribute modifier for TabContent.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TabContentAttribute-attributeModifier(modifier: AttributeModifier<TabContentAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-TabContentAttribute-attributeModifier(modifier: AttributeModifier<TabContentAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](../../apis-arkui/arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[TabContentAttribute](arkts-tabcontent-attribute.md)&gt; \| [AttributeModifier](../../apis-arkui/arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../../apis-arkui/arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| [TabContentAttribute](arkts-tabcontent-attribute.md) |  |

## onWillHide

```TypeScript
onWillHide(event: VoidCallback | undefined): this
```

Called when the tab content is about to be hidden. The scenarios include the tab switching, page switching, and window switching between the foreground and background.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TabContentAttribute-onWillHide(event: VoidCallback | undefined): this--><!--Device-TabContentAttribute-onWillHide(event: VoidCallback | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [VoidCallback](../../apis-arkui/arkts-apis/arkts-arkui-voidcallback-t.md) \| undefined | Yes | undefined means unbinding the callback. |

**Return value:**

| Type | Description |
| --- | --- |
| [TabContentAttribute](arkts-tabcontent-attribute.md) |  |

## onWillShow

```TypeScript
onWillShow(event: VoidCallback | undefined): this
```

Called when the tab content is about to be displayed. The scenarios include the first-time display, tab switching, page switching, and window switching between the foreground and background.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TabContentAttribute-onWillShow(event: VoidCallback | undefined): this--><!--Device-TabContentAttribute-onWillShow(event: VoidCallback | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [VoidCallback](../../apis-arkui/arkts-apis/arkts-arkui-voidcallback-t.md) \| undefined | Yes | undefined means unbinding the callback. |

**Return value:**

| Type | Description |
| --- | --- |
| [TabContentAttribute](arkts-tabcontent-attribute.md) |  |

## setTabContentOptions

```TypeScript
setTabContentOptions(): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-TabContentAttribute-setTabContentOptions(): this--><!--Device-TabContentAttribute-setTabContentOptions(): this-End-->

**Return value:**

| Type | Description |
| --- | --- |
## tabBar

```TypeScript
tabBar(content: ComponentContentBase | SubTabBarStyle | BottomTabBarStyle | string | Resource | CustomBuilder | TabBarOptions | undefined): this
```

Sets the content displayed on the tab bar. Anonymous Object Rectification

<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>If BottomTabBarStyle or TabBarOptions is used and an icon is set, a gray block will be displayed if the icon is invalid. <br>If the content exceeds the space provided by the tab bar, it will be clipped. </p>

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TabContentAttribute-tabBar(content: ComponentContentBase | SubTabBarStyle | BottomTabBarStyle | string | Resource | CustomBuilder | TabBarOptions | undefined): this--><!--Device-TabContentAttribute-tabBar(content: ComponentContentBase | SubTabBarStyle | BottomTabBarStyle | string | Resource | CustomBuilder | TabBarOptions | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| content | [ComponentContentBase](../arkts-apis/arkts-componentcontent-componentcontentbase-c.md) \| [SubTabBarStyle](arkts-tabcontent-subtabbarstyle-c.md) \| [BottomTabBarStyle](arkts-tabcontent-bottomtabbarstyle-c.md) \| string \| [Resource](../../apis-arkui/arkts-apis/arkts-arkui-resource-t.md) \| [CustomBuilder](../arkts-apis/arkts-custombuilder-t.md) \| [TabBarOptions](arkts-tabcontent-tabbaroptions-i.md) \| undefined | Yes | undefined means an empty tab bar. Content displayed on the tab bar. |

**Return value:**

| Type | Description |
| --- | --- |
| [TabContentAttribute](arkts-tabcontent-attribute.md) |  |

## default

```TypeScript
default
```

Set tabContent options.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TabContentAttribute-default--><!--Device-TabContentAttribute-default-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

