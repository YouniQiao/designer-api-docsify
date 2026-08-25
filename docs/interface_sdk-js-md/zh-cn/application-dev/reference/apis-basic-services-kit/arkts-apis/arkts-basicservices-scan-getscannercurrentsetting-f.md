# getScannerCurrentSetting

## 导入模块

```TypeScript
import { scan } from 'kits/@kit.BasicServicesKit';
```

## getScannerCurrentSetting

```TypeScript
function getScannerCurrentSetting(scannerId: string, optionIndex: number): Promise<ScannerOptionValue>
```

获取当前扫描仪设置。使用Promise异步回调。

**起始版本：** 20

**需要权限：** ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| scannerId | string | 是 |
| [optionIndex](arkts-basicservices-scan-scannerparameter-i.md) | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[ScannerOptionValue](arkts-basicservices-scan-scanneroptionvalue-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
