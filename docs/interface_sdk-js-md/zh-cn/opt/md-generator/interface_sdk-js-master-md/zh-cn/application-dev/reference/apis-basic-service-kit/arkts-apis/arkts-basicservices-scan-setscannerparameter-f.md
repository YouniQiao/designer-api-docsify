# setScannerParameter

## setScannerParameter

```TypeScript
function setScannerParameter(scannerId: string, optionIndex: number, value: ScannerOptionValue): Promise<void>
```

设置扫描仪参数。使用Promise异步回调。

**起始版本：** 20

**需要权限：** ohos.permission.PRINT

<!--Device-scan-function setScannerParameter(scannerId: string, optionIndex: int, value: ScannerOptionValue): Promise<void>--><!--Device-scan-function setScannerParameter(scannerId: string, optionIndex: int, value: ScannerOptionValue): Promise<void>-End-->

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| scannerId | string | 是 |
| [optionIndex](arkts-basicservices-scan-scannerparameter-i.md) | number | 是 |
| value | [ScannerOptionValue](arkts-basicservices-scan-scanneroptionvalue-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |

## 示例

```TypeScript
import { scan } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

let scannerId: string = 'scanner_001';
let optionIndex: number = 1;
let value: scan.ScannerOptionValue = {
    valueType: scan.OptionValueType.SCAN_TYPE_INT,
    numValue: 100
};
scan.setScannerParameter(scannerId, optionIndex, value).then(() => {
    console.info('set scanner parameter success');
}).catch((error: BusinessError) => {
    console.error(`Failed to set scanner parameter. Code: ${error.code}, message: ${error.message}`);
});
```
