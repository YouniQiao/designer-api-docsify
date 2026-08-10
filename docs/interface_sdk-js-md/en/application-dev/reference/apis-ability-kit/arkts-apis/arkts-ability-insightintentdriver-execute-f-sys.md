# execute (System API)

## Modules to Import

```TypeScript
import { insightIntentDriver } from 'kits/@kit.AbilityKit';
```

## execute

```TypeScript
function execute(param: ExecuteParam, callback: AsyncCallback<insightIntent.ExecuteResult>): void
```

执行意图调用的接口。使用callback异步回调。当调用方在后台时，需要申请`ohos.permission.START_ABILITIES_FROM_BACKGROUND`权限。当意图调用执行模式[ExecuteMode](arkts-ability-insightintent-executemode-e.md)取值为UI_ABILITY_BACKGROUND时，需要申请`ohos.permission.ABILITY_BACKGROUND_COMMUNICATION`权限。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.EXECUTE_INSIGHT_INTENT

**Model restriction:** This API can be used only in the stage model.

<!--Device-insightIntentDriver-function execute(param: ExecuteParam, callback: AsyncCallback<insightIntent.ExecuteResult>): void--><!--Device-insightIntentDriver-function execute(param: ExecuteParam, callback: AsyncCallback<insightIntent.ExecuteResult>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| param | [ExecuteParam](arkts-ability-insightintentdriver-executeparam-i-sys.md) | Yes | 执行意图调用的参数。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;insightIntent.ExecuteResult&gt; | Yes | 回调函数，返回意图调用执行结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 16000053 | The ability is not on the top of the UI. |
| 16000055 | Installation-free timed out. |
| 16000050 | Internal error. |
| 201 | Permission denied. |
| 202 | Not system application. |
| 16000004 | Cannot start an invisible component. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 16000005 | The specified process does not have the permission. |
| 16000006 | Cross-user operations are not allowed. |
| 16000001 | The specified ability does not exist. |
| 16000002 | Incorrect ability type. |
| 16000012 | The application is controlled. |
| 16000013 | The application is controlled by EDM. |
| 16000008 | The crowdtesting application expires. |
| 16000009 | An ability cannot be started or stopped in Wukong mode. |
| 16000137 | Cross-device execution failed due to a connection error.<br>**Applicable version:** 26.0.0 and later |
| 16000010 | The call with the continuation and prepare continuation flag is forbidden. |
| 16000138 | Device disconnected during cross-device intent execution.<br>**Applicable version:** 26.0.0 and later |
| 16000011 | The context does not exist. |

## Examples

```TypeScript
import { insightIntentDriver, insightIntent } from '@kit.AbilityKit';
  import { hilog } from '@kit.PerformanceAnalysisKit';

  function executeInsightIntentAsync() {
    let param: insightIntentDriver.ExecuteParam = {
      bundleName: 'com.ohos.intentexecutedemo',
      moduleName: 'entry',
      abilityName: 'EntryAbility',
      insightIntentName: 'PlayMusic',
      insightIntentParam: {
        songName: 'City Of Stars',
      },
      executeMode: insightIntent.ExecuteMode.UI_ABILITY_FOREGROUND,
    };

    try {
      insightIntentDriver.execute(param, (error, data: insightIntent.ExecuteResult) => {
        if (error) {
          hilog.error(0x0000, 'testTag', 'execute insight intent failed with %{public}s', JSON.stringify(error));
        } else {
          hilog.info(0x0000, 'testTag', '%{public}s', 'execute insight intent succeed');
        }
        hilog.info(0x0000, 'testTag', 'execute insight intent return %{public}d', data.code);
        hilog.info(0x0000, 'testTag', 'execute insight intent result %{public}s', JSON.stringify(data.result));
      })
    } catch (error) {
      hilog.error(0x0000, 'testTag', 'execute insight intent error caught %{public}s', JSON.stringify(error));
    }
  }
```


## execute

```TypeScript
function execute(param: ExecuteParam): Promise<insightIntent.ExecuteResult>
```

执行意图调用的接口。使用Promise异步回调。当调用方在后台时，需要申请`ohos.permission.START_ABILITIES_FROM_BACKGROUND`权限。当意图调用执行模式[ExecuteMode](arkts-ability-insightintent-executemode-e.md)取值为UI_ABILITY_BACKGROUND时，需要申请`ohos.permission.ABILITY_BACKGROUND_COMMUNICATION`权限。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.EXECUTE_INSIGHT_INTENT

**Model restriction:** This API can be used only in the stage model.

<!--Device-insightIntentDriver-function execute(param: ExecuteParam): Promise<insightIntent.ExecuteResult>--><!--Device-insightIntentDriver-function execute(param: ExecuteParam): Promise<insightIntent.ExecuteResult>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| param | [ExecuteParam](arkts-ability-insightintentdriver-executeparam-i-sys.md) | Yes | 执行意图调用的参数。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;insightIntent.ExecuteResult&gt; | Promise used to return the intent call execution result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 16000053 | The ability is not on the top of the UI. |
| 16000055 | Installation-free timed out. |
| 16000050 | Internal error. |
| 201 | Permission denied. |
| 202 | Not system application. |
| 16000004 | Cannot start an invisible component. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 16000005 | The specified process does not have the permission. |
| 16000006 | Cross-user operations are not allowed. |
| 16000001 | The specified ability does not exist. |
| 16000002 | Incorrect ability type. |
| 16000012 | The application is controlled. |
| 16000013 | The application is controlled by EDM. |
| 16000008 | The crowdtesting application expires. |
| 16000009 | An ability cannot be started or stopped in Wukong mode. |
| 16000137 | Cross-device execution failed due to a connection error.<br>**Applicable version:** 26.0.0 and later |
| 16000010 | The call with the continuation and prepare continuation flag is forbidden. |
| 16000138 | Device disconnected during cross-device intent execution.<br>**Applicable version:** 26.0.0 and later |
| 16000011 | The context does not exist. |

## Examples

```TypeScript
import { insightIntentDriver, insightIntent } from '@kit.AbilityKit';
  import { hilog } from '@kit.PerformanceAnalysisKit';

  async function executeSearchMusicIntentPromise() {
    let param: insightIntentDriver.ExecuteParam = {
      bundleName: 'com.ohos.intentexecutedemo',
      moduleName: 'entry',
      abilityName: 'EntryAbility',
      insightIntentName: 'PlayMusic',
      insightIntentParam: {
        songName: 'City Of Stars',
      },
      executeMode: insightIntent.ExecuteMode.UI_ABILITY_FOREGROUND,
    };

    try {
      let resultData: insightIntent.ExecuteResult = await insightIntentDriver.execute(param);
      hilog.info(0x0000, 'testTag', 'execute insight intent return %{public}d', resultData.code);
      hilog.info(0x0000, 'testTag', 'execute insight intent result %{public}s', JSON.stringify(resultData.result));
    } catch (error) {
      hilog.error(0x0000, 'testTag', 'execute insight intent error caught %{public}s', JSON.stringify(error));
    }
  }
```

