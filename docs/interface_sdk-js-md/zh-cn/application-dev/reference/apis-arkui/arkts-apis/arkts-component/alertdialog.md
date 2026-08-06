# component/alertDialog(AlertDialog)

显示警告弹窗组件，可设置文本内容与响应回调。
 > **说明：**
 >
 > - 本模块同时支持ArkTS-Dyn、ArkTS-Sta。
 >
 > - 从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
 >
 > - 本模块功能依赖UI的执行上下文，不可在[UI上下文不明确](../../../ui/arkts-global-interface.md#ui上下文不明确)的地方使用，参见
 > [UIContext](../arkts-arkui-uicontext.md)说明。


## 汇总

### 接口

| 名称 | 说明 |
| --- | --- |
| [AlertDialogButtonBaseOptions](alertdialog-alertdialogbuttonbaseoptions-i.md) | 警告弹窗中按钮的样式。  @since版本号高于内层元素版本号的情况，但这不影响接口的使用。 |
| [AlertDialogButtonOptions](alertdialog-alertdialogbuttonoptions-i.md) | 继承自[AlertDialogButtonBaseOptions]\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_。 |
| [AlertDialogParam](alertdialog-alertdialogparam-i.md) | 警告弹窗的样式。 |
| [AlertDialogParamWithButtons](alertdialog-alertdialogparamwithbuttons-i.md) | 继承自[AlertDialogParam]\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_。 |
| [AlertDialogParamWithConfirm](alertdialog-alertdialogparamwithconfirm-i.md) | 继承自[AlertDialogParam]\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_。 |
| [AlertDialogParamWithOptions](alertdialog-alertdialogparamwithoptions-i.md) | 继承自[AlertDialogParam]\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_。 |
| [AlertDialogTextStyleOptions](alertdialog-alertdialogtextstyleoptions-i.md) | 弹窗中message的截断方式。 |

<!--Del-->
### 接口（系统接口）

| 名称 | 说明 |
| --- | --- |
| [AlertDialogParam](alertdialog-alertdialogparam-i-sys.md) | 警告弹窗的样式。 |
<!--DelEnd-->

### 枚举

| 名称 | 说明 |
| --- | --- |
| [DialogAlignment](alertdialog-dialogalignment-e.md) | 警告弹窗的对齐方式。 |
| [DialogButtonDirection](alertdialog-dialogbuttondirection-e.md) | 警告弹窗中按钮的对齐方式。 |

