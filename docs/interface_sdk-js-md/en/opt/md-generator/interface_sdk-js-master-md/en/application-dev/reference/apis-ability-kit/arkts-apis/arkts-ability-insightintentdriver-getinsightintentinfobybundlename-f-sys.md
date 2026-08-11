# getInsightIntentInfoByBundleName (System API)

## Modules to Import

```TypeScript
import { insightIntentDriver } from 'kits/@kit.AbilityKit';
```

## getInsightIntentInfoByBundleName

```TypeScript
function getInsightIntentInfoByBundleName(bundleName: string, intentFlags: number): Promise<Array<InsightIntentInfo>>
```

Obtains the intent information on the current device based on the given bundle name. This API uses a promise to return the result.

**Since:** 20

**Required permissions:** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

**Model restriction:** This API can be used only in the stage model.

<!--Device-insightIntentDriver-function getInsightIntentInfoByBundleName(bundleName: string, intentFlags: int): Promise<Array<InsightIntentInfo>>--><!--Device-insightIntentDriver-function getInsightIntentInfoByBundleName(bundleName: string, intentFlags: int): Promise<Array<InsightIntentInfo>>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |
| intentFlags | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;InsightIntentInfo&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [16000050](../errorcode-ability.md#16000050-internal-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
