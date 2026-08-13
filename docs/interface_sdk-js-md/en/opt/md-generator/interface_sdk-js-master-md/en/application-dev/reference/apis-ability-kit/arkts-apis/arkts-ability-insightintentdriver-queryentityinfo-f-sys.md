# queryEntityInfo (System API)

## Modules to Import

```TypeScript
import { insightIntentDriver } from '@kit.AbilityKit';
```

## queryEntityInfo

```TypeScript
function queryEntityInfo(param: QueryParam): Promise<Array<Record<string, Object>>>
```

Query insight intent entity information.

**Since:** 26.0.0

**Deprecated since:** -1

**Required permissions:** ohos.permission.EXECUTE_INSIGHT_INTENT

**Model restriction:** This API can be used only in the stage model.

<!--Device-insightIntentDriver-function queryEntityInfo(param: QueryParam): Promise<Array<Record<string, Object>>>--><!--Device-insightIntentDriver-function queryEntityInfo(param: QueryParam): Promise<Array<Record<string, Object>>>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| param | [QueryParam](arkts-ability-insightintentdriver-queryparam-i-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[Record](../../apis-na/arkts-apis/arkts-na-record-t.md)&lt;string, Object&gt;&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [16000006](../errorcode-ability.md#16000006-crossuser-operation-is-not-allowed) |
| [16000050](../errorcode-ability.md#16000050-internal-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |


## queryEntityInfo

```TypeScript
function queryEntityInfo(param: QueryParam): Promise<Array<Record<string, RecordData>>>
```

Query insight intent entity information.

**Since:** 26.0.0

**Deprecated since:** -1

**Required permissions:** ohos.permission.EXECUTE_INSIGHT_INTENT

**Model restriction:** This API can be used only in the stage model.

<!--Device-insightIntentDriver-function queryEntityInfo(param: QueryParam): Promise<Array<Record<string, RecordData>>>--><!--Device-insightIntentDriver-function queryEntityInfo(param: QueryParam): Promise<Array<Record<string, RecordData>>>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| param | [QueryParam](arkts-ability-insightintentdriver-queryparam-i-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[Record](../../apis-na/arkts-apis/arkts-na-record-t.md)&lt;string, [RecordData](../../apis-arkdata/arkts-apis/arkts-arkdata-preferences-recorddata-t.md)&gt;&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [16000006](../errorcode-ability.md#16000006-crossuser-operation-is-not-allowed) |
| [16000050](../errorcode-ability.md#16000050-internal-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
