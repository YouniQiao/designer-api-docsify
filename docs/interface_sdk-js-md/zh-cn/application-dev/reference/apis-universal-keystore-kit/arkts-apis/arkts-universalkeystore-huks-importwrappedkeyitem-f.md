# importWrappedKeyItem

## 导入模块

```TypeScript
import { huks } from 'kits/@kit.UniversalKeystoreKit';
```

## importWrappedKeyItem

```TypeScript
function importWrappedKeyItem(
    keyAlias: string,
    wrappingKeyAlias: string,
    options: HuksOptions,
    callback: AsyncCallback<void>
  ): void
```

Imports a wrapped key. This API uses an asynchronous callback to return the result.

> **说明：**&gt;
> 导入[HuksKeySecurityLevel](arkts-universalkeystore-huks-hukskeysecuritylevel-e.md)中定义的SE安全级别加密密钥需要ohos.permission.ACCESS_SE_KEY权限。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** 
- API版本12+：SystemCapability.Security.Huks.Core
- API版本9-11：SystemCapability.Security.Huks.Extension

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| keyAlias | string | 是 |
| wrappingKeyAlias | string | 是 |
| options | [HuksOptions](arkts-universalkeystore-huks-huksoptions-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

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
| [12000013](../errorcode-huks.md#12000013-密钥设置生物访问控制时待绑定的凭据不存在) |
| [12000014](../errorcode-huks.md#12000014-内存不足) |
| [12000015](../errorcode-huks.md#12000015-调用其他系统服务失败) |
| [12000017](../errorcode-huks.md#12000017-同名密钥已存在) |
| [12000018](../errorcode-huks.md#12000018-输入参数非法) |
| [12000020](../errorcode-huks.md#12000020-依赖的模块报错) |
| [12000021](../errorcode-huks.md#12000021-ukey-pin码被锁定) |
| [12000023](../errorcode-huks.md#12000023-ukey-pin码未认证) |
| [12000024](../errorcode-huks.md#12000024-设备或资源繁忙) |
| [12000026](../errorcode-huks.md#12000026-安全元件故障) |


## importWrappedKeyItem

```TypeScript
function importWrappedKeyItem(keyAlias: string, wrappingKeyAlias: string, options: HuksOptions): Promise<void>
```

Imports a wrapped key. This API uses a promise to return the result.

> **说明：**&gt;
> 导入[HuksKeySecurityLevel](arkts-universalkeystore-huks-hukskeysecuritylevel-e.md)中定义的SE安全级别加密密钥需要ohos.permission.ACCESS_SE_KEY权限。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Security.Huks.Extension

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| keyAlias | string | 是 |
| wrappingKeyAlias | string | 是 |
| options | [HuksOptions](arkts-universalkeystore-huks-huksoptions-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

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
| [12000013](../errorcode-huks.md#12000013-密钥设置生物访问控制时待绑定的凭据不存在) |
| [12000014](../errorcode-huks.md#12000014-内存不足) |
| [12000015](../errorcode-huks.md#12000015-调用其他系统服务失败) |
| [12000017](../errorcode-huks.md#12000017-同名密钥已存在) |
| [12000018](../errorcode-huks.md#12000018-输入参数非法) |
| [12000020](../errorcode-huks.md#12000020-依赖的模块报错) |
| [12000021](../errorcode-huks.md#12000021-ukey-pin码被锁定) |
| [12000023](../errorcode-huks.md#12000023-ukey-pin码未认证) |
| [12000024](../errorcode-huks.md#12000024-设备或资源繁忙) |
| [12000026](../errorcode-huks.md#12000026-安全元件故障) |
