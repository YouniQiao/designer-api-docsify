# ToolbarItemStatus

工具栏单个选项的状态。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare enum ToolbarItemStatus--><!--Device-unnamed-export declare enum ToolbarItemStatus-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## NORMAL

```TypeScript
NORMAL = 0
```

设置工具栏单个选项为NORMAL态，该选项显示默认样式，可以触发Hover，Press，Focus事件并显示对应的多态样式。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ToolbarItemStatus-NORMAL = 0--><!--Device-ToolbarItemStatus-NORMAL = 0-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## DISABLED

```TypeScript
DISABLED = 1
```

设置工具栏单个选项为DISABLED态， 该选项显示DISABLED态样式，并且不可交互。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ToolbarItemStatus-DISABLED = 1--><!--Device-ToolbarItemStatus-DISABLED = 1-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## ACTIVE

```TypeScript
ACTIVE = 2
```

设置工具栏单个选项为ACTIVE态， 该选项通过点击事件可以将icon图标更新为activeIcon对应的图片资源。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ToolbarItemStatus-ACTIVE = 2--><!--Device-ToolbarItemStatus-ACTIVE = 2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

