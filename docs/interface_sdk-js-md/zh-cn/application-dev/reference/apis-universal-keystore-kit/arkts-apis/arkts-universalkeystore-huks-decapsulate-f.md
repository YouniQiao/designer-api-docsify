# decapsulate

## 导入模块

```TypeScript
import { huks } from 'kits/@kit.UniversalKeystoreKit';
```

## decapsulate

```TypeScript
function decapsulate(keyAlias: string, params: HuksParam[], encapData: Uint8Array,
      sharedKeyAlias?: string, sharedKeyParams?:  HuksParam[]): Promise<HuksReturnResult>
```

Post-Quantum Cryptography密钥解封装操作，支持HUKS密钥管理 或由应用程序本身决定。如果应用程序选择管理密钥， 对称密钥包含在HuksReturnResult的outData字段中。

**起始版本：** 26.0.0

**系统能力：** SystemCapability.Security.Huks.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| keyAlias | string | 是 |
| params | [HuksParam](arkts-universalkeystore-huks-huksparam-i.md)[] | 是 |
| encapData | Uint8Array | 是 |
| sharedKeyAlias | string | 否 |
| sharedKeyParams | [HuksParam](arkts-universalkeystore-huks-huksparam-i.md)[] | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[HuksReturnResult](arkts-universalkeystore-huks-huksreturnresult-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [12000001](../errorcode-huks.md#12000001-该子功能不支持特性) |
| [12000002](../errorcode-huks.md#12000002-缺少密钥算法参数) |
| [12000003](../errorcode-huks.md#12000003-无效的密钥算法参数) |
| [12000004](../errorcode-huks.md#12000004-文件错误) |
| [12000005](../errorcode-huks.md#12000005-进程通信错误) |
| [12000006](../errorcode-huks.md#12000006-算法库操作失败) |
| [12000011](../errorcode-huks.md#12000011-目标对象不存在) |
| [12000012](../errorcode-huks.md#12000012-外部错误) |
| [12000013](../errorcode-huks.md#12000013-密钥设置生物访问控制时待绑定的凭据不存在) |
| [12000014](../errorcode-huks.md#12000014-内存不足) |
| [12000015](../errorcode-huks.md#12000015-调用其他系统服务失败) |
| [12000016](../errorcode-huks.md#12000016-设备密码未设置) |
| [12000017](../errorcode-huks.md#12000017-同名密钥已存在) |
| [12000018](../errorcode-huks.md#12000018-输入参数非法) |
