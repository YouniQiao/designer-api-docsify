# isApplicationRunning（系统接口）

## isApplicationRunning

```TypeScript
function isApplicationRunning(bundleName: string): Promise<boolean>
```

查询所有用户下指定包名的应用是否正在运行。使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.GET_RUNNING_INFO

<!--Device-appManager-function isApplicationRunning(bundleName: string): Promise<boolean>--><!--Device-appManager-function isApplicationRunning(bundleName: string): Promise<boolean>-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { appManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let bundleName = 'com.example.myapplication';

appManager.isApplicationRunning(bundleName).then((data) => {
  console.info(`The application running is: ${JSON.stringify(data)}`);
}).catch((error: BusinessError) => {
  console.error(`error: ${JSON.stringify(error)}`);
});
```


## isApplicationRunning

```TypeScript
function isApplicationRunning(bundleName: string, callback: AsyncCallback<boolean>): void
```

查询所有用户下指定包名的应用是否正在运行。使用callback异步回调。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.GET_RUNNING_INFO

<!--Device-appManager-function isApplicationRunning(bundleName: string, callback: AsyncCallback<boolean>): void--><!--Device-appManager-function isApplicationRunning(bundleName: string, callback: AsyncCallback<boolean>): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { appManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let bundleName = 'com.example.myapplication';

try {
  appManager.isApplicationRunning(bundleName, (err, data) => {
    if (err) {
      console.error(`err: ${JSON.stringify(err)}`);
    } else {
      console.info(`The application running is: ${JSON.stringify(data)}`);
    }
  });
} catch (paramError) {
  let code = (paramError as BusinessError).code;
  let message = (paramError as BusinessError).message;
  console.error(`[appManager] error: ${code}, ${message}`);
}
```
