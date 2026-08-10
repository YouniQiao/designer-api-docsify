# EditMenuOptions

EditMenuOptions

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface EditMenuOptions--><!--Device-unnamed-export declare interface EditMenuOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onPrepareMenu

```TypeScript
onPrepareMenu?: OnPrepareMenuCallback
```

当文本选择区域变化后显示菜单之前触发该回调，可在该回调中进行菜单数据设置。与onCreateMenu功能相似但触发时机不同：onCreateMenu在菜单创建时触发，适用于初始化菜单项；本接口在每次选择区域变化后、菜单显示前触发，适用于根据选择内容动态调整菜单。两者可同时使用。

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EditMenuOptions-onPrepareMenu?: OnPrepareMenuCallback--><!--Device-EditMenuOptions-onPrepareMenu?: OnPrepareMenuCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onCreateMenu

```TypeScript
onCreateMenu: OnCreateMenuCallback | undefined
```

在菜单创建时触发该回调，可在该回调中进行菜单数据设置。

**Type:** [OnCreateMenuCallback](arkts-arkui-oncreatemenucallback-t.md) \| undefined

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EditMenuOptions-onCreateMenu: OnCreateMenuCallback | undefined--><!--Device-EditMenuOptions-onCreateMenu: OnCreateMenuCallback | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onMenuItemClick

```TypeScript
onMenuItemClick: OnMenuItemClickCallback | undefined
```

在菜单项被点击时触发该回调，用于处理菜单项的点击行为。

**Type:** [OnMenuItemClickCallback](arkts-arkui-onmenuitemclickcallback-t.md) \| undefined

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EditMenuOptions-onMenuItemClick: OnMenuItemClickCallback | undefined--><!--Device-EditMenuOptions-onMenuItemClick: OnMenuItemClickCallback | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

