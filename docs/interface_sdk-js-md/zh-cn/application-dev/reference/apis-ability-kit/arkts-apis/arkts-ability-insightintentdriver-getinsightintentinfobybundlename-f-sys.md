# getInsightIntentInfoByBundleName（系统接口）

## 导入模块

```TypeScript
import { insightIntentDriver } from '@kit.AbilityKit';
```

## getInsightIntentInfoByBundleName

```TypeScript
function getInsightIntentInfoByBundleName(bundleName: string, intentFlags: int): Promise<Array<InsightIntentInfo>>
```

根据包名查询当前设备上的意图信息。使用Promise异步回调。

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |
| [intentFlags](arkts-ability-insightintentdriver-insightintentinfofilter-i-sys.md) | ArkTS-Dyn: number<br>ArkTS-Sta：int | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;[InsightIntentInfo](arkts-ability-insightintentdriver-insightintentinfo-i-sys.md)&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |

**示例**

```TypeScript
import { insightIntentDriver } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

async function getInfosByBundleName() {
  try {
    let bundleName = "com.example.intent"; // 开发者需自行修改为实际包名
    insightIntentDriver.getInsightIntentInfoByBundleName(bundleName,
      insightIntentDriver.GetInsightIntentFlag.GET_FULL_INSIGHT_INTENT |
      insightIntentDriver.GetInsightIntentFlag.GET_ENTITY_INFO).then((data) => {
      hilog.info(0x0000, 'testTag', 'getInsightIntentInfoByBundleName return %{public}s', data);
    }).catch((error: Error) => {
      let err = error as BusinessError;
      hilog.info(0x0000, 'testTag', 'getInsightIntentInfoByBundleName errCode: %{public}d', err.code);
      hilog.info(0x0000, 'testTag', 'getInsightIntentInfoByBundleName errMessage: %{public}s', err.message);
    });
  } catch (error) {
    hilog.error(0x0000, 'testTag', 'getInsightIntentInfoByBundleName error caught %{public}s', error);
  }
}
```
