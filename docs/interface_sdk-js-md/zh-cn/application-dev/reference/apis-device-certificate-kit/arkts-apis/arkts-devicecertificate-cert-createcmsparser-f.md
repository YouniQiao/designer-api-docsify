# createCmsParser

## 导入模块

```TypeScript
import { cert } from 'kits/@kit.DeviceCertificateKit';
```

## createCmsParser

```TypeScript
function createCmsParser(): CmsParser
```

表示创建CmsParser对象。

**起始版本：** 22

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值：**

| 类型 |
| --- |
| [CmsParser](arkts-devicecertificate-cert-cmsparser-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [19020001](../errorcode-cert.md#19020001-内存错误) |
| [19020002](../errorcode-cert.md#19020002-运行时错误) |
| [19030001](../errorcode-cert.md#19030001-调用三方算法库api出错) |
