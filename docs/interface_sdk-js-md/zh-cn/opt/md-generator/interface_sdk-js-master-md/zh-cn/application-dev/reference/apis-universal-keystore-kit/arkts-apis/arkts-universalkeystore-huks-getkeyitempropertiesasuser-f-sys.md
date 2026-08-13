# getKeyItemPropertiesAsUser（系统接口）

## getKeyItemPropertiesAsUser

```TypeScript
function getKeyItemPropertiesAsUser(
    userId: number,
    keyAlias: string,
    huksOptions: HuksOptions
  ): Promise<HuksReturnResult>
```

Get properties of the key as user.

**起始版本：** 12

**废弃版本：** -1

**需要权限：** ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

<!--Device-huks-function getKeyItemPropertiesAsUser(    userId: number,    keyAlias: string,    huksOptions: HuksOptions  ): Promise<HuksReturnResult>--><!--Device-huks-function getKeyItemPropertiesAsUser(    userId: number,    keyAlias: string,    huksOptions: HuksOptions  ): Promise<HuksReturnResult>-End-->

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
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
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

## 示例

以下代码示例接口调用的前置条件同上文generateKeyItemAsUser的前置条件

```TypeScript
/* 以查询AES密钥属性为例 */
import { huks } from '@kit.UniversalKeystoreKit';
import { BusinessError } from '@kit.BasicServicesKit';

const aesKeyAlias = 'test_aesKeyAlias';
const userId = 100;
const userIdStorageLevel = huks.HuksAuthStorageLevel.HUKS_AUTH_STORAGE_LEVEL_CE;

function GetAesGenerateProperties(): Array<huks.HuksParam> {
  return [{
    tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS_ALG_AES
  }, {
    tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
    value: huks.HuksKeySize.HUKS_AES_KEY_SIZE_128
  }, {
    tag: huks.HuksTag.HUKS_TAG_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT |
    huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_DECRYPT
  }, {
    tag: huks.HuksTag.HUKS_TAG_PADDING,
    value: huks.HuksKeyPadding.HUKS_PADDING_PKCS7
  }, {
    tag: huks.HuksTag.HUKS_TAG_BLOCK_MODE,
    value: huks.HuksCipherMode.HUKS_MODE_CBC
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

/* 2. 查询密钥属性 */
async function GetKeyProperties(keyAlias: string) {
  const options: huks.HuksOptions = {
    properties: [{
      tag: huks.HuksTag.HUKS_TAG_AUTH_STORAGE_LEVEL,
      value: userIdStorageLevel,
    }]
  }
  await huks.getKeyItemPropertiesAsUser(userId, keyAlias, options).then((data) => {
    console.info("获取密钥属性成功！属性为: " + JSON.stringify(data))
  }).catch((err: BusinessError) => {
    console.error("获取密钥属性失败，错误码是： " + err.code + " 错误码信息： " + err.message)
  })
}

async function TestHuksGet() {
  await GenerateKey(aesKeyAlias, GetAesGenerateProperties())
  await GetKeyProperties(aesKeyAlias)
}

export default function HuksAsUserTest() {
  console.info('begin huks as user test')
  TestHuksGet()
}
```
