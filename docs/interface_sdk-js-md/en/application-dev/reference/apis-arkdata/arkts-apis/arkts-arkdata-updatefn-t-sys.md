# UpdateFn (System API)

```TypeScript
type UpdateFn = (
  uri: string,
  predicates: dataSharePredicates.DataSharePredicates,
  valueBucket: ValuesBucket,
  callback: AsyncCallback<int>
) => void
```

Callback function called when updating one or more data records in the database.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-type UpdateFn = (  uri: string,  predicates: dataSharePredicates.DataSharePredicates,  valueBucket: ValuesBucket,  callback: AsyncCallback<int>) => void--><!--Device-unnamed-type UpdateFn = (  uri: string,  predicates: dataSharePredicates.DataSharePredicates,  valueBucket: ValuesBucket,  callback: AsyncCallback<int>) => void-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Provider

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uri | string | Yes | Indicates the database table storing the data to update. |
| predicates | dataSharePredicates.DataSharePredicates | Yes | Indicates filter criteria. If this parameter is null, all data records will be updated by default. |
| valueBucket | [ValuesBucket](arkts-arkdata-valuesbucket-t.md) | Yes | Indicates the data to update. This parameter can be null. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;int&gt; | Yes | Returns the number of data records updated. |

