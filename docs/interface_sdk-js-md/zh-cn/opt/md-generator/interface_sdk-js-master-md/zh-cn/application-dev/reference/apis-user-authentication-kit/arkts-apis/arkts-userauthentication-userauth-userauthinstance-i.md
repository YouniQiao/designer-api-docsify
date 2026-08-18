# UserAuthInstance

用于执行用户身份认证，并支持使用统一用户身份认证控件。该接口提供了完整的用户认证能力，包括订阅认证结果、订阅认证中间状态、启动认证和取消认证等操作。通过统一认证控件，可以为用户提供标准化的认证界面和一致的认证体验。 使用以下接口前，需先通过[getUserAuthInstance](arkts-userauthentication-userauth-getuserauthinstance-f.md#getuserauthinstance)方法获取UserAuthInstance对象。 > **说明：** > > 每个UserAuthInstance实例只能用于一次认证过程。若需要再次认证，必须重新获取UserAuthInstance实例。

**起始版本：** 23

<!--Device-userAuth-interface UserAuthInstance--><!--Device-userAuth-interface UserAuthInstance-End-->

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

## 导入模块

```TypeScript
```

## cancel

```TypeScript
cancel(): void
```

取消认证。该接口常用于以下场景：应用因业务逻辑变化需要中止认证；超时或异常情况下中止认证操作。 > **说明：** > > 此时UserAuthInstance必须是正在进行认证的对象。

**起始版本：** 23

**需要权限：** ohos.permission.ACCESS_BIOMETRIC

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-UserAuthInstance-cancel(): void--><!--Device-UserAuthInstance-cancel(): void-End-->

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [12500002](../errorcode-useriam.md#12500002-身份认证系统通用错误码) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { userAuth } from '@kit.UserAuthenticationKit';

try {
  const rand = cryptoFramework.createRandom();
  const len: number = 16;
  let randData: Uint8Array | null = null;
  let retryCount = 0;
  while (retryCount < 3) {
    randData = rand?.generateRandomSync(len)?.data;
    if (randData) {
      break;
    }
    retryCount++;
  }
  if (!randData) {
    return;
  }
  const authParam : userAuth.AuthParam = {
    challenge: randData,
    authType: [userAuth.UserAuthType.PIN],
    authTrustLevel: userAuth.AuthTrustLevel.ATL3,
  };
  const widgetParam: userAuth.WidgetParam = {
    title: '请输入密码',
  };
  const userAuthInstance = userAuth.getUserAuthInstance(authParam, widgetParam);
  console.info('get userAuth instance successfully.');
  // 需要调用UserAuthInstance的start()接口，启动认证后，才能调用cancel()接口。
  userAuthInstance.start();
  console.info('auth start successfully.');
  userAuthInstance.cancel();
  console.info('auth cancel successfully.');
} catch (error) {
  const err: BusinessError = error as BusinessError;
  console.error(`auth failed. Code is ${err?.code}, message is ${err?.message}`);
}
```

## offAuthTip

```TypeScript
offAuthTip(callback?: AuthTipCallback): void
```

取消订阅用户身份认证中间状态。 > **说明：** > > 需要使用已经成功订阅事件的[UserAuthInstance](#userauthinstance)对象调用该接口进行取消订阅。

**起始版本：** 23

<!--Device-UserAuthInstance-offAuthTip(callback?: AuthTipCallback): void--><!--Device-UserAuthInstance-offAuthTip(callback?: AuthTipCallback): void-End-->

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AuthTipCallback](arkts-userauthentication-userauth-authtipcallback-t.md) | 否 |

**错误码：**

| 错误码ID |
| --- |
| [12500002](../errorcode-useriam.md#12500002-身份认证系统通用错误码) |

## offResult

```TypeScript
offResult(callback?: IAuthCallback): void
```

取消订阅用户身份认证的结果。 > **说明：** > > 需要使用已经成功订阅事件的[UserAuthInstance](#userauthinstance)对象调用该接口进行取消订阅。

**起始版本：** 23

<!--Device-UserAuthInstance-offResult(callback?: IAuthCallback): void--><!--Device-UserAuthInstance-offResult(callback?: IAuthCallback): void-End-->

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [IAuthCallback](arkts-userauthentication-userauth-iauthcallback-i.md) | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12500002](../errorcode-useriam.md#12500002-身份认证系统通用错误码) |

## off_authTip

```TypeScript
off(type: 'authTip', callback?: AuthTipCallback): void
```

取消订阅用户身份认证中间状态。该接口常用于以下场景：认证完成后清理订阅监听释放资源；不再需要监听认证过程中的提示信息时取消订阅；页面销毁或组件卸载时取消订阅。 > **说明：** > > 需要使用已经成功订阅事件的[UserAuthInstance](#userauthinstance)对象调用该接口进行取消订阅。

**起始版本：** 20

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-UserAuthInstance-off(type: 'authTip', callback?: AuthTipCallback): void--><!--Device-UserAuthInstance-off(type: 'authTip', callback?: AuthTipCallback): void-End-->

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'authTip' | 是 |
| callback | [AuthTipCallback](arkts-userauthentication-userauth-authtipcallback-t.md) | 否 |

**错误码：**

| 错误码ID |
| --- |
| [12500002](../errorcode-useriam.md#12500002-身份认证系统通用错误码) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { userAuth } from '@kit.UserAuthenticationKit';

try {
  const rand = cryptoFramework.createRandom();
  const len: number = 16;
  let randData: Uint8Array | null = null;
  let retryCount = 0;
  while (retryCount < 3) {
    randData = rand?.generateRandomSync(len)?.data;
    if (randData) {
      break;
    }
    retryCount++;
  }
  if (!randData) {
    return;
  }
  const authParam: userAuth.AuthParam = {
    challenge: randData,
    authType: [userAuth.UserAuthType.PIN],
    authTrustLevel: userAuth.AuthTrustLevel.ATL3,
  };
  const widgetParam: userAuth.WidgetParam = {
    title: '请输入密码',
  };
  const userAuthInstance = userAuth.getUserAuthInstance(authParam, widgetParam);
  console.info('get userAuth instance successfully.');
  userAuthInstance.off('authTip', (authTipInfo: userAuth.AuthTipInfo) => {
    console.info('userAuthInstance callback');
  });
  console.info('auth off successfully.');
} catch (error) {
  const err: BusinessError = error as BusinessError;
  console.error(`auth failed. Code is ${err?.code}, message is ${err?.message}`);
}
```

## off_result

```TypeScript
off(type: 'result', callback?: IAuthCallback): void
```

取消订阅用户身份认证的结果。该接口常用于以下场景：页面销毁或组件卸载时取消订阅；不再需要监听认证结果时释放资源。 > **说明：** > > 需要使用已经成功订阅事件的[UserAuthInstance](#userauthinstance)对象调用该接口进行取消订阅。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-UserAuthInstance-off(type: 'result', callback?: IAuthCallback): void--><!--Device-UserAuthInstance-off(type: 'result', callback?: IAuthCallback): void-End-->

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'result' | 是 |
| callback | [IAuthCallback](arkts-userauthentication-userauth-iauthcallback-i.md) | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12500002](../errorcode-useriam.md#12500002-身份认证系统通用错误码) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { userAuth } from '@kit.UserAuthenticationKit';

try {
  const rand = cryptoFramework.createRandom();
  const len: number = 16;
  let randData: Uint8Array | null = null;
  let retryCount = 0;
  while (retryCount < 3) {
    randData = rand?.generateRandomSync(len)?.data;
    if (randData) {
      break;
    }
    retryCount++;
  }
  if (!randData) {
    return;
  }
  const authParam: userAuth.AuthParam = {
    challenge: randData,
    authType: [userAuth.UserAuthType.PIN],
    authTrustLevel: userAuth.AuthTrustLevel.ATL3,
  };
  const widgetParam: userAuth.WidgetParam = {
    title: '请输入密码',
  };
  const userAuthInstance = userAuth.getUserAuthInstance(authParam, widgetParam);
  console.info('get userAuth instance successfully.');
  userAuthInstance.off('result', {
    onResult: (result) => {
      console.info(`auth off result = ${result.result}`);
    }
  });
  console.info('auth off successfully.');
} catch (error) {
  const err: BusinessError = error as BusinessError;
  console.error(`auth failed. Code is ${err?.code}, message is ${err?.message}`);
}
```

## onAuthTip

```TypeScript
onAuthTip(callback: AuthTipCallback): void
```

订阅身份认证过程中的提示信息。通过该接口可以获取到认证过程中控件的拉起和退出提示，以及认证过程中用户的每一次认证失败尝试。

**起始版本：** 23

<!--Device-UserAuthInstance-onAuthTip(callback: AuthTipCallback): void--><!--Device-UserAuthInstance-onAuthTip(callback: AuthTipCallback): void-End-->

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AuthTipCallback](arkts-userauthentication-userauth-authtipcallback-t.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [12500002](../errorcode-useriam.md#12500002-身份认证系统通用错误码) |

## onResult

```TypeScript
onResult(callback: IAuthCallback): void
```

订阅用户身份认证的最终结果。通过该接口获取到的是用户在认证控件完成身份认证交互后的最终身份认证结果。认证控件消失前，用户中间的认证失败尝试并不会通过该接口返回。 如果需要感知整个认证过程中用户的每一次认证失败尝试，请通过[on('authTip')](#onauthtip)接口订阅。

**起始版本：** 23

<!--Device-UserAuthInstance-onResult(callback: IAuthCallback): void--><!--Device-UserAuthInstance-onResult(callback: IAuthCallback): void-End-->

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [IAuthCallback](arkts-userauthentication-userauth-iauthcallback-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12500002](../errorcode-useriam.md#12500002-身份认证系统通用错误码) |

## on_authTip

```TypeScript
on(type: 'authTip', callback: AuthTipCallback): void
```

订阅身份认证过程中的提示信息。通过该接口可以获取到认证过程中控件的拉起和退出提示，以及认证过程中用户的每一次认证不通过尝试。使用callback异步回调。 > **说明：** > > 在PC/2in1设备上，应用如果使用模应用弹窗方式发起认证（即配置用户界面参数[widgetParam](arkts-userauthentication-userauth-widgetparam-i.md#widgetparam)时传入了有效的uiContext），收到认证结果后，若需弹出其 > 他窗口，应先获取控件弹窗释放的标志消息，通过 > [on('authTip')](#onresult)接口订阅控件释放消息（ > authTipInfo.tipCode = UserAuthTipCode.WIDGET_RELEASED）。

**起始版本：** 20

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-UserAuthInstance-on(type: 'authTip', callback: AuthTipCallback): void--><!--Device-UserAuthInstance-on(type: 'authTip', callback: AuthTipCallback): void-End-->

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'authTip' | 是 |
| callback | [AuthTipCallback](arkts-userauthentication-userauth-authtipcallback-t.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [12500002](../errorcode-useriam.md#12500002-身份认证系统通用错误码) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { userAuth } from '@kit.UserAuthenticationKit';

try {
  const rand = cryptoFramework.createRandom();
  const len: number = 16;
  let randData: Uint8Array | null = null;
  let retryCount = 0;
  while (retryCount < 3) {
    randData = rand?.generateRandomSync(len)?.data;
    if (randData) {
      break;
    }
    retryCount++;
  }
  if (!randData) {
    return;
  }
  const authParam: userAuth.AuthParam = {
    challenge: randData,
    authType: [userAuth.UserAuthType.PIN],
    authTrustLevel: userAuth.AuthTrustLevel.ATL3,
  };
  const widgetParam: userAuth.WidgetParam = {
    title: '请输入密码',
  };
  const userAuthInstance = userAuth.getUserAuthInstance(authParam, widgetParam);
  console.info('get userAuth instance successfully.');
  // 需要调用UserAuthInstance的start()接口，启动认证后，才能通过onAuthTip获取到认证中间状态。
  userAuthInstance.on('authTip', (authTipInfo: userAuth.AuthTipInfo) => {
    console.info('userAuthInstance callback.');
  });
  console.info('auth on successfully.');
  userAuthInstance.start();
  console.info('auth start successfully.');
} catch (error) {
  const err: BusinessError = error as BusinessError;
  console.error(`auth failed. Code is ${err?.code}, message is ${err?.message}`);
}
```

## on_result

```TypeScript
on(type: 'result', callback: IAuthCallback): void
```

订阅用户身份认证的最终结果。通过该接口获取到的是用户在认证控件完成身份认证交互后的最终身份认证结果。认证控件消失前，用户中间的认证不通过尝试并不会通过该接口返回，只有最终的认证结果（成功或最终失败）会通过此接口返回。如果需要感 知整个认证过程中用户的每一次认证不通过尝试和中间状态，请通过 [on('authTip')](#onresult)接口订阅。 > **说明：** > > 在PC/2in1设备上，应用如果使用模应用弹窗方式发起认证（即配置用户界面参数[widgetParam](arkts-userauthentication-userauth-widgetparam-i.md#widgetparam)时传入了有效的uiContext），收到认证结果后，若需弹出其 > 他窗口，应先获取控件弹窗释放的标志消息，通过 > [on('authTip')](#onresult)接口订阅控件释放消息（ > authTipInfo.tipCode = UserAuthTipCode.WIDGET_RELEASED）。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-UserAuthInstance-on(type: 'result', callback: IAuthCallback): void--><!--Device-UserAuthInstance-on(type: 'result', callback: IAuthCallback): void-End-->

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'result' | 是 |
| callback | [IAuthCallback](arkts-userauthentication-userauth-iauthcallback-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12500002](../errorcode-useriam.md#12500002-身份认证系统通用错误码) |

## start

```TypeScript
start(): void
```

开始认证。该接口常用于以下业务场景：用户点击支付按钮时发起身份认证；用户登录应用时进行身份验证；用户访问敏感数据或执行敏感操作时进行身份确认。 > **说明：** > > 每个UserAuthInstance只能进行一次认证，需要再次认证时，必须重新获取UserAuthInstance。

**起始版本：** 23

**需要权限：** 
- API版本20+：ohos.permission.ACCESS_BIOMETRIC or ohos.permission.USER_AUTH_FROM_BACKGROUND
- API版本10 - 19：ohos.permission.ACCESS_BIOMETRIC

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-UserAuthInstance-start(): void--><!--Device-UserAuthInstance-start(): void-End-->

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12500013](../errorcode-useriam.md#12500013-密码过期) |
| [12500010](../errorcode-useriam.md#12500010-该类型的凭据没有录入) |
| [12500011](../errorcode-useriam.md#12500011-提示通知切换自定义认证) |
| [12500009](../errorcode-useriam.md#12500009-认证被锁定) |
| [12500006](../errorcode-useriam.md#12500006-认证信任等级不支持) |
| [12500007](../errorcode-useriam.md#12500007-认证服务繁忙) |
| [12500004](../errorcode-useriam.md#12500004-认证操作超时) |
| [12500005](../errorcode-useriam.md#12500005-认证类型不支持) |
| [12500002](../errorcode-useriam.md#12500002-身份认证系统通用错误码) |
| [12500003](../errorcode-useriam.md#12500003-认证被取消) |
| [12500001](../errorcode-useriam.md#12500001-认证不通过) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { userAuth } from '@kit.UserAuthenticationKit';

try {
  const rand = cryptoFramework.createRandom();
  const len: number = 16;
  let randData: Uint8Array | null = null;
  let retryCount = 0;
  while (retryCount < 3) {
    randData = rand?.generateRandomSync(len)?.data;
    if (randData) {
      break;
    }
    retryCount++;
  }
  if (!randData) {
    return;
  }
  const authParam: userAuth.AuthParam = {
    challenge: randData,
    authType: [userAuth.UserAuthType.PIN],
    authTrustLevel: userAuth.AuthTrustLevel.ATL3,
  };
  const widgetParam: userAuth.WidgetParam = {
    title: '请输入密码',
  };
  const userAuthInstance = userAuth.getUserAuthInstance(authParam, widgetParam);
  console.info('get userAuth instance successfully.');
  userAuthInstance.start();
  console.info('auth start successfully.');
} catch (error) {
  const err: BusinessError = error as BusinessError;
  console.error(`auth failed. Code is ${err?.code}, message is ${err?.message}`);
}
```
