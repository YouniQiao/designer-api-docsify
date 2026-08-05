# registerFont

## registerFont

```TypeScript
function registerFont(options: FontOptions): void
```

Registers a custom font with the font manager. This API is asynchronous and does not support concurrent calls. > **NOTE** > > - Since API version 10, you can use the > \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_ API in > [UIContext]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ to obtain the [Font]\_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_ object associated with > the current UI context.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 18

**Substitutes:** ohos.arkui.UIContext.Font#registerFont

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-font-function registerFont(options: FontOptions): void--><!--Device-font-function registerFont(options: FontOptions): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Information about the custom font to register. |

