# unregisterRemoteAuthCallback（系统接口）

## unregisterRemoteAuthCallback

```TypeScript
function unregisterRemoteAuthCallback(): void
```

注销远程认证回调。该接口用于注销已注册的远程认证回调，注销后系统不再接收远程认证的页面参数请求和认证结果通知。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.ACCESS_USER_AUTH_INTERNAL

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-userAuth-function unregisterRemoteAuthCallback(): void--><!--Device-userAuth-function unregisterRemoteAuthCallback(): void-End-->

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**系统接口：** 此接口为系统接口。

**错误码：**

| 错误码ID |
| --- |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |
| [12500002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-user-authentication-kit/errorcode-useriam.md#12500002-身份认证系统通用错误码) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { userAuth } from '@kit.UserAuthenticationKit';

try {
  userAuth.unregisterRemoteAuthCallback();
  console.info('Remote auth callback unregistered successfully');
} catch (error) {
  const err: BusinessError = error as BusinessError;
  console.error(`failed to unregister remote auth callback. Code is ${err?.code}, message is ${err?.message}`);
}
```
