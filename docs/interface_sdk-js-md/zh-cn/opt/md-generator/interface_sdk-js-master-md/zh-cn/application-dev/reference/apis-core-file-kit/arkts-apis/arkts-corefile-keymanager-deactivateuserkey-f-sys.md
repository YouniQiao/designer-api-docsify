# deactivateUserKey（系统接口）

## deactivateUserKey

```TypeScript
function deactivateUserKey(userId: number):void
```

用户锁屏时，同步卸载指定用户对应密钥。**（该接口目前仅开放给锁屏应用）**

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.STORAGE_MANAGER_CRYPT

<!--Device-keyManager-function deactivateUserKey(userId: long):void--><!--Device-keyManager-function deactivateUserKey(userId: long):void-End-->

**系统能力：** SystemCapability.FileManagement.StorageService.Encryption

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| userId | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 13600009 |
| 13600008 |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| 13600001 |

## 示例

```TypeScript
import { keyManager } from '@kit.CoreFileKit';
import { BusinessError } from '@kit.BasicServicesKit';
let userId: number = 100;
try {
  keyManager.deactivateUserKey(userId);
  console.info('deactivateUserKey success');
} catch (err) {
  let error: BusinessError = err as BusinessError;
  console.error(`deactivateUserKey failed with error. Code: ${error.code}, message: ${error.message}`);
}
```
