# createBundleContext (System API)

## Modules to Import

```TypeScript
import { application } from '@kit.AbilityKit';
```

## createBundleContext

```TypeScript
export function createBundleContext(context: Context, bundleName: string): Promise<Context>
```

Creates the context for an application. This API uses a promise to return the result.

> **NOTE：**
> 
> Starting from API version 18, the context can obtain the
> [process name](../../../reference/apis-ability-kit/js-apis-inner-application-context.md#context) of the current
> application. The **processName** property in the context created by **createBundleContext** is the same as the
> **processName** property in the input parameter **Context**. The values of other properties are obtained based on
> the input parameters **Context**, **bundleName**, and **moduleName**.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

**Model restriction:** This API can be used only in the stage model.

<!--Device-application-export function createBundleContext(context: Context, bundleName: string): Promise<Context>--><!--Device-application-export function createBundleContext(context: Context, bundleName: string): Promise<Context>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [Context](arkts-ability-context-c.md) | Yes | Application context. |
| bundleName | string | Yes | Bundle name of the application. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[Context](arkts-ability-context-c.md)&gt; | Promise used to return the context created. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission denied, non-system app called system api. |

## Examples

```TypeScript
import { UIAbility, application, common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onCreate() {
    let moduleContext: common.Context;
    try {
      application.createBundleContext(this.context, 'bundlename').then((data: Context)=>{
        moduleContext = data;
        console.info('createBundleContext success!');
      }).catch((error : BusinessError)=>{
        console.error(`createBundleContext failed, error.code: ${(error as BusinessError).code}, error.message: ${(error as BusinessError).message}`);
      })
    } catch (error) {
      console.error(`createBundleContext failed, error.code: ${(error as BusinessError).code}, error.message: ${(error as BusinessError).message}`);
    }
  }
}
```

