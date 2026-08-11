# addScanner（系统接口）

## addScanner

```TypeScript
function addScanner(uniqueId: string, discoveryMode: ScannerDiscoveryMode): Promise<void>
```

添加扫描仪（系统API）。使用Promise异步回调。

**起始版本：** 20

**需要权限：** ohos.permission.MANAGE_PRINT_JOB

<!--Device-scan-function addScanner(uniqueId: string, discoveryMode: ScannerDiscoveryMode): Promise<void>--><!--Device-scan-function addScanner(uniqueId: string, discoveryMode: ScannerDiscoveryMode): Promise<void>-End-->

**系统能力：** SystemCapability.Print.PrintFramework

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uniqueId | string | 是 |
| discoveryMode | [ScannerDiscoveryMode](arkts-basicservices-scan-scannerdiscoverymode-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { scan } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

// uniqueId可通过getAddedScanners()获取已添加扫描仪的唯一ID，或从scan.on('scanDeviceAdd')事件回调中获得
let uniqueId: string = 'unique_scanner_001';
let discoveryMode: scan.ScannerDiscoveryMode = scan.ScannerDiscoveryMode.TCP_STR;
scan.addScanner(uniqueId, discoveryMode).then(() => {
    console.info('add scanner success');
}).catch((error: BusinessError) => {
    console.error(`Failed to add scanner. Code: ${error.code}, message: ${error.message}`);
});
```
