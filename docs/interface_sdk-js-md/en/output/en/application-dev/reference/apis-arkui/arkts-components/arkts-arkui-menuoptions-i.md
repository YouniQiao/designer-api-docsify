# MenuOptions

Configues menu item information, which is inherited from [ContextMenuOptions]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_.

**Inheritance/Implementation:** MenuOptions extends [ContextMenuOptions](../../apis-na/arkts-apis/arkts-na-component/common-contextmenuoptions-i.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-unnamed-declare interface MenuOptions extends ContextMenuOptions--><!--Device-unnamed-declare interface MenuOptions extends ContextMenuOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## showInSubWindow

```TypeScript
showInSubWindow?: boolean
```

Whether to show the menu in a subwindow. **true**: yes; **false**: no Default value: **true** for 2-in-1 devices and **false** for other devices **NOTE** This parameter takes effect only for 2-in-1 devices.

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

Menu title. **NOTE** This parameter is effective only when **content** is set to Array&lt;[MenuElement]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_&gt;.

**Type:** ResourceStr

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-MenuOptions-title?: ResourceStr--><!--Device-MenuOptions-title?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

