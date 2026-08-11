# isAppRunning

## isAppRunning

```TypeScript
function isAppRunning(bundleName: string, appCloneIndex?: number): Promise<boolean>
```

判断所有用户下指定包名和分身应用索引的应用是否正在运行。使用Promise异步回调。

> **说明：**
> 
> 如果当前用户未安装该应用，则返回错误码16000073；如果当前用户已安装该应用，则判断所有用户下该指定应用是否正在运行。

**起始版本：** 14

**需要权限：** ohos.permission.GET_RUNNING_INFO

<!--Device-appManager-function isAppRunning(bundleName: string, appCloneIndex?: int): Promise<boolean>--><!--Device-appManager-function isAppRunning(bundleName: string, appCloneIndex?: int): Promise<boolean>-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |
| appCloneIndex | number | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;boolean&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [16000073](../errorcode-ability.md#16000073-传入的appcloneindex是一个无效值) |

## 示例

```TypeScript
import { appManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let bundleName = 'ohos.samples.etsclock';
  appManager.isAppRunning(bundleName).then((data: boolean) => {
      console.info(`data: ${JSON.stringify(data)}`);
    }).catch((err: BusinessError) => {
      console.error(`isAppRunning error, code: ${err.code}, msg:${err.message}`);
    });
} catch (err) {
  let code = (err as BusinessError).code;
  let message = (err as BusinessError).message;
  console.error(`isAppRunning error, code: ${code}, msg:${message}`);
}
```
