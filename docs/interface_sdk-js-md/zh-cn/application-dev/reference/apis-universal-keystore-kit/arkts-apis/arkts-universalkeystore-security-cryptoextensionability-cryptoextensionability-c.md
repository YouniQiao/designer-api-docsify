# CryptoExtensionAbility

Class to be override for external crypto extension ability.

**起始版本：** 22

**系统能力：** SystemCapability.Security.Huks.CryptoExtension

## 导入模块

```TypeScript
import { CryptoExtensionAbility, HuksCryptoExtensionCertInfo, HuksCryptoExtensionResult, HuksCryptoExtensionResultCode, HuksCryptoExtensionParam, HuksCryptoExtensionParams } from 'kits/@kit.UniversalKeystoreKit';
```

## onAuthUkeyPin

```TypeScript
onAuthUkeyPin(handle: string, params: Array<huksExternalCrypto.HuksExternalCryptoParam> |
      HuksCryptoExtensionParam[]): Promise<HuksCryptoExtensionResult>
```

请求Ukey认证PIN码。使用Promise异步回调。

**起始版本：** 22

**系统能力：** SystemCapability.Security.Huks.CryptoExtension

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| handle | string | 是 |
| params | Array & lt;huksExternalCrypto.HuksExternalCryptoParam & gt; \ | [HuksCryptoExtensionParam](arkts-universalkeystore-security-cryptoextensionability-hukscryptoextensionparam-i.md)[] | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[HuksCryptoExtensionResult](arkts-universalkeystore-security-cryptoextensionability-hukscryptoextensionresult-i.md)&gt; |

## onClearUkeyPinAuthState

```TypeScript
onClearUkeyPinAuthState(handle: string, params: Array<huksExternalCrypto.HuksExternalCryptoParam> |
      HuksCryptoExtensionParam[]): Promise<HuksCryptoExtensionResult>
```

清除应用维度PIN码的认证状态。使用Promise异步回调。

**起始版本：** 22

**系统能力：** SystemCapability.Security.Huks.CryptoExtension

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| handle | string | 是 |
| params | Array & lt;huksExternalCrypto.HuksExternalCryptoParam & gt; \ | [HuksCryptoExtensionParam](arkts-universalkeystore-security-cryptoextensionability-hukscryptoextensionparam-i.md)[] | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[HuksCryptoExtensionResult](arkts-universalkeystore-security-cryptoextensionability-hukscryptoextensionresult-i.md)&gt; |

## onCloseResource

```TypeScript
onCloseResource(handle: string, params: Array<huksExternalCrypto.HuksExternalCryptoParam> |
      HuksCryptoExtensionParam[]): Promise<HuksCryptoExtensionResult>
```

根据参数中的handle，关闭Ukey的密钥资源。使用Promise异步回调。

**起始版本：** 22

**系统能力：** SystemCapability.Security.Huks.CryptoExtension

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| handle | string | 是 |
| params | Array & lt;huksExternalCrypto.HuksExternalCryptoParam & gt; \ | [HuksCryptoExtensionParam](arkts-universalkeystore-security-cryptoextensionability-hukscryptoextensionparam-i.md)[] | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[HuksCryptoExtensionResult](arkts-universalkeystore-security-cryptoextensionability-hukscryptoextensionresult-i.md)&gt; |

## onEnumCertificates

```TypeScript
onEnumCertificates(params?: Array<huksExternalCrypto.HuksExternalCryptoParam> | HuksCryptoExtensionParam[]):
      Promise<HuksCryptoExtensionResult>
```

枚举Extension下所有Ukey设备的证书信息。使用Promise异步回调。

**起始版本：** 22

**系统能力：** SystemCapability.Security.Huks.CryptoExtension

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| params | Array & lt;huksExternalCrypto.HuksExternalCryptoParam & gt; \ | [HuksCryptoExtensionParam](arkts-universalkeystore-security-cryptoextensionability-hukscryptoextensionparam-i.md)[] | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[HuksCryptoExtensionResult](arkts-universalkeystore-security-cryptoextensionability-hukscryptoextensionresult-i.md)&gt; |

## onExportCertificate

```TypeScript
onExportCertificate(resourceId: string, params?: Array<huksExternalCrypto.HuksExternalCryptoParam> |
      HuksCryptoExtensionParam[]): Promise<HuksCryptoExtensionResult>
```

查询指定resourceId下的证书。使用Promise异步回调。

**起始版本：** 22

