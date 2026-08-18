# getScannerCurrentSetting

## 导入模块

```TypeScript
```

## getScannerCurrentSetting

```TypeScript
function getScannerCurrentSetting(scannerId: string, optionIndex: number): Promise<ScannerOptionValue>
```

获取当前扫描仪设置。使用Promise异步回调。

**起始版本：** 23

**需要权限：** ohos.permission.PRINT

<!--Device-scan-function getScannerCurrentSetting(scannerId: string, optionIndex: int): Promise<ScannerOptionValue>--><!--Device-scan-function getScannerCurrentSetting(scannerId: string, optionIndex: int): Promise<ScannerOptionValue>-End-->

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

**示例**

```TypeScript
import { scan } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

let scannerId: string = 'scanner_001';
let optionIndex: number = 1;
scan.getScannerCurrentSetting(scannerId, optionIndex).then((value: scan.ScannerOptionValue) => {
    console.info('get scanner current setting success: ' + JSON.stringify(value));
}).catch((error: BusinessError) => {
    console.error(`Failed to get scanner current setting. Code: ${error.code}, message: ${error.message}`);
});
```
