# onScanDeviceFound

## onScanDeviceFound

```TypeScript
function onScanDeviceFound(callback: Callback<ScannerDevice>): void
```

Register event callback for scanner device found.

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.PRINT

<!--Device-scan-function onScanDeviceFound(callback: Callback<ScannerDevice>): void--><!--Device-scan-function onScanDeviceFound(callback: Callback<ScannerDevice>): void-End-->

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[ScannerDevice](arkts-basicservices-scan-scannerdevice-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
