# DHKeyUtil

根据素数P的长度和私钥长度（bit位数）生成DH公共密钥参数。

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

<!--Device-cryptoFramework-class DHKeyUtil--><!--Device-cryptoFramework-class DHKeyUtil-End-->

**系统能力：** 
- API版本12+：SystemCapability.Security.CryptoFramework.Key.AsymKey
- API版本11：SystemCapability.Security.CryptoFramework

## genDHCommonParamsSpec

ArkTS-Dyn:
```TypeScript
static genDHCommonParamsSpec(pLen: number, skLen?: number): DHCommonParamsSpec
```

ArkTS-Sta:
```TypeScript
static genDHCommonParamsSpec(pLen: int, skLen?: int): DHCommonParamsSpec
```

根据素数P的长度和私钥长度（单位为bit）生成DH公共密钥参数。详见  
[DH密钥生成规格](../../../security/CryptoArchitectureKit/crypto-key-generation-conversion.md#dh)。

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-DHKeyUtil-static genDHCommonParamsSpec(pLen: int, skLen?: int): DHCommonParamsSpec--><!--Device-DHKeyUtil-static genDHCommonParamsSpec(pLen: int, skLen?: int): DHCommonParamsSpec-End-->

**系统能力：** 
- API版本12+：SystemCapability.Security.CryptoFramework.Key.AsymKey
- API版本11：SystemCapability.Security.CryptoFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pLen | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 是 | 用于指定DH公共密钥参数中素数P的长度，单位为bits。 |
| skLen | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 否 | 用于指定生成DH私钥的最大长度，单位为bits，默认值为0。&lt;br&gt;当参数值设置为0时，生成DH私钥的最大长度为： &lt;br&gt;ffdhe2048：255 bits。&lt;br&gt;ffdhe3072：275 bits。&lt;br&gt;ffdhe4096：325 bits。&lt;br&gt;ffdhe6144：375 bits。 &lt;br&gt;ffdhe8192：400 bits。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DHCommonParamsSpec](arkts-cryptoarchitecture-cryptoframework-dhcommonparamsspec-i.md) | 返回DH公共密钥参数。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) | 非法入参。可能的原因： &lt;br&gt;1. 必填参数未指定； &lt;br&gt;2. 参数类型不正确； &lt;br&gt;3. 参数验证失败。 |
| [801](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/errorcode-universal.md#801-该设备不支持此api) | 该操作不支持。 |
| [17630001](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-crypto-architecture-kit/errorcode-crypto-framework.md#17630001-密码操作错误) | 密码操作错误。 |
| [17620001](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-crypto-architecture-kit/errorcode-crypto-framework.md#17620001-内存操作失败) | 内存操作失败。 |

## 示例

```TypeScript
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { BusinessError } from '@kit.BasicServicesKit';
try {
  let DHCommonParamsSpec = cryptoFramework.DHKeyUtil.genDHCommonParamsSpec(2048);
  console.info('genDHCommonParamsSpec result: success.');
} catch (err) {
  let e: BusinessError = err as BusinessError;
  console.error(`genDHCommonParamsSpec failed: errCode: ${e.code}, errMsg: ${e.message}`);
}
```

