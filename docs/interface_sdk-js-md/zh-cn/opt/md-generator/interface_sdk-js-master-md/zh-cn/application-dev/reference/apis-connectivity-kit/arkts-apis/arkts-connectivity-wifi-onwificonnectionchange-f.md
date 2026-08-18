# on_wifiConnectionChange

## 导入模块

```TypeScript
```

## on_wifiConnectionChange

```TypeScript
function on(type: 'wifiConnectionChange', callback: Callback<number>): void
```

订阅WLAN连接状态改变事件。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** wifiConnectionChange

**需要权限：** ohos.permission.GET_WIFI_INFO

<!--Device-wifi-function on(type: 'wifiConnectionChange', callback: Callback<number>): void--><!--Device-wifi-function on(type: 'wifiConnectionChange', callback: Callback<number>): void-End-->

**系统能力：** SystemCapability.Communication.WiFi.STA

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'wifiConnectionChange' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | 是 |
