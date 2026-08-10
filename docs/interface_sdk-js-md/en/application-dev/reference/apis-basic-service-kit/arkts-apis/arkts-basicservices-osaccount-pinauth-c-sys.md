# PINAuth (System API)

PIN码认证基类。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-osAccount-class PINAuth--><!--Device-osAccount-class PINAuth-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { osAccount } from 'kits/@kit.BasicServicesKit';
```

## constructor

```TypeScript
constructor()
```

创建PIN码认证的实例。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-PINAuth-constructor()--><!--Device-PINAuth-constructor()-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 202 | Not system application. |

## Examples

```TypeScript
let pinAuth: osAccount.PINAuth = new osAccount.PINAuth();
```

## registerInputer

```TypeScript
registerInputer(inputer: IInputer): void
```

注册PIN码输入器。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.ACCESS_PIN_AUTH

<!--Device-PINAuth-registerInputer(inputer: IInputer): void--><!--Device-PINAuth-registerInputer(inputer: IInputer): void-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| inputer | [IInputer](arkts-basicservices-osaccount-iinputer-i-sys.md) | Yes | PIN码输入器，用于获取PIN码。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameter types. |
| 201 | Permission denied. |
| 12300002 | Invalid inputer. |
| 202 | Not system application. |
| 12300001 | The system service works abnormally. |
| 12300103 | The credential inputer already exists. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let pinAuth: osAccount.PINAuth = new osAccount.PINAuth();
let password = new Uint8Array([0, 0, 0, 0, 0]);
try {
  pinAuth.registerInputer({
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
unregisterInputer(): void
```

解注册PIN码输入器。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.ACCESS_PIN_AUTH

<!--Device-PINAuth-unregisterInputer(): void--><!--Device-PINAuth-unregisterInputer(): void-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 201 | Permission denied. |
| 202 | Not system application. |

## Examples

```TypeScript
let pinAuth: osAccount.PINAuth = new osAccount.PINAuth();
pinAuth.unregisterInputer();
```

