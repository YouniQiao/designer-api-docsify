# getAddedScanners（系统接口）

## getAddedScanners

```TypeScript
function getAddedScanners(): Promise<ScannerDevice[]>
```

获取已添加的扫描仪（系统API）。使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.MANAGE_PRINT_JOB

<!--Device-scan-function getAddedScanners(): Promise<ScannerDevice[]>--><!--Device-scan-function getAddedScanners(): Promise<ScannerDevice[]>-End-->

**系统能力：** SystemCapability.Print.PrintFramework

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise&lt;[ScannerDevice](arkts-basicservices-scan-scannerdevice-i.md)[]&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { scan } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

scan.getAddedScanners().then((scanners: scan.ScannerDevice[]) => {
    console.info('get added scanners success: ' + JSON.stringify(scanners));
}).catch((error: BusinessError) => {
    console.error(`Failed to get added scanners. Code: ${error.code}, message: ${error.message}`);
});
```
