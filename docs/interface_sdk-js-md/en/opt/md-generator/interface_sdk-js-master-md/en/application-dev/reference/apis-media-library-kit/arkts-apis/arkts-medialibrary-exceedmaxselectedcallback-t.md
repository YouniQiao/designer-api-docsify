# ExceedMaxSelectedCallback

```TypeScript
export type ExceedMaxSelectedCallback = (exceedMaxCountType: MaxCountType) => void
```

Called when items are selected after the maximum count has been reached.

**Since:** 13

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 13.

<!--Device-unnamed-export type ExceedMaxSelectedCallback = (exceedMaxCountType: MaxCountType) => void--><!--Device-unnamed-export type ExceedMaxSelectedCallback = (exceedMaxCountType: MaxCountType) => void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| exceedMaxCountType | [MaxCountType](arkts-medialibrary-file-photopickercomponent-maxcounttype-e.md) | Yes |
