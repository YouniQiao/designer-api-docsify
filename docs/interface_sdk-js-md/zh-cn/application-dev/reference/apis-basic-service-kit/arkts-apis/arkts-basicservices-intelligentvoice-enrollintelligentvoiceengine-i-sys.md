# EnrollIntelligentVoiceEngine（系统接口）

Implements enroll intelligent voice engine.

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

<!--Device-intelligentVoice-interface EnrollIntelligentVoiceEngine--><!--Device-intelligentVoice-interface EnrollIntelligentVoiceEngine-End-->

**系统能力：** SystemCapability.AI.IntelligentVoice.Core

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { intelligentVoice } from 'kits/@kit.BasicServicesKit';
```

## commit

```TypeScript
commit(callback: AsyncCallback<void>): void
```

Commit enroll, This method uses an asynchronous callback to return the result.

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.MANAGE_INTELLIGENT_VOICE

<!--Device-EnrollIntelligentVoiceEngine-commit(callback: AsyncCallback<void>): void--><!--Device-EnrollIntelligentVoiceEngine-commit(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.AI.IntelligentVoice.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 | the callback used to return the result. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 22700104 | Failed to commit the enrollment. |
| 201 | Permission denied. |
| 202 | Not system application. |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

if (enrollIntelligentVoiceEngine != null) {
  (enrollIntelligentVoiceEngine as intelligentVoice.EnrollIntelligentVoiceEngine).commit((err: BusinessError) => {
    if (err) {
      console.error(`Failed to commit enroll, Code:${err.code}, message:${err.message}`);
    } else {
      console.info(`Succeeded in committing enroll.`);
    }
  });
}
```

## commit

```TypeScript
commit(): Promise<void>
```

Commit enroll, This method uses a promise to return the result.

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.MANAGE_INTELLIGENT_VOICE

<!--Device-EnrollIntelligentVoiceEngine-commit(): Promise<void>--><!--Device-EnrollIntelligentVoiceEngine-commit(): Promise<void>-End-->

**系统能力：** SystemCapability.AI.IntelligentVoice.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | the promise used to return the result. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 22700104 | Failed to commit the enrollment. |
| 201 | Permission denied. |
| 202 | Not system application. |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

if (enrollIntelligentVoiceEngine != null) {
  (enrollIntelligentVoiceEngine as intelligentVoice.EnrollIntelligentVoiceEngine).commit().then(() => {
    console.info(`Succeeded in committing enroll.`);
  }).catch((err: BusinessError) => {
    console.error(`Failed to commit enroll, Code:${err.code}, message:${err.message}`);
  });
}
```

## enrollForResult

```TypeScript
enrollForResult(isLast: boolean, callback: AsyncCallback<EnrollCallbackInfo>): void
```

Enrolls for result, This method uses an asynchronous callback to return the result.

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**需要权限：** ohos.permission.MANAGE_INTELLIGENT_VOICE and ohos.permission.MICROPHONE

<!--Device-EnrollIntelligentVoiceEngine-enrollForResult(isLast: boolean, callback: AsyncCallback<EnrollCallbackInfo>): void--><!--Device-EnrollIntelligentVoiceEngine-enrollForResult(isLast: boolean, callback: AsyncCallback<EnrollCallbackInfo>): void-End-->

**系统能力：** SystemCapability.AI.IntelligentVoice.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isLast | boolean | 是 | isLast indicates if it is the last time to enroll. |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;EnrollCallbackInfo&gt; | 是 | the callback used to return the result. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 22700107 | System error. |
| 201 | Permission denied. |
| 202 | Not system application. |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let callbackInfo: intelligentVoice.EnrollCallbackInfo | null = null;
if (enrollIntelligentVoiceEngine != null) {
  (enrollIntelligentVoiceEngine as intelligentVoice.EnrollIntelligentVoiceEngine).enrollForResult(true, (err: BusinessError, data: intelligentVoice.EnrollCallbackInfo) => {
    if (err) {
      console.error(`Failed to enroll for result, Code:${err.code}, message:${err.message}`);
    } else {
      callbackInfo = data;
      console.info(`Succeeded in enrolling for result, info:${callbackInfo}.`);
    }
  });
}
```

## enrollForResult

```TypeScript
enrollForResult(isLast: boolean): Promise<EnrollCallbackInfo>
```

