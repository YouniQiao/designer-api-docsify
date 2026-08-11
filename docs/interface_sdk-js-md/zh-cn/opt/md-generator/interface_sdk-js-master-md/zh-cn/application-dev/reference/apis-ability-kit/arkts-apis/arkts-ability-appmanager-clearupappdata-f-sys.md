# clearUpAppData（系统接口）

## clearUpAppData

```TypeScript
function clearUpAppData(bundleName: string, appCloneIndex?: number): Promise<void>
```

根据Bundle名称和应用分身索引，清除指定应用的数据。使用Promise异步回调。

**起始版本：** 13

**需要权限：** ohos.permission.CLEAN_APPLICATION_DATA

<!--Device-appManager-function clearUpAppData(bundleName: string, appCloneIndex?: int): Promise<void>--><!--Device-appManager-function clearUpAppData(bundleName: string, appCloneIndex?: int): Promise<void>-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |
| appCloneIndex | number | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [16000073](../errorcode-ability.md#16000073-传入的appcloneindex是一个无效值) |

## 示例

```TypeScript
import { appManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let bundleName: string = 'com.ohos.demo';
let appCloneIndex: number = 0;

try {
  appManager.clearUpAppData(bundleName, appCloneIndex).then(() => {
    console.info(`clearUpAppData success.`);
  }).catch((err: BusinessError) => {
    console.error(`clearUpAppData fail, err: ${JSON.stringify(err)}`);
  });
} catch (paramError) {
  let code = (paramError as BusinessError).code;
  let message = (paramError as BusinessError).message;
  console.error(`[appManager] error: ${code}, ${message}`);
}
```
