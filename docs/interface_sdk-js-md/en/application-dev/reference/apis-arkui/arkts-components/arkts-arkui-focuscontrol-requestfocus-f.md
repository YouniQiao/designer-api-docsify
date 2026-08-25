# requestFocus

## Modules to Import

```TypeScript
```

## requestFocus

```TypeScript
function requestFocus(value: string): boolean
```

Requests focus transfer to the specified component during the next frame rendering. This global API provides asynchronous focus control.For scenarios requiring immediate focus changes, it is recommended that you use the focus synchronization transfer API [requestFocus](../arkts-apis/arkts-arkui-arkui-uicontext-focuscontroller-c.md#requestfocus) in **FocusController**.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |
