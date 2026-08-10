# UserAuth (System API)

用户认证类。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-osAccount-class UserAuth--><!--Device-osAccount-class UserAuth-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { osAccount } from 'kits/@kit.BasicServicesKit';
```

## auth

```TypeScript
auth(
      challenge: Uint8Array,
      authType: AuthType,
      authTrustLevel: AuthTrustLevel,
      callback: IUserAuthCallback
    ): Uint8Array
```

认证当前用户。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.ACCESS_USER_AUTH_INTERNAL

<!--Device-UserAuth-auth(      challenge: Uint8Array,      authType: AuthType,      authTrustLevel: AuthTrustLevel,      callback: IUserAuthCallback    ): Uint8Array--><!--Device-UserAuth-auth(      challenge: Uint8Array,      authType: AuthType,      authTrustLevel: AuthTrustLevel,      callback: IUserAuthCallback    ): Uint8Array-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| challenge | Uint8Array | Yes | 指示挑战值，挑战值为一个随机数，用于提升安全性。 |
| authType | [AuthType](arkts-basicservices-osaccount-authtype-e-sys.md) | Yes | 指示认证类型。 |
| authTrustLevel | [AuthTrustLevel](arkts-basicservices-osaccount-authtrustlevel-e-sys.md) | Yes | 指示认证结果的信任级别。 |
| callback | [IUserAuthCallback](arkts-basicservices-osaccount-iuserauthcallback-i-sys.md) | Yes | 回调对象，返回认证结果。 |

**Return value:**

| Type | Description |
| --- | --- |
| Uint8Array | 返回取消的上下文ID。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 12300091 | Cross-device communication failed.<br>**Applicable version:** 20 and later |
| 12300090 | Cross-device capability not supported.<br>**Applicable version:** 20 and later |
| 12300120 | The credentials are no longer valid.<br>**Applicable version:** 23 and later |
| 12300211 | Server unreachable.<br>**Applicable version:** 12 and later |
| 201 | Permission denied. |
| 12300114 | The authentication service works abnormally.<br>**Applicable version:** 12 and later |
| 202 | Not system application. |
| 12300113 | The authentication service does not exist.<br>**Applicable version:** 12 and later |
| 12300112 | The authentication service is busy. |
| 12300119 | Multi-factor authentication failed.<br>**Applicable version:** 20 and later |
| 12300117 | PIN is expired.<br>**Applicable version:** 12 and later |
| 12300020 | Device hardware abnormal.<br>**Applicable version:** 20 and later |
| 12300106 | The authentication type is not supported. |
| 12300105 | The trust level is not supported. |
| 12300111 | The authentication time out. |
| 12300110 | The authentication is locked. |
| 12300013 | Network exception.<br>**Applicable version:** 12 and later |
| 12300109 | The authentication, enrollment, or update operation is canceled. |
| 12300002 | Invalid challenge, authType or authTrustLevel. |
| 12300001 | The system service works abnormally. |
| 12300102 | The credential does not exist. |
| 12300101 | The credential is incorrect. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let userAuth = new osAccount.UserAuth();
let challenge: Uint8Array = new Uint8Array([0]);
let authType: osAccount.AuthType = osAccount.AuthType.PIN;
let authTrustLevel: osAccount.AuthTrustLevel = osAccount.AuthTrustLevel.ATL1;
try {
  userAuth.auth(challenge, authType, authTrustLevel, {
    onResult: (result: number, extraInfo: osAccount.AuthResult) => {
      console.info('auth result = ' + result);
      console.info('auth extraInfo = ' + JSON.stringify(extraInfo));
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`auth exception = code is ${err.code}, message is ${err.message}`);
}
```

## auth

```TypeScript
auth(
      challenge: Uint8Array,
      authType: AuthType,
      authTrustLevel: AuthTrustLevel,
      options: AuthOptions,
      callback: IUserAuthCallback
    ): Uint8Array
```

基于指定的挑战值、认证类型（如口令、人脸、指纹等）、认证可信等级以及可选参数（如账号标识、认证意图等）进行身份认证。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.ACCESS_USER_AUTH_INTERNAL

