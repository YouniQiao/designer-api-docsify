# anonAttestKeyItemOfflineAsUser（系统接口）

## 导入模块

```TypeScript
import { huks } from 'kits/@kit.UniversalKeystoreKit';
```

## anonAttestKeyItemOfflineAsUser

```TypeScript
function anonAttestKeyItemOfflineAsUser(userId: number, keyAlias: string,
      params: HuksParam[]): Promise<HuksReturnResult>
```

离线获取匿名证明证书。该接口使用promise返回结果。此操作不需要每次都需要网络连接， 比anonAttestKeyItemAsUser函数性能高。

> **说明：**
> &gt;
> -离线密钥证明依赖于网络。您需要定期连接网络才能使用此API更新离线证书。
> &gt;
> -离线匿名密钥证明要求本地时间准确。否则，可能导致对端无法正常工作。验证证书过期。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.Huks.Extension

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| userId | number | 是 |
| keyAlias | string | 是 |
| params | [HuksParam](arkts-universalkeystore-huks-huksparam-i.md)[] | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[HuksReturnResult](arkts-universalkeystore-huks-huksreturnresult-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
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
| [12000018](../errorcode-huks.md#12000018-输入参数非法) |
| [12000024](../errorcode-huks.md#12000024-设备或资源繁忙) |
| [12000027](../errorcode-huks.md#12000027-网络不可用) |
