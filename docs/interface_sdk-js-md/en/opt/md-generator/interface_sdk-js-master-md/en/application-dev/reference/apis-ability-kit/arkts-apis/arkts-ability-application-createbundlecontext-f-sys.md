# createBundleContext (System API)

## Modules to Import

```TypeScript
import { application } from 'kits/@kit.AbilityKit';
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

**Required permissions:** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

**Model restriction:** This API can be used only in the stage model.

<!--Device-application-export function createBundleContext(context: Context, bundleName: string): Promise<Context>--><!--Device-application-export function createBundleContext(context: Context, bundleName: string): Promise<Context>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [Context](arkts-ability-context-c-sys.md) | Yes |
| bundleName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[Context](arkts-ability-context-c-sys.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

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
