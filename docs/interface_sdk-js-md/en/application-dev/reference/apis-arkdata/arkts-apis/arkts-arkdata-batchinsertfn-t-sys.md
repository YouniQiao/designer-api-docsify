# BatchInsertFn (System API)

```TypeScript
type BatchInsertFn = (uri: string, valueBuckets: Array<ValuesBucket>, callback: AsyncCallback<int>) => void
```

Callback function called when inserting multiple data records into the database.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-type BatchInsertFn = (uri: string, valueBuckets: Array<ValuesBucket>, callback: AsyncCallback<int>) => void--><!--Device-unnamed-type BatchInsertFn = (uri: string, valueBuckets: Array<ValuesBucket>, callback: AsyncCallback<int>) => void-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Provider

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uri | string | Yes | Indicates the position where the data is to insert. |
| valueBuckets | Array&lt;[ValuesBucket](arkts-arkdata-valuesbucket-t.md)&gt; | Yes | Indicates the data to insert. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;int&gt; | Yes | Returns the number of data records inserted. |

