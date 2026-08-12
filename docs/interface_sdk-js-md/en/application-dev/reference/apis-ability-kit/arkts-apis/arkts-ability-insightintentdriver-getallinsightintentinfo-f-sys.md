# getAllInsightIntentInfo (System API)

## Modules to Import

```TypeScript
import { insightIntentDriver } from '@kit.AbilityKit';
```

## getAllInsightIntentInfo

```TypeScript
function getAllInsightIntentInfo(intentFlags: int): Promise<Array<InsightIntentInfo>>
```

Obtains the information about all intents on the current device. This API uses a promise to return the result.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

**Model restriction:** This API can be used only in the stage model.

<!--Device-insightIntentDriver-function getAllInsightIntentInfo(intentFlags: int): Promise<Array<InsightIntentInfo>>--><!--Device-insightIntentDriver-function getAllInsightIntentInfo(intentFlags: int): Promise<Array<InsightIntentInfo>>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| intentFlags | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Flag of the intent information ( [InsightIntentInfo](arkts-ability-insightintentdriver-insightintentinfo-i-sys.md#InsightIntentInfo)). It is used to query full or brief intent information. For details, see [GetInsightIntentFlag](arkts-ability-insightintentdriver-getinsightintentflag-e-sys.md#GetInsightIntentFlag). |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;[InsightIntentInfo](arkts-ability-insightintentdriver-insightintentinfo-i-sys.md)&gt;&gt; | Promise used to return an array holding InsightIntentInfo objects. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [16000050](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000050-internal-error) | Internal error. Possible causes: 1. Failed to connect to the system service; 2. The system service fails to communicate with the dependency module. |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not system application. |

