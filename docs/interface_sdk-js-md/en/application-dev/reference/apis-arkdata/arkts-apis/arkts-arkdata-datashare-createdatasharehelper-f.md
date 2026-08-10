# createDataShareHelper

## Modules to Import

```TypeScript
import { dataShare } from 'kits/@kit.ArkData';
```

## createDataShareHelper

```TypeScript
function createDataShareHelper(context: Context, uri: string, callback: AsyncCallback<DataShareHelper>): void
```

创建DataShareHelper实例。使用callback异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-dataShare-function createDataShareHelper(context: Context, uri: string, callback: AsyncCallback<DataShareHelper>): void--><!--Device-dataShare-function createDataShareHelper(context: Context, uri: string, callback: AsyncCallback<DataShareHelper>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | Yes | 应用的上下文环境。 |
| uri | string | Yes | 要连接的服务端应用的路径。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;DataShareHelper&gt; | Yes | 回调函数。当创建DataShareHelper实例成功，err为undefined，data为获取到的 DataShareHelper实例；否则为错误对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error.Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15700010 | The DataShareHelper fails to be initialized. |
| 202 | Permission verification failed. A non-system application calls a system API.<br>**Applicable version:** 19 and later |

## Examples

```TypeScript
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    let uri = "datashare:///com.samples.datasharetest.DataShare";
    let dataShareHelper: dataShare.DataShareHelper | undefined = undefined;
    let context = this.context;
    try {
      dataShare.createDataShareHelper(context, uri, (err:BusinessError, data:dataShare.DataShareHelper) => {
        if (err !== undefined) {
          console.error(`Failed to create DataShareHelper. Code: ${err.code}, message: ${err.message}`);
          return;
        }
        console.info("createDataShareHelper succeed, data : " + data);
        dataShareHelper = data;
      });
    } catch (err) {
      let code = (err as BusinessError).code;
      let message = (err as BusinessError).message;
      console.error(`Failed to create DataShareHelper. Code: ${code}, message: ${message}`);
    };
  }
}
```


## createDataShareHelper

```TypeScript
function createDataShareHelper(
    context: Context,
    uri: string,
    options: DataShareHelperOptions,
    callback: AsyncCallback<DataShareHelper>
  ): void
```

创建DataShareHelper实例，通过DataShareHelperOptions指定是否通过代理访问。使用callback异步回调。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-dataShare-function createDataShareHelper(    context: Context,    uri: string,    options: DataShareHelperOptions,    callback: AsyncCallback<DataShareHelper>  ): void--><!--Device-dataShare-function createDataShareHelper(    context: Context,    uri: string,    options: DataShareHelperOptions,    callback: AsyncCallback<DataShareHelper>  ): void-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | Yes | Indicates the application context. |
| uri | string | Yes | Indicates the path of the file to open. |
| options | [DataShareHelperOptions](arkts-arkdata-datashare-datasharehelperoptions-i.md) | Yes | Indicates the optional config. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;DataShareHelper&gt; | Yes | {DataShareHelper}: The dataShareHelper for consumer. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error.Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15700010 | The DataShareHelper fails to be initialized. |
| 202 | Permission verification failed. A non-system application calls a system API.<br>**Applicable version:** 19 and later |

## Examples

```TypeScript
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    let uri = "datashareproxy://com.samples.datasharetest.DataShare";
    let dataShareHelper: dataShare.DataShareHelper | undefined = undefined;
    let context = this.context;
    try {
      dataShare.createDataShareHelper(context, uri, {isProxy : true}, (err:BusinessError, data:dataShare.DataShareHelper) => {
        if (err !== undefined) {
          console.error(`Failed to create DataShareHelper. Code: ${err.code}, message: ${err.message}`);
          return;
        }
        console.info("createDataShareHelper succeed, data : " + data);
        dataShareHelper = data;
      });
    } catch (err) {
      let code = (err as BusinessError).code;
      let message = (err as BusinessError).message;
      console.error(`Failed to create DataShareHelper. Code: ${code}, message: ${message}`);
    };
  }
}
```


## createDataShareHelper

```TypeScript
function createDataShareHelper(
    context: Context,
    uri: string,
    options?: DataShareHelperOptions
  ): Promise<DataShareHelper>
```

创建DataShareHelper实例，通过DataShareHelperOptions指定是否通过代理访问。使用Promise异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-dataShare-function createDataShareHelper(    context: Context,    uri: string,    options?: DataShareHelperOptions  ): Promise<DataShareHelper>--><!--Device-dataShare-function createDataShareHelper(    context: Context,    uri: string,    options?: DataShareHelperOptions  ): Promise<DataShareHelper>-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | Yes | 应用的上下文环境。 |
| uri | string | Yes | 要连接的服务端应用的路径。 |
| options | [DataShareHelperOptions](arkts-arkdata-datashare-datasharehelperoptions-i.md) | No | 可选配置。指定[DataShareHelper](arkts-arkdata-datashare-datasharehelperoptions-i.md)是否在代理模式 下，指定非静默访问时的等待拉起时间。如果不设置，则表示[DataShareHelper](arkts-arkdata-datashare-datasharehelperoptions-i.md)不在代理模式下，且非静默访问时的等待拉起时间 为2秒。如果uri以datashareproxy为开头，则必须设置options的isProxy参数，否则DataShareHelper创建失败返回错误。<br>**Since:** 10 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;DataShareHelper&gt; | Promise对象。返回DataShareHelper实例。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error.Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15700010 | The DataShareHelper fails to be initialized. |
| 202 | Permission verification failed. A non-system application calls a system API.<br>**Applicable version:** 19 and later |

## Examples

```TypeScript
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    let uri = "datashareproxy://com.samples.datasharetest.DataShare";
    let dataShareHelper: dataShare.DataShareHelper | undefined = undefined;
    let context = this.context;
    try {
      dataShare.createDataShareHelper(context, uri, {isProxy : true}).then((data: dataShare.DataShareHelper) => {
        console.info("createDataShareHelper succeed, data : " + data);
        dataShareHelper = data;
      }).catch((err: BusinessError) => {
        console.error(`Failed to create DataShareHelper. Code: ${err.code}, message: ${err.message}`);
      });
    } catch (err) {
      let code = (err as BusinessError).code;
      let message = (err as BusinessError).message;
      console.error(`Failed to create DataShareHelper. Code: ${code}, message: ${message}`);
    };
  }
}
```

