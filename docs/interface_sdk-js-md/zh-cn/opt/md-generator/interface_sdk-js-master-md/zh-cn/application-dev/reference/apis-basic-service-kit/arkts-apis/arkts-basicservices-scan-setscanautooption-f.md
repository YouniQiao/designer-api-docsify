# setScanAutoOption

## 导入模块

```TypeScript
```

## setScanAutoOption

```TypeScript
function setScanAutoOption(scannerId: string, optionIndex: number): Promise<void>
```

设置扫描选项为自动模式。使用Promise异步回调。

**起始版本：** 23

**需要权限：** ohos.permission.PRINT

<!--Device-scan-function setScanAutoOption(scannerId: string, optionIndex: int): Promise<void>--><!--Device-scan-function setScanAutoOption(scannerId: string, optionIndex: int): Promise<void>-End-->

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| scannerId | string | 是 |
| [optionIndex](arkts-basicservices-scan-scannerparameter-i.md) | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

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
scan.setScanAutoOption(scannerId, optionIndex).then(() => {
    console.info('set scan auto option success');
}).catch((error: BusinessError) => {
    console.error(`Failed to set scan auto option. Code: ${error.code}, message: ${error.message}`);
});
```
