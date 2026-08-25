# ProgressObserver

```TypeScript
type ProgressObserver = (sessionId: string, progress: int) => void
```

Defines an observer for obtaining the transfer progress.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**System capability:** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sessionId | string | Yes |
| progress | ArkTS-Dyn: number<br>ArkTS-Sta：int | Yes |
