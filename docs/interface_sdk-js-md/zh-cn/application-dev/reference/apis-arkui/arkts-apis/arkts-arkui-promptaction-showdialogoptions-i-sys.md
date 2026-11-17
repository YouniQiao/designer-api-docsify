# ShowDialogOptions（系统接口）

```TypeScript
interface ShowDialogOptions
```

对话框的选项。

**起始版本：** 9

<!--Device-promptAction-interface ShowDialogOptions--><!--Device-promptAction-interface ShowDialogOptions-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
import { promptAction, LevelMode, ImmersiveMode, LevelOrder } from '@kit.ArkUI';
```

## distortionMode

```TypeScript
distortionMode?: DistortionMode
```

设置弹窗的扭曲动画模式。

**类型：** [DistortionMode](../arkts-components/arkts-arkui-common-comp-distortionmode-e-sys.md)

**默认值：** DistortionMode.DISTORTION_AUTO

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ShowDialogOptions-distortionMode?: DistortionMode--><!--Device-ShowDialogOptions-distortionMode?: DistortionMode-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

## edgeLightMode

```TypeScript
edgeLightMode?: EdgeLightMode
```

设置弹窗的流光动画模式。

**类型：** [EdgeLightMode](../arkts-components/arkts-arkui-common-comp-edgelightmode-e-sys.md)

**默认值：** EdgeLightMode.EDGELIGHT_AUTO

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ShowDialogOptions-edgeLightMode?: EdgeLightMode--><!--Device-ShowDialogOptions-edgeLightMode?: EdgeLightMode-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。
