# IUserAuthCallback（系统接口）

表示用户认证回调类。

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-osAccount-interface IUserAuthCallback--><!--Device-osAccount-interface IUserAuthCallback-End-->

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

## onAcquireInfo

ArkTS-Dyn:
```TypeScript
onAcquireInfo?: (module: number, acquire: number, extraInfo: Uint8Array) => void
```

ArkTS-Sta:
```TypeScript
onAcquireInfo?: (module: int, acquire: int, extraInfo: Uint8Array) => void
```

身份认证信息获取回调函数。

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-IUserAuthCallback-onAcquireInfo?: (module: int, acquire: int, extraInfo: Uint8Array) => void--><!--Device-IUserAuthCallback-onAcquireInfo?: (module: int, acquire: int, extraInfo: Uint8Array) => void-End-->

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| module | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 是 |  |
| acquire | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 是 |  |
| extraInfo | Uint8Array | 是 |  |

## 示例

ArkTS-Dyn示例：

```TypeScript
let authCallback: osAccount.IUserAuthCallback = {
  onResult: (result: number, extraInfo: osAccount.AuthResult) => {
    console.info('auth result = ' + result)
    console.info('auth extraInfo = ' + JSON.stringify(extraInfo));
  },
  onAcquireInfo: (module: number, acquire: number, extraInfo: Uint8Array) => {
    console.info('auth module = ' + module);
    console.info('auth acquire = ' + acquire);
    console.info('auth extraInfo = ' + JSON.stringify(extraInfo));
  }
};
```

ArkTS-Sta示例：

```TypeScript
let authCallback: osAccount.IUserAuthCallback = {
  onResult: (result: int, extraInfo: osAccount.AuthResult) => {
    console.info('auth result = ' + result)
    console.info('auth extraInfo = ' + JSON.stringify(extraInfo));
  },
  onAcquireInfo: (module: int, acquire: int, extraInfo: Uint8Array) => {
    console.info('auth module = ' + module);
    console.info('auth acquire = ' + acquire);
    console.info('auth extraInfo = ' + JSON.stringify(extraInfo));
  }
};
```

## onResult

ArkTS-Dyn:
```TypeScript
onResult: (result: number, extraInfo: AuthResult) => void
```

ArkTS-Sta:
```TypeScript
onResult: (result: int, extraInfo: AuthResult) => void
```

身份认证结果回调函数，返回结果码和认证结果信息。

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-IUserAuthCallback-onResult: (result: int, extraInfo: AuthResult) => void--><!--Device-IUserAuthCallback-onResult: (result: int, extraInfo: AuthResult) => void-End-->

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| result | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 是 |  |
| extraInfo | AuthResult | 是 |  |

## 示例

ArkTS-Dyn示例：

```TypeScript
let authCallback: osAccount.IUserAuthCallback = {
  onResult: (result: number, extraInfo: osAccount.AuthResult) => {
    console.info('auth result = ' + result);
    console.info('auth extraInfo = ' + JSON.stringify(extraInfo));
  }
};
```

ArkTS-Sta示例：

```TypeScript
let authCallback: osAccount.IUserAuthCallback = {
  onResult: (result: int, extraInfo: osAccount.AuthResult) => {
    console.info('auth result = ' + result);
    console.info('auth extraInfo = ' + JSON.stringify(extraInfo));
  }
};
```

