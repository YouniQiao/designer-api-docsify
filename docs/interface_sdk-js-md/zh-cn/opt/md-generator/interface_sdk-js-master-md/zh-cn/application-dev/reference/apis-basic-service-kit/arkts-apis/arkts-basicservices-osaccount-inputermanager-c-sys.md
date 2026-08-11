# InputerManager（系统接口）

凭据输入管理器。

**起始版本：** 9

<!--Device-osAccount-class InputerManager--><!--Device-osAccount-class InputerManager-End-->

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

## registerInputer

```TypeScript
static registerInputer(authType: AuthType, inputer: IInputer): void
```

注册凭据输入器。

**起始版本：** 9

**需要权限：** ohos.permission.ACCESS_USER_AUTH_INTERNAL or ohos.permission.MANAGE_USER_IDM

<!--Device-InputerManager-static registerInputer(authType: AuthType, inputer: IInputer): void--><!--Device-InputerManager-static registerInputer(authType: AuthType, inputer: IInputer): void-End-->

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| authType | [AuthType](arkts-basicservices-osaccount-authtype-e-sys.md) | 是 |
| inputer | [IInputer](arkts-basicservices-osaccount-iinputer-i-sys.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [12300106](../../apis-basic-services-kit/errorcode-account.md#12300106-认证类型不支持) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [12300002](../../apis-basic-services-kit/errorcode-account.md#12300002-无效参数) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-系统服务异常) |
| [12300103](../../apis-basic-services-kit/errorcode-account.md#12300103-凭据输入器已注册) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let authType: osAccount.AuthType = osAccount.AuthType.DOMAIN;
let password: Uint8Array = new Uint8Array([0, 0, 0, 0, 0]);
try {
  osAccount.InputerManager.registerInputer(authType, {
    onGetData: (authSubType: osAccount.AuthSubType, callback: osAccount.IInputData) => {
      callback.onSetData(authSubType, password);
    }
  });
  console.info('registerInputer success.');
} catch (e) {
  const err = e as BusinessError;
  console.error(`registerInputer exception = code is ${err.code}, message is ${err.message}`);
}
```

## unregisterInputer

```TypeScript
static unregisterInputer(authType: AuthType): void
```

解注册凭据输入器。

**起始版本：** 9

**需要权限：** ohos.permission.ACCESS_USER_AUTH_INTERNAL or ohos.permission.MANAGE_USER_IDM

<!--Device-InputerManager-static unregisterInputer(authType: AuthType): void--><!--Device-InputerManager-static unregisterInputer(authType: AuthType): void-End-->

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| authType | [AuthType](arkts-basicservices-osaccount-authtype-e-sys.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [12300002](../../apis-basic-services-kit/errorcode-account.md#12300002-无效参数) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let authType: osAccount.AuthType = osAccount.AuthType.DOMAIN;
try {
  osAccount.InputerManager.unregisterInputer(authType);
  console.info('unregisterInputer success.');
} catch (e) {
  const err = e as BusinessError;
  console.error(`unregisterInputer code is ${err.code}, message is ${err.message}`);
}
```
