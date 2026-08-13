# importKeyItemAsUser（系统接口）

## importKeyItemAsUser

```TypeScript
function importKeyItemAsUser(userId: number, keyAlias: string, huksOptions: HuksOptions): Promise<void>
```

指定用户身份导入明文密钥，使用Promise方式异步返回结果。

**起始版本：** 12

**废弃版本：** -1

**需要权限：** ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

<!--Device-huks-function importKeyItemAsUser(userId: number, keyAlias: string, huksOptions: HuksOptions): Promise<void>--><!--Device-huks-function importKeyItemAsUser(userId: number, keyAlias: string, huksOptions: HuksOptions): Promise<void>-End-->

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
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [12000017](../errorcode-huks.md#12000017-同名密钥已存在) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12000006](../errorcode-huks.md#12000006-算法库操作失败) |
| [12000005](../errorcode-huks.md#12000005-进程通信错误) |
| [12000004](../errorcode-huks.md#12000004-文件错误) |
| [12000003](../errorcode-huks.md#12000003-无效的密钥算法参数) |
| [12000002](../errorcode-huks.md#12000002-缺少密钥算法参数) |
| [12000001](../errorcode-huks.md#12000001-该子功能不支持特性) |
| [12000015](../errorcode-huks.md#12000015-调用其他系统服务失败) |
| [12000014](../errorcode-huks.md#12000014-内存不足) |
| [12000013](../errorcode-huks.md#12000013-密钥设置生物访问控制时待绑定的凭据不存在) |
| [12000012](../errorcode-huks.md#12000012-外部错误) |
| [12000011](../errorcode-huks.md#12000011-目标对象不存在) |

## 示例

以下代码示例接口调用的前置条件同上文generateKeyItemAsUser的前置条件

```TypeScript
/* 以导入AES密钥为例 */
import { huks } from '@kit.UniversalKeystoreKit';
import { BusinessError } from '@kit.BasicServicesKit';

const aesKeyAlias = 'test_aesKeyAlias';
const userId = 100;
const userIdStorageLevel = huks.HuksAuthStorageLevel.HUKS_AUTH_STORAGE_LEVEL_CE;
const plainAesKey128 = new Uint8Array([
  0xfb, 0x8b, 0x9f, 0x12, 0xa0, 0x83, 0x19, 0xbe, 0x6a, 0x6f, 0x63, 0x2a, 0x7c, 0x86, 0xba, 0xca
]);
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
/* 导入密钥明文 */
async function ImportPlainKey(keyAlias: string, importProperties: Array<huks.HuksParam>, plainKey: Uint8Array) {
  const options: huks.HuksOptions = {
    properties: importProperties,
    inData: plainKey
  }
  await huks.importKeyItemAsUser(userId, keyAlias, options).then((data) => {
    console.info("成功导入了一个别名为：" + keyAlias + " 的密钥")
  }).catch((err: BusinessError) => {
    console.error("密钥导入失败，错误码是： " + err.code + " 错误码信息： " + err.message)
  })
}

export default function HuksAsUserTest() {
  console.info('begin huks as user test')
  ImportPlainKey(aesKeyAlias, GetAesGenerateProperties(), plainAesKey128)
}
```
