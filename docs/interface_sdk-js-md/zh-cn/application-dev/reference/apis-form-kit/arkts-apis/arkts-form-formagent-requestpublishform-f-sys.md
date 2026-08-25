# requestPublishForm（系统接口）

## 导入模块

```TypeScript
import { formAgent } from '@kit.FormKit';
```

## requestPublishForm

```TypeScript
function requestPublishForm(want: Want, callback: AsyncCallback<string>): void
```

请求发布一张卡片到使用方，使用callback异步回调。使用方通常为桌面。适用于系统应用需要主动将卡片添加到桌面的场景。

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.AGENT_REQUIRE_FORM

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| want | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16500050](../errorcode-form.md#16500050-进程间通信失败) |
| [16500100](../errorcode-form.md#16500100-获取卡片配置信息失败) |
| [16501000](../errorcode-form.md#16501000-内部功能错误) |
| [16501002](../errorcode-form.md#16501002-卡片数量达到上限) |
| [16501008](../errorcode-form.md#16501008-等待卡片加桌超时) |
| [16501017](../errorcode-form.md#16501017-无空间发布卡片) |
| [16501018](../errorcode-form.md#16501018-卡片不支持发布) |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { formAgent } from '@kit.FormKit';
import { Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let want: Want = {
  bundleName: 'com.ohos.exampledemo',
  abilityName: 'FormAbility',
  parameters: {
    'ohos.extra.param.key.form_dimension': 2,
    'ohos.extra.param.key.form_name': 'widget',
    'ohos.extra.param.key.module_name': 'entry'
  }
};
try {
  formAgent.requestPublishForm(want, (error: BusinessError, data: string) => {
    if (error) {
      console.error(`callback error, code: ${error.code}, message: ${error.message}`);
      return;
    }
    console.info(`formAgent requestPublishForm, form ID is: ${data}`);
  });
} catch (error) {
  console.error(`catch error, code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}`);
}
```

ArkTS-Sta示例：

```TypeScript
'use static'

import { formAgent } from '@kit.FormKit';
import { BusinessError, RecordData } from '@kit.BasicServicesKit';
import { Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const DOMAIN: int = 0x0000;
const TAG: string = 'testTag formAgentTest';

let want: Want = {
  bundleName: 'com.ohos.exampledemo',
  abilityName: 'FormAbility',
  parameters: {
    'ohos.extra.param.key.form_dimension': 2,
    'ohos.extra.param.key.form_name': 'widget',
    'ohos.extra.param.key.module_name': 'entry'
  } as Record<string, RecordData>
};
try {
  formAgent.requestPublishForm(want, (error: BusinessError | null, data: string | undefined) => {
    if (error?.code !== 0) {
      hilog.error(DOMAIN, TAG,
        `formAgent requestPublishForm callback error, code: ${error?.code}, message: ${error?.message}`);
      return;
    }
    console.info('testTag', `formAgent requestPublishForm callback success`);
  });
} catch (e) {
  let code = e.code;
  let message = e.message;
  hilog.error(DOMAIN, TAG, `formAgent requestPublishForm callback error, code: ${code}, message: ${message}`);
}
```

ArkTS-Dyn示例：

```TypeScript
import { formAgent } from '@kit.FormKit';
import { Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let want: Want = {
  bundleName: 'com.ohos.exampledemo',
  abilityName: 'FormAbility',
  parameters: {
    'ohos.extra.param.key.form_dimension': 2,
    'ohos.extra.param.key.form_name': 'widget',
    'ohos.extra.param.key.module_name': 'entry'
  }
};
try {
  formAgent.requestPublishForm(want).then((data: string) => {
    console.info(`formAgent requestPublishForm success, form ID is : ${data}`);
  }).catch((error: BusinessError) => {
    console.error(`promise error, code: ${error.code}, message: ${error.message}`);
  });
} catch (error) {
  console.error(`catch error, code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}`);
}
```

ArkTS-Sta示例：

```TypeScript
'use static'

import { formAgent } from '@kit.FormKit';
import { BusinessError, RecordData } from '@kit.BasicServicesKit';
import { Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const DOMAIN: int = 0x0000;
const TAG: string = 'testTag formAgentTest';

let want: Want = {
  bundleName: 'com.ohos.exampledemo',
  abilityName: 'FormAbility',
  parameters: {
    'ohos.extra.param.key.form_dimension': 2,
    'ohos.extra.param.key.form_name': 'widget',
    'ohos.extra.param.key.module_name': 'entry'
  } as Record<string, RecordData>
};
try {
  formAgent.requestPublishForm(want).then((data: string) => {
    console.info('testTag', `formAgent requestPublishForm promise success`);
  }).catch((e) => {
    let code = e.code;
    let message = e.message;
    hilog.error(DOMAIN, TAG, `formAgent requestPublishForm promise error, code: ${code}, message: ${message}`);
  });
} catch (e) {
  let code = e.code;
  let message = e.message;
  hilog.error(DOMAIN, TAG, `formAgent requestPublishForm promise catch error, code: ${code}, message: ${message}`);
}
```


## requestPublishForm

```TypeScript
function requestPublishForm(want: Want): Promise<string>
```

请求发布一张卡片到使用方，使用Promise异步回调。使用方通常为桌面。适用于系统应用需要主动将卡片添加到桌面的场景。

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.AGENT_REQUIRE_FORM

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| want | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16500050](../errorcode-form.md#16500050-进程间通信失败) |
| [16500100](../errorcode-form.md#16500100-获取卡片配置信息失败) |
| [16501000](../errorcode-form.md#16501000-内部功能错误) |
| [16501002](../errorcode-form.md#16501002-卡片数量达到上限) |
| [16501008](../errorcode-form.md#16501008-等待卡片加桌超时) |
| [16501017](../errorcode-form.md#16501017-无空间发布卡片) |
| [16501018](../errorcode-form.md#16501018-卡片不支持发布) |

**示例**

参见 [requestPublishForm](#requestpublishform)
