# RecordData

```TypeScript
export type RecordData = undefined | null | Object | Record<string, RecordData> | Array<RecordData>
```

RecordData 是一个联合类型，用于层级和每层数量都不确定的对象结构。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Base

| 类型 |
| --- |
| undefined |
| null |
| Object |
| Record & lt;string, RecordData & gt; |
| Array & lt;RecordData & gt; |
