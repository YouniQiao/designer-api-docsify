# InsertFn (System API)

```TypeScript
type InsertFn = (uri: string, valueBucket: ValuesBucket, callback: AsyncCallback<number>) => void
```

Callback function called when inserting a data record into the database.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-type InsertFn = (uri: string, valueBucket: ValuesBucket, callback: AsyncCallback<int>) => void--><!--Device-unnamed-type InsertFn = (uri: string, valueBucket: ValuesBucket, callback: AsyncCallback<int>) => void-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Provider

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |
| valueBucket | [ValuesBucket](arkts-arkdata-valuesbucket-t.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |
