# generateKeyItemAsUser（系统接口）

## 导入模块

```TypeScript
import { huks } from 'kits/@kit.UniversalKeystoreKit';
```

## generateKeyItemAsUser

```TypeScript
function generateKeyItemAsUser(userId: number, keyAlias: string, huksOptions: HuksOptions): Promise<void>
```

指定用户身份生成密钥，使用Promise方式异步返回结果。基于密钥不出[TEE](../../../security/UniversalKeystoreKit/huks-concepts.md#可信执行环境tee)原则，通过 promise不会返回密钥材料内容，只用于表示此次调用是否成功。

**起始版本：** 12

**需要权限：** ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

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
| Promise & lt;void & gt; |

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
| [12000012](../errorcode-huks.md#12000012-外部错误) |
| [12000013](../errorcode-huks.md#12000013-密钥设置生物访问控制时待绑定的凭据不存在) |
| [12000014](../errorcode-huks.md#12000014-内存不足) |
| [12000015](../errorcode-huks.md#12000015-调用其他系统服务失败) |
| [12000017](../errorcode-huks.md#12000017-同名密钥已存在) |
