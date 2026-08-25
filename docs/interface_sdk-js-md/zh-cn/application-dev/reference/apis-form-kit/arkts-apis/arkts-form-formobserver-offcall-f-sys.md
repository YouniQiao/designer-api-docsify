# offCall（系统接口）

## 导入模块

```TypeScript
import { formObserver } from '@kit.FormKit';
```

## offCall

```TypeScript
function offCall(hostBundleName?: string, observerCallback?: Callback<formInfo.RunningFormInfo>): void
```

Unregister form call event Listening.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.OBSERVE_FORM_RUNNING

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [hostBundleName](arkts-form-forminfo-runningforminfo-i-sys.md) | string | 否 |
| observerCallback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;formInfo.RunningFormInfo&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |

**示例**

```TypeScript
'use static'

import { formInfo, formObserver } from '@kit.FormKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const DOMAIN: int = 0x0000;
const TAG: string = 'testTag formAgentTest';

try {
  let hostBundleName: string = 'com.example.demoForm';
  let observerCallback = (data: formInfo.RunningFormInfo | undefined) => {
    console.info('testTag', `formObserverStaticTest observerCallback success`);
  };
  formObserver.onCall(observerCallback);
  console.info('testTag', 'formObserverStaticTest formObserver on success');
  formObserver.offCall(hostBundleName, observerCallback);
  console.info('testTag', 'formObserverStaticTest formObserver off success');
} catch (error) {
  hilog.error(DOMAIN, TAG, `formObserverStaticTest catch error, code: ${error.code} message: ${error.message}`);
}
```
