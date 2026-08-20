# LoadingDialog

进度加载类弹出框，用于显示操作执行中的提示信息。

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

<!--Device-unnamed-export declare struct LoadingDialog--><!--Device-unnamed-export declare struct LoadingDialog-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
```

## build

```TypeScript
@Builder build(): void
```

The method to build component.

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-LoadingDialog-@Builder build(): void--><!--Device-LoadingDialog-@Builder build(): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## Controller

```TypeScript
Controller: CustomDialogController
```

加载弹出框控制器。

**说明：** 未使用@Require装饰，构造时不强制校验参数。

**类型：** CustomDialogController

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-LoadingDialog-Controller: CustomDialogController--><!--Device-LoadingDialog-Controller: CustomDialogController-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## content

```TypeScript
content?: ResourceStr
```

加载弹出框内容。

默认不设置或设置为undefined，加载弹出框内容不显示。

**类型：** ResourceStr

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-LoadingDialog-content?: ResourceStr--><!--Device-LoadingDialog-content?: ResourceStr-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## theme

```TypeScript
theme?: Theme | CustomTheme
```

主题信息，可以是CustomTheme或从onWillApplyTheme中获取的Theme实例。

**类型：** [Theme](arkts-arkui-theme-theme-i.md) \| [CustomTheme](arkts-arkui-theme-customtheme-i.md)

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-LoadingDialog-theme?: Theme | CustomTheme--><!--Device-LoadingDialog-theme?: Theme | CustomTheme-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## themeColorMode

```TypeScript
themeColorMode?: ThemeColorMode
```

自定义弹出框深浅色模式。

默认值：ThemeColorMode.SYSTEM

**类型：** ThemeColorMode

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-LoadingDialog-themeColorMode?: ThemeColorMode--><!--Device-LoadingDialog-themeColorMode?: ThemeColorMode-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

