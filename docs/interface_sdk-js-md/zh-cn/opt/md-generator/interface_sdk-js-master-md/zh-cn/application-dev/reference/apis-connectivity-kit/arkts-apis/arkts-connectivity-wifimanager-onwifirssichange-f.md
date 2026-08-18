# onWifiRssiChange

## 导入模块

```TypeScript
```

## onWifiRssiChange

```TypeScript
function onWifiRssiChange(callback: Callback<number>): void
```

注册WLAN接收信号强度(RSSI)变化事件。

**起始版本：** 23

**需要权限：** ohos.permission.GET_WIFI_INFO

<!--Device-wifiManager-function onWifiRssiChange(callback: Callback<int>): void--><!--Device-wifiManager-function onWifiRssiChange(callback: Callback<int>): void-End-->

**系统能力：** SystemCapability.Communication.WiFi.STA

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [2501000](../errorcode-wifi.md#2501000-sta内部异常) |
