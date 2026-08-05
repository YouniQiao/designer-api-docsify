# BatchInsertFn (System API)

```TypeScript
type BatchInsertFn = (uri: string, valueBuckets: Array<ValuesBucket>, callback: AsyncCallback<int>) => void
```

Callback function called when inserting multiple data records into the database.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-type BatchInsertFn = (uri: string, valueBuckets: Array<ValuesBucket>, callback: AsyncCallback<int>) => void--><!--Device-unnamed-type BatchInsertFn = (uri: string, valueBuckets: Array<ValuesBucket>, callback: AsyncCallback<int>) => void-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Provider

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uri | string | Yes | Indicates the position where the data is to insert.  |
| valueBuckets | Array&lt;ValuesBucket&gt; | Yes | Indicates the data to insert.  |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;int&gt; | Yes | Returns the number of data records inserted.  |

