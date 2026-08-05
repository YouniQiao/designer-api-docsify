# AlertDialogParamWithButtons

Inherited from [AlertDialogParam]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_.

**Inheritance/Implementation:** AlertDialogParamWithButtons extends [AlertDialogParam](../../apis-na/arkts-apis/arkts-na-component/alertdialog-alertdialogparam-i.md)

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

<!--Device-unnamed-declare interface AlertDialogParamWithButtons extends AlertDialogParam--><!--Device-unnamed-declare interface AlertDialogParamWithButtons extends AlertDialogParam-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## primaryButton

```TypeScript
primaryButton: AlertDialogButtonBaseOptions
```

Information about the primary button, including the enabling status, default focus, button style, text content, text color, button background color, and click callback. When the dialog box has focus and focus has not been shifted using the **Tab** key, the button responds to the **Enter** key by default, and multiple dialog boxes can gain focus consecutively to respond automatically. The default response to the **Enter** key does not work when **defaultFocus** is set to **true**. For details, see \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_.

**Type:** AlertDialogButtonBaseOptions

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AlertDialogParamWithButtons-primaryButton: AlertDialogButtonBaseOptions--><!--Device-AlertDialogParamWithButtons-primaryButton: AlertDialogButtonBaseOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## secondaryButton

```TypeScript
secondaryButton: AlertDialogButtonBaseOptions
```

Information about the secondary button, including the enabling status, default focus, button style, text content, text color, button background color, and click callback.

**Type:** AlertDialogButtonBaseOptions

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AlertDialogParamWithButtons-secondaryButton: AlertDialogButtonBaseOptions--><!--Device-AlertDialogParamWithButtons-secondaryButton: AlertDialogButtonBaseOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

