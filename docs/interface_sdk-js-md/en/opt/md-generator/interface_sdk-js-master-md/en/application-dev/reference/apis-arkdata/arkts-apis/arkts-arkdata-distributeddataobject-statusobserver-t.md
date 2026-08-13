# StatusObserver

```TypeScript
type StatusObserver = (sessionId: string, networkId: string, status: string) => void
```

Defines an observer for obtaining the status change of a distributed object.

**Since:** 23

**Deprecated since:** -1

<!--Device-distributedDataObject-type StatusObserver = (sessionId: string, networkId: string, status: string) => void--><!--Device-distributedDataObject-type StatusObserver = (sessionId: string, networkId: string, status: string) => void-End-->

**System capability:** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sessionId | string | Yes |
| networkId | string | Yes |
| status | string | Yes |
