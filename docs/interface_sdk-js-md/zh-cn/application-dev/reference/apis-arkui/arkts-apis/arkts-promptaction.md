# @ohos.promptAction

创建并显示即时反馈、对话框和操作菜单，适用于系统通知、交互确认、菜单选择等场景。

> **说明：**

> - 本模块不支持在[UIAbility](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-uiability-uiability-c.md)的文件声明处使用，即不能在UIAbility的生命周期中调用，需要在 创建组件实例后使用。&gt;
> - 本模块功能依赖UI的执行上下文，不可在[UI上下文不明确](../../../ui/arkts-global-interface.md#ui上下文不明确)的地方使用，参见
> [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md)说明。建议<!--Del-->在除
> [ServiceExtensionAbility](../../../application-models/serviceextensionability-sys.md)等无UI界面的场景外，均<!--DelEnd-->使用
> UIContext中的弹窗方法。

## 导入模块

```TypeScript
import { promptAction, LevelMode, ImmersiveMode, LevelOrder } from 'kits/@kit.ArkUI';
```

## 汇总

### 命名空间

| 名称 |
| --- |
| [promptAction](arkts-arkui-promptaction-n.md) |

### 类

| 名称 |
| --- |
| [LevelOrder](arkts-arkui-promptaction-levelorder-c.md) |

### 接口

| 名称 |
| --- |
| [DismissDialogAction](arkts-arkui-promptaction-dismissdialogaction-i.md) |

### 枚举

| 名称 |
| --- |
| [ImmersiveMode](arkts-arkui-promptaction-immersivemode-e.md) |
| [LevelMode](arkts-arkui-promptaction-levelmode-e.md) |