**系统能力：** SystemCapability.Security.Huks.CryptoExtension

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| resourceId | string | 是 |
| params | Array & lt;huksExternalCrypto.HuksExternalCryptoParam & gt; \ | [HuksCryptoExtensionParam](arkts-universalkeystore-security-cryptoextensionability-hukscryptoextensionparam-i.md)[] | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[HuksCryptoExtensionResult](arkts-universalkeystore-security-cryptoextensionability-hukscryptoextensionresult-i.md)&gt; |

## onExportKeyItem

```TypeScript
onExportKeyItem(handle: string, params: HuksCryptoExtensionParam[]): Promise<HuksCryptoExtensionResult>
```

用于导出指定密钥的公钥。使用Promise异步回调。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.Huks.CryptoExtension

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| handle | string | 是 |
| params | [HuksCryptoExtensionParam](arkts-universalkeystore-security-cryptoextensionability-hukscryptoextensionparam-i.md)[] | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[HuksCryptoExtensionResult](arkts-universalkeystore-security-cryptoextensionability-hukscryptoextensionresult-i.md)&gt; |

## onFinishSession

```TypeScript
onFinishSession(initHandle: string, params: huks.HuksOptions | HuksCryptoExtensionParams):
      Promise<HuksCryptoExtensionResult>
```

三段式密钥会话结束操作。使用Promise异步回调。

**起始版本：** 22

