# IInputer（系统接口）

凭据输入器回调。

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-osAccount-interface IInputer--><!--Device-osAccount-interface IInputer-End-->

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

## onGetData

```TypeScript
onGetData: (authSubType: AuthSubType, callback: IInputData, options: GetInputDataOptions) => void
```

通知调用者获取数据的回调函数。

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-IInputer-onGetData: (authSubType: AuthSubType, callback: IInputData, options: GetInputDataOptions) => void--><!--Device-IInputer-onGetData: (authSubType: AuthSubType, callback: IInputData, options: GetInputDataOptions) => void-End-->

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| authSubType | \_\_\_MD\_LINK\_USD\_0\_\_\_ | 是 |  |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_ | 是 |  |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ | 是 |  |

**示例：**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

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
try {
  pinAuth.registerInputer(inputer);
  console.info('registerInputer called')
} catch (e: Error) {
  const err = e as BusinessError
  console.error(`registerInputer failed: code=${err.code}, message=${err.message}`)
}
```

