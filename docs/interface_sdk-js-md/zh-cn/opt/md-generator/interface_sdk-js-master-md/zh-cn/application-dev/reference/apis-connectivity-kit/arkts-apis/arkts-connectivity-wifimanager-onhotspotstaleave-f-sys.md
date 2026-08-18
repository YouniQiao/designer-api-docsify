# onHotspotStaLeave（系统接口）

## 导入模块

```TypeScript
```

## onHotspotStaLeave

```TypeScript
function onHotspotStaLeave(callback: Callback<StationInfo>): void
```

注册热点STA离开事件。

**起始版本：** 23

**需要权限：** ohos.permission.MANAGE_WIFI_HOTSPOT

<!--Device-wifiManager-function onHotspotStaLeave(callback: Callback<StationInfo>): void--><!--Device-wifiManager-function onHotspotStaLeave(callback: Callback<StationInfo>): void-End-->

**系统能力：** SystemCapability.Communication.WiFi.AP.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;StationInfo&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [2601000](../errorcode-wifi.md#2601000-hotspot模块异常) |
