# RecordData

```TypeScript
export type RecordData = undefined | null | Object | Record<string, RecordData> | Array<RecordData>
```

RecordData 是一个联合类型，用于层级和每层数量都不确定的对象结构。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export type RecordData = undefined | null | Object | Record<string, RecordData> | Array<RecordData>--><!--Device-unnamed-export type RecordData = undefined | null | Object | Record<string, RecordData> | Array<RecordData>-End-->

**System capability:** SystemCapability.Base

| Type | Description |
| --- | --- |
| undefined | 未定义类型。 |
| null | 空类型。 |
| Object | 对象类型。 |
| Record&lt;string, RecordData&gt; | 带有字符串键和RecordData值的记录类型。 |
| Array&lt;RecordData&gt; | 包含RecordData元素的数组类型。 |

