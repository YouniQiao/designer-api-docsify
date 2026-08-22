# getRunningFormInfos（系统接口）

## 导入模块

```TypeScript
import { formObserver } from '@kit.FormKit';
```

## getRunningFormInfos

```TypeScript
function getRunningFormInfos(callback: AsyncCallback<Array<formInfo.RunningFormInfo>>, hostBundleName?: string): void
```

获取设备上正在运行的所有非临时卡片信息。使用callback异步回调。

**起始版本：** 23

**需要权限：** ohos.permission.OBSERVE_FORM_RUNNING

<!--Device-formObserver-function getRunningFormInfos(callback: AsyncCallback<Array<formInfo.RunningFormInfo>>, hostBundleName?: string): void--><!--Device-formObserver-function getRunningFormInfos(callback: AsyncCallback<Array<formInfo.RunningFormInfo>>, hostBundleName?: string): void-End-->

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;formInfo.RunningFormInfo&gt;&gt; | 是 | 回调函数。获取设备上正在运行的所有非临时卡片信息。当获取卡片信息成功时，error为 undefined，data为查询到的卡片信息。 |
| hostBundleName | string | 否 | 指定要查询的卡片使用方名称，指定后会仅返回该卡片使用方下正在运行的非临时卡片信息。 <br> 缺省时，返回设备上所有正在运行的非临时卡片信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [201](../../errorcode-universal.md#201-权限校验失败) | Permissions denied. |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) | The application is not a system application. |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |
| [16500050](../errorcode-form.md#16500050-进程间通信失败) | IPC connection error. |
| [16500060](../errorcode-form.md#16500060-连接服务失败) | Service connection error. |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { formInfo, formObserver } from '@kit.FormKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  formObserver.getRunningFormInfos((error: BusinessError, data: formInfo.RunningFormInfo[]) => {
    if (error) {
      console.error(`error, code: ${error.code}, message: ${error.message}`);
    } else {
      data.forEach(item => {
        console.info(`formObserver getRunningFormInfos, formId: ${item.formId}`);
      });
    }
  }, 'com.example.ohos.formjsdemo');
} catch (error) {
  console.error(`catch error, code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}`);
}
```

ArkTS-Sta示例：

```TypeScript
'use static'

import { AsyncCallback } from '@ohos.base';
import { formInfo, formObserver } from '@kit.FormKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const DOMAIN: int = 0x0000;
const TAG: string = 'testTag formAgentTest';

try {
  let callback: AsyncCallback<Array<formInfo.RunningFormInfo>> = (error: BusinessError | null, data: Array<formInfo.RunningFormInfo> | undefined) => {
    if (error?.code != 0) {
      console.error(`error, code: ${error?.code}, message: ${error?.message}`);
    } else {
      console.info(`formObserver getRunningFormInfos, item count: ${data?.length}`);
    }
  };
  formObserver.getRunningFormInfos(callback, 'com.example.ohos.formjsdemo');
} catch(error) {
  console.error(`catch error, code: ${error.code}, message: ${error.message}`);
}
```

ArkTS-Dyn示例：

```TypeScript
import { formInfo, formObserver } from '@kit.FormKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  formObserver.getRunningFormInfos((error: BusinessError, data: formInfo.RunningFormInfo[]) => {
    if (error) {
      console.error(`error, code: ${error.code}, message: ${error.message}`);
    } else {
      data.forEach(item => {
        console.info(`formObserver getRunningFormInfos, formId: ${item.formId}`);
      });
    }
  }, true, 'com.example.ohos.formjsdemo');
} catch (error) {
  console.error(`catch error, code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}`);
}
```

ArkTS-Sta示例：

```TypeScript
'use static'

import { formInfo, formObserver } from '@kit.FormKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  formObserver.getRunningFormInfos((error: BusinessError | null, data: formInfo.RunningFormInfo[] | undefined) => {
    if (error?.code != 0) {
      console.error(`error, code: ${error?.code}, message: ${error?.message}`);
    } else {
      if (data !== undefined) {
        for (let runningFormInfo of data) {
          console.info(`formObserver getRunningFormInfos, hostBundleName : ${runningFormInfo.hostBundleName}`);
        }
      }
    }
  }, true, 'com.example.ohos.formjsdemo');
} catch (error) {
  console.error(`catch error, code: ${error.code}, message: ${error.message}`);
}
```

ArkTS-Dyn示例：

```TypeScript
import { formInfo, formObserver } from '@kit.FormKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  formObserver.getRunningFormInfos('com.example.ohos.formjsdemo').then((data: formInfo.RunningFormInfo[]) => {
    console.info('formObserver getRunningFormInfos success.');
  }).catch((error: BusinessError) => {
    console.error(`error, code: ${error.code}, message: ${error.message}`);
  });
} catch (error) {
  console.error(`catch error, code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}`);
}
```

ArkTS-Sta示例：

```TypeScript
'use static'

import { formInfo, formObserver } from '@kit.FormKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  formObserver.getRunningFormInfos('com.example.ohos.formjsdemo').then((data: formInfo.RunningFormInfo[]) => {
    for (let runningFormInfo of data) {
      console.info(`formObserver getRunningFormInfos, hostBundleName : ${runningFormInfo.hostBundleName}`);
    }
  }).catch((error) => {
    console.error(`error, code: ${error.code}, message: ${error.message}`);
  });
} catch (error) {
  console.error(`catch error, code: ${error.code}, message: ${error.message}`);
}
```

ArkTS-Dyn示例：

```TypeScript
import { formInfo, formObserver } from '@kit.FormKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  formObserver.getRunningFormInfos(true, 'com.example.ohos.formjsdemo').then((data: formInfo.RunningFormInfo[]) => {
    console.info('formObserver getRunningFormInfos success.');
  }).catch((error: BusinessError) => {
    console.error(`error, code: ${error.code}, message: ${error.message}`);
  });
} catch (error) {
  console.error(`catch error, code: ${error.code}, message: ${error.message}`);
}
```

ArkTS-Sta示例：

```TypeScript
'use static'

