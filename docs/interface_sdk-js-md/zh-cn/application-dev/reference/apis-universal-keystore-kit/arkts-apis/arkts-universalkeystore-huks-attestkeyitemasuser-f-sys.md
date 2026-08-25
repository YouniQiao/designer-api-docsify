# attestKeyItemAsUser（系统接口）

## 导入模块

```TypeScript
import { huks } from 'kits/@kit.UniversalKeystoreKit';
```

## attestKeyItemAsUser

```TypeScript
function attestKeyItemAsUser(userId: number, keyAlias: string, huksOptions: HuksOptions): Promise<HuksReturnResult>
```

指定用户身份获取密钥证书，使用Promise方式异步返回结果。

**起始版本：** 12

**需要权限：** ohos.permission.ATTEST_KEY and ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

**系统能力：** SystemCapability.Security.Huks.Extension

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| userId | number | 是 |
| keyAlias | string | 是 |
| huksOptions | [HuksOptions](arkts-universalkeystore-huks-huksoptions-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[HuksReturnResult](arkts-universalkeystore-huks-huksreturnresult-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [12000001](../errorcode-huks.md#12000001-该子功能不支持特性) |
| [12000002](../errorcode-huks.md#12000002-缺少密钥算法参数) |
| [12000003](../errorcode-huks.md#12000003-无效的密钥算法参数) |
| [12000004](../errorcode-huks.md#12000004-文件错误) |
| [12000005](../errorcode-huks.md#12000005-进程通信错误) |
| [12000006](../errorcode-huks.md#12000006-算法库操作失败) |
| [12000011](../errorcode-huks.md#12000011-目标对象不存在) |
| [12000012](../errorcode-huks.md#12000012-外部错误) |
| [12000014](../errorcode-huks.md#12000014-内存不足) |
