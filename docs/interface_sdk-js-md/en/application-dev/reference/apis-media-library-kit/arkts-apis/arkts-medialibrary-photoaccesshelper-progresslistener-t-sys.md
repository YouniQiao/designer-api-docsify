# ProgressListener (System API)

```TypeScript
type ProgressListener = (progress: Progress) => void
```

Indicates the type of the progress of batch operation.Progress callback, which can be the size or numberof files.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| progress | [Progress](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-agent-progress-i.md) | Yes |
