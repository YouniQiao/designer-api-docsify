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

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-type QueryFn = (  uri: string,  predicates: dataSharePredicates.DataSharePredicates,  columns: Array<string>,  callback: AsyncCallback<Object>) => void--><!--Device-unnamed-type QueryFn = (  uri: string,  predicates: dataSharePredicates.DataSharePredicates,  columns: Array<string>,  callback: AsyncCallback<Object>) => void-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Provider

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |
| predicates | dataSharePredicates.DataSharePredicates | Yes |
| columns | Array & lt;string & gt; | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Object&gt; | Yes |
