# getInsightIntentInfoByFilter (System API)

## Modules to Import

```TypeScript
import { insightIntentDriver } from 'kits/@kit.AbilityKit';
```

## getInsightIntentInfoByFilter

```TypeScript
function getInsightIntentInfoByFilter(filter: InsightIntentInfoFilter): Promise<Array<InsightIntentInfo>>
```

Obtains the intent information on the current device based on the given intent filter. This API uses a promise to return the result.If the user ID of the calling application is different from the user ID of the intent, the calling application must request the ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS permission.

**Since:** 23

**Required permissions:** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| filter | [InsightIntentInfoFilter](arkts-ability-insightintentdriver-insightintentinfofilter-i-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[InsightIntentInfo](arkts-ability-insightintentdriver-insightintentinfo-i-sys.md)&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [16000006](../errorcode-ability.md#16000006-cross-user-operation-is-not-allowed) |
| [16000050](../errorcode-ability.md#16000050-internal-error) |
