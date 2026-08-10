# RemoteWindow (System API)

## RemoteWindow

```TypeScript
export declare function RemoteWindow(
    target: WindowAnimationTarget
): RemoteWindowAttribute
```

远程控制窗口组件，可以通过此组件控制应用窗口，提供启动退出过程中控件动画和应用窗口联动动画的能力。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function RemoteWindow(    target: WindowAnimationTarget): RemoteWindowAttribute--><!--Device-unnamed-export declare function RemoteWindow(    target: WindowAnimationTarget): RemoteWindowAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| target | [WindowAnimationTarget](arkts-arkui-remotewindow-windowanimationtarget-i-sys.md) | Yes | 需要控制的动画窗口的描述。 |

**Return value:**

| Type | Description |
| --- | --- |
| [RemoteWindowAttribute](../arkts-components/arkts-arkui-remotewindow-attribute.md) |  |

