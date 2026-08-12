# exportKeyItemAsUser（系统接口）

## exportKeyItemAsUser

```TypeScript
function exportKeyItemAsUser(userId: number, keyAlias: string, huksOptions: HuksOptions): Promise<HuksReturnResult>
```

指定用户身份导出密钥，使用Promise方式回调异步返回的结果。

**起始版本：** 12

**需要权限：** ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

<!--Device-huks-function exportKeyItemAsUser(userId: number, keyAlias: string, huksOptions: HuksOptions): Promise<HuksReturnResult>--><!--Device-huks-function exportKeyItemAsUser(userId: number, keyAlias: string, huksOptions: HuksOptions): Promise<HuksReturnResult>-End-->

**系统能力：** SystemCapability.Security.Huks.Extension

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| userId | number | 是 |
| keyAlias | string | 是 |
| huksOptions | [HuksOptions](arkts-universalkeystore-huks-huksoptions-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[HuksReturnResult](arkts-universalkeystore-huks-huksreturnresult-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#801-该设备不支持此api) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [12000006](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000006-算法库操作失败) |
| [12000005](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000005-进程通信错误) |
| [12000004](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000004-文件错误) |
| [12000003](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000003-无效的密钥算法参数) |
| [12000002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000002-缺少密钥算法参数) |
| [12000001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000001-该子功能不支持特性) |
| [12000014](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000014-内存不足) |
| [12000012](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000012-外部错误) |
| [12000011](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000011-目标对象不存在) |

## 示例

以下代码示例接口调用的前置条件同上文[generateKeyItemAsUser](#huksgeneratekeyitemasuser)的前置条件

```TypeScript
/* 以导出RSA公钥为例 */
import { huks } from '@kit.UniversalKeystoreKit';
import { BusinessError } from '@kit.BasicServicesKit';

const rsaKeyAlias = 'test_rsaKeyAlias';
const userId = 100;
const userIdStorageLevel = huks.HuksAuthStorageLevel.HUKS_AUTH_STORAGE_LEVEL_CE;

function GetRSA4096GenerateProperties(): Array<huks.HuksParam> {
  return [{
    tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS_ALG_RSA
  }, {
    tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
    value: huks.HuksKeySize.HUKS_RSA_KEY_SIZE_4096
  }, {
    tag: huks.HuksTag.HUKS_TAG_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT |
    huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_DECRYPT
  }, {
    tag: huks.HuksTag.HUKS_TAG_DIGEST,
    value: huks.HuksKeyDigest.HUKS_DIGEST_SHA256
  }, {
    tag: huks.HuksTag.HUKS_TAG_PADDING,
    value: huks.HuksKeyPadding.HUKS_PADDING_PKCS1_V1_5
  }, {
    tag: huks.HuksTag.HUKS_TAG_BLOCK_MODE,
    value: huks.HuksCipherMode.HUKS_MODE_ECB
  }, {
    tag: huks.HuksTag.HUKS_TAG_AUTH_STORAGE_LEVEL,
    value: userIdStorageLevel,
  }]
}

/* 1. 生成密钥 */
async function GenerateKey(keyAlias: string, genProperties: Array<huks.HuksParam>) {
  const options: huks.HuksOptions = {
    properties: genProperties
  }
  await huks.generateKeyItemAsUser(userId, keyAlias, options).then((data) => {
    console.info("成功生成了一个别名为：" + keyAlias + " 的密钥")
  }).catch((err: BusinessError) => {
    console.error("密钥生成失败，错误码是： " + err.code + " 错误码信息： " + err.message)
  })
}

/* 2. 导出公钥 */
async function ExportPublicKey(keyAlias: string) {
  const options: huks.HuksOptions = {
    properties: [{
      tag: huks.HuksTag.HUKS_TAG_AUTH_STORAGE_LEVEL,
      value: userIdStorageLevel,
    }]
  }
  await huks.exportKeyItemAsUser(userId, keyAlias, options).then((data) => {
    console.info("成功将别名为：" + keyAlias + " 的公钥导出, data 的长度为" + data?.outData?.length)
  }).catch((err: BusinessError) => {
    console.error("密钥导出失败，错误码是： " + err.code + " 错误码信息： " + err.message)
  })
}

async function ExportHuksTest() {
  await GenerateKey(rsaKeyAlias, GetRSA4096GenerateProperties())
  await ExportPublicKey(rsaKeyAlias)
}

export default function HuksAsUserTest() {
  console.info('begin huks as user test')
  ExportHuksTest()
}
```
