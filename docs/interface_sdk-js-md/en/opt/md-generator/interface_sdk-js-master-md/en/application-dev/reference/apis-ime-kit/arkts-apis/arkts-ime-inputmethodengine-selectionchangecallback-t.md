# SelectionChangeCallback

```TypeScript
export type SelectionChangeCallback = (oldBegin: number, oldEnd: number, newBegin: number, newEnd: number) => void
```

The callback of 'selectionChange' event.

**Since:** 23

**Deprecated since:** -1

<!--Device-inputMethodEngine-export type SelectionChangeCallback = (oldBegin: int, oldEnd: int, newBegin: int, newEnd: int) => void--><!--Device-inputMethodEngine-export type SelectionChangeCallback = (oldBegin: int, oldEnd: int, newBegin: int, newEnd: int) => void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| oldBegin | number | Yes |
| oldEnd | number | Yes |
| newBegin | number | Yes |
| newEnd | number | Yes |
