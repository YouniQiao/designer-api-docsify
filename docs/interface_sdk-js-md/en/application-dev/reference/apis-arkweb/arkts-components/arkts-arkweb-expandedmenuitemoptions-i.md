# ExpandedMenuItemOptions

> **说明：**
> 
> 从API version 12开始支持，从API version 20开始废弃，建议使用
> [editMenuOptions](../arkts-apis/arkts-arkweb-web-webattribute-i.md/arkts-arkweb-web-webattribute-i.md#editmenuoptions)替代。
> 自定义菜单扩展项。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** 20

**Substitutes:** [EditMenuOptions](../../apis-arkui/arkts-apis/arkts-arkui-textcommon-editmenuoptions-i.md/arkts-arkui-textcommon-editmenuoptions-i.md)

<!--Device-unnamed-declare interface ExpandedMenuItemOptions--><!--Device-unnamed-declare interface ExpandedMenuItemOptions-End-->

**System capability:** SystemCapability.Web.Webview.Core

## action

```TypeScript
action: (selectedText: {plainText: string}) => void
```

选中的文本信息。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** 20

**Substitutes:** [EditMenuOptions](../../apis-arkui/arkts-apis/arkts-arkui-textcommon-editmenuoptions-i.md/arkts-arkui-textcommon-editmenuoptions-i.md)

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ExpandedMenuItemOptions-action: (selectedText: {plainText: string}) => void--><!--Device-ExpandedMenuItemOptions-action: (selectedText: {plainText: string}) => void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| selectedText | {plainText: string} | Yes |  |

## content

```TypeScript
content: ResourceStr
```

显示内容。

**Type:** [ResourceStr](../../apis-arkui/arkts-apis/arkts-arkui-resourcestr-t.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** 20

**Substitutes:** [EditMenuOptions](../../apis-arkui/arkts-apis/arkts-arkui-textcommon-editmenuoptions-i.md/arkts-arkui-textcommon-editmenuoptions-i.md)

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ExpandedMenuItemOptions-content: ResourceStr--><!--Device-ExpandedMenuItemOptions-content: ResourceStr-End-->

**System capability:** SystemCapability.Web.Webview.Core

## startIcon

```TypeScript
startIcon?: ResourceStr
```

显示图标。默认值为空，不显示图标。

**Type:** [ResourceStr](../../apis-arkui/arkts-apis/arkts-arkui-resourcestr-t.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** 20

**Substitutes:** [EditMenuOptions](../../apis-arkui/arkts-apis/arkts-arkui-textcommon-editmenuoptions-i.md/arkts-arkui-textcommon-editmenuoptions-i.md)

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ExpandedMenuItemOptions-startIcon?: ResourceStr--><!--Device-ExpandedMenuItemOptions-startIcon?: ResourceStr-End-->

**System capability:** SystemCapability.Web.Webview.Core

