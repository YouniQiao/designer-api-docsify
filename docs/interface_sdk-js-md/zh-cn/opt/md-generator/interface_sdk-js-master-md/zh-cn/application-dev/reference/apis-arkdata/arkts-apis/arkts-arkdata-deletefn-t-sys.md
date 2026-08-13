# DeleteFn（系统接口）

```TypeScript
type DeleteFn = (
  uri: string,
  predicates: dataSharePredicates.DataSharePredicates,
  callback: AsyncCallback<number>
) => void
```

删除操作的属性类型。

**起始版本：** 23

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-type DeleteFn = (  uri: string,  predicates: dataSharePredicates.DataSharePredicates,  callback: AsyncCallback<int>) => void--><!--Device-unnamed-type DeleteFn = (  uri: string,  predicates: dataSharePredicates.DataSharePredicates,  callback: AsyncCallback<int>) => void-End-->

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Provider

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |
| predicates | dataSharePredicates.DataSharePredicates | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |
