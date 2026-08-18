# openScanner

## 导入模块

```TypeScript
```

## openScanner

```TypeScript
function openScanner(scannerId: string): Promise<void>
```

打开扫描仪。使用Promise异步回调。

**起始版本：** 23

**需要权限：** ohos.permission.PRINT

<!--Device-scan-function openScanner(scannerId: string): Promise<void>--><!--Device-scan-function openScanner(scannerId: string): Promise<void>-End-->

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| scannerId | string | 是 |

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
scan.openScanner(scannerId).then(() => {
    console.info('open scanner success');
}).catch((error: BusinessError) => {
    console.error(`Failed to open scanner. Code: ${error.code}, message: ${error.message}`);
});
```