**系统能力：** SystemCapability.Security.Huks.CryptoExtension

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| initHandle | string | 是 |
| params | huks.HuksOptions \| [HuksCryptoExtensionParams](arkts-universalkeystore-security-cryptoextensionability-hukscryptoextensionparams-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[HuksCryptoExtensionResult](arkts-universalkeystore-security-cryptoextensionability-hukscryptoextensionresult-i.md)&gt; |

## onGenerateKeyItem

```TypeScript
onGenerateKeyItem(handle: string, params:HuksCryptoExtensionParam[]): Promise<HuksCryptoExtensionResult>
```

用于在扩展设备内生成密钥对。使用Promise异步回调。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.Huks.CryptoExtension

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| handle | string | 是 |
| params | [HuksCryptoExtensionParam](arkts-universalkeystore-security-cryptoextensionability-hukscryptoextensionparam-i.md)[] | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[HuksCryptoExtensionResult](arkts-universalkeystore-security-cryptoextensionability-hukscryptoextensionresult-i.md)&gt; |

## onGetProperty

```TypeScript
onGetProperty(handle: string, propertyId: string, params: Array<huksExternalCrypto.HuksExternalCryptoParam> |
      HuksCryptoExtensionParam[]): Promise<HuksCryptoExtensionResult>
```

查询操作回调。

**起始版本：** 22

**系统能力：** SystemCapability.Security.Huks.CryptoExtension

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| handle | string | 是 |
| propertyId | string | 是 |
| params | Array & lt;huksExternalCrypto.HuksExternalCryptoParam & gt; \ | [HuksCryptoExtensionParam](arkts-universalkeystore-security-cryptoextensionability-hukscryptoextensionparam-i.md)[] | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[HuksCryptoExtensionResult](arkts-universalkeystore-security-cryptoextensionability-hukscryptoextensionresult-i.md)&gt; |

## onGetResourceId

```TypeScript
onGetResourceId(params: HuksCryptoExtensionParam[]): Promise<HuksCryptoExtensionResult>
```

回调以获取加密扩展的资源ID。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.Huks.CryptoExtension

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| params | [HuksCryptoExtensionParam](arkts-universalkeystore-security-cryptoextensionability-hukscryptoextensionparam-i.md)[] | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[HuksCryptoExtensionResult](arkts-universalkeystore-security-cryptoextensionability-hukscryptoextensionresult-i.md)&gt; |

## onGetUkeyPinAuthState

```TypeScript
onGetUkeyPinAuthState(handle: string, params: Array<huksExternalCrypto.HuksExternalCryptoParam> |
      HuksCryptoExtensionParam[]): Promise<HuksCryptoExtensionResult>
```

获取Ukey的PIN码认证状态。使用Promise异步回调。

**起始版本：** 22

**系统能力：** SystemCapability.Security.Huks.CryptoExtension

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| handle | string | 是 |
| params | Array & lt;huksExternalCrypto.HuksExternalCryptoParam & gt; \ | [HuksCryptoExtensionParam](arkts-universalkeystore-security-cryptoextensionability-hukscryptoextensionparam-i.md)[] | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[HuksCryptoExtensionResult](arkts-universalkeystore-security-cryptoextensionability-hukscryptoextensionresult-i.md)&gt; |

## onImportCertificate

```TypeScript
onImportCertificate(handle: string, params: HuksCryptoExtensionParam[],
      certInfo: HuksCryptoExtensionCertInfo): Promise<HuksCryptoExtensionResult>
```

导入指定资源句柄的证书。使用Promise异步回调。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.Huks.CryptoExtension

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| handle | string | 是 |
| params | [HuksCryptoExtensionParam](arkts-universalkeystore-security-cryptoextensionability-hukscryptoextensionparam-i.md)[] | 是 |
| [certInfo](../../apis-device-certificate-kit/arkts-apis/arkts-devicecertificate-certificatemanager-cmresult-i.md) | [HuksCryptoExtensionCertInfo](arkts-universalkeystore-security-cryptoextensionability-hukscryptoextensioncertinfo-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[HuksCryptoExtensionResult](arkts-universalkeystore-security-cryptoextensionability-hukscryptoextensionresult-i.md)&gt; |

## onImportWrappedKeyItem

```TypeScript
onImportWrappedKeyItem(handle: string, wrappingHandle: string, params: HuksCryptoExtensionParam[],
      wrappedKey: Uint8Array): Promise<HuksCryptoExtensionResult>
```

用于导入加密封装的密钥对。使用Promise异步回调。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.Huks.CryptoExtension

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| handle | string | 是 |
| wrappingHandle | string | 是 |
| params | [HuksCryptoExtensionParam](arkts-universalkeystore-security-cryptoextensionability-hukscryptoextensionparam-i.md)[] | 是 |
| [wrappedKey](../../apis-crypto-architecture-kit/arkts-apis/arkts-cryptoarchitecture-cryptoframework-kemencapresult-i.md) | Uint8Array | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[HuksCryptoExtensionResult](arkts-universalkeystore-security-cryptoextensionability-hukscryptoextensionresult-i.md)&gt; |

## onInitSession

```TypeScript
onInitSession(handle: string, params: huks.HuksOptions | HuksCryptoExtensionParams):
      Promise<HuksCryptoExtensionResult>
```

三段式初始化密钥会话操作。使用Promise异步回调。

**起始版本：** 22

**系统能力：** SystemCapability.Security.Huks.CryptoExtension

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| handle | string | 是 |
| params | huks.HuksOptions \| [HuksCryptoExtensionParams](arkts-universalkeystore-security-cryptoextensionability-hukscryptoextensionparams-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[HuksCryptoExtensionResult](arkts-universalkeystore-security-cryptoextensionability-hukscryptoextensionresult-i.md)&gt; |

## onOpenResource

```TypeScript
onOpenResource(resourceId: string, params: Array<huksExternalCrypto.HuksExternalCryptoParam> |
     HuksCryptoExtensionParam[]): Promise<HuksCryptoExtensionResult>
```

打开资源句柄回调，在加密操作之前需打开资源，获取句柄。注意：返回的句柄必须被onCloseResource关闭。

**起始版本：** 22

**系统能力：** SystemCapability.Security.Huks.CryptoExtension

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| resourceId | string | 是 |
| params | Array & lt;huksExternalCrypto.HuksExternalCryptoParam & gt; \ | [HuksCryptoExtensionParam](arkts-universalkeystore-security-cryptoextensionability-hukscryptoextensionparam-i.md)[] | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[HuksCryptoExtensionResult](arkts-universalkeystore-security-cryptoextensionability-hukscryptoextensionresult-i.md)&gt; |

## onSetProperty

```TypeScript
onSetProperty(handle: string, propertyId: string, params: HuksCryptoExtensionParam[]):
      Promise<HuksCryptoExtensionResult>
```

根据参数中的handle和propertyId设置属性。使用Promise异步回调。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.Huks.CryptoExtension

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| handle | string | 是 |
| propertyId | string | 是 |
| params | [HuksCryptoExtensionParam](arkts-universalkeystore-security-cryptoextensionability-hukscryptoextensionparam-i.md)[] | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[HuksCryptoExtensionResult](arkts-universalkeystore-security-cryptoextensionability-hukscryptoextensionresult-i.md)&gt; |

## onUpdateSession

```TypeScript
onUpdateSession(initHandle: string, params: huks.HuksOptions | HuksCryptoExtensionParams):
      Promise<HuksCryptoExtensionResult>
```

三段式密钥会话更新数据操作。使用Promise异步回调。

**起始版本：** 22

**系统能力：** SystemCapability.Security.Huks.CryptoExtension

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| initHandle | string | 是 |
| params | huks.HuksOptions \| [HuksCryptoExtensionParams](arkts-universalkeystore-security-cryptoextensionability-hukscryptoextensionparams-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[HuksCryptoExtensionResult](arkts-universalkeystore-security-cryptoextensionability-hukscryptoextensionresult-i.md)&gt; |
