# OnSelectCallback

```TypeScript
declare type OnSelectCallback = (index: number, selectValue: string) => void
```

Called when an item in the drop-down list box is selected.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-unnamed-declare type OnSelectCallback = (index: number, selectValue: string) => void--><!--Device-unnamed-declare type OnSelectCallback = (index: number, selectValue: string) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| index | number | Yes |
| [selectValue](arkts-arkui-atomicservice-atomicservicesearch-selectparams-i.md) | string | Yes |
