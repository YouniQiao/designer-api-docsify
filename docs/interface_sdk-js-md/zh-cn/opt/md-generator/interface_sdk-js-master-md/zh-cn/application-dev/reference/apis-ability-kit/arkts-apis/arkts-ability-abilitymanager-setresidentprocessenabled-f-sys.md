# setResidentProcessEnabled（系统接口）

## setResidentProcessEnabled

```TypeScript
function setResidentProcessEnabled(bundleName: string, enable: boolean): Promise<void>
```

常驻进程支持按需启停。

**起始版本：** 12

<!--Device-abilityManager-function setResidentProcessEnabled(bundleName: string, enable: boolean): Promise<void>--><!--Device-abilityManager-function setResidentProcessEnabled(bundleName: string, enable: boolean): Promise<void>-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |
| enable | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [16200006](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16200006-没有权限设置常驻进程使能状态) |
| [16000050](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000050-内部错误) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { abilityManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  // 设置常驻进程的包名
  let residentProcessBundleName: string = 'com.xxx.xxxxxx';
  let enable: boolean = false;
  abilityManager.setResidentProcessEnabled(residentProcessBundleName, enable)
    .then(() => {
      console.info('setResidentProcessEnabled success.');
    })
    .catch((err: BusinessError) => {
      console.error(`setResidentProcessEnabled fail, err: ${JSON.stringify(err)}`);
    });
} catch (err) {
  let code = (err as BusinessError).code;
  let message = (err as BusinessError).message;
  console.error(`setResidentProcessEnabled failed, code is ${code}, message is ${message}`);
}
```
