# anonAttestKeyItem

## 导入模块

```TypeScript
import { huks } from 'kits/@kit.UniversalKeystoreKit';
```

## anonAttestKeyItem

```TypeScript
function anonAttestKeyItem(keyAlias: string, options: HuksOptions, callback: AsyncCallback<HuksReturnResult>): void
```

获取匿名化密钥证书。使用callback异步回调。该操作需要联网进行，且耗时较长。返回12000012错误码时，可能是由于网络异常导致。此时如果没有联网，需要提示用户网络没有连接，如果已经联网，可能是由于网络抖动导致失败，建议重试。

> **说明：**&gt;
> 获取[HuksKeySecurityLevel](arkts-universalkeystore-huks-hukskeysecuritylevel-e.md)中定义的SE安全级别密钥证书需要ohos.permission.ACCESS_SE_KEY权限。
<!--RP1--><!--RP1End-->

**起始版本：** 11

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Security.Huks.Extension

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| keyAlias | string | 是 |
| options | [HuksOptions](arkts-universalkeystore-huks-huksoptions-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[HuksReturnResult](arkts-universalkeystore-huks-huksreturnresult-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [12000001](../errorcode-huks.md#12000001-该子功能不支持特性) |
| [12000004](../errorcode-huks.md#12000004-文件错误) |
| [12000005](../errorcode-huks.md#12000005-进程通信错误) |
| [12000006](../errorcode-huks.md#12000006-算法库操作失败) |
| [12000011](../errorcode-huks.md#12000011-目标对象不存在) |
| [12000012](../errorcode-huks.md#12000012-外部错误) |
| [12000014](../errorcode-huks.md#12000014-内存不足) |
| [12000018](../errorcode-huks.md#12000018-输入参数非法) |
| [12000026](../errorcode-huks.md#12000026-安全元件故障) |


## anonAttestKeyItem

```TypeScript
function anonAttestKeyItem(keyAlias: string, options: HuksOptions): Promise<HuksReturnResult>
```

获取匿名化密钥证书。使用Promise异步回调。该操作需要联网进行，且耗时较长。返回12000012错误码时，可能是由于网络异常导致。此时如果没有联网，需要提示用户网络没有连接，如果已经联网，可能是由于网络抖动导致失败，建议重试。

> **说明：**&gt;
> 获取[HuksKeySecurityLevel](arkts-universalkeystore-huks-hukskeysecuritylevel-e.md)中定义的SE安全级别密钥证书需要ohos.permission.ACCESS_SE_KEY权限。
<!--RP1--><!--RP1End-->

**起始版本：** 11

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Security.Huks.Extension

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| keyAlias | string | 是 |
| options | [HuksOptions](arkts-universalkeystore-huks-huksoptions-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[HuksReturnResult](arkts-universalkeystore-huks-huksreturnresult-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
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
| [12000018](../errorcode-huks.md#12000018-输入参数非法) |
| [12000026](../errorcode-huks.md#12000026-安全元件故障) |
