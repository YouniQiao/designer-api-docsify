# @ohos.arkui.advanced.Dialog(Dialog)

弹出框是一种模态窗口，用于临时展示用户需关注的信息或待处理的操作，同时保持当前上下文环境。用户必须完成交互才能退出该模式。
 > **说明：**
 >
 > - 该组件仅可在Stage模型下使用。
 >
 > - 如果Dialog设置[通用属性](../../apis-arkui/arkts-components/arkts-arkui-common-attribute.md)和[通用事件](../../apis-arkui/arkts-components/arkts-arkui-common-attribute.md)，编译工具链会额外生
 > 成节点__Common__，并将通用属性或通用事件挂载在__Common__上，而不是直接应用到Dialog本身。这可能导致开发者设置的通用属性或通用事件不生效或不符合预期，因此，不建议Dialog设置通用属性和通用事件。
 ###### 子组件
 无
 ###### DialogAttribute
 不支持[通用事件](../../apis-arkui/arkts-components/arkts-arkui-common-attribute.md)。


## 导入模块

```TypeScript
import { AlertDialog, SelectDialog, ButtonOptions, PopoverOptions, TipsDialog, PopoverDialog, LoadingDialog, CustomContentDialog, ConfirmDialog } from 'kits/@kit.ArkUI';
```

## 汇总

