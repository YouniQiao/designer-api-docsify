# unwrapKeyItem

## 导入模块

```TypeScript
```

## unwrapKeyItem

```TypeScript
function unwrapKeyItem(keyAlias: string, params: HuksOptions, wrappedKey: Uint8Array): Promise<HuksReturnResult>
```

加密导入密钥。使用Promise异步回调。 > **说明：** > > 加密导入[HuksKeySecurityLevel](arkts-universalkeystore-huks-hukskeysecuritylevel-e.md#hukskeysecuritylevel)中定义的SE安全级别密钥需要ohos.permission.ACCESS_SE_KEY权限。 &lt;!--Del--&gt;该功能暂不支持。&lt;!--DelEnd--&gt;

**起始版本：** 20

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-huks-function unwrapKeyItem(keyAlias: string, params: HuksOptions, wrappedKey: Uint8Array): Promise<HuksReturnResult>--><!--Device-huks-function unwrapKeyItem(keyAlias: string, params: HuksOptions, wrappedKey: Uint8Array): Promise<HuksReturnResult>-End-->

**系统能力：** SystemCapability.Security.Huks.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| keyAlias | string | 是 |
| params | [HuksOptions](arkts-universalkeystore-huks-huksoptions-i.md) | 是 |
| [wrappedKey](../../apis-crypto-architecture-kit/arkts-apis/arkts-cryptoarchitecture-cryptoframework-kemencapresult-i.md) | Uint8Array | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[HuksReturnResult](arkts-universalkeystore-huks-huksreturnresult-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [12000005](../errorcode-huks.md#12000005-进程通信错误) |
| [12000004](../errorcode-huks.md#12000004-文件错误) |
| [12000018](../errorcode-huks.md#12000018-输入参数非法) |
| [12000015](../errorcode-huks.md#12000015-调用其他系统服务失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [12000014](../errorcode-huks.md#12000014-内存不足) |
| [12000012](../errorcode-huks.md#12000012-外部错误) |
| [12000026](../errorcode-huks.md#12000026-安全元件故障) |
