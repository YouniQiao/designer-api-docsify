# onScanDeviceDel（系统接口）

## 导入模块

```TypeScript
import { scan } from 'kits/@kit.BasicServicesKit';
```

## onScanDeviceDel

```TypeScript
function onScanDeviceDel(callback: Callback<ScannerDevice>): void
```

Register event callback for scanner device delete (system API).

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**需要权限：** ohos.permission.MANAGE_PRINT_JOB

<!--Device-scan-function onScanDeviceDel(callback: Callback<ScannerDevice>): void--><!--Device-scan-function onScanDeviceDel(callback: Callback<ScannerDevice>): void-End-->

**系统能力：** SystemCapability.Print.PrintFramework

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;ScannerDevice&gt; | 是 | Callback for device delete event. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 202 | Not system application. |