Enrolls for result, This method uses a promise to return the result.

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**需要权限：** ohos.permission.MANAGE_INTELLIGENT_VOICE and ohos.permission.MICROPHONE

<!--Device-EnrollIntelligentVoiceEngine-enrollForResult(isLast: boolean): Promise<EnrollCallbackInfo>--><!--Device-EnrollIntelligentVoiceEngine-enrollForResult(isLast: boolean): Promise<EnrollCallbackInfo>-End-->

**系统能力：** SystemCapability.AI.IntelligentVoice.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isLast | boolean | 是 | isLast indicates if it is the last time to enroll. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;EnrollCallbackInfo&gt; | the promise used to return the result. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 22700107 | System error. |
| 201 | Permission denied. |
| 202 | Not system application. |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let callbackInfo: intelligentVoice.EnrollCallbackInfo | null = null;
if (enrollIntelligentVoiceEngine != null) {
  (enrollIntelligentVoiceEngine as intelligentVoice.EnrollIntelligentVoiceEngine).enrollForResult(true).then((data: intelligentVoice.EnrollCallbackInfo) => {
    callbackInfo = data;
    console.info(`Succeeded in enrolling for result, info:${callbackInfo}.`);
  }).catch((err: BusinessError) => {
    console.error(`Failed to enroll for result, Code:${err.code}, message:${err.message}`);
  });
}
```

## evaluateForResult

```TypeScript
evaluateForResult(word: string): Promise<EvaluationResult>
```

Evaluates for result, This method uses a promise to return the result.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.MANAGE_INTELLIGENT_VOICE

<!--Device-EnrollIntelligentVoiceEngine-evaluateForResult(word: string): Promise<EvaluationResult>--><!--Device-EnrollIntelligentVoiceEngine-evaluateForResult(word: string): Promise<EvaluationResult>-End-->

**系统能力：** SystemCapability.AI.IntelligentVoice.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| word | string | 是 | the word to evaluate. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;EvaluationResult&gt; | the promise used to return the result. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 22700107 | System error. |
| 201 | Permission denied. |
| 202 | Not system application. |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

if (enrollIntelligentVoiceEngine != null) {
  (enrollIntelligentVoiceEngine as intelligentVoice.EnrollIntelligentVoiceEngine).evaluateForResult('word').then(
    (data: intelligentVoice.EvaluationResult) => {
    let param: intelligentVoice.EvaluationResult = data;
    console.info(`Succeeded in evaluating, param:${param}`);
  }).catch((err: BusinessError) => {
    console.error(`Failed to evaluate, Code:${err.code}, message:${err.message}`);
  });
}
```

## getParameter

```TypeScript
getParameter(key: string, callback: AsyncCallback<string>): void
```

Obtains the value of an intelligent voice parameter. This method uses an asynchronous callback to return the query result.

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.MANAGE_INTELLIGENT_VOICE

<!--Device-EnrollIntelligentVoiceEngine-getParameter(key: string, callback: AsyncCallback<string>): void--><!--Device-EnrollIntelligentVoiceEngine-getParameter(key: string, callback: AsyncCallback<string>): void-End-->

**系统能力：** SystemCapability.AI.IntelligentVoice.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | the key of the intelligent voice parameter whose value is to be obtained. |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 | the callback used to return the value of the intelligent voice parameter. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 201 | Permission denied. |
| 202 | Not system application. |
| 22700102 | Invalid parameter. |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

if (enrollIntelligentVoiceEngine != null) {
  (enrollIntelligentVoiceEngine as intelligentVoice.EnrollIntelligentVoiceEngine).getParameter('key', (err: BusinessError, data: string) => {
    if (err) {
      console.error(`Failed to get parameter, Code:${err.code}, message:${err.message}`);
    } else {
      let param: string = data;
      console.info(`Succeeded in getting parameter, param:${param}`);
    }
  });
}
```

## getParameter

```TypeScript
getParameter(key: string): Promise<string>
```

Obtains the value of an intelligent voice parameter. This method uses a promise to return the query result.

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.MANAGE_INTELLIGENT_VOICE

<!--Device-EnrollIntelligentVoiceEngine-getParameter(key: string): Promise<string>--><!--Device-EnrollIntelligentVoiceEngine-getParameter(key: string): Promise<string>-End-->

**系统能力：** SystemCapability.AI.IntelligentVoice.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | the key of the intelligent voice parameter whose value is to be obtained. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;string&gt; | the promise used to return the value of the intelligent voice parameter. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 201 | Permission denied. |
| 202 | Not system application. |
| 22700102 | Invalid parameter. |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

if (enrollIntelligentVoiceEngine != null) {
  (enrollIntelligentVoiceEngine as intelligentVoice.EnrollIntelligentVoiceEngine).getParameter('key').then((data: string) => {
    let param: string = data;
    console.info(`Succeeded in getting parameter, param:${param}`);
  }).catch((err: BusinessError) => {
    console.error(`Failed to get parameter, Code:${err.code}, message:${err.message}`);
  });
}
```

