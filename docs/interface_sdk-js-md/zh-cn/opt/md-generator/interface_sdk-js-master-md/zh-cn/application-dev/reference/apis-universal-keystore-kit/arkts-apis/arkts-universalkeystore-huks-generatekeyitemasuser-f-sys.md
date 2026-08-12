# generateKeyItemAsUser（系统接口）

## generateKeyItemAsUser

```TypeScript
function generateKeyItemAsUser(userId: number, keyAlias: string, huksOptions: HuksOptions): Promise<void>
```

指定用户身份生成密钥，使用Promise方式异步返回结果。基于密钥不出[TEE](../../../security/UniversalKeystoreKit/huks-concepts.md#可信执行环境tee)原则，通过promise不会返回密钥材料内容，只用于表示此次调用是否成功。

**起始版本：** 12

**需要权限：** ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

<!--Device-huks-function generateKeyItemAsUser(userId: number, keyAlias: string, huksOptions: HuksOptions): Promise<void>--><!--Device-huks-function generateKeyItemAsUser(userId: number, keyAlias: string, huksOptions: HuksOptions): Promise<void>-End-->

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
| [801](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#801-该设备不支持此api) |
| [12000017](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000017-同名密钥已存在) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [12000006](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000006-算法库操作失败) |
| [12000005](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000005-进程通信错误) |
| [12000004](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000004-文件错误) |
| [12000003](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000003-无效的密钥算法参数) |
| [12000002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000002-缺少密钥算法参数) |
| [12000001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000001-该子功能不支持特性) |
| [12000015](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000015-调用其他系统服务失败) |
| [12000014](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000014-内存不足) |
| [12000013](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000013-密钥设置生物访问控制时待绑定的凭据不存在) |
| [12000012](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-universal-keystore-kit/errorcode-huks.md#12000012-外部错误) |

## 示例

调用方必须是运行在User0~99（包含0和99）用户身份下的系统应用，同时需要申请ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS权限。允许应用安装到User0的配置指导，请参考[singleton|bool|false|是否允许应用安装到单用户下(U0)](../../../../zh-cn/device-dev/subsystems/subsys-app-privilege-config-guide.md#可由设备厂商配置的特权)

```TypeScript
/* 以生成AES密钥为例 */
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

/* 生成密钥 */
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

export default function HuksAsUserTest() {
  console.info('begin huks as user test')
  GenerateKey(aesKeyAlias, GetAesGenerateProperties())
}
```
