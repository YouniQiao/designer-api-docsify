# RecordData

```TypeScript
export type RecordData = undefined | null | Object | Record<string, RecordData> | Array<RecordData>
```

RecordData is a union type used for object structures with uncertain levels and quantities at each level.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-export type RecordData = undefined | null | Object | Record<string, RecordData> | Array<RecordData>--><!--Device-unnamed-export type RecordData = undefined | null | Object | Record<string, RecordData> | Array<RecordData>-End-->

**System capability:** SystemCapability.Base

| Type | Description |
| --- | --- |
| undefined | Undefined type. |
| null | Null type. |
| Object | Object type. |
| Record&lt;string, RecordData&gt; | Record type with string keys and RecordData values. |
| Array&lt;RecordData&gt; | Array type containing RecordData elements. |

