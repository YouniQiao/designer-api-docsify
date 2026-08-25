# TabContentAttribute

Define the TabContentAttribute.

**Inheritance/Implementation:** TabContentAttribute extends CommonMethod

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
attributeModifier(modifier: AttributeModifier<TabContentAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

Set the attribute modifier for TabContent.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[TabContentAttribute](arkts-arkui-tabcontent-tabcontentattribute-i.md)&gt; \| [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TabContentAttribute](arkts-arkui-tabcontent-tabcontentattribute-i.md) |

## onWillHide

```TypeScript
onWillHide(event: VoidCallback | undefined): this
```

Called when the tab content is about to be hidden. The scenarios include the tab switching, page switching, and window switching between the foreground and background.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | [VoidCallback](arkts-arkui-voidcallback-t.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TabContentAttribute](arkts-arkui-tabcontent-tabcontentattribute-i.md) |

## onWillShow

```TypeScript
onWillShow(event: VoidCallback | undefined): this
```

Called when the tab content is about to be displayed. The scenarios include the first-time display, tab switching, page switching, and window switching between the foreground and background.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | [VoidCallback](arkts-arkui-voidcallback-t.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TabContentAttribute](arkts-arkui-tabcontent-tabcontentattribute-i.md) |

## setTabContentOptions

```TypeScript
default setTabContentOptions(): this
```

Set tabContent options.

**Since:** 26.1.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TabContentAttribute](arkts-arkui-tabcontent-tabcontentattribute-i.md) |

## tabBar

```TypeScript
tabBar(content: ComponentContentBase | SubTabBarStyle | BottomTabBarStyle | string | Resource | CustomBuilder | TabBarOptions | undefined): this
```

Sets the content displayed on the tab bar. Anonymous Object Rectification<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>If BottomTabBarStyle or TabBarOptions is used and an icon is set, a gray block will be displayed if the icon is invalid. <br>If the content exceeds the space provided by the tab bar, it will be clipped. </p>

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| content | [ComponentContentBase](arkts-arkui-componentcontent-componentcontentbase-c.md) \| [SubTabBarStyle](arkts-arkui-tabcontent-subtabbarstyle-c.md) \| [BottomTabBarStyle](arkts-arkui-tabcontent-bottomtabbarstyle-c.md) \| string \| [Resource](arkts-arkui-resource-t.md) \| [CustomBuilder](arkts-arkui-custombuilder-t.md) \| [TabBarOptions](arkts-arkui-tabcontent-tabbaroptions-i.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TabContentAttribute](arkts-arkui-tabcontent-tabcontentattribute-i.md) |
