# registerProvider

## registerProvider

```TypeScript
function registerProvider(providerName: string, params: Array<HuksExternalCryptoParam>): Promise<void>
```

注册指定的外部provider。使用Promise异步回调。

若需使用自定义PIN码弹窗，在注册provider时需要同步注册UIExtensionAbility，注意事项如下：

1. 自定义ability通过UIExtensionAbility扩展实现。2. 注册的UIExtensionAbility可以通过证书管理kit提供的[openUKeyAuthDialog](../../apis-device-certificate-kit/arkts-apis/arkts-security-certmanager.md/arkts-security-certmanager.md)接口统一拉起。 3. 系统拉起自定义弹窗时会通过want接口向开发者传递以下参数：  
 - Action：string参数类型，在拉起自定义弹窗时want传输的Action为"UkeyPINAuth"。  
 - appUid：number参数类型，通过want.parameters传输。"appUid"字段为应用id，开发者可以通过该字段完成应用隔离。  
 - keyUri：string参数类型其值为resourceId，通过want.parameters传输，表示Ukey证书的索引。  
 4. 开发者实现UIExtensionAbility时，应用需根据指定场景返回对应的错误码：  
 - 用户取消操作时，返回-1001。  
 - keyUri指定的证书/密钥不存在时，返回-1008。  
 - 参数格式错误时，返回-1014。  
 - 其余失败场景返回错误码-1000，成功时返回0。

**起始版本：** 22

**需要权限：** ohos.permission.CRYPTO_EXTENSION_REGISTER

<!--Device-huksExternalCrypto-function registerProvider(providerName: string, params: Array<HuksExternalCryptoParam>): Promise<void>--><!--Device-huksExternalCrypto-function registerProvider(providerName: string, params: Array<HuksExternalCryptoParam>): Promise<void>-End-->

**系统能力：** SystemCapability.Security.Huks.CryptoExtension

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| providerName | string | 是 |
| params | Array&lt;HuksExternalCryptoParam&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [12000005](../errorcode-huks.md#12000005-进程通信错误) |
| [12000020](../errorcode-huks.md#12000020-依赖的模块报错) |
| [12000019](../errorcode-huks.md#12000019-同名provider已注册) |
| [12000002](../errorcode-huks.md#12000002-缺少密钥算法参数) |
| [12000018](../errorcode-huks.md#12000018-输入参数非法) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [12000014](../errorcode-huks.md#12000014-内存不足) |
| [12000025](../errorcode-huks.md#12000025-资源超过限制) |

## 示例

```TypeScript
import { huksExternalCrypto } from '@kit.UniversalKeystoreKit';

function stringToUint8Array(str: string) {
  let arr: number[] = [];
  for (let i = 0, j = str.length; i < j; ++i) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

const providerName = "testProviderName";
const extProperties: Array<huksExternalCrypto.HuksExternalCryptoParam> = [
  {
    tag: huksExternalCrypto.HuksExternalCryptoTag.HUKS_EXT_CRYPTO_TAG_ABILITY_NAME,
    value: stringToUint8Array("CryptoExtension")
  }
];
huksExternalCrypto.registerProvider(providerName, extProperties)
    .then(() => {
        console.info('promise: registerProvider success.');
    });
```