## getSupportedRegions

```TypeScript
getSupportedRegions(callback: AsyncCallback<Array<string>>): void
```

Obtains the supported regions, This method uses an asynchronous callback to return the query result.

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.MANAGE_INTELLIGENT_VOICE

<!--Device-EnrollIntelligentVoiceEngine-getSupportedRegions(callback: AsyncCallback<Array<string>>): void--><!--Device-EnrollIntelligentVoiceEngine-getSupportedRegions(callback: AsyncCallback<Array<string>>): void-End-->

**系统能力：** SystemCapability.AI.IntelligentVoice.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;string&gt;&gt; | 是 | the callback used to return the supported regions. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 202 | Not system application. |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let regions: Array<string> | null = null;

if (enrollIntelligentVoiceEngine != null) {
  (enrollIntelligentVoiceEngine as intelligentVoice.EnrollIntelligentVoiceEngine).getSupportedRegions((err: BusinessError, data: Array<string>) => {
    if (err) {
      console.error(`Failed to get supported regions, Code:${err.code}, message:${err.message}`);
    } else {
      regions = data;
      console.info(`Succeeded in getting supported regions, regions:${regions}.`);
    }
  });
}
```

## getSupportedRegions

```TypeScript
getSupportedRegions(): Promise<Array<string>>
```

Obtains the supported regions, This method uses a promise to return the query result.

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.MANAGE_INTELLIGENT_VOICE

<!--Device-EnrollIntelligentVoiceEngine-getSupportedRegions(): Promise<Array<string>>--><!--Device-EnrollIntelligentVoiceEngine-getSupportedRegions(): Promise<Array<string>>-End-->

**系统能力：** SystemCapability.AI.IntelligentVoice.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;Array&lt;string&gt;&gt; | the promise used to return the supported regions. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 202 | Not system application. |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let regions: Array<string> | null = null;
if (enrollIntelligentVoiceEngine != null) {
  (enrollIntelligentVoiceEngine as intelligentVoice.EnrollIntelligentVoiceEngine).getSupportedRegions().then((data: Array<string>) => {
    regions = data;
    console.info(`Succeeded in getting supported regions, regions:${regions}.`);
  }).catch((err: BusinessError) => {
    console.error(`Failed to get supported regions, Code:${err.code}, message:${err.message}`);
  });
}
```

## init

```TypeScript
init(config: EnrollEngineConfig, callback: AsyncCallback<void>): void
```

Initials the engine, This method uses an asynchronous callback to return the result.

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.MANAGE_INTELLIGENT_VOICE

