# BatchUpdateFn (System API)

```TypeScript
type BatchUpdateFn = (
  operations: Record<string, Array<UpdateOperation>>,
  callback: AsyncCallback<Record<string, Array<number>>>
) => void
```

Callback function called when updating multiple data records in the database.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-type BatchUpdateFn = (  operations: Record<string, Array<UpdateOperation>>,  callback: AsyncCallback<Record<string, Array<int>>>) => void--><!--Device-unnamed-type BatchUpdateFn = (  operations: Record<string, Array<UpdateOperation>>,  callback: AsyncCallback<Record<string, Array<int>>>) => void-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Provider

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| operations | [Record](../../apis-na/arkts-apis/arkts-na-record-t.md)&lt;string, Array&lt;[UpdateOperation](arkts-arkdata-updateoperation-t-sys.md)&gt;&gt; | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[Record](../../apis-na/arkts-apis/arkts-na-record-t.md)&lt;string, Array&lt;number&gt;&gt;&gt; | Yes |
