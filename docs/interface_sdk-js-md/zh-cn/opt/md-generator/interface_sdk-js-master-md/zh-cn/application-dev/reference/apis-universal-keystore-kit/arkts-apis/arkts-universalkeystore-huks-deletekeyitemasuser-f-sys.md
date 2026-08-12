# deleteKeyItemAsUser（系统接口）

## deleteKeyItemAsUser

```TypeScript
function deleteKeyItemAsUser(userId: number, keyAlias: string, huksOptions: HuksOptions): Promise<void>
```

指定用户身份删除密钥，使用Promise方式异步返回结果。

**起始版本：** 12

**需要权限：** ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

<!--Device-huks-function deleteKeyItemAsUser(userId: number, keyAlias: string, huksOptions: HuksOptions): Promise<void>--><!--Device-huks-function deleteKeyItemAsUser(userId: number, keyAlias: string, huksOptions: HuksOptions): Promise<void>-End-->

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
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [801](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#801-该设备不支持此api) |
| [12000005](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000005-进程通信错误) |
| [12000004](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000004-文件错误) |
| [12000001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000001-该子功能不支持特性) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [12000014](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000014-内存不足) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |
| [12000012](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000012-外部错误) |
| [12000011](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000011-目标对象不存在) |

## 示例

以下代码示例接口调用的前置条件同上文[generateKeyItemAsUser](#huksgeneratekeyitemasuser)的前置条件

```TypeScript
/* 以删除AES密钥为例 */
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
  }).catch((err: BusinessError) => {
    console.error("密钥生成失败，错误码是： " + err.code + " 错误码信息： " + err.message)
  })
}
/* 2. 删除密钥 */
async function DeleteKey(keyAlias: string) {
  const options: huks.HuksOptions = {
    properties: [{
      tag: huks.HuksTag.HUKS_TAG_AUTH_STORAGE_LEVEL,
      value: userIdStorageLevel,
    }]
  }
  await huks.deleteKeyItemAsUser(userId, keyAlias, options).then((data) => {
    console.info("别名为: " + keyAlias + " 密钥删除成功！")
  }).catch((err: BusinessError) => {
    console.error("密钥删除失败，错误码是： " + err.code + " 错误码信息： " + err.message)
  })
}

async function TestHuksDelete() {
  await GenerateKey(aesKeyAlias, GetAesGenerateProperties())
  await DeleteKey(aesKeyAlias)
}

export default function HuksAsUserTest() {
  console.info('begin huks as user test')
  TestHuksDelete()
}
```
