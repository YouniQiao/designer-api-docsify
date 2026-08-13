# encapsulate

## encapsulate

```TypeScript
function encapsulate(keyAlias: string, params: HuksParam[],
      sharedKeyAlias?: string, sharedKeyParams?: HuksParam[]): Promise<HuksReturnResult>
```

后量子加密密钥封装操作，支持HUKS密钥管理 或由应用程序本身决定。如果应用程序选择管理密钥， 对称密钥携带在HuksReturnResult的outData字段中。

**起始版本：** 26.0.0

**废弃版本：** -1

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-huks-function encapsulate(keyAlias: string, params: HuksParam[],      sharedKeyAlias?: string, sharedKeyParams?: HuksParam[]): Promise<HuksReturnResult>--><!--Device-huks-function encapsulate(keyAlias: string, params: HuksParam[],      sharedKeyAlias?: string, sharedKeyParams?: HuksParam[]): Promise<HuksReturnResult>-End-->

**系统能力：** SystemCapability.Security.Huks.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| keyAlias | string | 是 |
| params | [HuksParam](arkts-universalkeystore-huks-huksparam-i.md)[] | 是 |
| sharedKeyAlias | string | 否 |
| sharedKeyParams | [HuksParam](arkts-universalkeystore-huks-huksparam-i.md)[] | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[HuksReturnResult](arkts-universalkeystore-huks-huksreturnresult-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [12000018](../errorcode-huks.md#12000018-输入参数非法) |
| [12000017](../errorcode-huks.md#12000017-同名密钥已存在) |
| [12000016](../errorcode-huks.md#12000016-设备密码未设置) |
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

```TypeScript
import { huks } from '@kit.UniversalKeystoreKit';
import { BusinessError } from '@kit.BasicServicesKit';

let keyAlias = 'ml_kem_pub_key_b';
let params: huks.HuksParam[] = [{
  tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
  value: huks.HuksKeyAlg.HUKS_ALG_ML_KEM,
}, {
  tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
  value: huks.HuksKeySize.HUKS_ML_KEM_KEY_PARAM_SET_768,
}, {
  tag: huks.HuksTag.HUKS_TAG_PURPOSE,
  value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_WRAP,
}];

try {
  huks.encapsulate(keyAlias, params).then((data: huks.HuksReturnResult) => {
    console.info(`encapsulate success, encapsulatedData length: ${(data.outData as Uint8Array).length}`);
    console.info(`sharedSecret length: ${(data.sharedSecret as Uint8Array).length}`);
  }).catch((error: BusinessError) => {
    console.error(`encapsulate failed, code: ${error.code}, message: ${error.message}`);
  });
} catch (error) {
  console.error(`encapsulate input arg invalid`);
}
```
