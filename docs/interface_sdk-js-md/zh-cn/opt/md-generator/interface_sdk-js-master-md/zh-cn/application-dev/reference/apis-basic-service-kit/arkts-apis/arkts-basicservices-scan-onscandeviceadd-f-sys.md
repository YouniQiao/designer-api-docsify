# onScanDeviceAdd（系统接口）

## 导入模块

```TypeScript
```

## onScanDeviceAdd

```TypeScript
function onScanDeviceAdd(callback: Callback<ScannerDevice>): void
```

Register event callback for scanner device add (system API).

**起始版本：** 23

**需要权限：** ohos.permission.MANAGE_PRINT_JOB

<!--Device-scan-function onScanDeviceAdd(callback: Callback<ScannerDevice>): void--><!--Device-scan-function onScanDeviceAdd(callback: Callback<ScannerDevice>): void-End-->

**系统能力：** SystemCapability.Print.PrintFramework

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[ScannerDevice](arkts-basicservices-scan-scannerdevice-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
