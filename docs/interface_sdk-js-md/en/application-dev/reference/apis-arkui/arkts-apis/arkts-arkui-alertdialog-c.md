# AlertDialog

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 26.0.0

**Substitutes:** ohos.arkui.UIContext.UIContext#showAlertDialog

<!--Device-unnamed-declare class AlertDialog--><!--Device-unnamed-declare class AlertDialog-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## show

```TypeScript
static show(value: AlertDialogParamWithConfirm | AlertDialogParamWithButtons | AlertDialogParamWithOptions)
```

定义警告弹窗并弹出。

> **说明：**

showAlertDialog需先获取[UIContext](arkts-arkui-uicontext.md)实例后再进行调用。

> 从API version 10开始，可以通过使用[UIContext](arkts-arkui-uicontext.md)中的
> [showAlertDialog](arkts-arkui-arkui-uicontext-uicontext-c.md#showalertdialog)来明确UI的执行上下文。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 18

**Substitutes:** ohos.arkui.UIContext.UIContext#showAlertDialog

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AlertDialog-static show(value: AlertDialogParamWithConfirm | AlertDialogParamWithButtons | AlertDialogParamWithOptions)--><!--Device-AlertDialog-static show(value: AlertDialogParamWithConfirm | AlertDialogParamWithButtons | AlertDialogParamWithOptions)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [AlertDialogParamWithConfirm](arkts-arkui-alertdialogparamwithconfirm-i.md) \| AlertDialogParamWithButtons \| AlertDialogParamWithOptions | Yes | 定义并显示 AlertDialog组件。<br>**Since:** 10 |

