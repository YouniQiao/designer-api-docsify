# decapsulate

## 导入模块

```TypeScript
import { huks } from 'kits/@kit.UniversalKeystoreKit';
```

## decapsulate

```TypeScript
function decapsulate(keyAlias: string, params: HuksParam[], encapData: Uint8Array,
      sharedKeyAlias?: string, sharedKeyParams?:  HuksParam[]): Promise<HuksReturnResult>
```

Post-Quantum Cryptography密钥解封装操作，支持HUKS密钥管理或由应用程序本身决定。如果应用程序选择管理密钥，对称密钥包含在HuksReturnResult的outData字段中。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为26.0.0。

<!--Device-huks-function decapsulate(keyAlias: string, params: HuksParam[], encapData: Uint8Array,      sharedKeyAlias?: string, sharedKeyParams?:  HuksParam[]): Promise<HuksReturnResult>--><!--Device-huks-function decapsulate(keyAlias: string, params: HuksParam[], encapData: Uint8Array,      sharedKeyAlias?: string, sharedKeyParams?:  HuksParam[]): Promise<HuksReturnResult>-End-->

**系统能力：** SystemCapability.Security.Huks.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keyAlias | string | 是 | 后量子加密算法的密钥名称。 |
| params | [HuksParam](arkts-universalkeystore-huks-huksparam-i.md)[] | 是 | 表示解封装属性。 |
| encapData | Uint8Array | 是 | 表示封装后的共享密钥。 |
| sharedKeyAlias | string | 否 | 表示解封装密钥的密钥别名。 如果使用HUKS进行密钥管理，则必须指定该参数。 如果应用程序自己管理密钥，则忽略此参数。 |
| sharedKeyParams | [HuksParam](arkts-universalkeystore-huks-huksparam-i.md)[] | 否 | 表示解封装后的key的属性。 如果使用HUKS进行密钥管理，则必须指定该参数。 如果应用程序自己管理密钥，则忽略此参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;HuksReturnResult&gt; | 返回值 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | API is not supported. |
| 12000018 | Invalid input parameter. |
| 12000017 | A key with the same alias already exists. |
| 12000016 | The lock screen password is not set. |
| 12000006 | The algorithm engine reports an error. Check the input parameters. |
| 12000005 | IPC communication failed. |
| 12000004 | The file operation failed. |
| 12000003 | The algorithm parameter is invalid. Check the algorithm parameter. |
| 12000002 | The algorithm parameter is missing. Check the algorithm parameter. |
| 12000001 | Algorithm mode is not supported |
| 12000015 | Failed to obtain the security information using UserIAM. |
| 12000014 | Insufficient memory. |
| 12000013 | Queried credential does not exist |
| 12000012 | The device environment or input parameter is abnormal. |
| 12000011 | The queried key does not exist. Check the key-related parameters. |

## 示例

```TypeScript
import { huks } from '@kit.UniversalKeystoreKit';
import { BusinessError } from '@kit.BasicServicesKit';

let keyAlias = 'ml_kem_key_b';
let params: huks.HuksParam[] = [{
  tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
  value: huks.HuksKeyAlg.HUKS_ALG_ML_KEM,
}, {
  tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
  value: huks.HuksKeySize.HUKS_ML_KEM_KEY_PARAM_SET_768,
}, {
  tag: huks.HuksTag.HUKS_TAG_PURPOSE,
  value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_UNWRAP,
}];

let encapData = new Uint8Array(784);

try {
  huks.decapsulate(keyAlias, params, encapData).then((data: huks.HuksReturnResult) => {
    console.info(`decapsulate success, sharedSecret length: ${(data.sharedSecret as Uint8Array).length}`);
  }).catch((error: BusinessError) => {
    console.error(`decapsulate failed, code: ${error.code}, message: ${error.message}`);
  });
} catch (error) {
  console.error(`decapsulate input arg invalid`);
}
```

