# finishSession

## 导入模块

```TypeScript
```

## finishSession

```TypeScript
function finishSession(handle: number, options: HuksOptions, callback: AsyncCallback<HuksReturnResult>): void
```

finishSession操作密钥接口。使用callback异步回调。 huks.initSession、huks.updateSession、huks.finishSession为三段式接口，需要一起使用。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-huks-function finishSession(handle: number, options: HuksOptions, callback: AsyncCallback<HuksReturnResult>): void--><!--Device-huks-function finishSession(handle: number, options: HuksOptions, callback: AsyncCallback<HuksReturnResult>): void-End-->

**系统能力：** SystemCapability.Security.Huks.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| handle | number | 是 |
| options | [HuksOptions](arkts-universalkeystore-huks-huksoptions-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[HuksReturnResult](arkts-universalkeystore-huks-huksreturnresult-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [12000023](../errorcode-huks.md#12000023-ukey-pin码未认证) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [12000021](../errorcode-huks.md#12000021-ukey-pin码被锁定) |
| [12000020](../errorcode-huks.md#12000020-依赖的模块报错) |
| [12000018](../errorcode-huks.md#12000018-输入参数非法) |
| [12000017](../errorcode-huks.md#12000017-同名密钥已存在) |
| [12000026](../errorcode-huks.md#12000026-安全元件故障) |
| [12000024](../errorcode-huks.md#12000024-设备或资源繁忙) |
| [12000007](../errorcode-huks.md#12000007-密钥访问失败-密钥已失效) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12000006](../errorcode-huks.md#12000006-算法库操作失败) |
| [12000005](../errorcode-huks.md#12000005-进程通信错误) |
| [12000004](../errorcode-huks.md#12000004-文件错误) |
| [12000003](../errorcode-huks.md#12000003-无效的密钥算法参数) |
| [12000002](../errorcode-huks.md#12000002-缺少密钥算法参数) |
| [12000001](../errorcode-huks.md#12000001-该子功能不支持特性) |
| [12000014](../errorcode-huks.md#12000014-内存不足) |
| [12000012](../errorcode-huks.md#12000012-外部错误) |
| [12000011](../errorcode-huks.md#12000011-目标对象不存在) |
| [12000009](../errorcode-huks.md#12000009-密钥访问失败-密钥访问超时) |
| [12000008](../errorcode-huks.md#12000008-密钥访问失败-密钥认证失败) |


## finishSession

```TypeScript
function finishSession(
    handle: number,
    options: HuksOptions,
    token: Uint8Array,
    callback: AsyncCallback<HuksReturnResult>
  ): void
```

Finishes the key operation. This API uses an asynchronous callback to return the result. huks.initSession, huks.updateSession, and huks.finishSession must be used together.

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-huks-function finishSession(    handle: number,    options: HuksOptions,    token: Uint8Array,    callback: AsyncCallback<HuksReturnResult>  ): void--><!--Device-huks-function finishSession(    handle: number,    options: HuksOptions,    token: Uint8Array,    callback: AsyncCallback<HuksReturnResult>  ): void-End-->

**系统能力：** SystemCapability.Security.Huks.Extension

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| handle | number | 是 |
| options | [HuksOptions](arkts-universalkeystore-huks-huksoptions-i.md) | 是 |
| token | Uint8Array | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[HuksReturnResult](arkts-universalkeystore-huks-huksreturnresult-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [12000018](../errorcode-huks.md#12000018-输入参数非法) |
| [12000017](../errorcode-huks.md#12000017-同名密钥已存在) |
| [12000026](../errorcode-huks.md#12000026-安全元件故障) |
| [12000007](../errorcode-huks.md#12000007-密钥访问失败-密钥已失效) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12000006](../errorcode-huks.md#12000006-算法库操作失败) |
| [12000005](../errorcode-huks.md#12000005-进程通信错误) |
| [12000004](../errorcode-huks.md#12000004-文件错误) |
| [12000003](../errorcode-huks.md#12000003-无效的密钥算法参数) |
| [12000002](../errorcode-huks.md#12000002-缺少密钥算法参数) |
| [12000001](../errorcode-huks.md#12000001-该子功能不支持特性) |
| [12000014](../errorcode-huks.md#12000014-内存不足) |
| [12000012](../errorcode-huks.md#12000012-外部错误) |
| [12000011](../errorcode-huks.md#12000011-目标对象不存在) |
| [12000009](../errorcode-huks.md#12000009-密钥访问失败-密钥访问超时) |
| [12000008](../errorcode-huks.md#12000008-密钥访问失败-密钥认证失败) |


## finishSession

```TypeScript
function finishSession(handle: number, options: HuksOptions, token?: Uint8Array): Promise<HuksReturnResult>
```

finishSession操作密钥接口。使用Promise异步回调。 huks.initSession、huks.updateSession、huks.finishSession为三段式接口，需要一起使用。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-huks-function finishSession(handle: number, options: HuksOptions, token?: Uint8Array): Promise<HuksReturnResult>--><!--Device-huks-function finishSession(handle: number, options: HuksOptions, token?: Uint8Array): Promise<HuksReturnResult>-End-->

**系统能力：** SystemCapability.Security.Huks.Extension

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| handle | number | 是 |
| options | [HuksOptions](arkts-universalkeystore-huks-huksoptions-i.md) | 是 |
| token | Uint8Array | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[HuksReturnResult](arkts-universalkeystore-huks-huksreturnresult-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [12000023](../errorcode-huks.md#12000023-ukey-pin码未认证) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [12000021](../errorcode-huks.md#12000021-ukey-pin码被锁定) |
| [12000020](../errorcode-huks.md#12000020-依赖的模块报错) |
| [12000018](../errorcode-huks.md#12000018-输入参数非法) |
| [12000017](../errorcode-huks.md#12000017-同名密钥已存在) |
| [12000026](../errorcode-huks.md#12000026-安全元件故障) |
| [12000024](../errorcode-huks.md#12000024-设备或资源繁忙) |
| [12000007](../errorcode-huks.md#12000007-密钥访问失败-密钥已失效) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12000006](../errorcode-huks.md#12000006-算法库操作失败) |
| [12000005](../errorcode-huks.md#12000005-进程通信错误) |
| [12000004](../errorcode-huks.md#12000004-文件错误) |
| [12000003](../errorcode-huks.md#12000003-无效的密钥算法参数) |
| [12000002](../errorcode-huks.md#12000002-缺少密钥算法参数) |
| [12000001](../errorcode-huks.md#12000001-该子功能不支持特性) |
| [12000014](../errorcode-huks.md#12000014-内存不足) |
| [12000012](../errorcode-huks.md#12000012-外部错误) |
| [12000011](../errorcode-huks.md#12000011-目标对象不存在) |
| [12000009](../errorcode-huks.md#12000009-密钥访问失败-密钥访问超时) |
| [12000008](../errorcode-huks.md#12000008-密钥访问失败-密钥认证失败) |
