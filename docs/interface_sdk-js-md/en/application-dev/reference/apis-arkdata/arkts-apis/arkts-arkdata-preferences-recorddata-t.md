# RecordData

```TypeScript
type RecordData = undefined | null | Object | Record<string, RecordData> | Array<RecordData>
```

RecordData is used for input parameter obj of the equal function

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-preferences-type RecordData = undefined | null | Object | Record<string, RecordData> | Array<RecordData>--><!--Device-preferences-type RecordData = undefined | null | Object | Record<string, RecordData> | Array<RecordData>-End-->

**System capability:** 
- API version 23 and later: SystemCapability.DistributedDataManager.Preferences.Core

| Type | Description |
| --- | --- |
| undefined | 表示类型为未定义。 |
| null | 表示类型为空。 |
| Object | 表示类型为对象。 |
| Record&lt;string, RecordData&gt; | 表示类型为键值对类型。键的类型为string，值的类型为RecordData。 |
| Array&lt;RecordData&gt; | 表示类型为RecordData类型的数组。 |

