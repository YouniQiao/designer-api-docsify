# generateCsr

## 导入模块

```TypeScript
import { cert } from 'kits/@kit.DeviceCertificateKit';
```

## generateCsr

```TypeScript
function generateCsr(keyInfo: PrivateKeyInfo, config: CsrGenerationConfig): string | Uint8Array
```

表示使用指定的私钥，传入主体、扩展、摘要算法、输出格式等配置参数去生成CSR。

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Security.Cert

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [keyInfo](arkts-devicecertificate-cert-cmsenvelopeddecryptionconfig-i.md) | [PrivateKeyInfo](arkts-devicecertificate-cert-privatekeyinfo-i.md) | 是 |
| config | [CsrGenerationConfig](arkts-devicecertificate-cert-csrgenerationconfig-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| string \| Uint8Array |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [19020001](../errorcode-cert.md#19020001-内存错误) |
| [19020002](../errorcode-cert.md#19020002-运行时错误) |
| [19030001](../errorcode-cert.md#19030001-调用三方算法库api出错) |
| [19030008](../errorcode-cert.md#19030008-私钥密码错误) |
