# on_wifiScanStateChange

## 导入模块

```TypeScript
```

## on_wifiScanStateChange

```TypeScript
function on(type: 'wifiScanStateChange', callback: Callback<number>): void
```

订阅WLAN扫描状态改变事件。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** wifiScanStateChange

**需要权限：** ohos.permission.GET_WIFI_INFO

<!--Device-wifi-function on(type: 'wifiScanStateChange', callback: Callback<number>): void--><!--Device-wifi-function on(type: 'wifiScanStateChange', callback: Callback<number>): void-End-->

**系统能力：** SystemCapability.Communication.WiFi.STA

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'wifiScanStateChange' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | 是 |
