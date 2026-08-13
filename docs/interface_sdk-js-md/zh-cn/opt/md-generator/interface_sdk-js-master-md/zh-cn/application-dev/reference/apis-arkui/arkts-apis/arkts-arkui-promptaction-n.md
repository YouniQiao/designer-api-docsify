# promptAction

创建并显示即时反馈、对话框和操作菜单，适用于系统通知、交互确认、菜单选择等场景。 > **说明：** > - 本模块不支持在[UIAbility](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-uiability-uiability-c.md#UIAbility)的文件声明处使用，即不能在UIAbility的生命周期中调用，需要在 创建组件实例后使用。 > > - 本模块功能依赖UI的执行上下文，不可在[UI上下文不明确](../../../ui/arkts-global-interface.md#ui上下文不明确)的地方使用，参见 > [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md#UIContext)说明。建议&lt;!--Del--&gt;在除 > [ServiceExtensionAbility](../../../application-models/serviceextensionability-sys.md)等无UI界面的场景外，均&lt;!--DelEnd--&gt;使用 > UIContext中的弹窗方法。

**起始版本：** 9

**废弃版本：** -1

<!--Device-unnamed-declare namespace promptAction--><!--Device-unnamed-declare namespace promptAction-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 汇总

### 函数

| 名称 |
| --- |
| [showToast](arkts-arkui-promptaction-showtoast-f.md#showToast) |
| [openToast](arkts-arkui-promptaction-opentoast-f.md#openToast) |
| [closeToast](arkts-arkui-promptaction-closetoast-f.md#closeToast) |
| [showDialog](arkts-arkui-promptaction-showdialog-f.md#showDialog) |
| [showDialog](arkts-arkui-promptaction-showdialog-f.md#showDialog) |
| [openCustomDialog](arkts-arkui-promptaction-opencustomdialog-f.md#openCustomDialog) |
| [closeCustomDialog](arkts-arkui-promptaction-closecustomdialog-f.md#closeCustomDialog) |
| [showActionMenu](arkts-arkui-promptaction-showactionmenu-f.md#showActionMenu) |
| [showActionMenu](arkts-arkui-promptaction-showactionmenu-f.md#showActionMenu) |

### 类

| 名称 |
| --- |
| [CommonController](arkts-arkui-promptaction-commoncontroller-c.md) |
| [DialogController](arkts-arkui-promptaction-dialogcontroller-c.md) |

### 接口

| 名称 |
| --- |
| [ShowToastOptions](arkts-arkui-promptaction-showtoastoptions-i.md) |
| [Button](arkts-arkui-promptaction-button-i.md) |
| [ShowDialogSuccessResponse](arkts-arkui-promptaction-showdialogsuccessresponse-i.md) |
| [ShowDialogOptions](arkts-arkui-promptaction-showdialogoptions-i.md) |
| [BaseDialogOptions](arkts-arkui-promptaction-basedialogoptions-i.md) |
| [CustomDialogOptions](arkts-arkui-promptaction-customdialogoptions-i.md) |
| [DialogOptions](arkts-arkui-promptaction-dialogoptions-i.md) |
| [ActionMenuSuccessResponse](arkts-arkui-promptaction-actionmenusuccessresponse-i.md) |
| [ActionMenuOptions](arkts-arkui-promptaction-actionmenuoptions-i.md) |

<!--Del-->
### 接口（系统接口）

| 名称 |
| --- |
| [ShowDialogOptions](arkts-arkui-promptaction-showdialogoptions-i-sys.md) |
| [BaseDialogOptions](arkts-arkui-promptaction-basedialogoptions-i-sys.md) |
| [ActionMenuOptions](arkts-arkui-promptaction-actionmenuoptions-i-sys.md) |
<!--DelEnd-->

### 枚举

| 名称 |
| --- |
| [ToastShowMode](arkts-arkui-promptaction-toastshowmode-e.md) |
| [CommonState](arkts-arkui-promptaction-commonstate-e.md) |

<!--Del-->
### 枚举（系统接口）

| 名称 |
| --- |
| [ToastShowMode](arkts-arkui-promptaction-toastshowmode-e-sys.md) |
<!--DelEnd-->

### 类型

| 名称 |
| --- |
| [DialogOptionsCornerRadius](arkts-arkui-promptaction-dialogoptionscornerradius-t.md) |
| [DialogOptionsBorderWidth](arkts-arkui-promptaction-dialogoptionsborderwidth-t.md) |
| [DialogOptionsBorderColor](arkts-arkui-promptaction-dialogoptionsbordercolor-t.md) |
| [DialogOptionsBorderStyle](arkts-arkui-promptaction-dialogoptionsborderstyle-t.md) |
| [DialogOptionsShadow](arkts-arkui-promptaction-dialogoptionsshadow-t.md) |
