# RecordData

```TypeScript
type RecordData = undefined | null | Object | Record<string, RecordData> | Array<RecordData>
```

RecordData is used for input parameter obj of the equal function

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-preferences-type RecordData = undefined | null | Object | Record<string, RecordData> | Array<RecordData>--><!--Device-preferences-type RecordData = undefined | null | Object | Record<string, RecordData> | Array<RecordData>-End-->

**System capability:** 
- API version 23 and later: SystemCapability.DistributedDataManager.Preferences.Core

| Type | Description |
| --- | --- |
| undefined | The value is undefined. |
| null | The value is null. |
| Object | The value is an object. |
| Record&lt;string, RecordData&gt; | The value is a record of string keys mapping to RecordData. |
| Array&lt;RecordData&gt; | The value is an array of RecordData elements. |

