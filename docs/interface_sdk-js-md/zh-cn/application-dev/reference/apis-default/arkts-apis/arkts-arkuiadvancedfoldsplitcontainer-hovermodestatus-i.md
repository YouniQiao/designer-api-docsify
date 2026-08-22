# HoverModeStatus

设备或应用的折叠、旋转、窗口状态信息。

@interface HoverModeStatus

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-unnamed-export interface HoverModeStatus--><!--Device-unnamed-export interface HoverModeStatus-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
```

## appRotation

```TypeScript
appRotation: double
```

应用旋转角度。

**类型：** double

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-HoverModeStatus-appRotation: double--><!--Device-HoverModeStatus-appRotation: double-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## foldStatus

```TypeScript
foldStatus: display.FoldStatus
```

设备的折叠状态。

**类型：** display.FoldStatus

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-HoverModeStatus-foldStatus: display.FoldStatus--><!--Device-HoverModeStatus-foldStatus: display.FoldStatus-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## isHoverMode

```TypeScript
isHoverMode: boolean
```

app当前是否处于悬停态。设置为true时表示当前为悬停态， 设置为false时表示当前为非悬停态。

**类型：** boolean

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-HoverModeStatus-isHoverMode: boolean--><!--Device-HoverModeStatus-isHoverMode: boolean-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## windowStatusType

```TypeScript
windowStatusType: window.WindowStatusType
```

窗口模式。

**类型：** window.WindowStatusType

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-HoverModeStatus-windowStatusType: window.WindowStatusType--><!--Device-HoverModeStatus-windowStatusType: window.WindowStatusType-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

