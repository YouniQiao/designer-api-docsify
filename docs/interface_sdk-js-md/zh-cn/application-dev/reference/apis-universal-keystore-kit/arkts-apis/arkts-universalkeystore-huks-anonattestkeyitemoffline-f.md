# anonAttestKeyItemOffline

## 导入模块

```TypeScript
import { huks } from 'kits/@kit.UniversalKeystoreKit';
```

## anonAttestKeyItemOffline

```TypeScript
function anonAttestKeyItemOffline(keyAlias: string, params: HuksParam[]): Promise<HuksReturnResult>
```

离线模式下获取匿名化密钥证书。使用Promise异步回调。

> **说明：**&gt;
> - 离线密钥证明依赖网络，需要定期联网使用该接口以更新离线证书，推荐优先使用离线匿名密钥证明。&gt;
> - 离线匿名密钥证明需保证本地时间是准确的，否则可能导致对端校验证书超期失败。

> **说明：**
> &gt;
> - Offline key attestation depends on the network. You need to periodically connect to the network to use this API
> to update the offline certificate. Offline anonymous key attestation is recommended.
> &gt;
> - Offline anonymous key attestation requires that the local time be accurate. Otherwise, the peer end may fail to
> verify the certificate expiration。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Security.Huks.Extension

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| keyAlias | string | 是 |
| params | [HuksParam](arkts-universalkeystore-huks-huksparam-i.md)[] | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[HuksReturnResult](arkts-universalkeystore-huks-huksreturnresult-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [12000001](../errorcode-huks.md#12000001-该子功能不支持特性) |
| [12000004](../errorcode-huks.md#12000004-文件错误) |
| [12000005](../errorcode-huks.md#12000005-进程通信错误) |
| [12000006](../errorcode-huks.md#12000006-算法库操作失败) |
| [12000011](../errorcode-huks.md#12000011-目标对象不存在) |
| [12000012](../errorcode-huks.md#12000012-外部错误) |
| [12000014](../errorcode-huks.md#12000014-内存不足) |
| [12000018](../errorcode-huks.md#12000018-输入参数非法) |
| [12000024](../errorcode-huks.md#12000024-设备或资源繁忙) |
| [12000027](../errorcode-huks.md#12000027-网络不可用) |
