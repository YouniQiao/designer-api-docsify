# deactivateUserKey（系统接口）

## 导入模块

```TypeScript
import { keyManager } from '@kit.CoreFileKit';
```

## deactivateUserKey

```TypeScript
function deactivateUserKey(userId: long):void
```

用户锁屏时，同步卸载指定用户对应密钥。**（该接口目前仅开放给锁屏应用）**

**起始版本：** 15

**ArkTS模式：** ArkTS-Dyn起始版本为15；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.STORAGE_MANAGER_CRYPT

**系统能力：** SystemCapability.FileManagement.StorageService.Encryption

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| userId | ArkTS-Dyn: number<br>ArkTS-Sta：long | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 13600001 |
| 13600008 |
| 13600009 |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let userId: number = 100;
try {
  keyManager.deactivateUserKey(userId);
  console.info('deactivateUserKey success');
} catch (err) {
  let error: BusinessError = err as BusinessError;
  console.error(`deactivateUserKey failed with error, code is: ${err.code}, message is: ${err.message}`);
}
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let userId: long = 100;
try {
  keyManager.deactivateUserKey(userId);
  console.info('deactivateUserKey success');
} catch (err) {
  let error: BusinessError = err as BusinessError;
  console.error(`deactivateUserKey failed with error, code is: ${err.code}, message is: ${err.message}`);
}
```
