# LoadingDialogV2

进度加载类弹出框，操作正在执行时的提示信息。

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-unnamed-export declare struct LoadingDialogV2--><!--Device-unnamed-export declare struct LoadingDialogV2-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
```

## build

```TypeScript
@Builder
  build(): void
```

The method to build component.

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-LoadingDialogV2-@Builder  build(): void--><!--Device-LoadingDialogV2-@Builder  build(): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## content

```TypeScript
@Param
  content?: ResourceStr
```

加载弹出框内容。

默认为空。

**说明：** 内容超过十行会显示“...”。

**类型：** ResourceStr

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-LoadingDialogV2-@Param  content?: ResourceStr--><!--Device-LoadingDialogV2-@Param  content?: ResourceStr-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

