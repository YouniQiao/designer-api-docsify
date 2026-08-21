# promptAction

创建并显示即时反馈、对话框和操作菜单。

> **说明：**
> 
> - 本模块同时支持ArkTS-Dyn、ArkTS-Sta。
> 
> - 本模块不支持在[UIAbility](../../apis-ability-kit/arkts-apis/arkts-ability-appabilityuiability-uiability-c.md)的文件声明处使用，即不能在UIAbility的生命周期中调用，需要在创建组件实例后使用。
> 
> - 本模块功能依赖UI的执行上下文，不可在[UI上下文不明确](../../../ui/arkts-global-interface.md#ui上下文不明确)的地方使用，参见
> [UIContext](arkts-arkuiuicontext-uicontext-c.md)说明。建议<!--Del-->在除
> [ServiceExtensionAbility](../../../application-models/serviceextensionability-sys.md)等无UI界面的场景外，均<!--DelEnd-->使用
> UIContext中的弹窗方法。

@namespace promptAction

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-declare namespace promptAction--><!--Device-unnamed-declare namespace promptAction-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
```

## 汇总

### 函数

| 名称 | 说明 |
| --- | --- |
| [openToast](arkts-promptaction-opentoast-f.md) | 显示即时反馈并通过Promise返回其id。 |
| [closeToast](arkts-promptaction-closetoast-f.md) | 关闭即时反馈。 |

### 类

| 名称 | 说明 |
| --- | --- |
| [CommonController](arkts-promptaction-commoncontroller-c.md) | 公共控制器，可以控制promptAction相关组件。 |
| [DialogController](arkts-promptaction-dialogcontroller-c.md) | 自定义弹窗控制器，继承自CommonController。 |

### 接口

| 名称 | 说明 |
| --- | --- |
| [ShowToastOptions](arkts-promptaction-showtoastoptions-i.md) | Toast的选项。 |
| [Button](arkts-promptaction-button-i.md) | 菜单中的菜单项按钮。 |
| [ShowDialogSuccessResponse](arkts-promptaction-showdialogsuccessresponse-i.md) | 对话框的响应结果。 |
| [ShowDialogOptions](arkts-promptaction-showdialogoptions-i.md) | 对话框的选项。 |
| [BaseDialogOptions](arkts-promptaction-basedialogoptions-i.md) | 弹窗的选项。 |
| [CustomDialogOptions](arkts-promptaction-customdialogoptions-i.md) | 自定义弹窗的内容，继承自BaseDialogOptions。 |
| [DialogOptions](arkts-promptaction-dialogoptions-i.md) | 自定义弹窗的内容，继承自BaseDialogOptions。 |
| [ActionMenuSuccessResponse](arkts-promptaction-actionmenusuccessresponse-i.md) | 操作菜单的响应结果。 |
| [ActionMenuOptions](arkts-promptaction-actionmenuoptions-i.md) | 操作菜单的选项。 |

<!--Del-->
### 接口（系统接口）

| 名称 | 说明 |
| --- | --- |
| [ShowDialogOptions](arkts-promptaction-showdialogoptions-i-sys.md) | 对话框的选项。 |
| [BaseDialogOptions](arkts-promptaction-basedialogoptions-i-sys.md) | 弹窗的选项。 |
| [ActionMenuOptions](arkts-promptaction-actionmenuoptions-i-sys.md) | 操作菜单的选项。 |
<!--DelEnd-->

### 枚举

| 名称 | 说明 |
| --- | --- |
| [ToastShowMode](arkts-promptaction-toastshowmode-e.md) | 设置Toast的显示模式，默认显示在应用内，支持显示在子窗。 |
| [CommonState](arkts-promptaction-commonstate-e.md) | 自定义弹窗的状态。 |

<!--Del-->
### 枚举（系统接口）

| 名称 | 说明 |
| --- | --- |
| [ToastShowMode](arkts-promptaction-toastshowmode-e-sys.md) | 设置Toast的显示模式，默认显示在应用内，支持显示在子窗。 |
<!--DelEnd-->

### 类型

| 名称 | 说明 |
| --- | --- |
| [PromptActionSingleButton](arkts-promptaction-promptactionsinglebutton-t.md) | 菜单中的菜单项按钮，仅支持1个按钮。 |
| [PromptActionDoubleButtons](arkts-promptaction-promptactiondoublebuttons-t.md) | 菜单中的菜单项按钮，仅支持2个按钮。 |
| [PromptActionTripleButtons](arkts-promptaction-promptactiontriplebuttons-t.md) | 菜单中的菜单项按钮，仅支持3个按钮。 |
| [PromptActionQuadrupleButtons](arkts-promptaction-promptactionquadruplebuttons-t.md) | 菜单中的菜单项按钮，仅支持4个按钮。 |
| [PromptActionQuintupleButtons](arkts-promptaction-promptactionquintuplebuttons-t.md) | 菜单中的菜单项按钮，仅支持5个按钮。 |
| [PromptActionSextupleButtons](arkts-promptaction-promptactionsextuplebuttons-t.md) | 菜单中的菜单项按钮，仅支持6个按钮。 |
| [DialogOptionsCornerRadius](arkts-promptaction-dialogoptionscornerradius-t.md) | 表示弹窗背板的圆角半径允许的数据字段类型。 |
| [DialogOptionsBorderWidth](arkts-promptaction-dialogoptionsborderwidth-t.md) | 表示弹窗背板的边框宽度允许的数据字段类型。 |
| [DialogOptionsBorderColor](arkts-promptaction-dialogoptionsbordercolor-t.md) | 表示弹窗背板的边框颜色允许的数据字段类型。 |
| [DialogOptionsBorderStyle](arkts-promptaction-dialogoptionsborderstyle-t.md) | 表示弹窗背板的边框样式允许的数据字段类型。 |
| [DialogOptionsShadow](arkts-promptaction-dialogoptionsshadow-t.md) | 表示弹窗背板的阴影允许的数据字段类型。 |

