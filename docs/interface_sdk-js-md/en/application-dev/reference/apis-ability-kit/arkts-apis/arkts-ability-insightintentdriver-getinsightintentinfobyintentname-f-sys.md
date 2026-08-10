# getInsightIntentInfoByIntentName (System API)

## Modules to Import

```TypeScript
import { insightIntentDriver } from 'kits/@kit.AbilityKit';
```

## getInsightIntentInfoByIntentName

```TypeScript
function getInsightIntentInfoByIntentName(bundleName: string, moduleName: string, intentName: string, intentFlags: int): Promise<InsightIntentInfo>
```

根据包名、模块名和意图名查询当前设备上的意图信息。使用Promise异步回调。

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
| bundleName | string | Yes | 应用包名称。&lt;br/&gt;**说明：**&lt;br/&gt; 若包名不存在，则返回空对象。 |
| moduleName | string | Yes | 模块名称。&lt;br/&gt;**说明：**&lt;br/&gt; 若模块名不存在，则返回空对象。 |
| intentName | string | Yes | 意图名称。&lt;br/&gt;**说明：**&lt;br/&gt; 若意图名不存在，则返回空对象。 |
| intentFlags | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 意图信息（[InsightIntentInfo](arkts-ability-insightintentdriver-insightintentinfo-i-sys.md)）的标识，用于表示查询全量意图信息或者简要意 图信息，参考[GetInsightIntentFlag](arkts-ability-insightintentdriver-getinsightintentflag-e-sys.md)。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;InsightIntentInfo&gt; | Promise对象，返回意图信息对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 16000050 | Internal error. Possible causes: 1. Failed to connect to the system service; 2. The system service fails to communicate with the dependency module. |
| 201 | Permission denied. |
| 202 | Not system application. |

