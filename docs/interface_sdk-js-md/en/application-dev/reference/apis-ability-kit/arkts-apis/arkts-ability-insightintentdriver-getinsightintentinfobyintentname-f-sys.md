# getInsightIntentInfoByIntentName (System API)

## Modules to Import

```TypeScript
import { insightIntentDriver } from '@kit.AbilityKit';
```

## getInsightIntentInfoByIntentName

```TypeScript
function getInsightIntentInfoByIntentName(bundleName: string, moduleName: string, intentName: string, intentFlags: int): Promise<InsightIntentInfo>
```

Obtains the intent information on the current device based on the bundle name, module name, and intent name. This API uses a promise to return the result.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

**Model restriction:** This API can be used only in the stage model.

<!--Device-insightIntentDriver-function getInsightIntentInfoByIntentName(bundleName: string, moduleName: string, intentName: string, intentFlags: int): Promise<InsightIntentInfo>--><!--Device-insightIntentDriver-function getInsightIntentInfoByIntentName(bundleName: string, moduleName: string, intentName: string, intentFlags: int): Promise<InsightIntentInfo>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundleName | string | Yes | Bundle name of the application.&lt;br&gt;**NOTE：**&lt;br&gt; If the bundle name does not exist, an empty object is returned. |
| moduleName | string | Yes | Module name.&lt;br&gt;**NOTE：**&lt;br&gt; If the module name does not exist, an empty object is returned. |
| intentName | string | Yes | Intent name.&lt;br&gt;**NOTE：**&lt;br&gt; If the intent name does not exist, an empty object is returned. |
| intentFlags | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Flag of the intent information ( [InsightIntentInfo](arkts-ability-insightintentdriver-insightintentinfo-i-sys.md#InsightIntentInfo)). It is used to query full or brief intent information. For details, see [GetInsightIntentFlag](arkts-ability-insightintentdriver-getinsightintentflag-e-sys.md#GetInsightIntentFlag). |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[InsightIntentInfo](arkts-ability-insightintentdriver-insightintentinfo-i-sys.md)&gt; | Promise used to return the InsightIntentInfo object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [16000050](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000050-internal-error) | Internal error. Possible causes: 1. Failed to connect to the system service; 2. The system service fails to communicate with the dependency module. |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not system application. |

