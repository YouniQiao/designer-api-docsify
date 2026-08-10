# ContextMenu

在页面范围内关闭通过  
[bindContextMenu](arkts-arkui-common-commonmethod-i.md#bindcontextmenu)属性绑定的菜单。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

<!--Device-unnamed-declare class ContextMenu--><!--Device-unnamed-declare class ContextMenu-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## close

```TypeScript
static close()
```

在页面范围内关闭通过  
[bindContextMenu](arkts-arkui-common-commonmethod-i.md#bindcontextmenu)绑定的菜单。常用于页面跳转、拖拽开始等需要主动关闭已显示菜单的交互场景。

> **说明：**
> 
> 从API version 18开始废弃，建议使用[UIContext](arkts-arkui-uicontext.md)中的
> [getContextMenuController](arkts-arkui-arkui-uicontext-uicontext-c.md#getcontextmenucontroller)获取
> [ContextMenuController](arkts-arkui-uicontext.md)实例，再通过此实例调用替代方法
> [close](arkts-arkui-arkui-uicontext-contextmenucontroller-c.md#close)。
> 
> 从API version 12开始，可以通过使用[UIContext](arkts-arkui-uicontext.md)中的
> [getContextMenuController](arkts-arkui-arkui-uicontext-uicontext-c.md#getcontextmenucontroller)来明确UI的执行上下文。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 18

**Substitutes:** ohos.arkui.UIContext.ContextMenuController#close

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ContextMenu-static close()--><!--Device-ContextMenu-static close()-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

