# getAddedScanners（系统接口）

## 导入模块

```TypeScript
import { scan } from 'kits/@kit.BasicServicesKit';
```

## getAddedScanners

```TypeScript
function getAddedScanners(): Promise<ScannerDevice[]>
```

获取已添加的扫描仪（系统API）。使用Promise异步回调。

**起始版本：** 20

**需要权限：** ohos.permission.MANAGE_PRINT_JOB

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
