# DeleteFn (System API)

```TypeScript
type DeleteFn = (
  uri: string,
  predicates: dataSharePredicates.DataSharePredicates,
  callback: AsyncCallback<int>
) => void
```

Callback function called when deleting one or more data records in the database.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-type DeleteFn = (  uri: string,  predicates: dataSharePredicates.DataSharePredicates,  callback: AsyncCallback<int>) => void--><!--Device-unnamed-type DeleteFn = (  uri: string,  predicates: dataSharePredicates.DataSharePredicates,  callback: AsyncCallback<int>) => void-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Provider

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uri | string | Yes | Indicates the database table storing the data to delete. |
| predicates | dataSharePredicates.DataSharePredicates | Yes | Indicates filter criteria. If this parameter is null, all data records will be deleted by default. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;int&gt; | Yes | Returns the number of data records deleted. |

