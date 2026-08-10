# DataObserver

```TypeScript
type DataObserver = (sessionId: string, fields: Array<string>) => void
```

定义获取分布式对象数据变更的监听回调函数。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-distributedDataObject-type DataObserver = (sessionId: string, fields: Array<string>) => void--><!--Device-distributedDataObject-type DataObserver = (sessionId: string, fields: Array<string>) => void-End-->

**System capability:** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| sessionId | string | Yes | 标识变更对象的sessionId。长度不大于128字节，且只能包含字母、数字或下划线_。 |
| fields | Array&lt;string&gt; | Yes | 标识对象变更的属性名。属性名可自定义，要求字符串非空且长度不超过128字节。 |

