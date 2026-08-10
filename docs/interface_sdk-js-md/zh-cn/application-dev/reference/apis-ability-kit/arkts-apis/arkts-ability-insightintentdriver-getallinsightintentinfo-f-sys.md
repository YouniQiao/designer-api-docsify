# getAllInsightIntentInfo（系统接口）

## 导入模块

```TypeScript
import { insightIntentDriver } from 'kits/@kit.AbilityKit';
```

## getAllInsightIntentInfo

```TypeScript
function getAllInsightIntentInfo(intentFlags: int): Promise<Array<InsightIntentInfo>>
```

查询当前设备上的所有意图信息。使用Promise异步回调。

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-insightIntentDriver-function getAllInsightIntentInfo(intentFlags: int): Promise<Array<InsightIntentInfo>>--><!--Device-insightIntentDriver-function getAllInsightIntentInfo(intentFlags: int): Promise<Array<InsightIntentInfo>>-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| intentFlags | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 是 | 意图信息（[InsightIntentInfo](arkts-ability-insightintentdriver-insightintentinfo-i-sys.md)）的标识，用于表示查询全量意图信息或者简要意 图信息，参考[GetInsightIntentFlag](arkts-ability-insightintentdriver-getinsightintentflag-e-sys.md)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;Array&lt;InsightIntentInfo&gt;&gt; | Promise对象，返回意图信息对象数组。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 16000050 | Internal error. Possible causes: 1. Failed to connect to the system service; 2. The system service fails to communicate with the dependency module. |
| 201 | Permission denied. |
| 202 | Not system application. |

