# XComponentOptions

定义XComponent的具体配置参数。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface XComponentOptions--><!--Device-unnamed-export declare interface XComponentOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## screenId

```TypeScript
screenId?: long
```

给组件设置关联屏幕ID，通过此项可在组件上显示关联屏幕画面。屏幕ID可通过@ohos.screen模块的getAllScreens接口获取。

默认值：0，表示主屏幕。

**说明：**仅type为SURFACE时有效。

**Type:** long

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-XComponentOptions-screenId?: long--><!--Device-XComponentOptions-screenId?: long-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

