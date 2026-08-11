# QueryFn (System API)

```TypeScript
type QueryFn = (
  uri: string,
  predicates: dataSharePredicates.DataSharePredicates,
  columns: Array<string>,
  callback: AsyncCallback<Object>
) => void
```

Callback function called when querying one or more data records in the database.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-type QueryFn = (  uri: string,  predicates: dataSharePredicates.DataSharePredicates,  columns: Array<string>,  callback: AsyncCallback<Object>) => void--><!--Device-unnamed-type QueryFn = (  uri: string,  predicates: dataSharePredicates.DataSharePredicates,  columns: Array<string>,  callback: AsyncCallback<Object>) => void-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Provider

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uri | string | Yes | Indicates the database table storing the data to query. |
| predicates | dataSharePredicates.DataSharePredicates | Yes | Indicates filter criteria. If this parameter is null, all data records will be queried by default. |
| columns | Array&lt;string&gt; | Yes | Indicates the columns to be queried, in array, for example, {"name","age"}. You should define the processing logic when this parameter is null. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Object&gt; | Yes | Returns the queried data, only support result set of rdb or kvstore. |