<!--Device-EnrollIntelligentVoiceEngine-init(config: EnrollEngineConfig, callback: AsyncCallback<void>): void--><!--Device-EnrollIntelligentVoiceEngine-init(config: EnrollEngineConfig, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.AI.IntelligentVoice.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| config | [EnrollEngineConfig](arkts-basicservices-intelligentvoice-enrollengineconfig-i-sys.md) | 是 | config indicates enroll engine configuration. |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 | the callback used to return the result. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 201 | Permission denied. |
| 202 | Not system application. |
| 22700102 | Invalid parameter. |
| 22700103 | Init failed. |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let config: intelligentVoice.EnrollEngineConfig = {
  language: 'zh',
  region: 'CN',
}
if (enrollIntelligentVoiceEngine != null) {
  (enrollIntelligentVoiceEngine as intelligentVoice.EnrollIntelligentVoiceEngine).init(config, (err: BusinessError) => {
    if (err) {
      console.error(`Failed to initialize enrollIntelligentVoice engine. Code:${err.code}, message:${err.message}`);
    } else {
      console.info(`Succeeded in initializing enrollIntelligentVoice engine.`);
    }
  });
}
```

## init

```TypeScript
init(config: EnrollEngineConfig): Promise<void>
```

Initials the engine, This method uses a promise to return the result.

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.MANAGE_INTELLIGENT_VOICE

<!--Device-EnrollIntelligentVoiceEngine-init(config: EnrollEngineConfig): Promise<void>--><!--Device-EnrollIntelligentVoiceEngine-init(config: EnrollEngineConfig): Promise<void>-End-->

**系统能力：** SystemCapability.AI.IntelligentVoice.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| config | [EnrollEngineConfig](arkts-basicservices-intelligentvoice-enrollengineconfig-i-sys.md) | 是 | config indicates enroll engine configuration. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | the promise used to return the result. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 201 | Permission denied. |
| 202 | Not system application. |
| 22700102 | Invalid parameter. |
| 22700103 | Init failed. |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let config: intelligentVoice.EnrollEngineConfig = {
  language: 'zh',
  region: 'CN',
}
if (enrollIntelligentVoiceEngine != null) {
  (enrollIntelligentVoiceEngine as intelligentVoice.EnrollIntelligentVoiceEngine).init(config).then(() => {
    console.info(`Succeeded in initializing enrollIntelligentVoice engine.`);
  }).catch((err: BusinessError) => {
    console.error(`Failed to initialize enrollIntelligentVoice engine. Code:${err.code}, message:${err.message}`);
  });
}
```

## release

```TypeScript
release(callback: AsyncCallback<void>): void
```

Releases the engine, This method uses an asynchronous callback to return the result.

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.MANAGE_INTELLIGENT_VOICE

<!--Device-EnrollIntelligentVoiceEngine-release(callback: AsyncCallback<void>): void--><!--Device-EnrollIntelligentVoiceEngine-release(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.AI.IntelligentVoice.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 | the callback used to return the result. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 202 | Not system application. |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

if (enrollIntelligentVoiceEngine != null) {
  (enrollIntelligentVoiceEngine as intelligentVoice.EnrollIntelligentVoiceEngine).release((err: BusinessError) => {
    if (err) {
      console.error(`Failed to release enrollIntelligentVoice engine, Code:${err.code}, message:${err.message}`);
    } else {
      console.info(`Succeeded in releasing enrollIntelligentVoice engine.`);
    }
  });
}
```

## release

```TypeScript
release(): Promise<void>
```

Releases the engine, This method uses a promise to return the result.

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.MANAGE_INTELLIGENT_VOICE

<!--Device-EnrollIntelligentVoiceEngine-release(): Promise<void>--><!--Device-EnrollIntelligentVoiceEngine-release(): Promise<void>-End-->

**系统能力：** SystemCapability.AI.IntelligentVoice.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | the promise used to return the result. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 202 | Not system application. |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

if (enrollIntelligentVoiceEngine != null) {
  (enrollIntelligentVoiceEngine as intelligentVoice.EnrollIntelligentVoiceEngine).release().then(() => {
    console.info(`Succeeded in releasing enrollIntelligentVoice engine.`);
  }).catch((err: BusinessError) => {
    console.error(`Failed to release enrollIntelligentVoice engine, Code:${err.code}, message:${err.message}`);
  });
}
```

## setParameter

```TypeScript
setParameter(key: string, value: string, callback: AsyncCallback<void>): void
```

Sets an intelligent voice parameter. This method uses an asynchronous callback to return the result.

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.MANAGE_INTELLIGENT_VOICE

<!--Device-EnrollIntelligentVoiceEngine-setParameter(key: string, value: string, callback: AsyncCallback<void>): void--><!--Device-EnrollIntelligentVoiceEngine-setParameter(key: string, value: string, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.AI.IntelligentVoice.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | the key of the intelligent voice parameter to set. |
| value | string | 是 | the value of the intelligent voice parameter to set. |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 | the callback used to return the result. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 201 | Permission denied. |
| 202 | Not system application. |
| 22700102 | Invalid parameter. |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

if (enrollIntelligentVoiceEngine != null) {
  (enrollIntelligentVoiceEngine as intelligentVoice.EnrollIntelligentVoiceEngine).setParameter('scene', '0', (err: BusinessError) => {
    if (err) {
      console.error(`Failed to set parameter, Code:${err.code}, message:${err.message}`);
    } else {
      console.info(`Succeeded in setting parameter`);
    }
  });
}
```

## setParameter

```TypeScript
setParameter(key: string, value: string): Promise<void>
```

Sets an intelligent voice parameter. This method uses a promise to return the result.

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.MANAGE_INTELLIGENT_VOICE

<!--Device-EnrollIntelligentVoiceEngine-setParameter(key: string, value: string): Promise<void>--><!--Device-EnrollIntelligentVoiceEngine-setParameter(key: string, value: string): Promise<void>-End-->

**系统能力：** SystemCapability.AI.IntelligentVoice.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | the key of the intelligent voice parameter to set. |
| value | string | 是 | the value of the intelligent voice parameter to set. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | the promise used to return the result. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 201 | Permission denied. |
| 202 | Not system application. |
| 22700102 | Invalid parameter. |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

if (enrollIntelligentVoiceEngine != null) {
  (enrollIntelligentVoiceEngine as intelligentVoice.EnrollIntelligentVoiceEngine).setParameter('scene', '0').then(() => {
    console.info(`Succeeded in setting parameter`);
  }).catch((err: BusinessError) => {
    console.error(`Failed to set parameter, Code:${err.code}, message:${err.message}`);
  });
}
```

## setSensibility

```TypeScript
setSensibility(sensibility: SensibilityType, callback: AsyncCallback<void>): void
```

Sets sensibility, This method uses an asynchronous callback to return the result.

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.MANAGE_INTELLIGENT_VOICE

<!--Device-EnrollIntelligentVoiceEngine-setSensibility(sensibility: SensibilityType, callback: AsyncCallback<void>): void--><!--Device-EnrollIntelligentVoiceEngine-setSensibility(sensibility: SensibilityType, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.AI.IntelligentVoice.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sensibility | [SensibilityType](arkts-basicservices-intelligentvoice-sensibilitytype-e-sys.md) | 是 | sensibility to set. |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 | the callback used to return the result. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 201 | Permission denied. |
| 202 | Not system application. |
| 22700102 | Invalid parameter. |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

if (enrollIntelligentVoiceEngine != null) {
  (enrollIntelligentVoiceEngine as intelligentVoice.EnrollIntelligentVoiceEngine).setSensibility(intelligentVoice.SensibilityType.LOW_SENSIBILITY, (err: BusinessError) => {
    if (err) {
      console.error(`Failed to set sensibility, Code:${err.code}, message:${err.message}`);
    } else {
      console.info(`Succeeded in setting sensibility.`);
    }
  });
}
```

## setSensibility

```TypeScript
setSensibility(sensibility: SensibilityType): Promise<void>
```

Sets sensibility, This method uses a promise to return the result.

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.MANAGE_INTELLIGENT_VOICE

<!--Device-EnrollIntelligentVoiceEngine-setSensibility(sensibility: SensibilityType): Promise<void>--><!--Device-EnrollIntelligentVoiceEngine-setSensibility(sensibility: SensibilityType): Promise<void>-End-->

**系统能力：** SystemCapability.AI.IntelligentVoice.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sensibility | [SensibilityType](arkts-basicservices-intelligentvoice-sensibilitytype-e-sys.md) | 是 | sensibility to set. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | the promise used to return the result. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 201 | Permission denied. |
| 202 | Not system application. |
| 22700102 | Invalid parameter. |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

if (enrollIntelligentVoiceEngine != null) {
  (enrollIntelligentVoiceEngine as intelligentVoice.EnrollIntelligentVoiceEngine).setSensibility(intelligentVoice.SensibilityType.LOW_SENSIBILITY).then(() => {
    console.info(`Succeeded in setting sensibility.`);
  }).catch((err: BusinessError) => {
    console.error(`Failed to set sensibility, Code:${err.code}, message:${err.message}`);
  });
}
```

## setWakeupHapInfo

```TypeScript
setWakeupHapInfo(info: WakeupHapInfo, callback: AsyncCallback<void>): void
```

Sets wakeup hap information, This method uses an asynchronous callback to return the result.

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.MANAGE_INTELLIGENT_VOICE

<!--Device-EnrollIntelligentVoiceEngine-setWakeupHapInfo(info: WakeupHapInfo, callback: AsyncCallback<void>): void--><!--Device-EnrollIntelligentVoiceEngine-setWakeupHapInfo(info: WakeupHapInfo, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.AI.IntelligentVoice.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| info | [WakeupHapInfo](arkts-basicservices-intelligentvoice-wakeuphapinfo-i-sys.md) | 是 | info indicates wakeup hap information. |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 | the callback used to return the result. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 201 | Permission denied. |
| 202 | Not system application. |
| 22700102 | Invalid parameter. |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let info: intelligentVoice.WakeupHapInfo = {
  bundleName: 'com.wakeup',
  abilityName: 'WakeUpExtAbility',
}
if (enrollIntelligentVoiceEngine != null) {
  (enrollIntelligentVoiceEngine as intelligentVoice.EnrollIntelligentVoiceEngine).setWakeupHapInfo(info, (err: BusinessError) => {
    if (err) {
      console.error(`Failed to set wakeup hap info, Code:${err.code}, message:${err.message}`);
    } else {
      console.info(`Succeeded in setting wakeup hap info.`);
    }
  });
}
```

## setWakeupHapInfo

```TypeScript
setWakeupHapInfo(info: WakeupHapInfo): Promise<void>
```

Sets wakeup hap information, This method uses a promise to return the result.

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.MANAGE_INTELLIGENT_VOICE

<!--Device-EnrollIntelligentVoiceEngine-setWakeupHapInfo(info: WakeupHapInfo): Promise<void>--><!--Device-EnrollIntelligentVoiceEngine-setWakeupHapInfo(info: WakeupHapInfo): Promise<void>-End-->

**系统能力：** SystemCapability.AI.IntelligentVoice.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| info | [WakeupHapInfo](arkts-basicservices-intelligentvoice-wakeuphapinfo-i-sys.md) | 是 | info indicates wakeup hap information. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | the promise used to return the result. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 201 | Permission denied. |
| 202 | Not system application. |
| 22700102 | Invalid parameter. |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let info: intelligentVoice.WakeupHapInfo = {
  bundleName: 'com.wakeup',
  abilityName: 'WakeUpExtAbility',
}
if (enrollIntelligentVoiceEngine != null) {
  (enrollIntelligentVoiceEngine as intelligentVoice.EnrollIntelligentVoiceEngine).setWakeupHapInfo(info).then(() => {
    console.info(`Succeeded in setting wakeup hap info.`);
  }).catch((err: BusinessError) => {
    console.error(`Failed to set wakeup hap info, Code:${err.code}, message:${err.message}`);
  });
}
```

## stop

```TypeScript
stop(callback: AsyncCallback<void>): void
```

Stops the engine, This method uses an asynchronous callback to return the result.

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.MANAGE_INTELLIGENT_VOICE

<!--Device-EnrollIntelligentVoiceEngine-stop(callback: AsyncCallback<void>): void--><!--Device-EnrollIntelligentVoiceEngine-stop(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.AI.IntelligentVoice.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 | the callback used to return the result. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 202 | Not system application. |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

if (enrollIntelligentVoiceEngine != null) {
  (enrollIntelligentVoiceEngine as intelligentVoice.EnrollIntelligentVoiceEngine).stop((err: BusinessError) => {
    if (err) {
      console.error(`Failed to stop enrollIntelligentVoice engine, Code:${err.code}, message:${err.message}`);
    } else {
      console.info(`Succeeded in stopping enrollIntelligentVoice engine.`);
    }
  });
}
```

## stop

```TypeScript
stop(): Promise<void>
```

Stops the engine, This method uses a promise to return the result.

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.MANAGE_INTELLIGENT_VOICE

<!--Device-EnrollIntelligentVoiceEngine-stop(): Promise<void>--><!--Device-EnrollIntelligentVoiceEngine-stop(): Promise<void>-End-->

**系统能力：** SystemCapability.AI.IntelligentVoice.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | the promise used to return the result. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 202 | Not system application. |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

if (enrollIntelligentVoiceEngine != null) {
  (enrollIntelligentVoiceEngine as intelligentVoice.EnrollIntelligentVoiceEngine).stop().then(() => {
    console.info(`Succeeded in stopping enrollIntelligentVoice engine.`);
  }).catch((err:BusinessError) => {
    console.error(`Failed to stop enrollIntelligentVoice engine, Code:${err.code}, message:${err.message}`);
  });
}
```

