# queryBusinessAbilityInfo（系统接口）

## 导入模块

```TypeScript
import { businessAbilityRouter } from 'kits/@kit.AbilityKit';
```

## queryBusinessAbilityInfo

```TypeScript
function queryBusinessAbilityInfo(
    filter: BusinessAbilityFilter,
    callback: AsyncCallback<Array<BusinessAbilityInfo>>
  ): void
```

Query the business ability info of by the given filter. ohos.permission.GET_BUNDLE_INFO_PRIVILEGED is required for cross user access.

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

<!--Device-businessAbilityRouter-function queryBusinessAbilityInfo(    filter: BusinessAbilityFilter,    callback: AsyncCallback<Array<BusinessAbilityInfo>>  ): void--><!--Device-businessAbilityRouter-function queryBusinessAbilityInfo(    filter: BusinessAbilityFilter,    callback: AsyncCallback<Array<BusinessAbilityInfo>>  ): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| filter | [BusinessAbilityFilter](arkts-ability-businessabilityrouter-businessabilityfilter-i-sys.md) | 是 | Indicates the filter containing the business ability info to be queried. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;BusinessAbilityInfo&gt;&gt; | 是 | The callback of querying business ability info result. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 201 | Permission denied. |
| 202 | non-system app called system api. |

## 示例

```TypeScript
import { businessAbilityRouter } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let filter: businessAbilityRouter.BusinessAbilityFilter = { businessType: businessAbilityRouter.BusinessType.SHARE };

try {
  businessAbilityRouter.queryBusinessAbilityInfo(filter, (error, data) => {
    if (error) {
      console.error('queryBusinessAbilityInfo failed ' + error.message);
      return;
    }
    console.info('queryBusinessAbilityInfo success');
  });
} catch (error) {
  let message = (error as BusinessError).message;
  console.error('queryBusinessAbilityInfo failed ' + message);
}
```


## queryBusinessAbilityInfo

```TypeScript
function queryBusinessAbilityInfo(filter: BusinessAbilityFilter): Promise<Array<BusinessAbilityInfo>>
```

Query the business ability info of by the given filter. ohos.permission.GET_BUNDLE_INFO_PRIVILEGED is required for cross user access.

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

<!--Device-businessAbilityRouter-function queryBusinessAbilityInfo(filter: BusinessAbilityFilter): Promise<Array<BusinessAbilityInfo>>--><!--Device-businessAbilityRouter-function queryBusinessAbilityInfo(filter: BusinessAbilityFilter): Promise<Array<BusinessAbilityInfo>>-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| filter | [BusinessAbilityFilter](arkts-ability-businessabilityrouter-businessabilityfilter-i-sys.md) | 是 | Indicates the filter containing the business ability info to be queried. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;Array&lt;BusinessAbilityInfo&gt;&gt; | Returns a list of business ability info objects. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 201 | Permission denied. |
| 202 | non-system app called system api. |

## 示例

```TypeScript
import { businessAbilityRouter } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let filter: businessAbilityRouter.BusinessAbilityFilter = { businessType: businessAbilityRouter.BusinessType.SHARE };

try {
  businessAbilityRouter.queryBusinessAbilityInfo(filter)
    .then(() => {
      console.info('queryBusinessAbilityInfo success');
    }).catch((error: BusinessError) => {
    console.error('queryBusinessAbilityInfo failed ' + error.message);
  });
} catch (error) {
  let message = (error as BusinessError).message;
  console.error('queryBusinessAbilityInfo failed ' + message);
}
```

