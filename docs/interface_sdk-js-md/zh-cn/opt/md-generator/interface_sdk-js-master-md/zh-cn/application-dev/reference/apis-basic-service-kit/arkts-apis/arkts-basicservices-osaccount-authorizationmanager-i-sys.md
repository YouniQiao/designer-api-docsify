# AuthorizationManager（系统接口）

系统账号授权管理类，用于管理系统账号授权。

**起始版本：** 24

**废弃版本：** -1

<!--Device-osAccount-interface AuthorizationManager--><!--Device-osAccount-interface AuthorizationManager-End-->

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

## acquireAuthorization

```TypeScript
acquireAuthorization(privilege: string, options?: AcquireAuthorizationOptions): Promise<AcquireAuthorizationResult>
```

为当前进程获取授权。

**起始版本：** 24

**废弃版本：** -1

**需要权限：** ohos.permission.ACQUIRE_LOCAL_ACCOUNT_AUTHORIZATION

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AuthorizationManager-acquireAuthorization(privilege: string, options?: AcquireAuthorizationOptions): Promise<AcquireAuthorizationResult>--><!--Device-AuthorizationManager-acquireAuthorization(privilege: string, options?: AcquireAuthorizationOptions): Promise<AcquireAuthorizationResult>-End-->

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| privilege | string | 是 |
| options | [AcquireAuthorizationOptions](arkts-basicservices-osaccount-acquireauthorizationoptions-i-sys.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[AcquireAuthorizationResult](arkts-basicservices-osaccount-acquireauthorizationresult-i-sys.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [12300002](../../apis-basic-services-kit/errorcode-account.md#12300002-无效参数) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-系统服务异常) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let authorizationManager: osAccount.AuthorizationManager = osAccount.getAuthorizationManager();
let privilege: string = 'testPrivilege';
let options: osAccount.AcquireAuthorizationOptions = {
  challenge: new Uint8Array([1, 2, 3]),
  isReuseNeeded: true,
  isInteractionAllowed: true,
};
try {
  authorizationManager.acquireAuthorization(privilege, options).then((result: osAccount.AcquireAuthorizationResult) => {
    console.info(`acquireAuthorization successfully, resultCode: ${result.resultCode}`);
  }).catch((err: BusinessError) => {
    console.error(`acquireAuthorization failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`acquireAuthorization exception: code is ${err.code}, message is ${err.message}`);
}
```

## hasAuthorization

```TypeScript
hasAuthorization(privilege: string): Promise<boolean>
```

检查当前进程是否已获得指定特权的授权。

**起始版本：** 24

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AuthorizationManager-hasAuthorization(privilege: string): Promise<boolean>--><!--Device-AuthorizationManager-hasAuthorization(privilege: string): Promise<boolean>-End-->

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| privilege | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

**错误码：**

| 错误码ID |
| --- |
| [12300002](../../apis-basic-services-kit/errorcode-account.md#12300002-无效参数) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-系统服务异常) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let authorizationManager: osAccount.AuthorizationManager = osAccount.getAuthorizationManager();
let privilege: string = 'testPrivilege';

try {
  authorizationManager.hasAuthorization(privilege).then((isAuthorized: boolean) => {
    console.info(`Privilege: ${privilege} has been authorized: ${isAuthorized}`);
  }).catch((e:Error) => {
    const err = e as BusinessError;
    console.error(`hasAuthorization failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`hasAuthorization exception: code is ${err.code}, message is ${err.message}`);
}
```

## releaseAuthorization

```TypeScript
releaseAuthorization(privilege: string): Promise<void>
```

为当前进程撤销指定特权的授权。

**起始版本：** 24

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AuthorizationManager-releaseAuthorization(privilege: string): Promise<void>--><!--Device-AuthorizationManager-releaseAuthorization(privilege: string): Promise<void>-End-->

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| privilege | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [12300002](../../apis-basic-services-kit/errorcode-account.md#12300002-无效参数) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-系统服务异常) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let authorizationManager: osAccount.AuthorizationManager = osAccount.getAuthorizationManager();
let privilege: string = 'testPrivilege';

try {
  authorizationManager.releaseAuthorization(privilege).then(() => {
    console.info('releaseAuthorization success');
  }).catch((e:Error) => {
    const err = e as BusinessError;
    console.error(`releaseAuthorization failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`releaseAuthorization exception: code is ${err.code}, message is ${err.message}`);
}
```
