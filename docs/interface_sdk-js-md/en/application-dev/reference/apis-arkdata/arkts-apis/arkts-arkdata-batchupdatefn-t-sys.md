# BatchUpdateFn (System API)

```TypeScript
type BatchUpdateFn = (
  operations: Record<string, Array<UpdateOperation>>,
  callback: AsyncCallback<Record<string, Array<int>>>
) => void
```

Callback function called when updating multiple data records in the database.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-type BatchUpdateFn = (  operations: Record<string, Array<UpdateOperation>>,  callback: AsyncCallback<Record<string, Array<int>>>) => void--><!--Device-unnamed-type BatchUpdateFn = (  operations: Record<string, Array<UpdateOperation>>,  callback: AsyncCallback<Record<string, Array<int>>>) => void-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Provider

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| operations | Record&lt;string, Array&lt;[UpdateOperation](arkts-arkdata-updateoperation-t-sys.md)&gt;&gt; | Yes | Indicates the data to update. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;Record&lt;string, Array&lt;int&gt;&gt;&gt; | Yes | Callback used to return the result. |

