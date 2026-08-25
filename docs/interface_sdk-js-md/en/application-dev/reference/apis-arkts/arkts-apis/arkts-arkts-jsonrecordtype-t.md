# JsonRecordType

```TypeScript
export type JsonRecordType = boolean | bigint | string | undefined | null | Double | Long |
    Record<string, JsonRecordType> | Array<JsonRecordType>
```

Represents all types that can be serialized to JSON or parsed from JSON.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |
| bigint |
| string |
| undefined |
| null |
| Double |
| Long |
| Record & lt;string, JsonRecordType & gt; |
| Array & lt;JsonRecordType & gt; |
