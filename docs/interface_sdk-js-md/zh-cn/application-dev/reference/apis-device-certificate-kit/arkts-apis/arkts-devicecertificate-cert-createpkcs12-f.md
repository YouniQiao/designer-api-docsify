# createPkcs12

## 导入模块

```TypeScript
import { cert } from 'kits/@kit.DeviceCertificateKit';
```

## createPkcs12

```TypeScript
function createPkcs12(data: Pkcs12Data, config: Pkcs12CreationConfig): Promise<Uint8Array>
```

表示创建P12。使用Promise方式返回结果。

**起始版本：** 21

**原子化服务API：** 从API版本21开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Security.Cert

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| data | [Pkcs12Data](arkts-devicecertificate-cert-pkcs12data-i.md) | 是 |
| config | [Pkcs12CreationConfig](arkts-devicecertificate-cert-pkcs12creationconfig-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Uint8Array & gt; |

**错误码：**

| 错误码ID |
| --- |
| [19020001](../errorcode-cert.md#19020001-内存错误) |
| [19020002](../errorcode-cert.md#19020002-运行时错误) |
| [19020003](../errorcode-cert.md#19020003-参数检查失败) |
| [19030001](../errorcode-cert.md#19030001-调用三方算法库api出错) |
