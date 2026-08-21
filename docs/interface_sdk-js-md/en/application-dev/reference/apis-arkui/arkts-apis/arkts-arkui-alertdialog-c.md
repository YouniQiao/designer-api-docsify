# AlertDialog

**Since:** 7

**Deprecated since:** 26.0.0

**Substitutes:** [showAlertDialog](arkts-arkui-arkui-uicontext-uicontext-c.md#showalertdialog)

<!--Device-unnamed-declare class AlertDialog--><!--Device-unnamed-declare class AlertDialog-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## show

```TypeScript
static show(value: AlertDialogParamWithConfirm | AlertDialogParamWithButtons | AlertDialogParamWithOptions)
```

Shows an alert dialog box.

> **NOTE：**
> 
> Since API version 10, you can use the &gt; [showAlertDialog](arkts-arkui-arkui-uicontext-uicontext-c.md#showalertdialog) API in &gt; [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md), which ensures that the alert dialog box is shown in the intended UI &gt; instance.

**Since:** 7

**Deprecated since:** 18

**Substitutes:** [showAlertDialog](arkts-arkui-arkui-uicontext-uicontext-c.md#showalertdialog)

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AlertDialog-static show(value: AlertDialogParamWithConfirm | AlertDialogParamWithButtons | AlertDialogParamWithOptions)--><!--Device-AlertDialog-static show(value: AlertDialogParamWithConfirm | AlertDialogParamWithButtons | AlertDialogParamWithOptions)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [AlertDialogParamWithConfirm](arkts-arkui-alertdialogparamwithconfirm-i.md) \| [AlertDialogParamWithButtons](arkts-arkui-alertdialogparamwithbuttons-i.md) \| [AlertDialogParamWithOptions](arkts-arkui-alertdialogparamwithoptions-i.md) | Yes | Defines and displays the **AlertDialog** component.<br>**Since:** 10 |

