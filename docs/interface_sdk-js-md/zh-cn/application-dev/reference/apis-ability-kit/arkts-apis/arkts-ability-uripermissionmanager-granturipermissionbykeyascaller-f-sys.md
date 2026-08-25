# grantUriPermissionByKeyAsCaller（系统接口）

## 导入模块

```TypeScript
import { uriPermissionManager } from 'kits/@kit.AbilityKit';
```

## grantUriPermissionByKeyAsCaller

```TypeScript
function grantUriPermissionByKeyAsCaller(key: string, flag: wantConstant.Flags, callerTokenId: number, targetTokenId: number): Promise<void>
```

通过UDMF数据唯一标识key，将指定应用的文件URI访问权限授权给目标应用，权限将在目标应用退出后回收。使用Promise异步回调。 该接口仅在Phone、PC/2in1、Tablet设备中可正常调用，在其他设备中返回801错误码。 **系统接口**：此接口为系统接口。

**起始版本：** 20

**需要权限：** ohos.permission.GRANT_URI_PERMISSION_AS_CALLER

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | string | 是 |
| flag | wantConstant.Flags | 是 |
| callerTokenId | number | 是 |
| targetTokenId | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
| [16000058](../errorcode-ability.md#16000058-指定的uri-flag无效) |
| [16000060](../errorcode-ability.md#16000060-不支持沙箱应用授权uri) |
| [16000091](../errorcode-ability.md#16000091-根据key获取文件uri数据失败) |
| [16000092](../errorcode-ability.md#16000092-无权限授权uri) |
| [16000093](../errorcode-ability.md#16000093-调用方的token-id无效) |
| [16000094](../errorcode-ability.md#16000094-目标应用的token-id无效) |
