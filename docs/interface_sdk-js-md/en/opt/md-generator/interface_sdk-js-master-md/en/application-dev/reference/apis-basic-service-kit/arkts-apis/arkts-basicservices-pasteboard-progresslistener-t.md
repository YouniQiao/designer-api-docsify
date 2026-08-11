# ProgressListener

```TypeScript
type ProgressListener = (progress: ProgressInfo) => void
```

Defines a listener for progress data changes. If the default progress indicator is not used, you can set this API to obtain the paste progress.

**Since:** 15

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-pasteboard-type ProgressListener = (progress: ProgressInfo) => void--><!--Device-pasteboard-type ProgressListener = (progress: ProgressInfo) => void-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| progress | [ProgressInfo](arkts-basicservices-pasteboard-progressinfo-i.md) | Yes |
