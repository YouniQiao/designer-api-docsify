# Constants

表示常量的枚举。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-appAccount-enum Constants--><!--Device-appAccount-enum Constants-End-->

**System capability:** SystemCapability.Account.AppAccount

## ACTION_ADD_ACCOUNT_IMPLICITLY

```TypeScript
ACTION_ADD_ACCOUNT_IMPLICITLY = 'addAccountImplicitly'
```

表示操作，隐式添加账号。

**说明：**从API version 8开始支持，从API version 9开始废弃，建议使用ACTION_CREATE_ACCOUNT_IMPLICITLY替代。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [appAccount.Constants.ACTION_CREATE_ACCOUNT_IMPLICITLY](arkts-basicservices-appaccount-constants-e.md#action_create_account_implicitly)

<!--Device-Constants-ACTION_ADD_ACCOUNT_IMPLICITLY = 'addAccountImplicitly'--><!--Device-Constants-ACTION_ADD_ACCOUNT_IMPLICITLY = 'addAccountImplicitly'-End-->

**System capability:** SystemCapability.Account.AppAccount

## ACTION_AUTHENTICATE

```TypeScript
ACTION_AUTHENTICATE = 'authenticate'
```

表示操作，鉴权。

**说明：**从API version 8开始支持，从API version 9开始废弃，建议使用ACTION_AUTH替代。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [appAccount.Constants.ACTION_AUTH](arkts-basicservices-appaccount-constants-e.md#action_auth)

<!--Device-Constants-ACTION_AUTHENTICATE = 'authenticate'--><!--Device-Constants-ACTION_AUTHENTICATE = 'authenticate'-End-->

**System capability:** SystemCapability.Account.AppAccount

## ACTION_CREATE_ACCOUNT_IMPLICITLY

```TypeScript
ACTION_CREATE_ACCOUNT_IMPLICITLY = "createAccountImplicitly"
```

表示操作，隐式创建账号。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-Constants-ACTION_CREATE_ACCOUNT_IMPLICITLY = "createAccountImplicitly"--><!--Device-Constants-ACTION_CREATE_ACCOUNT_IMPLICITLY = "createAccountImplicitly"-End-->

**System capability:** SystemCapability.Account.AppAccount

## ACTION_AUTH

```TypeScript
ACTION_AUTH = "auth"
```

表示操作，鉴权。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-Constants-ACTION_AUTH = "auth"--><!--Device-Constants-ACTION_AUTH = "auth"-End-->

**System capability:** SystemCapability.Account.AppAccount

## ACTION_VERIFY_CREDENTIAL

```TypeScript
ACTION_VERIFY_CREDENTIAL = "verifyCredential"
```

表示操作，验证凭据。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-Constants-ACTION_VERIFY_CREDENTIAL = "verifyCredential"--><!--Device-Constants-ACTION_VERIFY_CREDENTIAL = "verifyCredential"-End-->

**System capability:** SystemCapability.Account.AppAccount

## ACTION_SET_AUTHENTICATOR_PROPERTIES

```TypeScript
ACTION_SET_AUTHENTICATOR_PROPERTIES = "setAuthenticatorProperties"
```

表示操作，设置认证器属性。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-Constants-ACTION_SET_AUTHENTICATOR_PROPERTIES = "setAuthenticatorProperties"--><!--Device-Constants-ACTION_SET_AUTHENTICATOR_PROPERTIES = "setAuthenticatorProperties"-End-->

**System capability:** SystemCapability.Account.AppAccount

## KEY_NAME

```TypeScript
KEY_NAME = "name"
```

表示键名，应用账号的名称。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-Constants-KEY_NAME = "name"--><!--Device-Constants-KEY_NAME = "name"-End-->

**System capability:** SystemCapability.Account.AppAccount

## KEY_OWNER

```TypeScript
KEY_OWNER = "owner"
```

表示键名，应用账号所有者的包名。最大长度为1024个字符。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-Constants-KEY_OWNER = "owner"--><!--Device-Constants-KEY_OWNER = "owner"-End-->

**System capability:** SystemCapability.Account.AppAccount

## KEY_TOKEN

```TypeScript
KEY_TOKEN = "token"
```

表示键名，令牌。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-Constants-KEY_TOKEN = "token"--><!--Device-Constants-KEY_TOKEN = "token"-End-->

**System capability:** SystemCapability.Account.AppAccount

## KEY_ACTION

```TypeScript
KEY_ACTION = "action"
```

表示键名，操作。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-Constants-KEY_ACTION = "action"--><!--Device-Constants-KEY_ACTION = "action"-End-->

**System capability:** SystemCapability.Account.AppAccount

## KEY_AUTH_TYPE

```TypeScript
KEY_AUTH_TYPE = "authType"
```

表示键名，鉴权类型。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-Constants-KEY_AUTH_TYPE = "authType"--><!--Device-Constants-KEY_AUTH_TYPE = "authType"-End-->

**System capability:** SystemCapability.Account.AppAccount

## KEY_SESSION_ID

```TypeScript
KEY_SESSION_ID = "sessionId"
```

表示键名，会话标识。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-Constants-KEY_SESSION_ID = "sessionId"--><!--Device-Constants-KEY_SESSION_ID = "sessionId"-End-->

**System capability:** SystemCapability.Account.AppAccount

## KEY_CALLER_PID

```TypeScript
KEY_CALLER_PID = "callerPid"
```

表示键名，调用方PID。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-Constants-KEY_CALLER_PID = "callerPid"--><!--Device-Constants-KEY_CALLER_PID = "callerPid"-End-->

**System capability:** SystemCapability.Account.AppAccount

## KEY_CALLER_UID

```TypeScript
KEY_CALLER_UID = "callerUid"
```

表示键名，调用方UID。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-Constants-KEY_CALLER_UID = "callerUid"--><!--Device-Constants-KEY_CALLER_UID = "callerUid"-End-->

**System capability:** SystemCapability.Account.AppAccount

## KEY_CALLER_BUNDLE_NAME

```TypeScript
KEY_CALLER_BUNDLE_NAME = "callerBundleName"
```

表示键名，调用方包名。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-Constants-KEY_CALLER_BUNDLE_NAME = "callerBundleName"--><!--Device-Constants-KEY_CALLER_BUNDLE_NAME = "callerBundleName"-End-->

**System capability:** SystemCapability.Account.AppAccount

## KEY_REQUIRED_LABELS

```TypeScript
KEY_REQUIRED_LABELS = "requiredLabels"
```

表示键名，必需的标签。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-Constants-KEY_REQUIRED_LABELS = "requiredLabels"--><!--Device-Constants-KEY_REQUIRED_LABELS = "requiredLabels"-End-->

**System capability:** SystemCapability.Account.AppAccount

## KEY_BOOLEAN_RESULT

```TypeScript
KEY_BOOLEAN_RESULT = "booleanResult"
```

表示键名，布尔返回值。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-Constants-KEY_BOOLEAN_RESULT = "booleanResult"--><!--Device-Constants-KEY_BOOLEAN_RESULT = "booleanResult"-End-->

**System capability:** SystemCapability.Account.AppAccount

