# offFormRemove（系统接口）

## 导入模块

```TypeScript
import { formObserver } from '@kit.FormKit';
```

## offFormRemove

```TypeScript
function offFormRemove(hostBundleName?: string, observerCallback?: Callback<formInfo.RunningFormInfo>): void
```

Cancels listening to the event of remove form. <p>You can use this method to cancel listening to the event of remove form.</p>

**起始版本：** 23

**需要权限：** ohos.permission.OBSERVE_FORM_RUNNING

<!--Device-formObserver-function offFormRemove(hostBundleName?: string, observerCallback?: Callback<formInfo.RunningFormInfo>): void--><!--Device-formObserver-function offFormRemove(hostBundleName?: string, observerCallback?: Callback<formInfo.RunningFormInfo>): void-End-->

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| hostBundleName | string | 否 | Indicates the bundle name of the form host application. |
| observerCallback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;formInfo.RunningFormInfo&gt; | 否 | The callback is used to return the running form info. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [201](../../errorcode-universal.md#201-权限校验失败) | Permissions denied. |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) | The application is not a system application. |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |

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
  formObserver.onFormRemove(observerCallback);
  console.info('testTag', 'formObserverStaticTest formObserver on success');
  formObserver.offFormRemove(hostBundleName, observerCallback);
  console.info('testTag', 'formObserverStaticTest formObserver off success');
} catch (error) {
  let code = error.code;
  let message = error.message;
  hilog.error(DOMAIN, TAG, `formObserverStaticTest catch error, code: ${code}, message: ${message})`);
}
```

