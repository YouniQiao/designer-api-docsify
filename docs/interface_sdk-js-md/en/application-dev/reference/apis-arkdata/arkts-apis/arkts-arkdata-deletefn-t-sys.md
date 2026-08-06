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

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-type DeleteFn = (  uri: string,  predicates: dataSharePredicates.DataSharePredicates,  callback: AsyncCallback<int>) => void--><!--Device-unnamed-type DeleteFn = (  uri: string,  predicates: dataSharePredicates.DataSharePredicates,  callback: AsyncCallback<int>) => void-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Provider

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uri | string | Yes | Indicates the database table storing the data to delete.  |
| predicates | dataSharePredicates.DataSharePredicates | Yes | Indicates filter criteria. If this parameter is null, all data records will be deleted by default.  |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;int&gt; | Yes | Returns the number of data records deleted.  |

