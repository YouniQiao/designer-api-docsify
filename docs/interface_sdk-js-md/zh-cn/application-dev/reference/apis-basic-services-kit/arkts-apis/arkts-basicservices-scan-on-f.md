# on

## 导入模块

```TypeScript
import { scan } from 'kits/@kit.BasicServicesKit';
```

## on('scanDeviceFound')

```TypeScript
function on(type: 'scanDeviceFound', callback: Callback<ScannerDevice>): void
```

注册扫描仪设备发现事件回调。使用callback异步回调。

**起始版本：** 20

**需要权限：** ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'scanDeviceFound' | 是 |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[ScannerDevice](arkts-basicservices-scan-scannerdevice-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |


## on('scanDeviceSync')

```TypeScript
function on(type: 'scanDeviceSync', callback: Callback<ScannerSyncDevice>): void
```

注册扫描仪设备同步事件回调。使用callback异步回调。

**起始版本：** 20

**需要权限：** ohos.permission.MANAGE_PRINT_JOB

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'scanDeviceSync' | 是 |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[ScannerSyncDevice](arkts-basicservices-scan-scannersyncdevice-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
