# createDataShareHelper（系统接口）

## createDataShareHelper

```TypeScript
function createDataShareHelper(context: Context, uri: string, callback: AsyncCallback<DataShareHelper>): void
```

创建DataShareHelper实例。使用callback异步回调。

**起始版本：** 23

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-dataShare-function createDataShareHelper(context: Context, uri: string, callback: AsyncCallback<DataShareHelper>): void--><!--Device-dataShare-function createDataShareHelper(context: Context, uri: string, callback: AsyncCallback<DataShareHelper>): void-End-->

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Consumer

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | 是 |
| uri | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[DataShareHelper](arkts-arkdata-datashare-datasharehelper-i-sys.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15700010](../errorcode-datashare.md#15700010-创建datasharehelper异常) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

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

**起始版本：** 23

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-dataShare-function createDataShareHelper(    context: Context,    uri: string,    options: DataShareHelperOptions,    callback: AsyncCallback<DataShareHelper>  ): void--><!--Device-dataShare-function createDataShareHelper(    context: Context,    uri: string,    options: DataShareHelperOptions,    callback: AsyncCallback<DataShareHelper>  ): void-End-->

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Consumer

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | 是 |
| uri | string | 是 |
| options | [DataShareHelperOptions](arkts-arkdata-datashare-datasharehelperoptions-i-sys.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[DataShareHelper](arkts-arkdata-datashare-datasharehelper-i-sys.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15700010](../errorcode-datashare.md#15700010-创建datasharehelper异常) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

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

**起始版本：** 23

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-dataShare-function createDataShareHelper(    context: Context,    uri: string,    options?: DataShareHelperOptions  ): Promise<DataShareHelper>--><!--Device-dataShare-function createDataShareHelper(    context: Context,    uri: string,    options?: DataShareHelperOptions  ): Promise<DataShareHelper>-End-->

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Consumer

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | 是 |
| uri | string | 是 |
| options | [DataShareHelperOptions](arkts-arkdata-datashare-datasharehelperoptions-i-sys.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[DataShareHelper](arkts-arkdata-datashare-datasharehelper-i-sys.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15700010](../errorcode-datashare.md#15700010-创建datasharehelper异常) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

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
