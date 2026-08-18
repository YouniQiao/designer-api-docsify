# DataObserver

```TypeScript
type DataObserver = (sessionId: string, fields: Array<string>) => void
```

Defines an observer for obtaining the data change of a distributed object.

**Since:** 23

<!--Device-distributedDataObject-type DataObserver = (sessionId: string, fields: Array<string>) => void--><!--Device-distributedDataObject-type DataObserver = (sessionId: string, fields: Array<string>) => void-End-->

**System capability:** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sessionId | string | Yes |
| [fields](arkts-arkdata-cloudextension-table-i-sys.md) | Array & lt;string & gt; | Yes |
