# getKeepAliveBundles（系统接口）

## 导入模块

```TypeScript
import { appManager } from 'kits/@kit.AbilityKit';
```

## getKeepAliveBundles

```TypeScript
function getKeepAliveBundles(type: KeepAliveAppType, userId?: number): Promise<Array<KeepAliveBundleInfo>>
```

获取指定用户下指定类型的保活应用信息。该应用信息由[KeepAliveBundleInfo](arkts-ability-appmanager-keepalivebundleinfo-i-sys.md)定义。使用Promise异步回调。 该接口在PC/2in1中可正常调用，在其他设备类型中返回801错误码。 **需要权限**：ohos.permission.MANAGE_APP_KEEP_ALIVE

**起始版本：** 14

**需要权限：** ohos.permission.MANAGE_APP_KEEP_ALIVE

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | [KeepAliveAppType](arkts-ability-appmanager-keepaliveapptype-e-sys.md) | 是 |
| userId | number | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;[KeepAliveBundleInfo](arkts-ability-appmanager-keepalivebundleinfo-i-sys.md)&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
