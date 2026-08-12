# getResourceId

## getResourceId

```TypeScript
function getResourceId(providerName: string, params: HuksExternalCryptoParam[]): Promise<string>
```

获取密钥扩展能力的资源ID。使用Promise异步回调。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-huksExternalCrypto-function getResourceId(providerName: string, params: HuksExternalCryptoParam[]): Promise<string>--><!--Device-huksExternalCrypto-function getResourceId(providerName: string, params: HuksExternalCryptoParam[]): Promise<string>-End-->

**系统能力：** SystemCapability.Security.Huks.CryptoExtension

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| providerName | string | 是 |
| params | [HuksExternalCryptoParam](arkts-universalkeystore-huksexternalcrypto-huksexternalcryptoparam-i.md)[] | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#801-该设备不支持此api) |
| [12000005](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000005-进程通信错误) |
| [12000020](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000020-依赖的模块报错) |
| [12000002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000002-缺少密钥算法参数) |
| [12000018](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000018-输入参数非法) |
| [12000014](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000014-内存不足) |
| [12000012](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000012-外部错误) |
| [12000011](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000011-目标对象不存在) |
| [12000024](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000024-设备或资源繁忙) |

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
const abilityName = "CryptoExtension";
const bundleName = "com.example.cryptoapplication";
// 资源信息，格式和内容由厂商自定义
const resourceInfo = "vendor_defined_resource_info";

const extProperties: Array<huksExternalCrypto.HuksExternalCryptoParam> = [
  {
    tag: huksExternalCrypto.HuksExternalCryptoTag.HUKS_EXT_CRYPTO_TAG_ABILITY_NAME,
    value: stringToUint8Array(abilityName)
  },
  {
    tag: huksExternalCrypto.HuksExternalCryptoTag.HUKS_EXT_CRYPTO_TAG_BUNDLE_NAME,
    value: stringToUint8Array(bundleName)
  },
  {
    tag: huksExternalCrypto.HuksExternalCryptoTag.HUKS_EXT_CRYPTO_TAG_RESOURCE_INFO,
    value: stringToUint8Array(resourceInfo)
  }
];

huksExternalCrypto.getResourceId(providerName, extProperties)
    .then((resourceId) => {
      console.info(`promise: getResourceId success, resourceId: ${resourceId}`);
    });
```
