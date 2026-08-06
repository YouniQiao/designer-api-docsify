# IInputer (System API)

Provides callbacks for credential inputers.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-osAccount-interface IInputer--><!--Device-osAccount-interface IInputer-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

## onGetData

```TypeScript
onGetData: (authSubType: AuthSubType, callback: IInputData, options: GetInputDataOptions) => void
```

Called to notify the caller that data is obtained.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-IInputer-onGetData: (authSubType: AuthSubType, callback: IInputData, options: GetInputDataOptions) => void--><!--Device-IInputer-onGetData: (authSubType: AuthSubType, callback: IInputData, options: GetInputDataOptions) => void-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| authSubType | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes |  |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes |  |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes |  |

**Example**

```TypeScript
let password: Uint8Array = new Uint8Array([0, 0, 0, 0, 0, 0]);
let passwordNumber: Uint8Array = new Uint8Array([1, 2, 3, 4]);
let inputer: osAccount.IInputer = {
  onGetData: (authSubType: osAccount.AuthSubType,
    callback: osAccount.IInputData, options: osAccount.GetInputDataOptions) => {
      if (authSubType == osAccount.AuthSubType.PIN_NUMBER) {
        callback.onSetData(authSubType, passwordNumber);
      } else {
        callback.onSetData(authSubType, password);
      }
  }
};
let pinAuth: osAccount.PINAuth = new osAccount.PINAuth();
let result = pinAuth.registerInputer(inputer);
console.info('registerInputer result: ' + result);
```

