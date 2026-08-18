# getInsightIntentInfoByFilter (System API)

## Modules to Import

```TypeScript
```

## getInsightIntentInfoByFilter

```TypeScript
function getInsightIntentInfoByFilter(filter: InsightIntentInfoFilter): Promise<Array<InsightIntentInfo>>
```

Obtains the intent information on the current device based on the given intent filter. This API uses a promise to return the result.<br>If the user ID of the calling application is different from the user ID of the intent, the calling application must request the ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS permission.

**Since:** 23

**Required permissions:** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

**Model restriction:** This API can be used only in the stage model.

<!--Device-insightIntentDriver-function getInsightIntentInfoByFilter(filter: InsightIntentInfoFilter): Promise<Array<InsightIntentInfo>>--><!--Device-insightIntentDriver-function getInsightIntentInfoByFilter(filter: InsightIntentInfoFilter): Promise<Array<InsightIntentInfo>>-End-->

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
| [16000006](../errorcode-ability.md#16000006-crossuser-operation-is-not-allowed) |
| [16000050](../errorcode-ability.md#16000050-internal-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

**Examples**

```TypeScript
import { insightIntentDriver } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

function getInfoByFilter() {
  let filter: insightIntentDriver.InsightIntentInfoFilter = {
    intentFlags: insightIntentDriver.GetInsightIntentFlag.GET_FULL_INSIGHT_INTENT | insightIntentDriver.GetInsightIntentFlag.GET_ENTITY_INFO,
    bundleName: 'com.example.intent', // Use the actual bundle name.
    moduleName: 'entry', // Use the actual module name.
    intentName: 'play', // Use the actual intent name.
    userId: 100, // Use the actual user ID.
  };

  try {
    insightIntentDriver.getInsightIntentInfoByFilter(filter).then((data) => {
      hilog.info(0x0000, 'testTag', 'getInsightIntentInfoByFilter return %{public}s', JSON.stringify(data));
    }).catch((err: BusinessError) => {
      hilog.info(0x0000, 'testTag', 'getInsightIntentInfoByFilter errCode: %{public}d', err.code);
      hilog.info(0x0000, 'testTag', 'getInsightIntentInfoByFilter errMessage: %{public}s', err.message);
    });
  } catch (error) {
    hilog.error(0x0000, 'testTag', 'getInsightIntentInfoByFilter error caught %{public}s', JSON.stringify(error));
  }
}
```