import { formInfo, formObserver } from '@kit.FormKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  formObserver.getRunningFormInfos(true, 'com.example.ohos.formjsdemo')
    .then((data: Array<formInfo.RunningFormInfo>) => {
      console.info(`formObserver getRunningFormInfos, item count: ${data?.length}`);
    })
    .catch((error) => {
      console.error(`error, code: ${error.code}, message: ${error.message}`);
    });
} catch (error) {
  console.error(`catch error, code: ${error.code}, message: ${error.message}`);
}
```


## getRunningFormInfos

```TypeScript
function getRunningFormInfos(
    callback: AsyncCallback<Array<formInfo.RunningFormInfo>>,
    isUnusedIncluded: boolean,
    hostBundleName?: string
  ): void
```

获取设备上正在运行的所有非临时卡片信息。使用callback异步回调。

**起始版本：** 23

**需要权限：** ohos.permission.OBSERVE_FORM_RUNNING

<!--Device-formObserver-function getRunningFormInfos(    callback: AsyncCallback<Array<formInfo.RunningFormInfo>>,    isUnusedIncluded: boolean,    hostBundleName?: string  ): void--><!--Device-formObserver-function getRunningFormInfos(    callback: AsyncCallback<Array<formInfo.RunningFormInfo>>,    isUnusedIncluded: boolean,    hostBundleName?: string  ): void-End-->

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;formInfo.RunningFormInfo&gt;&gt; | 是 | 回调函数。获取设备上正在运行的所有非临时卡片信息。当获取成功时，回调中的error为 undefined，data为查询到的卡片信息。 |
| isUnusedIncluded | boolean | 是 | 表示是否包含未使用的卡片。 <br>true: 表示包含未使用的卡片。 <br>false: 表示不包含未使用的卡片。 |
| hostBundleName | string | 否 | 指定要查询的卡片使用方名称，指定后会仅返回该卡片使用方下正在运行的非临时卡片信息。 <br> 缺省时，返回设备上所有正在运行的非临时卡片信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [201](../../errorcode-universal.md#201-权限校验失败) | Permissions denied. |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) | The application is not a system application. |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |
| [16500050](../errorcode-form.md#16500050-进程间通信失败) | IPC connection error. |
| [16500060](../errorcode-form.md#16500060-连接服务失败) | Service connection error. |

**示例**

参见 [getRunningFormInfos](#getrunningforminfos)


## getRunningFormInfos

```TypeScript
function getRunningFormInfos(hostBundleName?: string): Promise<Array<formInfo.RunningFormInfo>>
```

获取设备上正在运行的所有非临时卡片信息。使用Promise异步回调。

**起始版本：** 23

**需要权限：** ohos.permission.OBSERVE_FORM_RUNNING

<!--Device-formObserver-function getRunningFormInfos(hostBundleName?: string): Promise<Array<formInfo.RunningFormInfo>>--><!--Device-formObserver-function getRunningFormInfos(hostBundleName?: string): Promise<Array<formInfo.RunningFormInfo>>-End-->

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| hostBundleName | string | 否 | 指定要查询的卡片使用方名称，指定后会仅返回该卡片使用方下正在运行的非临时卡片信息。 <br> 缺省时，返回设备上所有正在运行的非临时卡片信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;Array&lt;formInfo.RunningFormInfo&gt;&gt; | Promise对象。返回设备上正在运行的所有非临时卡片信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [201](../../errorcode-universal.md#201-权限校验失败) | Permissions denied. |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) | The application is not a system application. |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |
| [16500050](../errorcode-form.md#16500050-进程间通信失败) | IPC connection error. |
| [16500060](../errorcode-form.md#16500060-连接服务失败) | Service connection error. |

**示例**

参见 [getRunningFormInfos](#getrunningforminfos)


## getRunningFormInfos

```TypeScript
function getRunningFormInfos(
    isUnusedIncluded: boolean,
    hostBundleName?: string
  ): Promise<Array<formInfo.RunningFormInfo>>
```

获取设备上正在运行的所有非临时卡片信息。使用Promise异步回调。

**起始版本：** 23

**需要权限：** ohos.permission.OBSERVE_FORM_RUNNING

<!--Device-formObserver-function getRunningFormInfos(    isUnusedIncluded: boolean,    hostBundleName?: string  ): Promise<Array<formInfo.RunningFormInfo>>--><!--Device-formObserver-function getRunningFormInfos(    isUnusedIncluded: boolean,    hostBundleName?: string  ): Promise<Array<formInfo.RunningFormInfo>>-End-->

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isUnusedIncluded | boolean | 是 | 表示是否包含未使用的卡片。 <br>true: 表示包含未使用的卡片。 <br>false: 表示不包含未使用的卡片。 |
| hostBundleName | string | 否 | 指定要查询的卡片使用方名称，指定后会仅返回该卡片使用方下正在运行的非临时卡片信息。 <br> 缺省时，返回设备上所有正在运行的非临时卡片信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;Array&lt;formInfo.RunningFormInfo&gt;&gt; | Promise对象。返回设备上正在运行的所有非临时卡片信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [201](../../errorcode-universal.md#201-权限校验失败) | Permissions denied. |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) | The application is not a system application. |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |
| [16500050](../errorcode-form.md#16500050-进程间通信失败) | IPC connection error. |
| [16500060](../errorcode-form.md#16500060-连接服务失败) | Service connection error. |

**示例**

参见 [getRunningFormInfos](#getrunningforminfos)

