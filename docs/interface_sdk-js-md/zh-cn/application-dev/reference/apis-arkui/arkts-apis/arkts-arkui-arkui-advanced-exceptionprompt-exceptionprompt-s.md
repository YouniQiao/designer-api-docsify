# ExceptionPrompt

```TypeScript
export declare struct ExceptionPrompt
```

异常提示，适用于有异常需要提示异常内容的情况。

**起始版本：** 11

**装饰器类型：** @Component

<!--Device-unnamed-export declare struct ExceptionPrompt--><!--Device-unnamed-export declare struct ExceptionPrompt-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
import { MarginType, PromptOptions, ExceptionPrompt } from '@kit.ArkUI';
```

## build

```TypeScript
build(): void
```

build函数是一个成员函数，必须返回一个ArkTS组件类型（Element），用于表示将要渲染为用户界面的组件。

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务中使用。

<!--Device-ExceptionPrompt-build(): void--><!--Device-ExceptionPrompt-build(): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## onActionTextClick

```TypeScript
onActionTextClick?: () => void
```

点击右侧图标按钮的回调函数。缺省时不执行任何操作。

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务中使用。

<!--Device-ExceptionPrompt-onActionTextClick?: () => void--><!--Device-ExceptionPrompt-onActionTextClick?: () => void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## onTipClick

```TypeScript
onTipClick?: () => void
```

点击左侧提示文本的回调函数，缺省时不执行任何操作。

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务中使用。

<!--Device-ExceptionPrompt-onTipClick?: () => void--><!--Device-ExceptionPrompt-onTipClick?: () => void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## options

```TypeScript
options: PromptOptions
```

指定当前异常提示的配置信息。

**类型：** [PromptOptions](arkts-arkui-arkui-advanced-exceptionprompt-promptoptions-i.md)

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务中使用。

<!--Device-ExceptionPrompt-options: PromptOptions--><!--Device-ExceptionPrompt-options: PromptOptions-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full
