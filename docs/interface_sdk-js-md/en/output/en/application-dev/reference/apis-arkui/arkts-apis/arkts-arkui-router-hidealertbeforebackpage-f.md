# hideAlertBeforeBackPage

## hideAlertBeforeBackPage

```TypeScript
function hideAlertBeforeBackPage(): void
```

Disables the display of a confirm dialog box before returning to the previous page. > **NOTE** > > - Since API version 10, you can use the > \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_ API in > [UIContext]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ to obtain the [Router]\_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_ object associated > with the current UI context.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 18

**Substitutes:** [@ohos.arkui.UIContext:Router#hideAlertBeforeBackPage](arkts-arkui-arkui-uicontext-router-c.md#hidealertbeforebackpage)

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-router-function hideAlertBeforeBackPage(): void--><!--Device-router-function hideAlertBeforeBackPage(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Example**

```TypeScript
this.getUIContext().getRouter().hideAlertBeforeBackPage();
```

