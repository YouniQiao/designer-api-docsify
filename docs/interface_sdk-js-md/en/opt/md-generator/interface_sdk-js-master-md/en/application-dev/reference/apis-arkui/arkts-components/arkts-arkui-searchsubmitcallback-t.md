# SearchSubmitCallback

```TypeScript
declare type SearchSubmitCallback = (searchContent: string, event?: SubmitEvent) => void
```

Called when the search icon, search button, or soft keyboard search button is clicked.

**Since:** 14

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-unnamed-declare type SearchSubmitCallback = (searchContent: string, event?: SubmitEvent) => void--><!--Device-unnamed-declare type SearchSubmitCallback = (searchContent: string, event?: SubmitEvent) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| searchContent | string | Yes |
| event | [SubmitEvent](arkts-arkui-submitevent-i.md) | No |
