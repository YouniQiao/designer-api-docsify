# IIdmCallback（系统接口）

表示身份管理回调类。

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { osAccount } from '@kit.BasicServicesKit';
```

## onAcquireInfo

ArkTS-Dyn:
```TypeScript
onAcquireInfo?: (module: number, acquire: number, extraInfo: Uint8Array) => void
```

ArkTS-Sta:
```TypeScript
onAcquireInfo?: (module: int, acquire: int, extraInfo: Uint8Array) => void
```

身份管理信息获取回调函数。

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| module | ArkTS-Dyn: number<br>ArkTS-Sta：int | 是 |
| acquire | ArkTS-Dyn: number<br>ArkTS-Sta：int | 是 |
| extraInfo | Uint8Array | 是 |

**示例**

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

ArkTS-Dyn示例：

```TypeScript
let idmCallback: osAccount.IIdmCallback = {
  onResult: (result: number, extraInfo: Object) => {
    console.info('callback result = ' + result)
    console.info('callback onResult = ' + JSON.stringify(extraInfo));
  },
  onAcquireInfo: (module: number, acquire: number, extraInfo: Uint8Array) => {
    console.info('callback module = ' + module);
    console.info('callback acquire = ' + acquire);
    console.info('callback onacquireinfo = ' + JSON.stringify(extraInfo));
  }
};
```

ArkTS-Sta示例：

```TypeScript
let idmCallback: osAccount.IIdmCallback = {
  onResult: (result: int, extraInfo: Object) => {
    console.info('callback result = ' + result)
    console.info('callback onResult = ' + JSON.stringify(extraInfo));
  },
  onAcquireInfo: (module: int, acquire: int, extraInfo: Uint8Array) => {
    console.info('callback module = ' + module);
    console.info('callback acquire = ' + acquire);
    console.info('callback onacquireinfo = ' + JSON.stringify(extraInfo));
  }
};
```

## onResult

ArkTS-Dyn:
```TypeScript
onResult: (result: number, extraInfo: RequestResult) => void
```

ArkTS-Sta:
```TypeScript
onResult: (result: int, extraInfo: RequestResult) => void
```

身份管理操作结果回调函数，返回结果码和请求结果信息。

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| result | ArkTS-Dyn: number<br>ArkTS-Sta：int | 是 |
| extraInfo | [RequestResult](arkts-basicservices-osaccount-requestresult-i-sys.md) | 是 |

**示例**

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

ArkTS-Dyn示例：

```TypeScript
let idmCallback: osAccount.IIdmCallback = {
  onResult: (result: number, extraInfo: osAccount.RequestResult) => {
    console.info('callback result = ' + result)
    console.info('callback extraInfo = ' + JSON.stringify(extraInfo));
  }
};
```

ArkTS-Sta示例：

```TypeScript
let idmCallback: osAccount.IIdmCallback = {
  onResult: (result: int, extraInfo: osAccount.RequestResult) => {
    console.info('callback result = ' + result)
    console.info('callback extraInfo = ' + JSON.stringify(extraInfo));
  }
};
```
