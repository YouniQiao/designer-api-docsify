# createCmsGenerator

## 导入模块

```TypeScript
import { cert } from 'kits/@kit.DeviceCertificateKit';
```

## createCmsGenerator

```TypeScript
function createCmsGenerator(contentType: CmsContentType): CmsGenerator
```

表示创建CmsGenerator对象。

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Security.Cert

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| contentType | [CmsContentType](arkts-devicecertificate-cert-cmscontenttype-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [CmsGenerator](arkts-devicecertificate-cert-cmsgenerator-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [19020001](../errorcode-cert.md#19020001-内存错误) |
| [19020002](../errorcode-cert.md#19020002-运行时错误) |
| [19030001](../errorcode-cert.md#19030001-调用三方算法库api出错) |
