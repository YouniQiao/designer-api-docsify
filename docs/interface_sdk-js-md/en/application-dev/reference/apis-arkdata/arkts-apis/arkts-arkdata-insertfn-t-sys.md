# InsertFn (System API)

```TypeScript
type InsertFn = (uri: string, valueBucket: ValuesBucket, callback: AsyncCallback<int>) => void
```

Callback function called when inserting a data record into the database.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-type InsertFn = (uri: string, valueBucket: ValuesBucket, callback: AsyncCallback<int>) => void--><!--Device-unnamed-type InsertFn = (uri: string, valueBucket: ValuesBucket, callback: AsyncCallback<int>) => void-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Provider

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uri | string | Yes | Indicates the position where the data is to insert. |
| valueBucket | [ValuesBucket](arkts-arkdata-valuesbucket-t.md) | Yes | Indicates the data to insert. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;int&gt; | Yes | Returns the index of the newly inserted data record. |

