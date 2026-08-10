# JsonRecordType

```TypeScript
export type JsonRecordType = boolean | bigint | string | undefined | null | Double | Long |
    Record<string, JsonRecordType> | Array<JsonRecordType>
```

Represents all types that can be serialized to JSON or parsed from JSON.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export type JsonRecordType = boolean | bigint | string | undefined | null | Double | Long |    Record<string, JsonRecordType> | Array<JsonRecordType>--><!--Device-unnamed-export type JsonRecordType = boolean | bigint | string | undefined | null | Double | Long |    Record<string, JsonRecordType> | Array<JsonRecordType>-End-->

**系统能力：** SystemCapability.Utils.Lang

| 类型 | 说明 |
| --- | --- |
| boolean |  |
| bigint |  |
| string |  |
| undefined |  |
| null |  |
| Double |  |
| Long |  |
| Record&lt;string, JsonRecordType&gt; |  |
| Array&lt;JsonRecordType&gt; |  |

