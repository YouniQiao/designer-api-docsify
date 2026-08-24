# ExceptionPrompt

异常提示，适用于有异常需要提示异常内容的情况。

> **说明：**&gt;
> - 该组件仅可在Stage模型下使用。&gt;
> - 如果ExceptionPrompt设置通用属性和通用事件，
> 编译工具链会额外生成节点__Common__，并将通用属性或通用事件挂载在__Common__上，而不是直接应用到ExceptionPrompt本身。这可能导致开发者设置的通用属性或通用事件不生效或不符合预期，因此，不建议
> ExceptionPrompt设置通用属性和通用事件。

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**装饰器类型：** @Component

<!--Device-unnamed-export declare struct ExceptionPrompt--><!--Device-unnamed-export declare struct ExceptionPrompt-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
```

## build

```TypeScript

```

The method to build component.

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**装饰器类型：** @Builder

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ExceptionPrompt-@Builder build(): void--><!--Device-ExceptionPrompt-@Builder build(): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## onActionTextClick

```TypeScript
onActionTextClick?: () => void
```

点击右侧图标按钮的回调函数。缺省时不执行任何操作。

**类型：** () =&gt; void

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ExceptionPrompt-onActionTextClick?: () => void--><!--Device-ExceptionPrompt-onActionTextClick?: () => void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## onTipClick

```TypeScript
onTipClick?: () => void
```

点击左侧提示文本的回调函数，缺省时不执行任何操作。

**类型：** () =&gt; void

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ExceptionPrompt-onTipClick?: () => void--><!--Device-ExceptionPrompt-onTipClick?: () => void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## options

指定当前异常提示的配置信息。

**类型：** [PromptOptions](arkts-arkui-advanced-exceptionprompt-promptoptions-i.md)

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**装饰器类型：** @PropRef

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ExceptionPrompt-@PropRef options: PromptOptions--><!--Device-ExceptionPrompt-@PropRef options: PromptOptions-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

