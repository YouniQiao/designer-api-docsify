# updatePrinterInDiscovery

## 导入模块

```TypeScript
import { print } from 'kits/@kit.BasicServicesKit';
```

## updatePrinterInDiscovery

```TypeScript
function updatePrinterInDiscovery(printerInformation: PrinterInformation): Promise<void>
```

更新打印机能力到系统打印机发现列表，使用Promise异步回调。

**起始版本：** 14

**需要权限：** ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| printerInformation | [PrinterInformation](arkts-basicservices-print-printerinformation-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
