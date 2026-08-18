# setScanAlwaysAllowed（系统接口）

## 导入模块

```TypeScript
```

## setScanAlwaysAllowed

```TypeScript
function setScanAlwaysAllowed(isScanAlwaysAllowed: boolean): void
```

用户可以在WLAN关闭时触发扫描。

**起始版本：** 23

**需要权限：** ohos.permission.SET_WIFI_INFO and ohos.permission.SET_WIFI_CONFIG

<!--Device-wifiManager-function setScanAlwaysAllowed(isScanAlwaysAllowed: boolean): void--><!--Device-wifiManager-function setScanAlwaysAllowed(isScanAlwaysAllowed: boolean): void-End-->

**系统能力：** SystemCapability.Communication.WiFi.STA

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| isScanAlwaysAllowed | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [2501000](../errorcode-wifi.md#2501000-sta内部异常) |