<!--Device-UserAuth-auth(      challenge: Uint8Array,      authType: AuthType,      authTrustLevel: AuthTrustLevel,      options: AuthOptions,      callback: IUserAuthCallback    ): Uint8Array--><!--Device-UserAuth-auth(      challenge: Uint8Array,      authType: AuthType,      authTrustLevel: AuthTrustLevel,      options: AuthOptions,      callback: IUserAuthCallback    ): Uint8Array-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| challenge | Uint8Array | Yes | 指示挑战值，挑战值为一个随机数，用于防止重放攻击，提升安全性。 |
| authType | [AuthType](arkts-basicservices-osaccount-authtype-e-sys.md) | Yes | 指示认证类型。 |
| authTrustLevel | [AuthTrustLevel](arkts-basicservices-osaccount-authtrustlevel-e-sys.md) | Yes | 指示认证结果的信任级别。 |
| options | [AuthOptions](arkts-basicservices-osaccount-authoptions-i-sys.md) | Yes | 指示认证用户的可选参数集合。 |
| callback | [IUserAuthCallback](arkts-basicservices-osaccount-iuserauthcallback-i-sys.md) | Yes | 回调对象，返回认证结果。 |

**Return value:**

| Type | Description |
| --- | --- |
| Uint8Array | 返回取消的上下文ID。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 12300091 | Cross-device communication failed.<br>**Applicable version:** 20 and later |
| 12300090 | Cross-device capability not supported.<br>**Applicable version:** 20 and later |
| 12300120 | The credentials are no longer valid.<br>**Applicable version:** 23 and later |
| 12300211 | Server unreachable. |
| 201 | Permission denied. |
| 12300114 | The authentication service works abnormally. |
| 202 | Not system application. |
| 12300113 | The authentication service does not exist. |
| 12300112 | The authentication service is busy. |
| 12300119 | Multi-factor authentication failed.<br>**Applicable version:** 20 and later |
| 12300117 | PIN is expired. |
| 12300020 | Device hardware abnormal.<br>**Applicable version:** 20 and later |
| 12300106 | The authentication type is not supported. |
| 12300105 | The trust level is not supported. |
| 12300111 | The authentication timeout. |
| 12300110 | The authentication is locked. |
| 12300013 | Network exception. |
| 12300109 | The authentication, enrollment, or update operation is canceled. |
| 12300003 | Account not found. |
| 12300002 | Invalid challenge, authType, authTrustLevel or options. |
| 12300001 | The system service works abnormally. |
| 12300102 | The credential does not exist. |
| 12300101 | The credential is incorrect. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let userAuth = new osAccount.UserAuth();
let challenge: Uint8Array = new Uint8Array([0]);
let authType: osAccount.AuthType = osAccount.AuthType.PIN;
let authTrustLevel: osAccount.AuthTrustLevel = osAccount.AuthTrustLevel.ATL1;
let options: osAccount.AuthOptions = {
  accountId: 100
};
try {
  userAuth.auth(challenge, authType, authTrustLevel, options, {
    onResult: (result: number, extraInfo: osAccount.AuthResult) => {
      console.info('auth result = ' + result);
      console.info('auth extraInfo = ' + JSON.stringify(extraInfo));
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`auth exception = code is ${err.code}, message is ${err.message}`);
}
```

## authUser

ArkTS-Dyn:
```TypeScript
authUser(
      userId: number,
      challenge: Uint8Array,
      authType: AuthType,
      authTrustLevel: AuthTrustLevel,
      callback: IUserAuthCallback
    ): Uint8Array
```

ArkTS-Sta:
```TypeScript
authUser(
      userId: int,
      challenge: Uint8Array,
      authType: AuthType,
      authTrustLevel: AuthTrustLevel,
      callback: IUserAuthCallback
    ): Uint8Array
```

认证指定用户。使用callback异步回调。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.ACCESS_USER_AUTH_INTERNAL

<!--Device-UserAuth-authUser(      userId: int,      challenge: Uint8Array,      authType: AuthType,      authTrustLevel: AuthTrustLevel,      callback: IUserAuthCallback    ): Uint8Array--><!--Device-UserAuth-authUser(      userId: int,      challenge: Uint8Array,      authType: AuthType,      authTrustLevel: AuthTrustLevel,      callback: IUserAuthCallback    ): Uint8Array-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| userId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 指示用户身份。 |
| challenge | Uint8Array | Yes | 指示挑战值，挑战值为一个随机数，用于提升安全性。 |
| authType | [AuthType](arkts-basicservices-osaccount-authtype-e-sys.md) | Yes | 指示认证类型。 |
| authTrustLevel | [AuthTrustLevel](arkts-basicservices-osaccount-authtrustlevel-e-sys.md) | Yes | 指示认证结果的信任级别。 |
| callback | [IUserAuthCallback](arkts-basicservices-osaccount-iuserauthcallback-i-sys.md) | Yes | 回调对象，返回认证结果。 |

**Return value:**

| Type | Description |
| --- | --- |
| Uint8Array | 返回取消的上下文ID。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 12300091 | Cross-device communication failed.<br>**Applicable version:** 20 and later |
| 12300090 | Cross-device capability not supported.<br>**Applicable version:** 20 and later |
| 12300120 | The credentials are no longer valid.<br>**Applicable version:** 23 and later |
| 12300211 | Server unreachable.<br>**Applicable version:** 12 and later |
| 201 | Permission denied. |
| 12300114 | The authentication service works abnormally.<br>**Applicable version:** 12 and later |
| 202 | Not system application. |
| 12300113 | The authentication service does not exist.<br>**Applicable version:** 12 and later |
| 12300112 | The authentication service is busy. |
| 12300119 | Multi-factor authentication failed.<br>**Applicable version:** 20 and later |
| 12300117 | PIN is expired.<br>**Applicable version:** 12 and later |
| 12300020 | Device hardware abnormal.<br>**Applicable version:** 20 and later |
| 12300106 | The authentication type is not supported. |
| 12300105 | The trust level is not supported. |
| 12300111 | The authentication timeout. |
| 12300110 | The authentication is locked. |
| 12300013 | Network exception.<br>**Applicable version:** 12 and later |
| 12300109 | The authentication, enrollment, or update operation is canceled. |
| 12300003 | Account not found.<br>**Applicable version:** 12 and later |
| 12300002 | Invalid challenge, authType or authTrustLevel. |
| 12300001 | The system service works abnormally. |
| 12300102 | The credential does not exist. |
| 12300101 | The credential is incorrect. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let userAuth = new osAccount.UserAuth();
let userID: number = 100;
let challenge: Uint8Array = new Uint8Array([0]);
let authType: osAccount.AuthType = osAccount.AuthType.PIN;
let authTrustLevel: osAccount.AuthTrustLevel = osAccount.AuthTrustLevel.ATL1;
try {
  userAuth.authUser(userID, challenge, authType, authTrustLevel, {
    onResult: (result,extraInfo) => {
      console.info('authUser result = ' + result);
      console.info('authUser extraInfo = ' + JSON.stringify(extraInfo));
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`authUser exception = code is ${err.code}, message is ${err.message}`);
}
```

## cancelAuth

```TypeScript
cancelAuth(contextID: Uint8Array): void
```

取消指定的认证操作。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.ACCESS_USER_AUTH_INTERNAL

<!--Device-UserAuth-cancelAuth(contextID: Uint8Array): void--><!--Device-UserAuth-cancelAuth(contextID: Uint8Array): void-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| contextID | Uint8Array | Yes | 指示身份验证上下文ID，此ID动态生成没有具体值。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameter types. |
| 201 | Permission denied. |
| 12300002 | Invalid contextId. |
| 202 | Not system application. |
| 12300001 | The system service works abnormally. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let userAuth = new osAccount.UserAuth();
let pinAuth: osAccount.PINAuth = new osAccount.PINAuth();
let challenge = new Uint8Array([0]);
let contextId: Uint8Array = userAuth.auth(challenge, osAccount.AuthType.PIN, osAccount.AuthTrustLevel.ATL1, {
  onResult: (result: number, extraInfo: osAccount.AuthResult) => {
    console.info('auth result = ' + result);
    console.info('auth extraInfo = ' + JSON.stringify(extraInfo));
  }
});
try {
  userAuth.cancelAuth(contextId);
} catch (e) {
  const err = e as BusinessError;
  console.error(`cancelAuth exception = code is ${err.code}, message is ${err.message}`);
}
```

## constructor

```TypeScript
constructor()
```

创建用户认证的实例。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-UserAuth-constructor()--><!--Device-UserAuth-constructor()-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 202 | Not system application. |

## Examples

```TypeScript
let userAuth = new osAccount.UserAuth();
```

## getAvailableStatus

ArkTS-Dyn:
```TypeScript
getAvailableStatus(authType: AuthType, authTrustLevel: AuthTrustLevel): number
```

ArkTS-Sta:
```TypeScript
getAvailableStatus(authType: AuthType, authTrustLevel: AuthTrustLevel): int
```

获取指定认证类型和认证可信等级的认证能力的可用状态。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.ACCESS_USER_AUTH_INTERNAL

<!--Device-UserAuth-getAvailableStatus(authType: AuthType, authTrustLevel: AuthTrustLevel): int--><!--Device-UserAuth-getAvailableStatus(authType: AuthType, authTrustLevel: AuthTrustLevel): int-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| authType | [AuthType](arkts-basicservices-osaccount-authtype-e-sys.md) | Yes | 认证类型。 |
| authTrustLevel | [AuthTrustLevel](arkts-basicservices-osaccount-authtrustlevel-e-sys.md) | Yes | 认证的可信等级。 |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：int | 返回认证能力的可用状态。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameter types. |
| 201 | Permission denied. |
| 12300002 | Invalid authType or authTrustLevel. |
| 202 | Not system application. |
| 12300001 | The system service works abnormally. |
| 12300117 | PIN is expired. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let userAuth = new osAccount.UserAuth();
let authType: osAccount.AuthType = osAccount.AuthType.PIN;
let authTrustLevel: osAccount.AuthTrustLevel = osAccount.AuthTrustLevel.ATL1;
try {
  let status: number = userAuth.getAvailableStatus(authType, authTrustLevel);
  console.info('getAvailableStatus status = ' + status);
} catch (e) {
  const err = e as BusinessError;
  console.error(`getAvailableStatus exception = code is ${err.code}, message is ${err.message}`);
}
```

## getProperty

```TypeScript
getProperty(request: GetPropertyRequest, callback: AsyncCallback<ExecutorProperty>): void
```

基于指定的请求信息获取属性。使用callback异步回调。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.ACCESS_USER_AUTH_INTERNAL

<!--Device-UserAuth-getProperty(request: GetPropertyRequest, callback: AsyncCallback<ExecutorProperty>): void--><!--Device-UserAuth-getProperty(request: GetPropertyRequest, callback: AsyncCallback<ExecutorProperty>): void-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| request | [GetPropertyRequest](arkts-basicservices-osaccount-getpropertyrequest-i-sys.md) | Yes | 请求信息，包括认证类型和属性类型列表。 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;ExecutorProperty&gt; | Yes | 回调函数。如果获取成功，err为null，data为执行器属性信息；否则为错误对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 12300003 | Account not found.<br>**Applicable version:** 12 and later |
| 201 | Permission denied. |
| 12300002 | Invalid request. |
| 202 | Not system application. |
| 12300001 | The system service works abnormally. |
| 12300020 | Device hardware abnormal.<br>**Applicable version:** 23 and later |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let userAuth = new osAccount.UserAuth();
let keys: Array<osAccount.GetPropertyType>  = [
  osAccount.GetPropertyType.AUTH_SUB_TYPE,
  osAccount.GetPropertyType.REMAIN_TIMES,
  osAccount.GetPropertyType.FREEZING_TIME
];
let request: osAccount.GetPropertyRequest = {
  authType: osAccount.AuthType.PIN,
  keys: keys
};
try {
  userAuth.getProperty(request, (err: BusinessError, result: osAccount.ExecutorProperty) => {
    if (err) {
      console.error(`getProperty exception = code is ${err.code}, message is ${err.message}`);
    } else {
      console.info('getProperty result = ' + JSON.stringify(result));
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getProperty exception = code is ${err.code}, message is ${err.message}`);
}
```

## getProperty

```TypeScript
getProperty(request: GetPropertyRequest): Promise<ExecutorProperty>
```

基于指定的请求信息获取属性。使用Promise异步回调。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.ACCESS_USER_AUTH_INTERNAL

<!--Device-UserAuth-getProperty(request: GetPropertyRequest): Promise<ExecutorProperty>--><!--Device-UserAuth-getProperty(request: GetPropertyRequest): Promise<ExecutorProperty>-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| request | [GetPropertyRequest](arkts-basicservices-osaccount-getpropertyrequest-i-sys.md) | Yes | 请求信息，包括认证类型和属性类型列表。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;ExecutorProperty&gt; | Promise对象，返回执行器属性信息。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 12300003 | Account not found.<br>**Applicable version:** 12 and later |
| 201 | Permission denied. |
| 12300002 | Invalid request. |
| 202 | Not system application. |
| 12300001 | The system service works abnormally. |
| 12300020 | Device hardware abnormal.<br>**Applicable version:** 23 and later |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let userAuth = new osAccount.UserAuth();
let keys: Array<osAccount.GetPropertyType> = [
  osAccount.GetPropertyType.AUTH_SUB_TYPE,
  osAccount.GetPropertyType.REMAIN_TIMES,
  osAccount.GetPropertyType.FREEZING_TIME
];
let request: osAccount.GetPropertyRequest = {
  authType: osAccount.AuthType.PIN,
  keys: keys
};
try {
  userAuth.getProperty(request).then((result: osAccount.ExecutorProperty) => {
    console.info('getProperty result = ' + JSON.stringify(result));
  }).catch((err: BusinessError) => {
    console.error(`getProperty error = code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getProperty exception = code is ${err.code}, message is ${err.message}`);
}
```

## getPropertyByCredentialId

```TypeScript
getPropertyByCredentialId(credentialId: Uint8Array, keys: Array<GetPropertyType>): Promise<ExecutorProperty>
```

基于凭据id获取关联执行器的指定属性信息。使用Promise异步回调。

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.ACCESS_USER_AUTH_INTERNAL

<!--Device-UserAuth-getPropertyByCredentialId(credentialId: Uint8Array, keys: Array<GetPropertyType>): Promise<ExecutorProperty>--><!--Device-UserAuth-getPropertyByCredentialId(credentialId: Uint8Array, keys: Array<GetPropertyType>): Promise<ExecutorProperty>-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| credentialId | Uint8Array | Yes | 指示凭据索引。 |
| keys | Array&lt;GetPropertyType&gt; | Yes | 指示要查询的属性类型数组。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;ExecutorProperty&gt; | Promise对象，返回执行器的属性信息。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 201 | Permission denied. |
| 12300002 | Invalid keys. |
| 202 | Not system application. |
| 12300001 | The system service works abnormally. |
| 12300102 | The credential does not exist. |
| 12300020 | Device hardware abnormal.<br>**Applicable version:** 23 and later |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let userIDM = new osAccount.UserIdentityManager();
let credInfo: osAccount.EnrolledCredInfo[] = [];
async function getProperty() {
  try {
    credInfo = await userIDM.getAuthInfo(osAccount.AuthType.PRIVATE_PIN);
  } catch (e) {
    const err = e as BusinessError;
    console.error(`getAuthInfo exception = code is ${err.code}, message is ${err.message}`);
    return;
  }
  if (credInfo.length == 0) {
    console.info('no credential infos');
    return;
  }
  let testCredentialId: Uint8Array = credInfo[0].credentialId;
  let keys: Array<osAccount.GetPropertyType> = [
    osAccount.GetPropertyType.AUTH_SUB_TYPE,
    osAccount.GetPropertyType.REMAIN_TIMES,
    osAccount.GetPropertyType.FREEZING_TIME
  ];
  try {
    let userAuth = new osAccount.UserAuth();
    userAuth.getPropertyByCredentialId(testCredentialId, keys).then((result: osAccount.ExecutorProperty) => {
      console.info('getPropertyByCredentialId result = ' + JSON.stringify(result));
    }).catch((err: BusinessError) => {
      console.error(`getPropertyByCredentialId error = code is ${err.code}, message is ${err.message}`);
    });
  } catch (e) {
    const err = e as BusinessError;
    console.error(`getPropertyByCredentialId exception = code is ${err.code}, message is ${err.message}`);
  }
}
```

## getVersion

ArkTS-Dyn:
```TypeScript
getVersion(): number
```

ArkTS-Sta:
```TypeScript
getVersion(): int
```

返回版本信息。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-UserAuth-getVersion(): int--><!--Device-UserAuth-getVersion(): int-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：int | 返回版本信息。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 202 | Not system application. |

## Examples

```TypeScript
let userAuth = new osAccount.UserAuth();
let version: number = userAuth.getVersion();
console.info('getVersion version = ' + version);
```

## prepareRemoteAuth

```TypeScript
prepareRemoteAuth(remoteNetworkId: string): Promise<void>
```

准备远端认证。使用Promise异步回调。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.ACCESS_USER_AUTH_INTERNAL

<!--Device-UserAuth-prepareRemoteAuth(remoteNetworkId: string): Promise<void>--><!--Device-UserAuth-prepareRemoteAuth(remoteNetworkId: string): Promise<void>-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| remoteNetworkId | string | Yes | 远端网络Id。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 12300091 | Cross-device communication failed.<br>**Applicable version:** 20 and later |
| 12300090 | Cross-device capability not supported.<br>**Applicable version:** 20 and later |
| 12300111 | Operation timeout.<br>**Applicable version:** 20 and later |
| 201 | Permission denied. |
| 12300002 | Invalid remoteNetworkId. |
| 202 | Not system application. |
| 12300001 | System service exception. |

## Examples

```TypeScript
import { distributedDeviceManager } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

let userAuth = new osAccount.UserAuth();
let distributedDeviceMgr = distributedDeviceManager.createDeviceManager("com.example.bundleName");
distributedDeviceMgr.getAvailableDeviceList().then((data: Array<distributedDeviceManager.DeviceBasicInfo>) => {
    try {
      if (data.length > 0 && data[0].networkId != null) {
        userAuth.prepareRemoteAuth(data[0].networkId).then(() => {
          console.info('prepareRemoteAuth successfully');
        }).catch((err: BusinessError) => {
          console.error(`prepareRemoteAuth failed, error = code is ${err.code}, message is ${err.message}`);
        });
      }
    } catch (e) {
      const err = e as BusinessError;
      console.error(`prepareRemoteAuth exception = code is ${err.code}, message is ${err.message}`);
    }
  }
)
```

## setProperty

```TypeScript
setProperty(request: SetPropertyRequest, callback: AsyncCallback<void>): void
```

设置可用于初始化算法的属性。使用callback异步回调。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.ACCESS_USER_AUTH_INTERNAL

<!--Device-UserAuth-setProperty(request: SetPropertyRequest, callback: AsyncCallback<void>): void--><!--Device-UserAuth-setProperty(request: SetPropertyRequest, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| request | [SetPropertyRequest](arkts-basicservices-osaccount-setpropertyrequest-i-sys.md) | Yes | 请求信息，包括认证类型和要设置的密钥值。 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 回调函数。如果设置成功，err为null，否则为错误对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameter types. |
| 201 | Permission denied. |
| 12300002 | Invalid request. |
| 202 | Not system application. |
| 12300001 | The system service works abnormally. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let userAuth = new osAccount.UserAuth();
let request: osAccount.SetPropertyRequest = {
  authType: osAccount.AuthType.PIN,
  key: osAccount.SetPropertyType.INIT_ALGORITHM,
  setInfo: new Uint8Array([0])
};
try {
  userAuth.setProperty(request, (err: BusinessError) => {
    if (err) {
      console.error(`setProperty failed, error = code is ${err.code}, message is ${err.message}`);
    } else {
      console.info('setProperty successfully');
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`setProperty exception = code is ${err.code}, message is ${err.message}`);
}
```

## setProperty

```TypeScript
setProperty(request: SetPropertyRequest): Promise<void>
```

设置可用于初始化算法的属性。使用Promise异步回调。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.ACCESS_USER_AUTH_INTERNAL

<!--Device-UserAuth-setProperty(request: SetPropertyRequest): Promise<void>--><!--Device-UserAuth-setProperty(request: SetPropertyRequest): Promise<void>-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| request | [SetPropertyRequest](arkts-basicservices-osaccount-setpropertyrequest-i-sys.md) | Yes | 请求信息，包括身份验证类型和要设置的密钥值。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameter types. |
| 201 | Permission denied. |
| 12300002 | Invalid request. |
| 202 | Not system application. |
| 12300001 | The system service works abnormally. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let userAuth = new osAccount.UserAuth();
let request: osAccount.SetPropertyRequest = {
  authType: osAccount.AuthType.PIN,
  key: osAccount.SetPropertyType.INIT_ALGORITHM,
  setInfo: new Uint8Array([0])
};
try {
  userAuth.setProperty(request).then(() => {
    console.info('setProperty successfully');
  }).catch((err: BusinessError) => {
    console.error(`setProperty failed, error = code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`setProperty exception = code is ${err.code}, message is ${err.message}`);
}
```

