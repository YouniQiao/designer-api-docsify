# createDataShareHelper (System API)

## Modules to Import

```TypeScript
import { dataShare } from '@kit.ArkData';
```

## createDataShareHelper

```TypeScript
function createDataShareHelper(context: Context, uri: string, callback: AsyncCallback<DataShareHelper>): void
```

Creates a **DataShareHelper** instance. This API uses an asynchronous callback to return the result.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-dataShare-function createDataShareHelper(context: Context, uri: string, callback: AsyncCallback<DataShareHelper>): void--><!--Device-dataShare-function createDataShareHelper(context: Context, uri: string, callback: AsyncCallback<DataShareHelper>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | Yes |
| uri | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[DataShareHelper](arkts-arkdata-datashare-datasharehelper-i-sys.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [15700010](../errorcode-datashare.md#15700010-failed-to-create-a-datasharehelper) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

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

Creates a **DataShareHelper** instance. **DataShareHelperOptions** specifies whether **DataShareHelper** is in proxy mode. This API uses an asynchronous callback to return the result.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-dataShare-function createDataShareHelper(    context: Context,    uri: string,    options: DataShareHelperOptions,    callback: AsyncCallback<DataShareHelper>  ): void--><!--Device-dataShare-function createDataShareHelper(    context: Context,    uri: string,    options: DataShareHelperOptions,    callback: AsyncCallback<DataShareHelper>  ): void-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | Yes |
| uri | string | Yes |
| options | [DataShareHelperOptions](arkts-arkdata-datashare-datasharehelperoptions-i-sys.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[DataShareHelper](arkts-arkdata-datashare-datasharehelper-i-sys.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [15700010](../errorcode-datashare.md#15700010-failed-to-create-a-datasharehelper) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

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

Creates a **DataShareHelper** instance. **DataShareHelperOptions** specifies whether **DataShareHelper** is in proxy mode. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-dataShare-function createDataShareHelper(    context: Context,    uri: string,    options?: DataShareHelperOptions  ): Promise<DataShareHelper>--><!--Device-dataShare-function createDataShareHelper(    context: Context,    uri: string,    options?: DataShareHelperOptions  ): Promise<DataShareHelper>-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | Yes |
| uri | string | Yes |
| options | [DataShareHelperOptions](arkts-arkdata-datashare-datasharehelperoptions-i-sys.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[DataShareHelper](arkts-arkdata-datashare-datasharehelper-i-sys.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [15700010](../errorcode-datashare.md#15700010-failed-to-create-a-datasharehelper) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

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
