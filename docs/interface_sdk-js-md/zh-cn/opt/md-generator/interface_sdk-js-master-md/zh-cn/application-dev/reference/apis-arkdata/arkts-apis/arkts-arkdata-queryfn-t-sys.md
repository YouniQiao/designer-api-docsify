# QueryFn（系统接口）

```TypeScript
type QueryFn = (
  uri: string,
  predicates: dataSharePredicates.DataSharePredicates,
  columns: Array<string>,
  callback: AsyncCallback<Object>
) => void
```

查询操作的属性类型。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-type QueryFn = (  uri: string,  predicates: dataSharePredicates.DataSharePredicates,  columns: Array<string>,  callback: AsyncCallback<Object>) => void--><!--Device-unnamed-type QueryFn = (  uri: string,  predicates: dataSharePredicates.DataSharePredicates,  columns: Array<string>,  callback: AsyncCallback<Object>) => void-End-->

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Provider

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |
| predicates | dataSharePredicates.DataSharePredicates | 是 |
| columns | Array & lt;string & gt; | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Object&gt; | 是 |
