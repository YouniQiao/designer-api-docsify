# MenuOptions

配置弹出菜单的参数，继承自[ContextMenuOptions](arkts-arkui-contextmenuoptions-i.md)。

**Inheritance/Implementation:** MenuOptions extends [ContextMenuOptions](arkts-arkui-contextmenuoptions-i.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-unnamed-declare interface MenuOptions extends ContextMenuOptions--><!--Device-unnamed-declare interface MenuOptions extends ContextMenuOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## showInSubWindow

```TypeScript
showInSubWindow?: boolean
```

是否在子窗口显示菜单。

true：在子窗口显示菜单；false：不在子窗显示菜单。

默认值：2in1设备上为true，其他设备为false。

**说明：**

仅对2in1设备生效。

**Type:** boolean

**Default:** true for 2-in-1 devices [since 12]

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-MenuOptions-showInSubWindow?: boolean--><!--Device-MenuOptions-showInSubWindow?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## title

```TypeScript
title?: ResourceStr
```

菜单标题。

**说明：**

仅在content设置为Array&lt;[MenuElement](arkts-arkui-menuelement-i.md)&gt; 时生效。

**Type:** [ResourceStr](../arkts-apis/arkts-arkui-resourcestr-t.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-MenuOptions-title?: ResourceStr--><!--Device-MenuOptions-title?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

